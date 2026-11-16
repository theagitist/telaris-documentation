<?php
declare(strict_types=1);

/**
 * Seed the demo galaxies used in the editor-manual screenshots.
 *
 * Creates (idempotently) two galaxies on starmaps prefixed [manual-demo]
 * and populates them with synthetic content: enough wormholes, keywords,
 * and a portal to illustrate every editor surface the manual references.
 * Also creates an editor-only screenshot account sandboxed to these two
 * galaxies, so every shot's peripheral chrome (galaxy picker, sidebar,
 * portal target dropdown) only ever reveals demo content.
 *
 * Demo content is deliberately neutral (coastal plants, tide pools): no
 * personal, political, or organisational material. The seed re-runs
 * safely: existing rows are detected by name and reused.
 *
 * Usage:
 *     php tools/seed_demo_content.php
 *
 * Prints the editor account credentials to stdout on success; copy them
 * into ~/.telaris-capture-credentials before running the capture script.
 */

require_once '/var/www/starmaps.polivoxia.ca/config.php';
require_once '/var/www/starmaps.polivoxia.ca/inc/db.php';
require_once '/var/www/starmaps.polivoxia.ca/utils/auth.php';

const DEMO_TAG = '[manual-demo]';
const DEMO_GALAXY_MAIN = '[manual-demo] Coastal plants';
const DEMO_GALAXY_PORTAL_TARGET = '[manual-demo] Tide pools';
const DEMO_EDITOR_EMAIL = 'manual-capture-editor@telaris.local';
const DEMO_EDITOR_FIRST = 'Manual';
const DEMO_EDITOR_LAST = 'Capture';

/** Find a constellation by its exact name (case sensitive). */
function find_constellation_by_name(string $name): ?int
{
    $pdo = getDB();
    $stmt = $pdo->prepare('SELECT id FROM constellations WHERE name = :name LIMIT 1');
    $stmt->execute([':name' => $name]);
    $row = $stmt->fetch();
    return $row ? (int)$row['id'] : null;
}

/** Get-or-create a constellation by name, return its id. */
function ensure_constellation(string $name, string $tagline, string $theme = 'cosmic'): int
{
    $existing = find_constellation_by_name($name);
    if ($existing !== null) {
        echo "  reusing: {$name} (id={$existing})\n";
        return $existing;
    }
    $id = db_create_constellation($name, $tagline, null, $theme, null);
    echo "  created: {$name} (id={$id})\n";
    return $id;
}

/** Build a random animation-position JSON blob, matching the format in db.php. */
function random_animation(): string
{
    return json_encode([
        'radius' => 5 + rand(0, 3),
        'theta'  => rand(0, 628) / 100,
        'phi'    => rand(0, 314) / 100,
        'speed'  => 0.002 + (rand(0, 4) / 1000),
        'phase'  => rand(0, 628) / 100,
    ], JSON_THROW_ON_ERROR);
}

/** Get-or-create a wormhole inside a galaxy. Returns its id. */
function ensure_node(int $constellationId, array $node): int
{
    $pdo = getDB();
    $stmt = $pdo->prepare('SELECT id FROM nodes WHERE constellation_id = :cid AND name = :name LIMIT 1');
    $stmt->execute([':cid' => $constellationId, ':name' => $node['name']]);
    $row = $stmt->fetch();
    if ($row) {
        echo "    reusing wormhole: {$node['name']} (id={$row['id']})\n";
        $id = (int)$row['id'];
    } else {
        $id = db_create_node(
            name: $node['name'],
            description: $node['description'] ?? null,
            url: null,
            animation: random_animation(),
            constellationId: $constellationId,
            nodeType: $node['node_type'] ?? 'object',
            targetConstellationId: $node['target_constellation_id'] ?? null,
            imageUrl: $node['image_url'] ?? null,
            embedCode: null,
            audioUrl: $node['audio_url'] ?? null,
            audioAutoplay: false,
            isAccentuated: $node['accentuated'] ?? false,
            videoUrl: $node['video_url'] ?? null,
            videoAutoplay: false,
            audioLoop: false,
            showKeywords: false,
            iconUrl: null,
            imageAttribution: null,
            useImageAsNode: false,
            pdfUrl: $node['pdf_url'] ?? null,
            createdBy: null,
        );
        echo "    created wormhole: {$node['name']} (id={$id})\n";
    }
    if (!empty($node['keywords'])) {
        db_save_node_keywords($id, $node['keywords'], null);
    }
    return $id;
}

/** Ensure a user account exists, return its id. Creates if missing. */
function ensure_user(string $email, string $first, string $last, int $type): string
{
    $existing = db_get_user_by_email($email);
    if ($existing) {
        echo "  reusing user: {$email} (id={$existing['id']})\n";
        return (string)$existing['id'];
    }
    // db_get_user_by_email is the only way to read the id; createUser
    // returns null on success or an error string. We need a fresh password.
    $password = bin2hex(random_bytes(14)); // 28 hex chars.
    $hash = hashPassword($password);
    $err = createUser(getDB(), $email, $hash, $first, $last, $type);
    if ($err !== null) {
        fwrite(STDERR, "createUser failed: {$err}\n");
        exit(1);
    }
    $row = db_get_user_by_email($email);
    if (!$row) {
        fwrite(STDERR, "user not found after creation: {$email}\n");
        exit(1);
    }
    echo "  created user: {$email} (id={$row['id']}, password={$password})\n";
    echo "  ^^^ COPY THIS PASSWORD; it is shown only here.\n";
    return (string)$row['id'];
}

// ---------------------------------------------------------------------------
// Demo content payloads.
// ---------------------------------------------------------------------------

$coastalPlants = [
    [
        'name' => 'Beach Strawberry',
        'description' => "Low-growing perennial with white flowers and small red fruit. Spreads along the sand by runners; tolerates salt spray; native to the Pacific coast.",
        'keywords' => ['native', 'edible', 'ground-cover', 'perennial', 'salt-tolerant'],
    ],
    [
        'name' => 'Sea Lavender',
        'description' => "Low rosette of leathery leaves topped by sprays of small lavender flowers in summer. Loves salt; common at the upper edge of salt marshes.",
        'keywords' => ['native', 'salt-tolerant', 'flower', 'perennial'],
    ],
    [
        'name' => 'Pacific Wax Myrtle',
        'description' => "Evergreen shrub or small tree with aromatic leaves. Tolerant of wind and salt; a quiet anchor in older dune communities.",
        'keywords' => ['native', 'evergreen', 'shrub', 'salt-tolerant'],
    ],
    [
        'name' => 'Yellow Bush Lupine',
        'description' => "Spiky golden flowers in late spring; nitrogen-fixing roots that quietly enrich poor sandy soils.",
        'keywords' => ['native', 'flower', 'perennial', 'nitrogen-fixer'],
        'accentuated' => true,
    ],
    [
        'name' => 'Beach Grass',
        'description' => "Stiff grey-green grass with deep rhizomes. The non-native species (European Beach Grass) builds taller dunes than the natives it replaced, with knock-on effects on the dune community.",
        'keywords' => ['ground-cover', 'perennial', 'invasive'],
    ],
    [
        'name' => 'Sea Rocket',
        'description' => "Annual succulent of the upper beach. Crunchy salty leaves; small pale flowers; quietly edible if you know it.",
        'keywords' => ['edible', 'salt-tolerant', 'annual'],
    ],
    [
        'name' => 'Coastal Sage',
        'description' => "Soft grey-leaved shrub with a strong fragrance. The dominant smell of California chaparral on warm days; once an everyday medicinal across the coast.",
        'keywords' => ['native', 'medicinal', 'perennial', 'drought-tolerant'],
    ],
    [
        'name' => 'Wild Cucumber',
        'description' => "Climbing vine with deeply lobed leaves and spiny seed pods. Native; vigorous; the pods are not edible despite the name.",
        'keywords' => ['native', 'vine', 'annual'],
    ],
    [
        'name' => 'Beach Pea',
        'description' => "Sprawling perennial with purple pea flowers and salt-tolerant seed pods. Stabilises sand; nitrogen-fixing.",
        'keywords' => ['native', 'flower', 'annual', 'nitrogen-fixer'],
    ],
    [
        'name' => 'Ice Plant',
        'description' => "Sprawling mat of fleshy three-sided leaves; pink or yellow daisy-like flowers. Introduced for erosion control in the 1900s; now widely considered invasive.",
        'keywords' => ['ground-cover', 'perennial', 'invasive', 'succulent'],
    ],
    [
        'name' => 'Sea Palm',
        'description' => "Short brown algae that grows in dense colonies on wave-pounded intertidal rocks. Resembles a tiny palm tree; the namesake of many a hidden beach.",
        'keywords' => ['native', 'intertidal'],
    ],
    [
        'name' => 'Coastal field guide',
        'description' => "Reference document covering the plants in this galaxy. Demonstrates how a PDF wormhole reads in the visitor view.",
        'keywords' => ['reference', 'guide'],
        // pdf_url left null; the manual's PDF-upload section uses the empty modal.
    ],
];

$tidePools = [
    [
        'name' => 'Ochre Sea Star',
        'description' => "Slow-moving predator of mussels and barnacles; a keystone of the rocky intertidal. Comes in orange, brown, and deep purple.",
        'keywords' => ['intertidal', 'animal'],
    ],
    [
        'name' => 'Giant Green Anemone',
        'description' => "Fist-sized anemone in tide pools; symbiotic with algae that lend it the green colour. Closes into a sticky knob between tides.",
        'keywords' => ['intertidal', 'animal'],
    ],
    [
        'name' => 'Tidepool Sculpin',
        'description' => "Small bottom-dwelling fish that survives temperature swings, salinity swings, and oxygen swings most fish would die from. Camouflaged against algae and rock.",
        'keywords' => ['intertidal', 'fish'],
    ],
    [
        'name' => 'Hermit Crab',
        'description' => "Lives in borrowed snail shells and trades up as it grows. Tide pools are full of them on quiet days.",
        'keywords' => ['intertidal', 'animal'],
    ],
    // The four below give the Map editor demo (chapter 8) enough wormholes to
    // read as a walk from the splash zone down to the low tide line.
    [
        'name' => 'Gooseneck Barnacle',
        'description' => "Clusters on wave-battered rock in the splash zone, feeding with feathery legs when the surf washes over.",
        'keywords' => ['intertidal', 'animal'],
    ],
    [
        'name' => 'Black Turban Snail',
        'description' => "Grazes algae film off the upper rocks; its empty shells often become homes for hermit crabs.",
        'keywords' => ['intertidal', 'animal'],
    ],
    [
        'name' => 'Purple Shore Crab',
        'description' => "Quick, shy crab of the middle shore, hiding under rocks by day and scavenging at night.",
        'keywords' => ['intertidal', 'animal'],
    ],
    [
        'name' => 'Sea Lettuce',
        'description' => "Thin, bright green alga that carpets tide pools and feeds snails, crabs and fish.",
        'keywords' => ['intertidal', 'alga'],
    ],
];

// Map editor demo (chapter 8): placements, paths and one route on the tide
// pools galaxy, laid out from the splash zone (left) to the low tide line
// (right). Kept off the coastal plants galaxy so its keyword-line shots stay valid.
$tidePoolMap = [
    'positions' => [
        'Gooseneck Barnacle' => [300, 700], 'Black Turban Snail' => [300, 1300],
        'Purple Shore Crab' => [700, 1000],
        'Hermit Crab' => [1050, 650], 'Sea Lettuce' => [1050, 1350],
        'Ochre Sea Star' => [1400, 650], 'Tidepool Sculpin' => [1400, 1350],
        'Giant Green Anemone' => [1750, 1000],
    ],
    // [from, to, directed, note]
    'paths' => [
        ['Gooseneck Barnacle', 'Purple Shore Crab', true, 'Down from the splash zone'],
        ['Black Turban Snail', 'Purple Shore Crab', true, null],
        ['Gooseneck Barnacle', 'Hermit Crab', true, null],
        ['Purple Shore Crab', 'Hermit Crab', true, null],
        ['Purple Shore Crab', 'Sea Lettuce', true, null],
        ['Hermit Crab', 'Sea Lettuce', false, null],
        ['Hermit Crab', 'Ochre Sea Star', true, null],
        ['Sea Lettuce', 'Tidepool Sculpin', true, null],
        ['Ochre Sea Star', 'Giant Green Anemone', true, null],
        ['Tidepool Sculpin', 'Giant Green Anemone', true, null],
    ],
    'route' => ['Low tide walk', ['Gooseneck Barnacle', 'Purple Shore Crab', 'Hermit Crab', 'Ochre Sea Star', 'Giant Green Anemone']],
];

// ---------------------------------------------------------------------------
// Seed.
// ---------------------------------------------------------------------------

echo "Telaris demo seed\n=================\n";

echo "\nGalaxies:\n";
$tidePoolsId = ensure_constellation(
    DEMO_GALAXY_PORTAL_TARGET,
    'Portal-target galaxy used in editor manual demos.',
);
$coastalId = ensure_constellation(
    DEMO_GALAXY_MAIN,
    'Sample galaxy used in editor manual screenshots.',
);

echo "\nWormholes in coastal plants:\n";
foreach ($coastalPlants as $plant) {
    ensure_node($coastalId, $plant);
}

// Add the portal wormhole in the main galaxy pointing at the tide pools.
echo "\nPortal wormhole:\n";
ensure_node($coastalId, [
    'name' => 'To the tide pools',
    'description' => 'A portal wormhole. Visitors who open this travel to the [manual-demo] Tide pools galaxy.',
    'node_type' => 'portal',
    'target_constellation_id' => $tidePoolsId,
    'keywords' => ['portal'],
]);

echo "\nWormholes in tide pools galaxy:\n";
foreach ($tidePools as $animal) {
    ensure_node($tidePoolsId, $animal);
}

// Keyword canvas relations so the canvas screenshot has visible lines, not just
// a grid of chips. The relations are illustrative; the editorial point is that
// these connections make sense given the wormholes' keywords (native plants
// are usually salt-tolerant on the coast; edible and medicinal overlap; etc.).
echo "\nKeyword canvas relations:\n";
$kwIds = [];
$stmt = getDB()->prepare("SELECT id, keyword FROM keywords WHERE constellation_id = :cid");
$stmt->execute([':cid' => $coastalId]);
foreach ($stmt->fetchAll() as $row) {
    $kwIds[$row['keyword']] = (int)$row['id'];
}

$desiredRelations = [
    ['native', 'salt-tolerant', 'Most natives on this coast tolerate salt.'],
    ['edible', 'native', 'Most edible plants here are native; ice plant is the exception.'],
    ['edible', 'medicinal', 'Some species are both food and medicine in source-community use.'],
    ['invasive', 'ground-cover', 'The most-spread invasives here are ground-covers.'],
    ['nitrogen-fixer', 'native', null],
    ['perennial', 'ground-cover', null],
];

foreach ($desiredRelations as [$a, $b, $note]) {
    if (!isset($kwIds[$a]) || !isset($kwIds[$b])) {
        echo "  skipped: {$a} <-> {$b} (keyword missing)\n";
        continue;
    }
    // Idempotency: skip if a relation between these two already exists in
    // either direction.
    $check = getDB()->prepare(
        "SELECT 1 FROM keyword_relations
         WHERE (keyword_a_id = :a1 AND keyword_b_id = :b1)
            OR (keyword_a_id = :b2 AND keyword_b_id = :a2)
         LIMIT 1"
    );
    $check->execute([
        ':a1' => $kwIds[$a], ':b1' => $kwIds[$b],
        ':a2' => $kwIds[$a], ':b2' => $kwIds[$b],
    ]);
    if ($check->fetch()) {
        echo "  reusing: {$a} <-> {$b}\n";
        continue;
    }
    db_create_keyword_relation($kwIds[$a], $kwIds[$b], null, $note);
    echo "  created: {$a} <-> {$b}" . ($note ? " ({$note})" : '') . "\n";
}

// Seed default positions for every chip so the canvas does not render with
// every chip on top of every other at first load. The helper is idempotent.
echo "\nKeyword canvas positions:\n";
$seeded = db_seed_keyword_positions_for_galaxy($coastalId);
echo "  seeded {$seeded} chip position(s) for coastal plants.\n";

echo "\nEditor account:\n";
$editorId = ensure_user(DEMO_EDITOR_EMAIL, DEMO_EDITOR_FIRST, DEMO_EDITOR_LAST, USER_TYPE_EDITOR);
db_set_user_constellations($editorId, [$coastalId, $tidePoolsId]);
echo "  assigned to: coastal plants (id={$coastalId}) and tide pools (id={$tidePoolsId})\n";

// Map editor demo on the tide pools galaxy. Authored by the capture editor so
// the path window shows Change direction / Edit note / Delete. Idempotent:
// placements are upserts; paths and the route are created only when missing.
echo "\nMap (tide pools):\n";
$pdo = getDB();
$ids = [];
$st = $pdo->prepare('SELECT id, name FROM nodes WHERE constellation_id = :cid');
$st->execute([':cid' => $tidePoolsId]);
foreach ($st->fetchAll() as $r) $ids[$r['name']] = (int)$r['id'];
foreach ($tidePoolMap['positions'] as $name => [$x, $y]) {
    db_record_node_position($ids[$name], (float)$x, (float)$y, $editorId);
}
echo "  placed " . count($tidePoolMap['positions']) . " wormholes\n";
$anchors = function (array $p, array $q): array {
    $dx = $q[0] - $p[0]; $dy = $q[1] - $p[1];
    if (abs($dx) >= abs($dy)) return $dx >= 0 ? ['right', 'left'] : ['left', 'right'];
    return $dy >= 0 ? ['bottom', 'top'] : ['top', 'bottom'];
};
$exists = $pdo->prepare('SELECT 1 FROM node_paths WHERE node_a_id = :a AND node_b_id = :b');
foreach ($tidePoolMap['paths'] as [$from, $to, $directed, $note]) {
    $a = $ids[$from]; $b = $ids[$to];
    $exists->execute([':a' => min($a, $b), ':b' => max($a, $b)]);
    if ($exists->fetch()) { echo "  reusing path: {$from} -> {$to}\n"; continue; }
    [$aa, $ab] = $anchors($tidePoolMap['positions'][$from], $tidePoolMap['positions'][$to]);
    db_create_node_path($a, $b, $editorId, $note, $aa, $ab, $directed);
    echo "  created path: {$from} -> {$to}\n";
}
[$routeName, $stops] = $tidePoolMap['route'];
$hasRoute = array_filter(db_get_galaxy_routes($tidePoolsId), fn($r) => $r['name'] === $routeName);
if ($hasRoute) {
    echo "  reusing route: {$routeName}\n";
} else {
    db_create_node_route($tidePoolsId, $routeName, array_map(fn($n) => $ids[$n], $stops), $editorId);
    echo "  created route: {$routeName}\n";
}

echo "\nSeed complete.\n";
echo "Capture credentials env vars (set in ~/.telaris-capture-credentials):\n";
echo "  TELARIS_EDITOR_URL=https://starmaps.polivoxia.ca\n";
echo "  TELARIS_EDITOR_USERNAME=" . DEMO_EDITOR_EMAIL . "\n";
echo "  (password printed above if the account was just created; otherwise reuse the existing one)\n";
