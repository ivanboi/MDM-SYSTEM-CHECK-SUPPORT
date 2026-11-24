"""Refresh public stable release metadata without building or modifying releases."""
import json
import os
import re
import urllib.request
from pathlib import Path

REPO = "ivanboi/MDM-SYSTEM-CHECK-SUPPORT"
ROOT = Path("releases.json")
RULES = {
    "android": (r"v(\d+\.\d+\.\d+)", {"MDM-SystemCheck.apk", "SHA256SUMS.txt"}),
    "windows": (r"windows-v(\d+\.\d+\.\d+)", {"MDM-SystemCheck-Windows-x64.zip", "SHA256SUMS-windows.txt"}),
    "macos": (r"macos-v(\d+\.\d+\.\d+)", {"MDM-SystemCheck-macOS.zip", "SHA256SUMS-macos.txt"}),
    "linux": (r"linux-v(\d+\.\d+\.\d+)", {"MDM-SystemCheck-Linux-x64.AppImage", "MDM-SystemCheck-Linux-x64.deb", "MDM-SystemCheck-Linux-x64.tar.gz", "SHA256SUMS-linux.txt", "SHA256SUMS-linux.txt.asc", "MDM-SystemCheck-public.asc"}),
}

def version(value):
    return tuple(map(int, value.split(".")))

def refresh(current, releases):
    for platform, (pattern, required) in RULES.items():
        matches = []
        for release in releases:
            m = re.fullmatch(pattern, release["tag_name"])
            if not m or release["draft"] or release["prerelease"]:
                continue
            matches.append((version(m[1]), m[1], release))
        if not matches:
            continue
        _, v, release = max(matches, key=lambda item: item[0])
        old = current["platforms"][platform]
        if version(v) < version(old["version"]):
            continue
        assets = {a["name"]: a for a in release["assets"]}
        if not required <= assets.keys():
            raise ValueError(f"Incomplete stable release: {release['tag_name']}")
        selected = []
        for name in sorted(required):
            a = assets[name]
            if not re.fullmatch(r"sha256:[0-9a-f]{64}", a.get("digest") or "") or a["size"] <= 0:
                raise ValueError(f"Invalid asset metadata: {name}")
            expected = f"https://github.com/{REPO}/releases/download/{release['tag_name']}/{name}"
            if a["browser_download_url"] != expected:
                raise ValueError(f"Unexpected URL: {name}")
            selected.append(dict(name=name, url=expected, size=a["size"], digest=a["digest"]))
        if v == old["version"]:
            if {a["name"]: (a["digest"], a["size"], a["url"]) for a in selected} != {a["name"]: (a["digest"], a["size"], a["url"]) for a in old["assets"]}:
                raise ValueError(f"Existing stable asset changed: {platform}")
            continue
        # Build numbers cannot be inferred reliably from a semantic version.
        build = re.search(r"\bbuild\s+(\d+)\b", release.get("body") or "", re.I)
        if not build:
            build = re.search(r"\b" + re.escape(v) + r"\+(\d+)\b", release.get("body") or "")
        if not build:
            raise ValueError(f"Missing explicit build number: {release['tag_name']}")
        current["platforms"][platform] = dict(version=v, build=int(build[1]), tag=release["tag_name"], url=release["html_url"], assets=selected)
    return current

def main():
    releases = []
    for page in range(1, 101):
        url = f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json", "User-Agent": "mdm-release-manifest"})
        with urllib.request.urlopen(req, timeout=30) as response:
            batch = json.load(response)
        releases.extend(batch)
        if len(batch) < 100:
            break
    else:
        raise RuntimeError("Release pagination limit reached")
    current = json.loads(ROOT.read_text())
    ROOT.write_text(json.dumps(refresh(current, releases), indent=2) + "\n")

if __name__ == "__main__":
    main()
