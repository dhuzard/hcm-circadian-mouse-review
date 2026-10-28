# HCM circadian mouse evidence review

Version 0.1.0 · abstract-level pilot · 28 October 2026

**Research question:** Which metadata and evidence elements are consistently
needed to interpret mouse home-cage circadian locomotor activity studies for
MNMS-style reuse?

Read the [pilot report](knowledge/oratlas/report.md), its
[traceability matrix](knowledge/oratlas/traceability.md), and the
[export provenance and skipped records](knowledge/oratlas/provenance.json).

This repository publishes the completed deterministic HCM pilot from
[murmuration](https://github.com/Neuronautix/murmuration). Its fixed corpus contains
five papers (PMIDs 39880968, 39371613, 39763604, 39296476 and 39534023). The pilot
extracts source-linked text and metadata from titles and abstracts. Publication
of this pilot does not establish peer review, full-method completeness or
cross-study comparability. HCMO and MNMS conformance are not assessed.

## Machine-readable review

The root [review-manifest.json](review-manifest.json) declares ORAtlas schema
1.0.0 and review type `ai-synthesis`, following murmuration's export contract.
The underlying pilot extraction and this export are deterministic and use no
model calls.

| Artifact | Exported records |
|---|---:|
| [Claims](knowledge/oratlas/claims.jsonl) | 58 |
| [Citations](knowledge/oratlas/citations.jsonl) | 5 |
| [Claim–citation relations](knowledge/oratlas/relations.jsonl) | 58 |

Relations use `unclear`: a recorded citation alone does not establish support.
No TRUST assessments are declared. The export skips 58 matrix rows: 44 metadata
rows absent verbatim from the report, 4 internal notes without scholarly
identifiers, and 10 notes without a matching citation at their report
occurrence. The provenance file identifies every skipped row and reason.

## Reproduce and ingest

The exact report, matrix and MAPPPP bundle used for export are frozen under
`source/run/`. The pilot specification and original run manifest are also
included. See [REPRODUCING.md](REPRODUCING.md) for the pinned exporter, commands
and validation. Regeneration makes no network or model calls.

From an ORAtlas checkout:

```sh
pnpm ingest https://github.com/dhuzard/hcm-circadian-mouse-review
```

The [v0.1.0 release](https://github.com/dhuzard/hcm-circadian-mouse-review/releases/tag/v0.1.0)
freezes this pilot for citation. No Zenodo DOI has been assigned; cite the release
URL and commit until an archival identifier is available.

## License

Original repository material is distributed under [MIT](LICENSE). Quotations
and bibliographic material from the cited papers retain their original authorship
and applicable licenses; the repository license does not relicense those works.
