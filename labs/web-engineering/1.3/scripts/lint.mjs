/** Minimal lint script for lab CI — no external deps */
import { readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(new URL("..", import.meta.url)));
const ignore = new Set(["node_modules", ".git", ".husky", "scripts"]);

function walk(dir, files = []) {
  for (const name of readdirSync(dir)) {
    if (ignore.has(name)) continue;
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, files);
    else if (name.endsWith(".js") || name.endsWith(".mjs")) files.push(p);
  }
  return files;
}

const bad = [];
for (const file of walk(root)) {
  const text = readFileSync(file, "utf8");
  if (text.includes("TODO: remove before prod")) bad.push(file);
}

if (bad.length) {
  console.error("lint failed:", bad);
  process.exit(1);
}
console.log("lint ok");
