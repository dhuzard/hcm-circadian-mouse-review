# Reproduce version 0.1.0

The exporter is pinned to murmuration commit
`f14d167571a392979958fa4e2a8b33faf24b8d77` (merged PR #12). Python 3.10–3.12
passed the exporter project's CI at this commit.

Install this version of murmuration in your Python environment, then run from
this review repository:

```sh
python -m pip install "git+https://github.com/Neuronautix/murmuration.git@f14d167571a392979958fa4e2a8b33faf24b8d77"
python scripts/export_review.py
python -m automation.exporters.oratlas --check --out .
```

The script calls the exporter with the frozen source files and
`publication.json`, then adds the declared release tag, report URL and exporter
commit. These publishing metadata additions are deterministic. It never
modifies claim wording, citation identities, relations or skipped-row decisions.
`--out path/to/empty-directory` writes an independent copy for byte comparison.

Inputs:

- `source/run/final_report.md`: the existing completed HCM pilot report.
- `source/run/traceability.md`: the original run's traceability matrix.
- `source/run/mapppp_bundle.json`: source assertions and the existing run timestamp.
- `source/run/pilot_manifest.json`: fixed PMIDs, package ID and corpus digest.
- `source/pilot_spec.yaml`: the original pilot question and PMID list.

The original run was created by `automation.hcm_pilot.run_hcm_pilot`; this
publication reuses that run rather than fetching fresh abstracts or creating new
evidence. The exporter uses only the report, matrix and bundle. The input run
timestamp is 2026-10-28T10:39:17+00:00.

All generated JSON uses sorted keys, UTF-8, LF and a trailing newline. Claim and
citation IDs are derived from content. `--check` validates the manifest and
record shapes, normalized identifiers, safe artifact paths and relation endpoints.
The packaged upstream manifest JSON Schema is unmodified; its documented
in-memory `ai-synthesis` enum override remains necessary until ORAtlas PR #244
is released and the pinned schema is updated.
