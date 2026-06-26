<?php
/**
 * Seed the demo content for the Hotglue-manual screenshots on the starmaps
 * instance: a small art-themed demo galaxy ([manual-demo] Masterworks) with two
 * famous-painting wormholes, each carrying a composed, visually rich Hotglue
 * page, plus an unassigned draft. The pages use the actual public-domain
 * paintings (royalty-free, from Wikimedia Commons) as bleeding hero images, with
 * overlapping titles, a colour accent, body text, and a translucent caption
 * card, to show off what hotglue layouts can do (Review 3: the text-only version
 * did not reflect hotglue's flexibility).
 *
 * Run as www-data so the page files + downloaded images are www-data-owned and
 * the DB writes use the instance config:
 *   sudo -u www-data php tools/seed_hotglue_demo.php
 *
 * Re-runnable: galaxy + wormholes are get-or-create, images are downloaded only
 * if missing, page files are overwritten, registry rows are upserted. Prints the
 * wormhole ids the capture script needs.
 */

declare(strict_types=1);

require '/var/www/starmaps.polivoxia.ca/config.php';   // also pulls inc/db.php

const CAPTURE_EDITOR = 'user_7a14bc5e6e63dc58'; // manual-capture-editor@telaris.local
const CONTENT_DIR    = '/var/www/starmaps.polivoxia.ca/hg/content';

$FONT   = 'Helvetica, Arial, sans-serif';
$INDIGO = 'rgb(18, 28, 52)';        // page background: deep gallery indigo
$CREAM  = 'rgb(240, 236, 228)';     // body text on the dark ground
$GOLD   = 'rgb(226, 168, 94)';      // accent
$WHITE  = 'rgb(255, 255, 255)';
$SCRIM  = 'rgba(14, 22, 42, 0.62)'; // translucent caption card over an image

/** Write one Hotglue object file (sorted props, blank line, body). */
function write_obj(string $headDir, string $id, array $props, string $body): void {
    ksort($props);
    $lines = [];
    foreach ($props as $k => $v) {
        $lines[] = "$k:$v";
    }
    file_put_contents("$headDir/$id", implode("\n", $lines) . "\n\n" . $body);
}

/** Download an image into a page's shared/ dir if it is not already there. */
function ensure_image(string $pageSlug, string $filename, string $url): void {
    $dir = CONTENT_DIR . '/' . $pageSlug . '/shared';
    if (!is_dir($dir)) {
        mkdir($dir, 0775, true);
    }
    $dest = "$dir/$filename";
    if (is_file($dest) && filesize($dest) > 2000) {
        echo "image present: $pageSlug/$filename\n";
        return;
    }
    $ctx = stream_context_create(['http' => [
        'header'  => "User-Agent: TelarisDocsBot/1.0 (https://telaris.ca; aemjcr@gmail.com)\r\n",
        'timeout' => 30,
        'follow_location' => 1,
    ]]);
    $data = @file_get_contents($url, false, $ctx);
    if ($data === false || strlen($data) < 2000) {
        fwrite(STDERR, "WARN: could not download $filename from $url\n");
        return;
    }
    file_put_contents($dest, $data);
    echo "downloaded $pageSlug/$filename (" . strlen($data) . " bytes)\n";
}

/**
 * Reset a page's head dir and write a fresh object set. $bgColor (optional)
 * writes the special `page` object that sets the CSS page background colour.
 */
function seed_page(string $slug, array $objects, ?string $bgColor = null): void {
    $headDir = CONTENT_DIR . '/' . $slug . '/head';
    if (!is_dir($headDir)) {
        mkdir($headDir, 0775, true);
    }
    foreach (glob("$headDir/*") as $f) {
        if (is_file($f)) {
            unlink($f);
        }
    }
    if ($bgColor !== null) {
        write_obj($headDir, 'page', [
            'type' => 'page', 'module' => 'page',
            'page-background-color' => $bgColor,
        ], '');
    }
    foreach ($objects as $id => [$props, $body]) {
        write_obj($headDir, (string)$id, $props, $body);
    }
    echo "seeded $slug (" . count($objects) . " objects" . ($bgColor ? " + bg" : "") . ")\n";
}

/** Convenience: an image object sized to keep the source aspect ratio. */
function img_obj(string $file, int $natW, int $natH, int $left, int $top, int $dispW, int $z, string $title): array {
    $dispH = (int) round($dispW * $natH / $natW);
    return [[
        'type' => 'image', 'module' => 'image',
        'image-file' => $file,
        'image-file-width' => (string) $natW,
        'image-file-height' => (string) $natH,
        'image-title' => $title,
        'object-left' => $left . 'px', 'object-top' => $top . 'px',
        'object-width' => $dispW . 'px', 'object-height' => $dispH . 'px',
        'object-zindex' => (string) $z,
    ], ''];
}

/** Get-or-create a constellation by exact name, return its id. */
function ensure_galaxy(string $name, string $tagline, string $theme): int {
    $pdo = getDB();
    $st = $pdo->prepare('SELECT id FROM constellations WHERE name = :n LIMIT 1');
    $st->execute([':n' => $name]);
    $id = $st->fetchColumn();
    return $id ? (int) $id : db_create_constellation($name, $tagline, null, $theme, null);
}

/** Get-or-create an object wormhole by name in a galaxy, return its id. */
function ensure_wormhole(int $galaxyId, string $name, string $desc, array $keywords): int {
    $pdo = getDB();
    $st = $pdo->prepare('SELECT id FROM nodes WHERE constellation_id = :c AND name = :n LIMIT 1');
    $st->execute([':c' => $galaxyId, ':n' => $name]);
    $id = $st->fetchColumn();
    if (!$id) {
        $anim = json_encode(['radius' => 6, 'theta' => 1.2, 'phi' => 1.6, 'speed' => 0.003, 'phase' => 0.5]);
        $id = db_create_node($name, $desc, null, $anim, $galaxyId);
    }
    db_save_node_keywords((int) $id, $keywords, null);
    return (int) $id;
}

// --- The art-themed demo galaxy + wormholes -----------------------------------

$galaxyId = ensure_galaxy(
    '[manual-demo] Masterworks',
    'Famous paintings, used for the Hotglue manual screenshots.',
    'cosmic'
);
$galaxySlug = (function (int $gid): string {
    $st = getDB()->prepare('SELECT slug FROM constellations WHERE id = :id');
    $st->execute([':id' => $gid]);
    return (string) $st->fetchColumn();
})($galaxyId);

$greatWaveId = ensure_wormhole(
    $galaxyId,
    'The Great Wave off Kanagawa',
    'A woodblock print by Katsushika Hokusai, about 1831. A towering wave curls over boats with Mount Fuji small in the distance.',
    ['hokusai', 'ukiyo-e', 'woodblock', 'seascape', 'edo']
);
$starryNightId = ensure_wormhole(
    $galaxyId,
    'The Starry Night',
    'An oil painting by Vincent van Gogh, 1889. A swirling night sky over a quiet town, with a dark cypress in the foreground.',
    ['van-gogh', 'post-impressionism', 'night-sky', 'cypress']
);

$current = array_map(static fn ($g) => (int) $g['id'], db_get_constellations_for_user(CAPTURE_EDITOR, false));
$ids = array_values(array_unique(array_merge($current, [$galaxyId])));
db_set_user_constellations(CAPTURE_EDITOR, $ids, 'read_write');
echo "galaxy [$galaxyId] slug=$galaxySlug; wormholes great-wave=$greatWaveId starry-night=$starryNightId\n";
echo "editor galaxies: " . implode(',', $ids) . "\n";

// --- Images (public domain, Wikimedia Commons via the stable Special:FilePath) -

$greatWaveSlug   = 'node-' . $greatWaveId;
$starryNightSlug = 'node-' . $starryNightId;
ensure_image($greatWaveSlug, 'great-wave.jpg',
    'https://commons.wikimedia.org/wiki/Special:FilePath/Tsunami_by_hokusai_19th_century.jpg?width=1400');
ensure_image($starryNightSlug, 'starry-night.jpg',
    'https://commons.wikimedia.org/wiki/Special:FilePath/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg?width=1400');

// --- The Great Wave: the hero page (canvas + menu shots) -----------------------
// Hero image bleeds off the top/right; title + accent + body sit on the indigo
// left column; a translucent card captions the image.

$greatWave = [
    // hero image, bleeding off the top and right edges
    '200000000020' => img_obj('great-wave.jpg', 1920, 1291, 540, -36, 1000, 20, 'The Great Wave off Kanagawa'),
    // gold accent rule
    '200000000030' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '80px', 'object-top' => '154px',
        'object-width' => '66px', 'object-height' => '8px',
        'object-zindex' => '30',
        'text-background-color' => $GOLD,
        'text-font-family' => $FONT, 'text-font-size' => '8px',
    ], ''],
    // title (overlaps the image's left edge), two lines via <br>
    '200000000040' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '80px', 'object-top' => '184px',
        'object-width' => '560px', 'object-height' => '128px',
        'object-zindex' => '50',
        'text-font-color' => $WHITE,
        'text-font-family' => $FONT, 'text-font-size' => '52px',
        'text-font-weight' => 'bold', 'text-line-height' => '1.05',
    ], 'The Great Wave<br>off Kanagawa'],
    // attribution
    '200000000050' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '82px', 'object-top' => '330px',
        'object-width' => '460px', 'object-height' => '34px',
        'object-zindex' => '50',
        'text-font-color' => $GOLD,
        'text-font-family' => $FONT, 'text-font-size' => '22px', 'text-font-style' => 'italic',
    ], 'Katsushika Hokusai, about 1831'],
    // body paragraph, left column on the indigo ground
    '200000000060' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '80px', 'object-top' => '392px',
        'object-width' => '400px', 'object-height' => '260px',
        'object-zindex' => '40',
        'text-font-color' => $CREAM,
        'text-font-family' => $FONT, 'text-font-size' => '17px', 'text-line-height' => '1.6',
    ], 'A great wave rears up and curls over three boats, its crest breaking into fingers of foam. Far off and very small, Mount Fuji sits calm beneath it. The colour comes from a then-new blue, printed from carved wooden blocks and repeated by the thousand.'],
    // translucent caption card sitting on the image
    '200000000070' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '600px', 'object-top' => '548px',
        'object-width' => '430px', 'object-height' => '54px',
        'object-zindex' => '60',
        'text-background-color' => $SCRIM,
        'text-font-color' => $WHITE,
        'text-font-family' => $FONT, 'text-font-size' => '15px',
        'text-padding' => '14px',
    ], 'From Thirty-six Views of Mount Fuji'],
];
seed_page($greatWaveSlug, $greatWave, $INDIGO);

// --- The Starry Night: a narrow page that scales to fit a phone ----------------
// Full-width hero image with the title on a translucent strip over it, then
// attribution + a short paragraph on the indigo ground below.

$starryNight = [
    '200000000020' => img_obj('starry-night.jpg', 1920, 1520, 0, 0, 560, 20, 'The Starry Night'),
    // title on a translucent strip across the lower image
    '200000000040' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '0px', 'object-top' => '352px',
        'object-width' => '560px', 'object-height' => '90px',
        'object-zindex' => '40',
        'text-background-color' => $SCRIM,
        'text-font-color' => $WHITE,
        'text-font-family' => $FONT, 'text-font-size' => '30px',
        'text-font-weight' => 'bold', 'text-padding' => '18px',
    ], 'The Starry Night'],
    // attribution
    '200000000050' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '24px', 'object-top' => '468px',
        'object-width' => '512px', 'object-height' => '30px',
        'object-zindex' => '50',
        'text-font-color' => $GOLD,
        'text-font-family' => $FONT, 'text-font-size' => '17px', 'text-font-style' => 'italic',
    ], 'Vincent van Gogh, 1889'],
    // paragraph
    '200000000060' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '24px', 'object-top' => '508px',
        'object-width' => '512px', 'object-height' => '180px',
        'object-zindex' => '40',
        'text-font-color' => $CREAM,
        'text-font-family' => $FONT, 'text-font-size' => '17px', 'text-line-height' => '1.6',
    ], 'A night sky rolls in thick spirals above a quiet town. A dark cypress rises in front, and a bright crescent moon glows in the corner. Van Gogh painted it from memory, from the window of his room.'],
];
seed_page($starryNightSlug, $starryNight, $INDIGO);

// --- One unassigned standalone draft ------------------------------------------

seed_page('page-900', [
    '200000000010' => [[
        'type' => 'text', 'module' => 'text',
        'object-left' => '64px', 'object-top' => '60px',
        'object-width' => '900px', 'object-height' => '60px',
        'object-zindex' => '100',
        'text-font-color' => $WHITE,
        'text-font-family' => $FONT, 'text-font-size' => '36px', 'text-font-weight' => 'bold',
    ], 'Exhibition notes (draft)'],
], $INDIGO);

// --- Registry rows so the editor's Hotglue-content list is populated ----------

$pdo = getDB();
db_ensure_hotglue_pages_table();

function upsert_page(PDO $pdo, string $slug, string $title, ?int $nodeId, string $owner): void {
    $st = $pdo->prepare("SELECT id FROM hotglue_pages WHERE slug = :slug");
    $st->execute([':slug' => $slug]);
    $id = $st->fetchColumn();
    if ($id) {
        $pdo->prepare("UPDATE hotglue_pages SET title=:t, node_id=:n, owner_user_id=:o, updated_at=CURRENT_TIMESTAMP WHERE id=:id")
            ->execute([':t' => $title, ':n' => $nodeId, ':o' => $owner, ':id' => $id]);
        echo "updated registry row $slug\n";
    } else {
        $pdo->prepare("INSERT INTO hotglue_pages (slug, title, node_id, owner_user_id) VALUES (:slug,:t,:n,:o)")
            ->execute([':slug' => $slug, ':t' => $title, ':n' => $nodeId, ':o' => $owner]);
        echo "inserted registry row $slug\n";
    }
}

$pdo->prepare("DELETE FROM hotglue_pages WHERE slug IN ('node-279','node-290')")->execute();

upsert_page($pdo, $greatWaveSlug,   'The Great Wave off Kanagawa', $greatWaveId,   CAPTURE_EDITOR);
upsert_page($pdo, $starryNightSlug, 'The Starry Night',            $starryNightId, CAPTURE_EDITOR);
upsert_page($pdo, 'page-900',       'Exhibition notes (draft)',    null,           CAPTURE_EDITOR);

echo "\nCAPTURE CONSTANTS -> DEMO_SLUG={$galaxySlug}  GREAT_WAVE_NODE={$greatWaveId}  STARRY_NIGHT_NODE={$starryNightId}\n";
echo "done.\n";
