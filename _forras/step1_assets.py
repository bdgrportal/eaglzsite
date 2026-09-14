# -*- coding: utf-8 -*-
"""1. lepes: minden data: URI kiemelese fajlba, a HTML-ben utvonalra csereleve."""
import re, io, os, base64, hashlib

S = io.open('index.html', encoding='utf-8').read()
os.makedirs('assets', exist_ok=True)

# a mar kimentett fajlok tartalom-hash szerint, hogy beszedes nevuk maradjon
known = {}
for root, _, files in os.walk('assets'):
    for f in files:
        p = os.path.join(root, f)
        known[hashlib.md5(open(p, 'rb').read()).hexdigest()] = p.replace(os.sep, '/')

EXT = {'jpeg': 'jpg', 'svg+xml': 'svg', 'x-icon': 'ico'}
seen, n = {}, 0

def repl(m):
    global n
    uri = m.group(0)
    if uri in seen:
        return seen[uri]
    mm = re.match(r'data:image/([a-z+.-]+);base64,(.+)$', uri, re.S)
    if not mm:
        return uri
    try:
        raw = base64.b64decode(mm.group(2))
    except Exception:
        return uri
    h = hashlib.md5(raw).hexdigest()
    if h in known:
        path = known[h]
    else:
        n += 1
        ext = EXT.get(mm.group(1), mm.group(1))
        path = 'assets/img-%02d.%s' % (n, ext)
        open(path, 'wb').write(raw)
        known[h] = path
    seen[uri] = path
    return path

OUT = re.sub(r'data:image/[a-z+.-]+;base64,[A-Za-z0-9+/=\s]+?(?=["\')])', repl, S)

io.open('index_assets.html', 'w', encoding='utf-8').write(OUT)
print('eredeti: %d KB  ->  uj: %d KB' % (len(S) // 1024, len(OUT) // 1024))
print('kulon mentett uj kepek: %d' % n)
print('maradt data: URI:', OUT.count('data:image'))
