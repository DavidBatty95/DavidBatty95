"""Create compact profile previews from the owner's recorded project GIFs.

Requires Pillow and an authenticated GitHub CLI. Run from the repository root:
    python3 scripts/prepare_media.py --gh /path/to/gh
"""

import argparse
import base64
import io
import json
import math
from pathlib import Path
import subprocess

from PIL import Image, ImageOps, ImageSequence


ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    ("Geoff-Sim", "docs/media/onboard-crowd.gif", "geoff-sim.gif"),
    ("Dougie-Sim", "docs/media/dougie/walking.gif", "dougie-sim.gif"),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gh", default="gh")
    args = parser.parse_args()
    manifest = []
    for repo, path, output in SOURCES:
        def api(endpoint, *options):
            return subprocess.check_output([args.gh, "api", endpoint, *options])

        commit = json.loads(api(f"repos/DavidBatty95/{repo}/commits/main"))["sha"]
        endpoint = f"repos/DavidBatty95/{repo}/contents/{path}?ref={commit}"
        metadata = json.loads(api(endpoint))
        blob = json.loads(api(f"repos/DavidBatty95/{repo}/git/blobs/{metadata['sha']}"))
        raw = base64.b64decode(blob["content"])
        source = Image.open(io.BytesIO(raw))
        frames, durations = [], []
        # Keep at most 48 frames while preserving the total playback duration.
        stride = max(1, math.ceil(source.n_frames / 48))
        for index, frame in enumerate(ImageSequence.Iterator(source)):
            duration = frame.info.get("duration", 100)
            if index % stride:
                durations[-1] += duration
                continue
            preview = ImageOps.pad(
                frame.convert("RGB"), (560, 350),
                method=getattr(Image, "Resampling", Image).LANCZOS, color="#0b1424",
            )
            frames.append(preview.quantize(colors=64))
            durations.append(duration)
        target = ROOT / "assets" / output
        frames[0].save(
            target, save_all=True, append_images=frames[1:],
            duration=durations, loop=0, optimize=True, disposal=2,
        )
        manifest.append({
            "file": f"assets/{output}", "repository": f"DavidBatty95/{repo}",
            "source_path": path, "commit": commit, "source_blob": metadata["sha"],
            "frames": len(frames), "duration_ms": sum(durations),
            "bytes": target.stat().st_size,
        })
        print(f"{output}: {len(frames)} frames, {target.stat().st_size:,} bytes")
    (ROOT / "assets" / "sources.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
