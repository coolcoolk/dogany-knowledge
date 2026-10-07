#!/usr/bin/env python3
"""Check a knowledge-module tree against its modules.json manifest.

Usage: python3 tools/verify_manifest.py [ROOT]

For every module listed in ROOT/modules.json, recompute the content hash of
ROOT/<path> and compare it with the manifest's `sha256`, and check that the
manifest's `files` list matches the files on disk. Exit 0 when every module
matches, 1 otherwise. Python 3 standard library only.

Hash definition: for each file under the module directory (path components
starting with '.' and __pycache__ skipped), in bytewise-sorted order of the
'/'-separated relative path, form the line
    "<sha256 hex of the file bytes>  <relative path>\\n"
and take the sha256 hex of the UTF-8 concatenation of those lines. Shell
equivalent, run inside the module directory:
    find . -type f ! -path '*/.*' ! -path '*/__pycache__/*' \\
      | sed 's#^\\./##' | LC_ALL=C sort \\
      | while IFS= read -r f; do shasum -a 256 "$f"; done | shasum -a 256

License: MIT (see LICENSE-TOOLS).
"""

import hashlib
import json
import os
import sys


def module_files(base):
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if not d.startswith(".") and d != "__pycache__"]
        for name in filenames:
            if name.startswith("."):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), base)
            out.append(rel.replace(os.sep, "/"))
    return sorted(out)


def tree_sha256(base, files):
    outer = hashlib.sha256()
    for rel in files:
        with open(os.path.join(base, *rel.split("/")), "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        outer.update(("%s  %s\n" % (digest, rel)).encode("utf-8"))
    return outer.hexdigest()


def main(argv):
    root = argv[0] if argv else "."
    with open(os.path.join(root, "modules.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    bad = 0
    for mod in manifest.get("modules", []):
        base = os.path.join(root, mod["path"])
        files = module_files(base)
        problems = []
        if files != mod.get("files"):
            problems.append("file list differs")
        if tree_sha256(base, files) != mod.get("sha256"):
            problems.append("sha256 differs")
        status = "ok" if not problems else "FAIL (%s)" % ", ".join(problems)
        print("%-20s %-8s %s" % (mod["id"], mod.get("version"), status))
        bad += bool(problems)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
