// Scans public/character/ and writes src/data/assets.json so the React tree
// never references a file that doesn't exist (OffthreadVideo/img hang or
// crash the renderer on a missing src instead of failing cleanly).
const fs = require("fs");
const path = require("path");

const CLIP_IDS = ["s1", "s2", "s3", "s4", "s5"];
const POSES = [
  "neutral",
  "thumbsup",
  "pointing",
  "thinking",
  "shock",
  "pointup",
];

const dir = path.join(__dirname, "..", "public", "character");
const exists = (f) => fs.existsSync(path.join(dir, f));

const clips = {};
for (const id of CLIP_IDS) clips[id] = exists(`${id}.mp4`);

const poses = {};
for (const p of POSES) poses[p] = exists(`${p}.png`);

const out = { clips, poses };
const outPath = path.join(__dirname, "..", "src", "data", "assets.json");
fs.writeFileSync(outPath, JSON.stringify(out, null, 2) + "\n");

const clipCount = Object.values(clips).filter(Boolean).length;
const poseCount = Object.values(poses).filter(Boolean).length;
console.log(
  `assets.json: ${clipCount}/5 HeyGen clips, ${poseCount}/6 pose PNGs found.`
);
