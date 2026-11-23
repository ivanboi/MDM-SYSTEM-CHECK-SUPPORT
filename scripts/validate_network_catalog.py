"""Validate public network flow schema and Ed25519-signed publication manifests.

Use network-flows.csv + manifest as the *only live* catalogue.
Staged v6 files can coexist during client key rotation, but are not automatically active.
"""
import base64
import csv
import hashlib
import json
import pathlib
import re
from urllib.parse import urlsplit
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = pathlib.Path("data/network")
COLUMNS = ["id", "category", "name", "host", "port", "protocol",
           "execution_point", "region", "testability", "purpose", "reference"]
PROTOCOLS = {"TCP", "HTTP", "HTTPS", "NTP", "UDP"}
TESTABILITY = {"testable", "server-side flow", "wildcard required",
               "documentation only", "base domain only; subdomains vary"}
CATEGORIES = {
    "mdm:knox-manage", "mdm:intune", "mdm:workspace-one", "mdm:ivanti",
    "mdm:meraki", "mdm:citrix", "mdm:blackberry",
    "device:apple", "device:android", "device:rooms", "device:samsung",
    "device:windows", "device:macos", "device:vowifi",
    "device:motorola", "device:crosscall",
}
KEYS = {
    "legacy": "FB35t95FFpMxnYEMNuaP9w4d2XXbN2K0zO9GB7vlGhA=",
    "rotated": "ixWzwR3lwhP6DGEczGXrgfBHYHleboUi/dIyZZ3E56Q=",
}

def validate_csv(path: pathlib.Path) -> tuple[int, bytes]:
    raw = path.read_bytes()
    assert 0 < len(raw) <= 1048576, f"{path}: invalid size"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == COLUMNS, f"{path}: schema mismatch"
        rows = list(reader)
    assert 0 < len(rows) <= 5000, f"{path}: invalid record count"
    ids = set()
    for index, row in enumerate(rows, 2):
        assert None not in row and all(v is not None and len(v) < 2000 for v in row.values()), (path, index)
        assert re.fullmatch(r"[a-z0-9-]+", row["id"]) and row["id"] not in ids, (path, index)
        ids.add(row["id"])
        assert row["category"] in CATEGORIES, (path, index, "category")
        assert row["protocol"] in PROTOCOLS, (path, index, "protocol")
        assert row["execution_point"] in {"DEVICE", "MDM_SERVER"}, (path, index, "execution_point")
        assert row["testability"] in TESTABILITY, (path, index, "testability")
        assert row["execution_point"] != "MDM_SERVER" or row["testability"] != "testable", (path, index)
        assert 1 <= int(row["port"]) <= 65535, (path, index, "port")
        host = row["host"]
        assert host and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.:-]*", host), (path, index, "host")
        if row["reference"]:
            reference = urlsplit(row["reference"])
            assert reference.scheme == "https" and reference.hostname and not reference.username, (path, index)
    return len(rows), raw

def validate_signature(manifest_path: pathlib.Path, raw: bytes) -> int:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    version = manifest["version"]
    digest = manifest["sha256"]
    assert isinstance(version, int) and version > 0, manifest_path
    assert re.fullmatch("[a-f0-9]{64}", digest), manifest_path
    assert hashlib.sha256(raw).hexdigest() == digest, f"{manifest_path}: SHA mismatch"
    pub = KEYS["legacy" if version <= 5 else "rotated"]
    key = Ed25519PublicKey.from_public_bytes(base64.b64decode(pub))
    key.verify(base64.b64decode(manifest["signature"]), f"{version}\n{digest}\n".encode("utf-8"))
    return version

live_count, live_bytes = validate_csv(ROOT / "network-flows.csv")
live_version = validate_signature(ROOT / "network-flows.manifest.json", live_bytes)
print(f"Live signed catalogue v{live_version}: {live_count} records")

staged = ROOT / "network-flows-v6.csv"
if staged.exists():
    count, raw = validate_csv(staged)
    version = validate_signature(ROOT / "network-flows-v6.manifest.json", raw)
    assert version == 6 and count == 480, "The staged v6 snapshot must be immutable."
    assert live_version <= version, "A stale staged catalogue was left behind."
    print(f"Staged signed catalogue v{version}: {count} records")
