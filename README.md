# Knowledge warehouse: exercise, nutrition, sleep-recovery

Curated, graded knowledge items for a personal-assistant product: what the
evidence says, how strongly, and the rules an assistant may build on it. Each
item states a claim, the sources it was read from, a confidence grade, and
where the evidence stops. Most items end with a short Korean summary written
for answering a user.

This repository is a generated export. It holds the modules that are marked
published; it is regenerated, not edited by hand. Corrections and gap reports
are welcome as issues.

Not medical advice. Items describe research findings and product rules; they
do not diagnose, treat or replace a clinician.

## Modules

| module | what it covers |
|---|---|
| `exercise` | resistance training: volume, intensity, progression, warm-up and ramp sets, recovery and deloads, machine vs free weight, injury caution and pain, body-ideal archetypes |
| `nutrition` | protein intake and distribution, energy balance and cuts, diet adherence, Korean convenience-store and eating-out protein options, alcohol |
| `sleep-recovery` | sleep duration and regularity, early-morning and late-night training, short nights, trackers, recovery |

Versions, file lists and content hashes are in `modules.json`.

## Layout

```
README.md            this file
LICENSE              CC BY 4.0 -- the knowledge content (everything under modules/)
LICENSE-TOOLS        MIT -- the code under tools/
modules.json         module manifest
modules/
  <module-id>/
    CHANGELOG.yaml   the module's release history; top entry = its version
    GAPS.md          what is known to be missing, contested or unread
    items/
      <domain>-<slug>-NNN.md
tools/
  verify_manifest.py check modules/ against modules.json
```

## Item format

Each item is a markdown file with a leading `---` YAML frontmatter block (the
machine record) followed by prose (the human-readable layer).

- `id` -- stable id, `<domain>/<slug>-NNN`. Never reused or renumbered once
  released.
- `domain` -- equals the id prefix and the module id.
- `grade` -- confidence on a ladder A..D: A converged consensus, B randomised
  evidence before consensus, C observational, D practitioner consensus or a
  product rule with no direct evidence. A trailing qualifier is allowed
  (`B (direction); D (exact number)`). `contested: true` is independent of the
  letter.
- `lane` -- the verification culture the item was graded under (for example
  `@performance-lit`, `@clinical-physio`, `@gym-craft`, `@meal-craft`).
- `locale` -- `universal` or a jurisdiction such as `KR`.
- `as_of` -- the date or range of the underlying evidence.
- `sources` -- the sources, each with a note on what was read (abstract, full
  text, registry record). Entries of the form `<domain>/<slug>-NNN` point to
  other items.
- `applicability.axes`, `refraction_notes` -- optional: which user facts change
  the answer, and graded adjustments for them.
- `claim`, `reasoning` -- the prose payload. Rule items also carry an
  engine-readable block (`*_rules`) whose field names are the product's.

A reference to an item in a module that is not published here is written as
`<module> item NNN (module not published)`.

## Manifest and hashes

`modules.json` has `schema_version`, `min_resolver` and one entry per module:
`id`, `path`, `version` (semver, equal to the top release in the module's
`CHANGELOG.yaml`), `published`, `sha256`, `updated_at`, `files` and
`license`.

`sha256` is the content hash of the module tree: for each file in bytewise
sorted relative-path order, the line `<sha256 of the file>  <relative path>\n`;
the hash of those lines concatenated. Check it with:

```
python3 tools/verify_manifest.py .
```

or, inside `modules/<id>`:

```
find . -type f ! -path '*/.*' ! -path '*/__pycache__/*' | sed 's#^\./##' \
  | LC_ALL=C sort | while IFS= read -r f; do shasum -a 256 "$f"; done \
  | shasum -a 256
```

## Changelogs

Each module's `CHANGELOG.yaml` lists releases newest first, with the ids that
were `added`, `changed` or `retracted` and any grade transitions. A consumer
that caches items can diff these lists against what it holds and re-read only
the ids that moved.

## License

- Knowledge content (`modules/`, this README): Creative Commons Attribution
  4.0 International (CC BY 4.0), see `LICENSE`.
- Code (`tools/`): MIT, see `LICENSE-TOOLS`.

Cited papers, statutes and datasets remain under their own terms; items link to
them and quote at most single attributed sentences.
