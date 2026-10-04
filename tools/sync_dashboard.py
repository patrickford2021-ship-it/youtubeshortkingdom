# Theodore-only helper: copies episodes.json + calendar.json into dashboard.html
# so the dashboard works by double-clicking (no server, no installs for Patrick).
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "dashboard.html").read_text(encoding="utf-8")
def blob(p): return json.dumps(json.loads((root / p).read_text(encoding="utf-8")), ensure_ascii=False).replace("</", "<\\/")
for sid, path in [("db", "shows/trailer-park-boys/episodes.json"), ("cal", "calendar/calendar.json")]:
    html, n = re.subn(r'(<script id="%s" type="application/json">).*?(</script>)' % sid,
                      lambda m: m.group(1) + blob(path) + m.group(2), html, flags=re.S)
    assert n == 1, sid
(root / "dashboard.html").write_text(html, encoding="utf-8")
print("dashboard synced")
