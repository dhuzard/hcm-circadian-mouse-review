"""Re-export the frozen pilot and attach its explicitly declared publishing metadata."""

import argparse
import json
from pathlib import Path

from automation.exporters.oratlas import canonical, check_export, export_oratlas


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=root)
    out = parser.parse_args().out
    publication = json.loads((root / "publication.json").read_text(encoding="utf-8"))
    result = export_oratlas(
        root / "source/run", out,
        repository_url=publication["repositoryUrl"], title=publication["title"],
        abstract=publication["abstract"], license=publication["license"],
        keywords=publication["keywords"],
    )
    manifest_path = out / "review-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["repository"]["releaseTag"] = publication["releaseTag"]
    manifest["publication"] = {
        "reviewUrl": publication["repositoryUrl"] + "/blob/" + publication["releaseTag"]
        + "/knowledge/oratlas/report.md"
    }
    manifest_path.write_bytes((canonical(manifest) + "\n").encode("utf-8"))
    provenance_path = out / manifest["artifacts"]["provenance"]
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    provenance["murmurationCommit"] = publication["murmurationCommit"]
    provenance_path.write_bytes((canonical(provenance) + "\n").encode("utf-8"))
    result["counts"] = check_export(out)
    print(canonical({"counts": result["counts"], "skippedRows": len(result["skipped"])}))


if __name__ == "__main__":
    main()
