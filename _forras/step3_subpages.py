# -*- coding: utf-8 -*-
"""3. lepes: ugyanaz a portal-fejlec az aloldalakra is."""
import re, io, os, base64, hashlib

CSS = io.open('portal.css', encoding='utf-8').read()
JS  = io.open('portal.js',  encoding='utf-8').read()

# a fejlec csak a menut es a gyorskalkulator nelkuli reszt hasznalja -> a JS
# kalkulator-blokkja kimarad, ha nincs widget az oldalon
JS_NAV = JS.split('/* ══════════ GYORSKALKULÁTOR ══════════ */')[0] + \
         "document.querySelectorAll('[data-upd]').forEach(function(e){ e.textContent = RATES.updated; });\n})();\n"

HEAD = u'''<div class="ehead" id="ehead">
  <div class="uhead">
    <div class="uhead-in">
      <a href="index.html">← Főoldal</a>
      <a href="index.html#for-whom">Kinek?</a>
      <a href="index.html#why">Miért mi?</a>
      <a href="index.html#about">Rólunk</a>
      <a href="index.html#faq">GYIK</a>
      <a href="http://eaglzcareer.hu" target="_blank" rel="noopener">Karrier ↗</a>
      <span class="u-sep"></span>
      <a class="u-cta" href="index.html#advisors">📅 Díjmentes konzultáció</a>
    </div>
  </div>
  <div class="mhead">
    <div class="mhead-in">
      <a class="elogo" href="index.html" aria-label="EAGLZ Finance">
        <img src="assets/eaglz-lockup-nav.png" alt="EAGLZ">
        <span>powered by OVB Gentischer Direction</span>
      </a>
      <div class="mnav" id="mnav" role="navigation" aria-label="Fő navigáció"></div>
      <a class="mhead-cta" href="index.html#advisors">Időpontot foglalok →</a>
      <button class="mburger" id="mburger" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div id="megaHost"></div>
</div>
<div class="mega-scrim" id="megaScrim"></div>
<div class="mmob" id="mmob"><div id="mmobHost"></div></div>
'''

# az aloldalakon a horgonyok a fooldalra mutatnak
def fix_links(js):
    for a in ['#advisors', '#services', '#online', '#lead', '#hero']:
        js = js.replace("h:'%s'" % a, "h:'index.html%s'" % a)
        js = js.replace("bh:'%s'" % a, "bh:'index.html%s'" % a)
    js = js.replace("<a href=\"#for-whom\">", "<a href=\"index.html#for-whom\">")
    js = js.replace("<a href=\"#how\">",      "<a href=\"index.html#how\">")
    js = js.replace("<a href=\"#why\">",      "<a href=\"index.html#why\">")
    js = js.replace("<a href=\"#video-testimonial\">", "<a href=\"index.html#video-testimonial\">")
    js = js.replace("<a href=\"#about\">",    "<a href=\"index.html#about\">")
    js = js.replace("<a href=\"#faq\">",      "<a href=\"index.html#faq\">")
    js = js.replace("<a class=\"a1\" href=\"#advisors\">", "<a class=\"a1\" href=\"index.html#advisors\">")
    return js

KNOWN = {}
for root, _, files in os.walk('assets'):
    for f in files:
        p = os.path.join(root, f)
        KNOWN[hashlib.md5(open(p, 'rb').read()).hexdigest()] = p.replace(os.sep, '/')

EXT = {'jpeg': 'jpg', 'svg+xml': 'svg', 'x-icon': 'ico'}

for name in ['kalkulator.html', 'kviz.html', 'lakashitel-folyamat.html']:
    S = io.open(name, encoding='utf-8').read()

    # a) data: URI-k kiemelese (ugyanazokra a fajlokra mutatnak, mint a fooldalon)
    seen, extra = {}, [0]
    def repl(m):
        uri = m.group(0)
        if uri in seen: return seen[uri]
        mm = re.match(r'data:image/([a-z+.-]+);base64,(.+)$', uri, re.S)
        if not mm: return uri
        try: raw = base64.b64decode(mm.group(2))
        except Exception: return uri
        h = hashlib.md5(raw).hexdigest()
        if h in KNOWN:
            path = KNOWN[h]
        else:
            extra[0] += 1
            ext = EXT.get(mm.group(1), mm.group(1))
            path = 'assets/%s-%02d.%s' % (name.replace('.html',''), extra[0], ext)
            open(path,'wb').write(raw); KNOWN[h] = path
        seen[uri] = path
        return path
    S = re.sub(r'data:image/[a-z+.-]+;base64,[A-Za-z0-9+/=\s]+?(?=["\')])', repl, S)

    # b) CSS
    S = S.replace('</style>', '\n' + CSS + '\n</style>', 1)

    # c) regi nav csere
    i = S.index('<nav>')
    end = '</nav>'
    j = S.index(end, i) + len(end)
    # ha van utana mobile-menu blokk, az is menjen
    mm = S.find('<div class="mobile-menu"', j, j + 400)
    if mm != -1:
        j = S.index('</div>', S.index('</ul>', mm)) + len('</div>')
    S = S[:i] + HEAD + S[j:]

    # c/2) a regi hamburger-script arvan maradt, ki kell venni
    dead = '''<script>
(function(){
  var btn=document.getElementById('hamburger'), menu=document.getElementById('mobileMenu');
  btn.addEventListener('click',function(){menu.classList.toggle('open');});
  document.querySelectorAll('.mm-link').forEach(function(a){a.addEventListener('click',function(){menu.classList.remove('open');});});
})();
</script>'''
    if dead in S:
        S = S.replace(dead, '')
    else:
        print('   FIGYELEM: a regi hamburger-script nem talalhato:', name)

    # d) JS
    S = S.replace('</body>', '<script>\n' + fix_links(JS_NAV) + '\n</script>\n</body>', 1)

    import theme_inject, landing
    # landing-vaz: bizalmi sav a hero utan, kozbenso CTA a 3. szekcio utan
    b0 = S.index('<body'); b1 = S.index('</body>')
    body = landing.inject(S[b0:b1],
        landing.trust_bar(u'Adatok: <b data-upd></b>'),
        landing.mid_cta(u'Kérdésed van ehhez?', u'30 perc, és a saját számaidat látod, nem egy példát.',
                        u'Díjmentes, kötelezettség nélkül. Ha kiderül, hogy a mostani megoldásod jó, azt is megmondjuk.',
                        u'<a class="apt-btn-inner" href="index.html#advisors">📅 Időpontot foglalok</a>',
                        u'Válassz tanácsadót és időpontot'), after_section=2)
    S = S[:b0] + body + S[b1:]
    S = theme_inject.apply(S)
    io.open(name.replace('.html', '_portal.html'), 'w', encoding='utf-8').write(S)
    print('%-26s -> %-32s %4d KB (+%d kep)' % (name, name.replace('.html','_portal.html'), len(S)//1024, extra[0]))
