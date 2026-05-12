#!/usr/bin/env python3
"""
Comprueba datePublished en el HTML de cada post Wix (misma lista que generate_wix_posts).
Siempre termina con código 0: imprime MISSING cuando no hay coincidencia o falla la red.

  python3 scripts/probe_wix_dates.py
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gw", ROOT / "scripts" / "generate_wix_posts.py")
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
SLUGS: list[str] = mod.SLUGS  # type: ignore[misc]

PAT = re.compile(r'"datePublished"\s*:\s*"([^"]+)"')


def main() -> None:
    base = "https://miguelmarengo1.wixsite.com/my-site/post/"
    for slug in SLUGS:
        url = base + slug
        try:
            r = subprocess.run(
                ["/usr/bin/curl", "-sL", "--max-time", "30", url],
                capture_output=True,
                text=True,
                timeout=45,
            )
            html = r.stdout or ""
            m = PAT.search(html)
            if m:
                print(f"{slug}\t{m.group(1)}")
            else:
                print(f"{slug}\tMISSING\t(exit {r.returncode})", file=sys.stderr)
                print(f"{slug}\tMISSING")
        except Exception as e:
            print(f"{slug}\tERROR\t{e}", file=sys.stderr)
            print(f"{slug}\tERROR")


if __name__ == "__main__":
    main()
