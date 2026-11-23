import csv
import pathlib
import re
import sys
from urllib.parse import urlsplit

path = pathlib.Path("data/network/network-flows.csv")
columns = ["id","category","name","host","port","protocol","execution_point","region","testability","purpose","reference"]
protocols = {"TCP", "HTTP", "HTTPS", "NTP", "UDP"}
testability = {"testable", "server-side flow", "wildcard required", "documentation only"}
with path.open(encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    assert reader.fieldnames == columns, "Schema mismatch"
    rows = list(reader)
assert 0 < len(rows) <= 5000
seen = set()
for line, r in enumerate(rows, 2):
    assert None not in r and all(v is not None and len(v) < 2000 for v in r.values()), line
    assert re.fullmatch(r"[a-z0-9-]+", r["id"]) and r["id"] not in seen, line
    seen.add(r["id"])
    assert r["protocol"] in protocols, line
    assert r["execution_point"] in {"DEVICE", "MDM_SERVER"}, line
    assert r["testability"] in testability, line
    assert 1 <= int(r["port"]) <= 65535, line
    host = r["host"]
    assert host and "://" not in host and "/" not in host and not any(c.isspace() for c in host), line
    if "*" in host or "<" in host or ">" in host:
        assert r["testability"] != "testable", line
    else:
        assert re.fullmatch(r"[A-Za-z0-9.:-]+", host), line
    if r["reference"]:
        url = urlsplit(r["reference"])
        assert url.scheme == "https" and url.hostname, line
print(f"Validated {len(rows)} catalogue entries")
