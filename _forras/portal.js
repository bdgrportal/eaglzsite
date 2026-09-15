/* ══════════════════════════════════════════════════════════════════════
   EAGLZ PORTÁL-RÉTEG, KARBANTARTÁSI BLOKK
   NEGYEDÉVENTE CSAK EZT A KÉT OBJEKTUMOT KELL ÁTNÉZNI, MÁST SEMMIT.
   Egyik érték sem egy konkrét pénzintézet ajánlata: mind tájékoztató
   piaci nagyságrend, és a látogató mindegyiket átállíthatja a csúszkán.
   ══════════════════════════════════════════════════════════════════════ */
var RATES = {
  advertised:  7.49,   /* jellemző hirdetett lakáshitel-kamat, %      */
  best:        5.59,   /* egyedi bírálattal elérhető kamat, %         */
  otthonStart: 3.00,   /* Otthon Start fix kamata, jogszabályból      */
  savingYield: 6.00,   /* megtakarítás tájékoztató éves hozama, %     */
  updated: '2026. szeptember'
};

/* a menüszerkezet: egy sor egy menüpont */
var _BANKS = ['otp-bank','erste','kandh','mbh-bank','cib-bank','raiffeisen','unicredit'];
var _INSUR = ['generali','groupama','uniqa','union','alfa','signal-iduna','metlife','mapfre'];
var _LTP   = ['fundamenta','otp-bank','erste'];

var NAV = [
{ key:'hitel', label:'Lakásfinanszírozás',
  side:{ h:'Egy igénylés, hét nagybank',
         p:'Nem egy pénzintézetnél nézünk körül, hanem az egész piacon. Az ajánlatokat egymás mellé tesszük, és azt visszük végig, amelyik neked a legkedvezőbb. <b>A munkánk díjmentes.</b>',
         bt:'Hitelkalkulátorok', bh:'kalkulator.html', logos:_BANKS },
  items:[
    {i:'🧮', t:'Lakáshitel kalkulátor',   m:'Hirdetett és egyedi kamat',      h:'kalkulator.html'},
    {i:'🔁', t:'Hitelkiváltás',           m:'Mennyit hoz a meglévő hiteleden?', h:'kalkulator.html'},
    {i:'📊', t:'Mennyi hitelt kaphatok?', m:'JTM, az MNB szabálya szerint',   h:'kalkulator.html'},
    {i:'🔑', t:'Otthon Start 3%',         m:'Jár nekem? 2 perces kvíz',       h:'kviz.html', tag:'ÚJ', tagc:'new'},
    {i:'🗺️', t:'A lakáshitel folyamata',  m:'Mi történik és mikor',           h:'lakashitel-folyamat.html'},
    {i:'📅', t:'Időpontot foglalok',      m:'Válassz tanácsadót',             h:'#advisors'}
  ]},
{ key:'bank', label:'Banki termékek',
  side:{ h:'0 forintos számlavezetés',
         p:'A bankszámla a leggyorsabban javítható tétel a családi költségvetésben. Évi <b>20-100 ezer forint</b> maradhat a zsebedben, a váltás pedig törvény szerint díjmentes.',
         bt:'Bankszámla-díjkimutatás', bh:'https://online.ovb.hu/bankszamladijkimutatas/', logos:_BANKS },
  items:[
    {i:'🏦', t:'Díjmentes bankszámlák',   m:'A 2026 őszi ajánlatok',          h:'bankszamla.html', tag:'ÚJ', tagc:'new'},
    {i:'📄', t:'Online díjkimutatás',     m:'Az OVB hivatalos felületén',     h:'https://online.ovb.hu/bankszamladijkimutatas/'},
    {i:'🔄', t:'Számlaváltás lépésenként',m:'13 munkanap, díjmentesen',       h:'bankszamla.html#valasztas'},
    {i:'💳', t:'Személyi kölcsön',        m:'Jó és rossz kamat különbsége',   h:'kalkulator.html'},
    {i:'💠', t:'Csoportos beszedések',    m:'Online átvezetés',               h:'https://online.ovb.hu/csob/'},
    {i:'📅', t:'Időpontot foglalok',      m:'Válassz tanácsadót',             h:'#advisors'}
  ]},
{ key:'megtak', label:'Megtakarítás',
  side:{ h:'Előbb a cél, utána a termék',
         p:'Először az derül ki, mire és mikor kell a pénz, és csak utána, hogy milyen formában. <b>Egy eszköz sem jó mindenre</b>, és ezt meg is mondjuk.',
         bt:'Befektetés és TBSZ', bh:'befektetesek.html', logos:_LTP },
  items:[
    {i:'🐖', t:'Lakástakarék',            m:'Megéri még támogatás nélkül?',   h:'lakastakarek.html', tag:'ÚJ', tagc:'new'},
    {i:'📦', t:'Befektetés, TBSZ',        m:'Adómentes hozam 5 év után',      h:'befektetesek.html', tag:'ÚJ', tagc:'new'},
    {i:'🌅', t:'Nyugdíj-megtakarítás',    m:'20% adó-visszatérítéssel',       h:'nyugdij.html', tag:'ÚJ', tagc:'new'},
    {i:'👶', t:'Gyermek-megtakarítás',    m:'Babakötvény, oktatási alap',     h:'gyermekjovo.html', tag:'ÚJ', tagc:'new'},
    {i:'📈', t:'Megtakarítás-kalkulátor', m:'Mennyi lesz belőle?',            h:'#hero'},
    {i:'📅', t:'Időpontot foglalok',      m:'Válassz tanácsadót',             h:'#advisors'}
  ]},
{ key:'tamog', label:'Támogatások',
  side:{ h:'Amit sokan nem is igényelnek',
         p:'Az otthonteremtési támogatások feltételrendszere évente változik. Átnézzük, mire vagy jogosult <b>most</b>, és milyen sorrendben érdemes igényelni.',
         bt:'Jogosultsági kvíz', bh:'kviz.html', logos:_BANKS.slice(0,5) },
  items:[
    {i:'🔑', t:'Otthon Start 3%',         m:'Fix kamat, 50 M Ft-ig',          h:'kviz.html', tag:'ÚJ', tagc:'new'},
    {i:'📋', t:'Támogatások áttekintés',  m:'Mi él 2026-ban és mi nem',       h:'tamogatasok.html', tag:'ÚJ', tagc:'new'},
    {i:'👨‍👩‍👧', t:'CSOK Plusz',              m:'Gyermekvállaláshoz kötött',      h:'tamogatasok.html#csokplusz'},
    {i:'🌾', t:'Falusi CSOK',             m:'Preferált kistelepüléseken',     h:'tamogatasok.html#falusi'},
    {i:'🍼', t:'Babaváró',                m:'Szabad felhasználású',           h:'tamogatasok.html#babavaro'},
    {i:'✅', t:'Jár nekem? kvíz',          m:'12 kérdés, 2 perc',              h:'kviz.html'}
  ]},
{ key:'bizt', label:'Biztosítások',
  side:{ h:'30+ biztosító egy kézben',
         p:'A biztosítás díja egyéni, ezért itt nincs kalkulátor. Ami van: <b>a teljes paletta átnézése</b>, és több terméknél azonnali online kötés, akár most.',
         bt:'Biztosítási útmutató', bh:'biztositasok.html', logos:_INSUR },
  items:[
    {i:'🚗', t:'Gépjármű-biztosítás',     m:'Online köthető, azonnal',        h:'https://ovbportal.hu/ovbphp/public/onlineKotesKGFB.php?hash=gentischer.richard'},
    {i:'🏠', t:'Lakásbiztosítás',         m:'Otthon, vagyon, felelősség',     h:'https://online.ovb.hu/lakasbiztositas-informaciok/'},
    {i:'🛡️', t:'Biztosítási áttekintés',  m:'Mit mikor érdemes kötni',        h:'biztositasok.html', tag:'ÚJ', tagc:'new'},
    {i:'❤️', t:'Élet és egészség',        m:'Családvédelem, hitelfedezet',    h:'biztositasok.html#szemelyi'},
    {i:'✈️', t:'Utasbiztosítás',          m:'Online köthető, azonnal',        h:'https://ovbportal.hu/ovbphp/public/onlineKotesUtasbiztositas.php?hash=gentischer.richard'},
    {i:'☂️', t:'Gépjármű-asszisztencia',  m:'Online köthető, azonnal',        h:'https://ovbportal.hu/ovbphp/public/onlineKotesAsszisztencia.php?hash=gentischer.richard'}
  ]},
{ key:'ceges', label:'Vállalati',
  side:{ h:'Cégeknek, vállalkozóknak',
         p:'Adóhatékony juttatás, kulcsember-biztosítás, céges vagyonvédelem és vállalkozói finanszírozás. <b>Egy kézben</b>, a magánpénzügyeiddel összehangolva.',
         bt:'Vállalati megoldások', bh:'vallalati.html', logos:_INSUR.slice(0,6) },
  items:[
    {i:'📊', t:'Vállalati áttekintés',    m:'Hitel, juttatás, védelem',       h:'vallalati.html', tag:'ÚJ', tagc:'new'},
    {i:'🏦', t:'Széchenyi Kártya Program',m:'Kedvezményes vállalkozói hitel', h:'vallalati.html#szechenyi'},
    {i:'🎁', t:'Cafeteria, juttatások',   m:'Adóhatékonyan, 2026-os keretek', h:'vallalati.html#cafeteria'},
    {i:'🏢', t:'Céges biztosítások',      m:'Telephely, gép, felelősség',     h:'vallalati.html#biztositas'},
    {i:'🤝', t:'Kulcsember-biztosítás',   m:'Ha a cég egy emberen múlik',     h:'vallalati.html#biztositas'},
    {i:'📋', t:'Céges átvilágítás',       m:'Díjmentes, kötelezettség nélkül',h:'#lead'}
  ]},
{ key:'ceg', label:'Rólunk', simple:true,
  items:[
    {i:'🎯', t:'Kinek segítünk?',        h:'#for-whom'},
    {i:'🗺️', t:'Hogyan dolgozunk?',      h:'#how'},
    {i:'⭐', t:'Miért mi?',              h:'#about'},
    {i:'🎬', t:'Ügyfélvélemények',       h:'#video-testimonial'},
    {i:'🏢', t:'Rólunk, röviden',        h:'#about'},
    {i:'❓', t:'Gyakori kérdések',       h:'#faq'},
    {i:'🚀', t:'Karrier az EAGLZ-nél',   h:'/karrier'}
  ]}
];

/* ══════════════════════════════════════════════════════════════════════
   INNENTŐL MŰKÖDÉS, ehhez nem kell hozzányúlni.
   ══════════════════════════════════════════════════════════════════════ */
(function(){
function el(id){ return document.getElementById(id); }
function huf(v){ return Math.round(v).toLocaleString('hu-HU') + ' Ft'; }
function hufM(v){ return (Math.round(v/100000)/10).toLocaleString('hu-HU') + ' M Ft'; }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

/* ── mega-menü kirajzolása ── */
/* A fololdali horgonyok (#advisors, #hero, ...) aloldalrol az index.html-re mutassanak. */
var IS_INDEX = /(^|\/)(index\.html)?$/.test(location.pathname);
function HREF(h){ return (!IS_INDEX && h.charAt(0) === '#') ? 'index.html' + h : h; }

var bar = el('mnav'), host = el('megaHost'), mob = el('mmobHost');
var barH = [], panH = [], mobH = [];
NAV.forEach(function(c, idx){
  if(c.simple){
    barH.push('<button type="button" class="sec" data-mega="'+c.key+'" aria-expanded="false">'+esc(c.label)+
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></button>');
    panH.push('<div class="mega simple" id="mega-'+c.key+'"><div class="mega-simple"><div class="mega-simple-in">'+
      c.items.map(function(it){
        var ext = it.ext ? ' target="_blank" rel="noopener"' : '';
        return '<a href="'+HREF(it.h)+'"'+ext+(it.ext?' class="ext"':'')+'><span class="i">'+it.i+'</span>'+esc(it.t)+(it.ext?' ↗':'')+'</a>';
      }).join('')+'</div></div></div>');
    return;   /* a mobil menuben az extra linkek kulon vannak */
  }
  barH.push('<button type="button" data-mega="'+c.key+'" aria-expanded="false">'+esc(c.label)+
    '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></button>');

  var items = c.items.map(function(it){
    var tag = it.tag ? '<span class="mega-tag '+(it.tagc||'')+'">'+esc(it.tag)+'</span>' : '';
    var ext = /^https?:/.test(it.h) ? ' target="_blank" rel="noopener"' : '';
    return '<a class="mega-item" href="'+HREF(it.h)+'"'+ext+'>'+
      '<span class="mega-ico">'+it.i+'</span>'+
      '<span class="mega-tx"><span class="mega-t">'+esc(it.t)+'</span><span class="mega-m">'+esc(it.m)+'</span></span>'+
      tag+'<span class="mega-arrow">›</span></a>';
  }).join('');

  var logos = (c.side.logos||[]).map(function(f){
    return '<span><img src="assets/logos/'+f+'.png" alt="" loading="lazy"></span>';
  }).join('');
  var sext = /^https?:/.test(c.side.bh) ? ' target="_blank" rel="noopener"' : '';

  panH.push('<div class="mega" id="mega-'+c.key+'"><div class="mega-in">'+
    '<div class="mega-list">'+items+'</div>'+
    '<div class="mega-side"><h4>'+esc(c.side.h)+'</h4><p>'+c.side.p+'</p>'+
    '<a class="mbtn" href="'+HREF(c.side.bh)+'"'+sext+'>'+esc(c.side.bt)+' →</a>'+
    '<div class="mega-logos">'+logos+'</div></div></div></div>');

  mobH.push('<details'+(idx===0?' open':'')+'><summary>'+esc(c.label)+'</summary><div class="mmob-sub">'+
    c.items.map(function(it){
      var ext = /^https?:/.test(it.h) ? ' target="_blank" rel="noopener"' : '';
      return '<a href="'+HREF(it.h)+'"'+ext+'>'+it.i+'  '+esc(it.t)+'</a>';
    }).join('')+'</div></details>');
});
bar.innerHTML = barH.join('');
host.innerHTML = panH.join('');
mob.innerHTML = mobH.join('') +
  '<div class="mmob-extra">'+
  '<a href="'+HREF('#for-whom')+'">Kinek?</a><a href="'+HREF('#how')+'">Hogyan?</a><a href="'+HREF('#about')+'">Miért mi?</a>'+
  '<a href="'+HREF('#video-testimonial')+'">Vélemények</a><a href="'+HREF('#about')+'">Rólunk</a><a href="'+HREF('#faq')+'">GYIK</a>'+
  '<a href="/karrier">Karrier</a></div>'+
  '<div class="mmob-foot"><a class="a1" href="'+HREF('#advisors')+'">Időpontot foglalok</a>'+
  '<a class="a2" href="'+HREF('#lead')+'">Kérek visszahívást</a></div>';

/* ── nyitás, zárás ── */
var scrim = el('megaScrim'), open = null, openedAt = 0, hoverT = null;
function close(){
  if(!open) return;
  el('mega-'+open).classList.remove('open');
  var b = bar.querySelector('[data-mega="'+open+'"]');
  b.classList.remove('open'); b.setAttribute('aria-expanded','false');
  scrim.classList.remove('open'); open = null;
}
function openPanel(k){
  if(open === k) return;
  close();
  el('mega-'+k).classList.add('open');
  var b = bar.querySelector('[data-mega="'+k+'"]');
  b.classList.add('open'); b.setAttribute('aria-expanded','true');
  scrim.classList.add('open'); open = k; openedAt = Date.now();
}
bar.querySelectorAll('[data-mega]').forEach(function(b){
  var k = b.dataset.mega;
  b.addEventListener('click', function(){
    clearTimeout(hoverT);
    if(open === k){ if(Date.now() - openedAt > 450) close(); return; }
    openPanel(k);
  });
  b.addEventListener('mouseenter', function(){
    clearTimeout(hoverT);
    hoverT = setTimeout(function(){ openPanel(k); }, open ? 0 : 130);
  });
  b.addEventListener('mouseleave', function(){ clearTimeout(hoverT); });
  b.addEventListener('focus', function(){ openPanel(k); });
});
scrim.addEventListener('click', close);
document.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
el('ehead').addEventListener('mouseleave', function(){ clearTimeout(hoverT); close(); });
host.addEventListener('click', function(e){ if(e.target.closest('a')) close(); });

/* ── mobil ── */
var burger = el('mburger'), mmob = el('mmob');
burger.addEventListener('click', function(){
  var o = mmob.classList.toggle('open');
  burger.classList.toggle('open', o);
  burger.setAttribute('aria-expanded', o ? 'true' : 'false');
  document.body.style.overflow = o ? 'hidden' : '';
});
mmob.addEventListener('click', function(e){
  if(e.target.closest('a')){ mmob.classList.remove('open'); burger.classList.remove('open'); document.body.style.overflow = ''; }
});

/* ── fejléc árnyék ── */
var head = el('ehead');
window.addEventListener('scroll', function(){
  head.classList.toggle('scrolled', window.scrollY > 8);
}, {passive:true});

/* ══════════ GYORSKALKULÁTOR ══════════ */
function pmt(P, r, n){ var i = r/100/12, m = n*12; return i === 0 ? P/m : P*i/(1-Math.pow(1+i,-m)); }
function paint(e){ e.style.setProperty('--p', (e.value-e.min)/(e.max-e.min)*100 + '%'); }
function slide(id, fmt, fn){
  var r = el(id), v = el(id+'_v');
  function show(){ paint(r); if(v) v.textContent = fmt(+r.value); fn(); }
  r.addEventListener('input', show); show();
}
function calcLoan(){
  var A = +el('w_amt').value, Y = +el('w_yrs').value;
  var m1 = pmt(A, RATES.advertised, Y), m2 = pmt(A, RATES.best, Y);
  el('w_m1').textContent = huf(m1);
  el('w_m2').textContent = huf(m2);
  el('w_big').textContent = huf((m1-m2)*Y*12);
  el('w_sub').textContent = 'havi ' + huf(m1-m2) + ' különbség, ' + Y + ' éven át';
}
function calcSave(){
  var m = +el('s_amt').value, Y = +el('s_yrs').value, r = RATES.savingYield/100/12, n = Y*12;
  var fv = r === 0 ? m*n : m*((Math.pow(1+r,n)-1)/r)*(1+r), dep = m*n;
  el('s_dep').textContent = huf(dep);
  el('s_gain').textContent = '+' + huf(fv-dep);
  el('s_big').textContent = huf(fv);
  el('s_sub').textContent = Y + ' év alatt, ' + RATES.savingYield.toFixed(2).replace('.',',') + '% tájékoztató éves hozammal';
}
slide('w_amt', hufM, calcLoan);
slide('w_yrs', function(v){ return v + ' év'; }, calcLoan);
slide('s_amt', function(v){ return huf(v) + ' / hó'; }, calcSave);
slide('s_yrs', function(v){ return v + ' év'; }, calcSave);
var tabs = document.querySelectorAll('.hw-tabs button');
tabs.forEach(function(b){
  b.addEventListener('click', function(){
    tabs.forEach(function(x){ x.classList.remove('on'); });
    document.querySelectorAll('.hw-pane').forEach(function(p){ p.classList.remove('on'); });
    b.classList.add('on'); el('pane-'+b.dataset.pane).classList.add('on');
  });
});
document.querySelectorAll('[data-upd]').forEach(function(e){ e.textContent = RATES.updated; });
})();

/* ── hatter-video: csak szeles kepernyon, mozgascsokkentes nelkul ── */
(function(){
  var box = document.querySelector('.hero-video-bg[data-vimeo]');
  if(!box) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce || window.innerWidth < 1000) return;          /* mobilon allokep marad */
  function load(){
    if(box.querySelector('iframe')) return;
    var f = document.createElement('iframe');
    f.src = 'https://player.vimeo.com/video/' + box.dataset.vimeo +
            '?background=1&autoplay=1&muted=1&loop=1&byline=0&title=0';
    f.setAttribute('allow','autoplay; fullscreen');
    f.setAttribute('title','EAGLZ');
    f.setAttribute('tabindex','-1');
    f.setAttribute('aria-hidden','true');
    f.loading = 'lazy';
    f.addEventListener('load', function(){ f.classList.add('is-on'); });
    box.appendChild(f);
  }
  if('requestIdleCallback' in window) requestIdleCallback(load, {timeout:2200}); else setTimeout(load, 1200);
})();
