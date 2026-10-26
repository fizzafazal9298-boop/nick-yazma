/* ============================================================
NickUstası — Şekilli Nick Motoru (engine.js)
Tek paylaşılan motor: stil dönüşümleri, süsleyiciler,
sembol / emoji / kaomoji kütüphaneleri, kopyalama, sayaç.
Türkçe karakterler (ğ ü ş ı ö ç İ i) her stilde korunur:
Unicode karşılığı yoksa birleşik işaret (combining mark)
yöntemiyle üretilir; harf asla sessizce silinmez.
============================================================ */
'use strict';

/* ---------- Yardımcılar ---------- */
function cp(n) { return String.fromCodePoint(n);}

function graphemes(s) {
if (window.Intl && Intl.Segmenter) {
try {
const seg = new Intl.Segmenter('tr', { granularity: 'grapheme'});
return Array.from(seg.segment(s), x => x.segment);
} catch (e) { /* yedek yönteme düş */}
}
return Array.from(s);
}
function graphemeLength(s) { return graphemes(s).length;}

/* Türkçe harf -> [taban harf, eklenecek birleşik işaret] */
const TR_MAP = {
'ç': ['c', '̧'], 'ğ': ['g', '̆'], 'ş': ['s', '̧'],
'ö': ['o', '̈'], 'ü': ['u', '̈'], 'ı': ['i', null],
'Ç': ['C', '̧'], 'Ğ': ['G', '̆'], 'Ş': ['S', '̧'],
'Ö': ['O', '̈'], 'Ü': ['U', '̈'], 'İ': ['I', '̇'],
'I': ['I', null]
};

/* Matematik / blok stilleri için taban kod noktaları ve istisnalar */
const MATH_BASES = {
bold: { A: 0x1D400, a: 0x1D41A, d: 0x1D7CE},
italic: { A: 0x1D434, a: 0x1D44E, d: null, exc: { h: 'ℎ'}},
bolditalic: { A: 0x1D468, a: 0x1D482, d: null},
script: { A: 0x1D49C, a: 0x1D4B6, d: null, exc: {
B: 'ℬ', E: 'ℰ', F: 'ℱ', H: 'ℋ', I: 'ℐ', L: 'ℒ', M: 'ℳ', R: 'ℛ',
e: 'ℯ', g: 'ℊ', o: 'ℴ'}},
boldscript: { A: 0x1D4D0, a: 0x1D4EA, d: null},
fraktur: { A: 0x1D504, a: 0x1D51E, d: null, exc: {
C: 'ℭ', H: 'ℌ', I: 'ℑ', R: 'ℜ', Z: 'ℨ'}},
boldfraktur: { A: 0x1D56C, a: 0x1D586, d: null},
doublestruck: { A: 0x1D538, a: 0x1D552, d: 0x1D7D8, exc: {
C: 'ℂ', H: 'ℍ', N: 'ℕ', P: 'ℙ', Q: 'ℚ', R: 'ℝ', Z: 'ℤ'}},
sans: { A: 0x1D5A0, a: 0x1D5BA, d: 0x1D7E2},
sansbold: { A: 0x1D5D4, a: 0x1D5EE, d: 0x1D7EC},
sansitalic: { A: 0x1D608, a: 0x1D622, d: null},
sansbolditalic:{ A: 0x1D63C, a: 0x1D656, d: null},
mono: { A: 0x1D670, a: 0x1D68A, d: 0x1D7F6},
circled: { A: 0x24B6, a: 0x24D0, d: null},
negcircled: { A: 0x1F150, a: 0x1F150, d: null},
squared: { A: 0x1F130, a: 0x1F130, d: null},
negsquared: { A: 0x1F170, a: 0x1F170, d: null},
parenthesized: { A: null, a: 0x249C, d: null},
fullwidth: { A: 0xFF21, a: 0xFF41, d: 0xFF10}
};

function mathChar(ch, kind) {
const cfg = MATH_BASES[kind];
if (!cfg) return ch;
if (cfg.exc && cfg.exc[ch]) return cfg.exc[ch];
let base = ch, mark = null;
if (TR_MAP[ch]) { base = TR_MAP[ch][0]; mark = TR_MAP[ch][1];}
if (cfg.exc && cfg.exc[base]) return mark ? cfg.exc[base] + mark : cfg.exc[base];
/* ı için italik stilde noktasız i karşılığı vardır */
if (ch === 'ı' && kind === 'italic') return '𝚤';
let out = null;
if (base >= 'A' && base <= 'Z') {
if (cfg.A!== null && cfg.A!== undefined) out = cp(cfg.A + base.charCodeAt(0) - 65);
} else if (base >= 'a' && base <= 'z') {
if (cfg.a!== null && cfg.a!== undefined) out = cp(cfg.a + base.charCodeAt(0) - 97);
} else if (base >= '0' && base <= '9') {
if (kind === 'circled') {
out = base === '0'? '⓪': cp(0x2460 + Number(base) - 1);
} else if (kind === 'parenthesized') {
out = base === '0'? '0': cp(0x2474 + Number(base) - 1);
} else if (cfg.d) {
out = cp(cfg.d + Number(base));
} else {
out = base;
}
}
if (out === null) out = base; /* üst simge yoksa harfin kendisi */
return mark? out + mark: out;
}

function mathStyle(kind) {
return function (text) {
return graphemes(text).map(g => {
if (g === ' ') return kind === 'fullwidth'? '　': ' ';
const first = Array.from(g)[0];
const rest = g.slice(first.length);
return mathChar(first, kind) + rest;
}).join('');
};
}

/* Küçük büyük harf (small caps) haritası */
const SMALLCAPS = {
a:'ᴀ',b:'ʙ',c:'ᴄ',d:'ᴅ',e:'ᴇ',f:'ꜰ',g:'ɢ',h:'ʜ',i:'ɪ',j:'ᴊ',k:'ᴋ',l:'ʟ',m:'ᴍ',
n:'ɴ',o:'ᴏ',p:'ᴘ',q:'ǫ',r:'ʀ',s:'ꜱ',t:'ᴛ',u:'ᴜ',v:'ᴠ',w:'ᴡ',x:'x',y:'ʏ',z:'ᴢ'
};
function smallCapsChar(ch) {
let base = ch, mark = null;
if (TR_MAP[ch]) { base = TR_MAP[ch][0]; mark = TR_MAP[ch][1];}
if (ch === 'ı') return 'ɪ';
if (ch === 'i') return 'ɪ' + '̇';
const low = base.toLowerCase();
const out = SMALLCAPS[low];
if (!out) return ch;
return mark? out + mark: out;
}

/* Üst simge (superscript) haritası */
const SUPERSCRIPT = {
a:'ᵃ',b:'ᵇ',c:'ᶜ',d:'ᵈ',e:'ᵉ',f:'ᶠ',g:'ᵍ',h:'ʰ',i:'ⁱ',j:'ʲ',k:'ᵏ',l:'ˡ',m:'ᵐ',
n:'ⁿ',o:'ᵒ',p:'ᵖ',q:'ᵠ',r:'ʳ',s:'ˢ',t:'ᵗ',u:'ᵘ',v:'ᵛ',w:'ʷ',x:'ˣ',y:'ʸ',z:'ᶻ',
A:'ᴬ',B:'ᴮ',D:'ᴰ',E:'ᴱ',G:'ᴳ',H:'ᴴ',I:'ᴵ',J:'ᴶ',K:'ᴷ',L:'ᴸ',M:'ᴹ',N:'ᴺ',
O:'ᴼ',P:'ᴾ',R:'ᴿ',T:'ᵀ',U:'ᵁ',V:'ⱽ',W:'ᵂ',
'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'
};
function superscriptChar(ch) {
if (SUPERSCRIPT[ch]) return SUPERSCRIPT[ch];
let base = ch, mark = null;
if (TR_MAP[ch]) { base = TR_MAP[ch][0]; mark = TR_MAP[ch][1];}
if (ch === 'ı') return 'ⁱ';
if (ch === 'i') return 'ⁱ' + '̇';
if (base === 'C') return 'ᶜ' + (mark || '');
if (base === 'F') return 'ᶠ' + (mark || '');
if (base === 'S') return 'ˢ' + (mark || '');
if (base === 'Y') return 'ʸ' + (mark || '');
if (base === 'Z') return 'ᶻ' + (mark || '');
const out = SUPERSCRIPT[base];
if (!out) return ch;
return mark? out + mark: out;
}

function dictStyle(dict, fn) {
return function (text) {
return graphemes(text).map(g => {
if (g === ' ') return ' ';
const first = Array.from(g)[0];
return fn(first) + g.slice(first.length);
}).join('');
};
}

/* Ters çevirme (upside-down) haritası */
const FLIP = {
a:'ɐ',b:'q',c:'ɔ',d:'p',e:'ǝ',f:'ɟ',g:'ƃ',h:'ɥ',i:'ᴉ',j:'ɾ',k:'ʞ',l:'ʅ',m:'ɯ',
n:'u',o:'o',p:'d',q:'b',r:'ɹ',s:'s',t:'ʇ',u:'n',v:'ʌ',w:'ʍ',x:'x',y:'ʎ',z:'z',
A:'∀',B:'𐐒',C:'Ɔ',D:'ᗡ',E:'Ǝ',F:'Ⅎ',G:'⅁',H:'H',I:'I',J:'ᒐ',K:'ʞ',L:'˥',
M:'W',N:'N',O:'O',P:'Ԁ',Q:'b',R:'ᴚ',S:'S',T:'⊥',U:'∩',V:'Λ',W:'M',X:'X',Y:'⅄',Z:'Z',
'0':'0','1':'Ɩ','2':'Ƨ','3':'Ɛ','4':'4','5':'Ƽ','6':'9','7':'ㄥ','8':'8','9':'6',
'.':'˙',',':"'",'?':'¿','!':'¡','(': ')',')':'(','[':']',']':'[','{':'}','}':'{',
'<':'>','>':'<','_':'‾',"'":',','&':'⅋'
};
function flipChar(ch) {
if (FLIP[ch]) return FLIP[ch];
let base = ch, mark = null;
if (TR_MAP[ch]) { base = TR_MAP[ch][0]; mark = TR_MAP[ch][1];}
if (ch === 'ı') return 'ı';
if (ch === 'İ') return 'I' + '̣';
const out = FLIP[base];
if (!out) return ch;
return mark? out + mark: out;
}
function upsideDown(text) {
return graphemes(text).map(g => {
const first = Array.from(g)[0];
return flipChar(first) + g.slice(first.length);
}).reverse().join('');
}
function reverseText(text) { return graphemes(text).reverse().join('');}

/* Birleşik işaret stilleri: harfin kendisi + işaret (Türkçe harfler aynen korunur) */
function combiningStyle(mark) {
return function (text) {
return graphemes(text).map(g => (g === ' '? g: g + mark)).join('');
};
}

/* Leet */
const LEET = { a:'4',b:'8',c:'(',e:'3',g:'9',i:'1',l:'1',o:'0',s:'5',t:'7',z:'2',
A:'4',B:'8',C:'(',E:'3',G:'9',I:'1',L:'1',O:'0',S:'5',T:'7',Z:'2',
'ı':'1','ş':'5','ğ':'9','ö':'0','ç':'('};
function leetStyle(text) {
return graphemes(text).map(g => LEET[g] || g).join('');
}
function spacedStyle(text) { return graphemes(text).join(' ');}

/* ---------- Stil listesi ---------- */
const STYLES = [
{ id: 'bold', name: 'Kalın', group: 'Klasik', fn: mathStyle('bold')},
{ id: 'italic', name: 'İtalik', group: 'Klasik', fn: mathStyle('italic')},
{ id: 'bolditalic', name: 'Kalın İtalik', group: 'Klasik', fn: mathStyle('bolditalic')},
{ id: 'script', name: 'El Yazısı', group: 'Klasik', fn: mathStyle('script')},
{ id: 'boldscript', name: 'Kalın El Yazısı', group: 'Klasik', fn: mathStyle('boldscript')},
{ id: 'fraktur', name: 'Gotik', group: 'Klasik', fn: mathStyle('fraktur')},
{ id: 'boldfraktur', name: 'Kalın Gotik', group: 'Klasik', fn: mathStyle('boldfraktur')},
{ id: 'doublestruck', name: 'Çift Çizgili', group: 'Klasik', fn: mathStyle('doublestruck')},
{ id: 'sans', name: 'Modern', group: 'Modern', fn: mathStyle('sans')},
{ id: 'sansbold', name: 'Modern Kalın', group: 'Modern', fn: mathStyle('sansbold')},
{ id: 'sansitalic', name: 'Modern İtalik', group: 'Modern', fn: mathStyle('sansitalic')},
{ id: 'sansbolditalic', name: 'Modern Kalın İtalik', group: 'Modern', fn: mathStyle('sansbolditalic')},
{ id: 'mono', name: 'Daktilo', group: 'Modern', fn: mathStyle('mono')},
{ id: 'circled', name: 'Balon', group: 'Çerçeveli', fn: mathStyle('circled')},
{ id: 'negcircled', name: 'Siyah Balon', group: 'Çerçeveli', fn: mathStyle('negcircled')},
{ id: 'squared', name: 'Kare', group: 'Çerçeveli', fn: mathStyle('squared')},
{ id: 'negsquared', name: 'Siyah Kare', group: 'Çerçeveli', fn: mathStyle('negsquared')},
{ id: 'parenthesized', name: 'Parantezli', group: 'Çerçeveli', fn: mathStyle('parenthesized')},
{ id: 'fullwidth', name: 'Geniş (Vapor)', group: 'Çerçeveli', fn: mathStyle('fullwidth')},
{ id: 'smallcaps', name: 'Küçük Büyük Harf', group: 'Küçük', fn: dictStyle(null, smallCapsChar)},
{ id: 'superscript', name: 'Minik Üst Yazı', group: 'Küçük', fn: dictStyle(null, superscriptChar)},
{ id: 'strike', name: 'Üstü Çizili', group: 'Efekt', fn: combiningStyle('̶')},
{ id: 'underline', name: 'Altı Çizili', group: 'Efekt', fn: combiningStyle('̲')},
{ id: 'dblunderline', name: 'Çift Altı Çizili', group: 'Efekt', fn: combiningStyle('̳')},
{ id: 'slash', name: 'Eğik Çizgili', group: 'Efekt', fn: combiningStyle('̸')},
{ id: 'wavunderline', name: 'Dalgalı Alt Çizgi', group: 'Efekt', fn: combiningStyle('̰')},
{ id: 'upside', name: 'Ters Çevrilmiş', group: 'Efekt', fn: upsideDown},
{ id: 'reverse', name: 'Tersten Yazılış', group: 'Efekt', fn: reverseText},
{ id: 'leet', name: 'Leet (1337)', group: 'Efekt', fn: leetStyle},
{ id: 'spaced', name: 'Aralıklı', group: 'Efekt', fn: spacedStyle}
];

/* ---------- Süsleyiciler ---------- */
const WRAPPERS = [
{ id: 'none', name: 'Süsleme yok', pre: '', post: ''},
{ id: 'star', name: 'Yıldızlı', pre: '★彡', post: '彡★'},
{ id: 'royal', name: 'Kraliyet Çerçevesi', pre: '꧁༺', post: '༻꧂'},
{ id: 'jp', name: 'Japon Köşeli', pre: '『', post: '』'},
{ id: 'boldbr', name: 'Kalın Köşeli', pre: ''},
{ id: 'crown', name: 'Taçlı', pre: '♛', post: '♛'},
{ id: 'heart', name: 'Kalpli', pre: '♡', post: '♡'},
{ id: 'fheart', name: 'Dolu Kalpli', pre: '♥', post: '♥'},
{ id: 'flower', name: 'Çiçekli', pre: '✿', post: '✿'},
{ id: 'spark', name: 'Parıltılı', pre: '✦', post: '✦'},
{ id: 'arrow', name: 'Oklu', pre: '➢', post: '➢'},
{ id: 'moon', name: 'Ay Süslemeli', pre: '☾', post: '☽'},
{ id: 'music', name: 'Notalı', pre: '♪', post: '♪'},
{ id: 'wing', name: 'Kanatlı', pre: '𓆩', post: '𓆪'},
{ id: 'bolt', name: 'Şimşekli', pre: '⚡', post: '⚡'},
{ id: 'cross', name: 'Haçlı', pre: '†', post: '†'}
];
const SEPARATORS = [
{ id: 'none', name: 'Ayraç yok', ch: ''},
{ id: 'star', name: 'Yıldız', ch: '★'},
{ id: 'heart', name: 'Kalp', ch: '♥'},
{ id: 'dot', name: 'Nokta', ch: '•'},
{ id: 'flower',name: 'Çiçek', ch: '✿'},
{ id: 'cross', name: 'Çarpı', ch: '×'},
{ id: 'spark', name: 'Parıltı', ch: '✦'},
{ id: 'crown', name: 'Taç', ch: '♛'}
];

function applyWrapper(text, wrapId) {
const w = WRAPPERS.find(x => x.id === wrapId) || WRAPPERS[0];
return w.pre + text + w.post;
}
function applySeparator(text, sepId) {
const s = SEPARATORS.find(x => x.id === sepId) || SEPARATORS[0];
if (!s.ch) return text;
return graphemes(text).join(s.ch);
}

/* Hazır kombinasyonlar: [stilId, wrapperId] çiftleri */
const COMBOS = [
['bold','star'], ['script','heart'], ['fraktur','royal'], ['doublestruck','crown'],
['circled','spark'], ['sansbold','jp'], ['smallcaps','boldbr'], ['mono','arrow'],
['bold','royal'], ['script','flower'], ['fraktur','cross'], ['doublestruck','star'],
['circled','heart'], ['sansbold','bolt'], ['boldscript','moon'], ['negsquared','royal'],
['bold','crown'], ['italic','spark'], ['fraktur','star'], ['sansbolditalic','jp'],
['script','royal'], ['bold','jp'], ['doublestruck','boldbr'], ['smallcaps','music'],
['mono','star'], ['circled','flower'], ['sans','crown'], ['boldfraktur','cross'],
['boldscript','fheart'], ['sansbold','star'], ['fraktur','moon'], ['doublestruck','spark'],
['bold','flower'], ['script','star'], ['negsquared','bolt'], ['bolditalic','heart'],
['mono','royal'], ['smallcaps','crown'], ['circled','royal'], ['sansitalic','moon'],
['bold','moon'], ['fraktur','jp'], ['doublestruck','heart'], ['script','jp'],
['sansbold','flower'], ['bold','bolt'], ['boldscript','spark'], ['squared','star'],
['bold','music'], ['italic','heart'], ['mono','jp'], ['sansbold','royal'],
['fraktur','fheart'], ['smallcaps','star'], ['bold','fheart'], ['doublestruck','jp'],
['script','crown'], ['sansbold','moon'], ['circled','bolt'], ['boldfraktur','royal']
];
const SEP_COMBOS = [
['bold','star'], ['sansbold','heart'], ['mono','dot'], ['smallcaps','flower'],
['script','spark'], ['bold','heart'], ['doublestruck','dot'], ['fraktur','cross'],
['sansbold','flower'], ['circled','star'], ['bolditalic','crown'], ['mono','heart'],
['boldscript','dot'], ['sans','spark'], ['bold','flower'], ['negsquared','dot'],
['italic','star'], ['fraktur','heart'], ['sansbolditalic','flower'], ['doublestruck','crown']
];

/* ---------- Sembol kütüphanesi ---------- */
const SYMBOLS = [
{ cat: 'Kalpler', items: ['♥','♡','❤','❥','❣','ღ','❧','❦','დ','♡̶']},
{ cat: 'Yıldızlar ve Parıltılar', items: ['★','☆','✦','✧','✩','✪','✫','✬','✭','✮','✯','✰','✡','✴','✵','✶','✷','✸','✹','✺','✻','✼','✽','✾','✟','☀','☼','✶','⋆','✧','✥','✤']},
{ cat: 'Taçlar ve Satranç', items: ['♔','♕','♖','♗','♘','♙','♚','♛','♜','♝','♞','♟','♠','♣','♦','♤','♧','♢','♡']},
{ cat: 'Oklar', items: ['→','←','↑','↓','↔','↕','↗','↘','↙','↖','↩','↪','➔','➜','➤','➢','➣','➥','➦','➧','➨','➩','➪','➫','➬','➭','➮','➯','➱','➲','➳','➴','➵','➶','➷','➸','➹','➺','➻','➼','➽','➾','⟶','⟹','⬅','⬆','⬇','⤴','⤵']},
{ cat: 'Çiçekler ve Doğa', items: ['✿','❀','❁','✽','✾','❃','❋','✼','❀','☘','❧','☙','❦','⚘','✾','❈','❉','❊','✱','✲','✳','✴','❄','❅','❆','☃','☂','☁','☾','☽','☼','☀','♨','⚡','☇','☈','☉']},
{ cat: 'Köşeler ve Çerçeveler', items: ['「','」','『','』','','〔','〕','〈','〉','《','》','«','»','‹','›','❰','❱','❮','❯','꧁','꧂','༺','༻','﴾','﴿','╭','╮','╰','╯','⌜','⌝','⌞','⌟','⟦','⟧','⟨','⟩']},
{ cat: 'Para Birimleri', items: ['₺','$','€','£','¥','¢','₽','₹','₩','฿','₴','₸','₼','₾','₿']},
{ cat: 'Matematik ve Bilim', items: ['∞','≠','≤','≥','±','×','÷','√','∑','∏','π','∆','∇','∈','∉','∀','∃','∅','∠','⊥','∥','∴','∵','≈','≡','Ω','µ','°','‰','§','¶','†','‡']},
{ cat: 'Müzik', items: ['♩','♪','♫','♬','♭','♮','♯','𝄞','𝄢','𝄡','𝄟','𝄾','𝄿','𝅝','𝅗𝅥','𝅘𝅥','𝅘𝅥𝅮']},
{ cat: 'Burçlar', items: ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']},
{ cat: 'Din ve Felsefe', items: ['✝','✞','✟','✠','✚','†','‡','☦','☪','✡','☮','☯','♰','♱','☸','ॐ','☤','☥','☦']},
{ cat: 'Şekiller ve Noktalar', items: ['■','□','▢','▣','▤','▥','▦','▧','▨','▩','▪','▫','●','○','◐','◑','◒','◓','◆','◇','◈','◉','◊','▲','△','▼','▽','►','◄','◢','◣','◤','◥','⬛','⬜','◘','◙','◚','◛']},
{ cat: 'Çizgiler ve Ayraçlar', items: ['─','│','┃','┄','┅','┆','┇','┈','┉','┊','┋','┌','┐','└','┘','├','┤','═','║','╔','╗','╚','╝','╠','╣','╦','╩','╬','━','┃','╱','╲','╳']},
{ cat: 'Popüler Nick Sembolleri', items: ['彡','〆','乂','乡','么','丶','丿','个','ッ','ツ','々','〤','ゝ','ヽ','ヾ','・','᭄','Ƭ','Ɩ','Ø','ø','Ł','ł','Đ','đ','꓄','꓅']},
{ cat: 'Oyun ve Tehlike', items: ['☠','☢','☣','⚠','⚔','⚓','⚰','⚱','♞','♜','☤','⚕','⚖','⚙','⚛','⚜','♱','☦','✞']},
{ cat: 'İletişim ve Nesneler', items: ['☎','☏','✆','✉','✈','☚','☛','☜','☝','☞','☟','✌','✍','✎','✏','✐','✑','✒','⌚','⌛','♻','⚑','⚐','✉','☑','☒','✓','✔','✗','✘','★']}
];
/* Yinelenenleri temizle, toplamı hesapla */
(function () {
const seen = new Set();
SYMBOLS.forEach(g => {
g.items = g.items.filter(s => { if (!s || seen.has(s)) return false; seen.add(s); return true;});
});
SYMBOLS.totalCount = seen.size;
})();

/* PUBG ve benzeri oyunlarda genelde sorunsuz çalışan semboller */
const SAFE_SYMBOLS = ['★','☆','♛','♜','♞','✿','❀','♪','♩','♫','☂','☀','☁','☃','♠','♣','♥','♦','♤','♡','•','彡','〆','×','々','ッ','ツ','Ø','ø','Ł','ł','Đ','đ','♚','♠','✦','➢','『','』',''];

/* ---------- Emoji kütüphanesi ---------- */
const EMOJIS = [
{ cat: 'Yüzler', items: ['😀','😁','😂','🤣','😊','😍','😘','😎','🤩','🥳','😏','😌','😴','🤤','😜','🤪','😝','🤑','🤠','😈','👿','💀','👻','👽','🤖','🎃','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🥺','😤','😡','🤯','🥶','🥵']},
{ cat: 'Kalpler', items: ['❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','💔','❣️','💕','💞','💓','💗','💖','💘','💝','💟','♥️','💌']},
{ cat: 'Eller ve Güç', items: ['👍','👎','👌','✌️','🤞','🤟','🤘','🤙','👊','✊','🙌','👏','👐','🤲','🙏','💪','🦾','🖖','👋','🤚','✋','🖐️','☝️','👆','👇','👈','👉']},
{ cat: 'Hayvanlar', items: ['🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🦁','🐯','🐸','🐵','🙈','🙉','🙊','🐷','🐔','🐧','🦄','🐲','🦅','🦉','🦇','🐺','🐗','🐴','🦋','🐞','🐢','🦖']},
{ cat: 'Oyun ve Spor', items: ['⚽','🏀','🏈','⚾','🎾','🏐','🏉','🎱','🏓','🏸','🥊','🎮','🕹️','🎲','🎯','🏆','🥇','🎧','🎸','⚔️','🛡️','🏹','🎣','🚀','🏎️','🏍️']},
{ cat: 'Yiyecek ve İçecek', items: ['🍔','🍟','🍕','🌭','🍿','🍩','🍪','🍫','🍬','🍭','🍓','🍉','🍇','🍒','🍑','🍍','🍎','🍐','🍊','🍋','🍌','🍨','🍦','🍰','🎂','🍯','☕','🧋']},
{ cat: 'Nesneler ve Simgeler', items: ['💎','👑','🔥','⭐','🌟','✨','⚡','💥','💯','🎁','🎈','🎉','⌚','📱','💻','🎧','🔑','💰','💸','🧲','🔫','💣','🗡️','🎭','🎨']},
{ cat: 'Doğa ve Hava', items: ['🌹','🌸','🌺','🌻','🌼','🌷','🍀','🌿','🌙','☀️','🌈','❄️','🔥','💧','🌊','🌍','🍁','🍂','🌵','🌴','⚡','🌪️']}
];
(function () {
const seen = new Set();
EMOJIS.forEach(g => { g.items = g.items.filter(s => { if (seen.has(s)) return false; seen.add(s); return true;});});
EMOJIS.totalCount = seen.size;
})();

/* ---------- Kaomoji (yazılı yüz ifadeleri) ---------- */
const KAOMOJI = [
{ cat: 'Mutlu', items: ['(•‿•)','(◕‿◕)','(◠‿◠)','(≧◡≦)','(｡♥‿♥｡)','(˶ᵔᵕᵔ˶)','(≧▽≦)','(◕ᴗ◕✿)','(✿◠‿◠)','(◕‿◕✿)','(^‿^)','(≧ω≦)']},
{ cat: 'Sevimli', items: ['(づ｡◕‿‿◕｡)づ','(づ￣ ³￣)づ','ʕ•ᴥ•ʔ','ʕᵔᴥᵔʔ','(ᵔᴥᵔ)','(っ˘ڡ˘ς)','(˵ ͡° ͜ʖ ͡°˵)','(◕‿◕)','(ꈍᴗꈍ)','(♡˙︶˙♡)']},
{ cat: 'Savaşçı ve Kararlı', items: ['ᕦ(ò_óˇ)ᕤ','(ง\'̀-\'́)ง','(ง •̀_•́)ง','ᕙ(⇀‸↼‶)ᕗ','(•̀o•́)ง','ᕙ( •̀ ᗜ •́)ᕗ','(ง\'̀-\'́)ง','ᕦ(ò_ó)ᕤ']},
{ cat: 'Umursamaz ve Havalı', items: ['¯\\_(ツ)_/¯','(¬‿¬)','(¬_¬)','( ͡° ͜ʖ ͡°)','(☞ ͡° ͜ʖ ͡°)☞','☜(ﾟヮﾟ☜)','(☞ﾟヮﾟ)☞','( •_•)>⌐■-■','(⌐■_■)','(ʘ‿ʘ)','(；一_一)','(¬‿¬)']},
{ cat: 'Üzgün ve Şaşkın', items: ['(╥﹏╥)','(T_T)','(ಥ﹏ಥ)','(︶︹︺)','( ಥ ʖ̯ ಥ)','(╯°□°）╯︵ ┻━┻','(⊙_⊙)','(°ロ°)','(•_•)','(⊙﹏⊙)']}
];
(function () {
const seen = new Set();
KAOMOJI.forEach(g => { g.items = g.items.filter(s => { if (seen.has(s)) return false; seen.add(s); return true;});});
KAOMOJI.totalCount = seen.size;
})();

/* ---------- Kopyalama ---------- */
function showToast(msg) {
let t = document.getElementById('copy-toast');
if (!t) {
t = document.createElement('div');
t.id = 'copy-toast';
t.className = 'toast';
document.body.appendChild(t);
}
t.textContent = msg || 'Kopyalandı ✓';
t.classList.add('show');
clearTimeout(t._h);
t._h = setTimeout(() => t.classList.remove('show'), 1400);
}
function copyText(text, el) {
const done = () => {
showToast('Kopyalandı ✓');
if (el) {
el.classList.add('copied');
setTimeout(() => el.classList.remove('copied'), 900);
}
};
if (navigator.clipboard && navigator.clipboard.writeText) {
navigator.clipboard.writeText(text).then(done).catch(() => fallbackCopy(text, done));
} else {
fallbackCopy(text, done);
}
}
function fallbackCopy(text, done) {
const ta = document.createElement('textarea');
ta.value = text;
ta.style.position = 'fixed';
ta.style.opacity = '0';
document.body.appendChild(ta);
ta.select();
try { document.execCommand('copy'); done();} catch (e) { showToast('Kopyalama başarısız');}
document.body.removeChild(ta);
}

/* Genel tıklayıp-kopyala bağlayıcısı: [data-copy] taşıyan her öğe */
document.addEventListener('click', function (e) {
const el = e.target.closest('[data-copy]');
if (el) { copyText(el.getAttribute('data-copy'), el);}
});

/* ---------- Ana üreteç (tool sayfaları) ---------- */
const state = { wrap: 'none', sep: 'none'};

function renderResults() {
const input = document.getElementById('nick-input');
const grid = document.getElementById('results');
if (!input ||!grid) return;
const cfg = window.PAGE_CFG || {};
const sample = cfg.sample || 'Şahin';
const raw = input.value.trim() === ''? sample: input.value.trim();
const limit = cfg.limit || 0;

/* Sayaç */
const counter = document.getElementById('char-count');
if (counter) {
const n = graphemeLength(input.value);
counter.textContent = limit? (n + ' / ' + limit + ' karakter'): (n + ' karakter');
counter.classList.toggle('over', limit > 0 && n > limit);
}

grid.innerHTML = '';
const frag = document.createDocumentFragment();
let curGrid = null;

function addCard(text, label) {
const card = document.createElement('button');
card.type = 'button';
card.className = 'result-card';
card.setAttribute('data-copy', text);
const tooLong = limit > 0 && graphemeLength(text) > limit;
if (tooLong) card.classList.add('too-long');
const span = document.createElement('span');
span.className = 'result-text';
span.textContent = text;
const tag = document.createElement('span');
tag.className = 'result-tag';
tag.textContent = tooLong? label + ' • limit dışı': label;
card.appendChild(span);
card.appendChild(tag);
(curGrid || frag).appendChild(card);
}
function addHeading(txt) {
const h = document.createElement('h3');
h.className = 'results-heading';
h.textContent = txt;
frag.appendChild(h);
curGrid = document.createElement('div');
curGrid.className = 'results-grid';
frag.appendChild(curGrid);
}

/* 1) Temel stiller (seçili süsleyici uygulanır) */
addHeading('Tüm Stiller');
STYLES.forEach(st => {
let t = st.fn(raw);
t = applySeparator(t, state.sep);
t = applyWrapper(t, state.wrap);
addCard(t, st.name);
});

/* 2) Hazır kombinasyonlar */
addHeading('Süslü Kombinasyonlar');
COMBOS.forEach(([sid, wid]) => {
const st = STYLES.find(x => x.id === sid);
const wr = WRAPPERS.find(x => x.id === wid);
addCard(wr.pre + st.fn(raw) + wr.post, st.name + ' + ' + wr.name);
});

/* 3) Ayraçlı stiller */
addHeading('Ayraçlı Stiller');
SEP_COMBOS.forEach(([sid, spid]) => {
const st = STYLES.find(x => x.id === sid);
const sp = SEPARATORS.find(x => x.id === spid);
addCard(applySeparator(st.fn(raw), spid), st.name + ' + ' + sp.name + ' ayracı');
});

grid.appendChild(frag);

const countEl = document.getElementById('result-count');
if (countEl) countEl.textContent = grid.querySelectorAll('.result-card').length + ' farklı stil üretildi';
}

function initGenerator() {
const input = document.getElementById('nick-input');
if (!input) return;
const cfg = window.PAGE_CFG || {};
if (!input.value && cfg.sample) input.value = cfg.sample;
input.addEventListener('input', renderResults);

const wrapSel = document.getElementById('wrap-select');
const sepSel = document.getElementById('sep-select');
if (wrapSel) {
WRAPPERS.forEach(w => {
const o = document.createElement('option');
o.value = w.id;
o.textContent = w.name + (w.pre? ' (' + w.pre + ' … ' + w.post + ')': '');
wrapSel.appendChild(o);
});
wrapSel.addEventListener('change', () => { state.wrap = wrapSel.value; renderResults();});
}
if (sepSel) {
SEPARATORS.forEach(s => {
const o = document.createElement('option');
o.value = s.id;
o.textContent = s.name + (s.ch? ' (' + s.ch + ')': '');
sepSel.appendChild(o);
});
sepSel.addEventListener('change', () => { state.sep = sepSel.value; renderResults();});
}

document.querySelectorAll('[data-fill]').forEach(chip => {
chip.addEventListener('click', () => {
input.value = chip.getAttribute('data-fill');
      input.dispatchEvent(new Event('input'));
renderResults();
input.focus();
});
});

renderResults();
}

/* ---------- Stil kütüphanesi sayfası (gruplu görünüm) ---------- */
function initStyleLibrary() {
const wrap = document.getElementById('style-groups');
if (!wrap) return;
const groups = {};
STYLES.forEach(st => { (groups[st.group] = groups[st.group] || []).push(st);});
const sampleInput = document.getElementById('nick-input');
function currentText() {
const v = sampleInput && sampleInput.value.trim();
return v || 'Şahin';
}
function draw() {
wrap.innerHTML = '';
Object.keys(groups).forEach(gname => {
const sec = document.createElement('section');
sec.className = 'lib-group';
const h = document.createElement('h2');
h.textContent = gname + ' Stiller';
sec.appendChild(h);
const grid = document.createElement('div');
grid.className = 'results-grid';
groups[gname].forEach(st => {
const t = st.fn(currentText());
const card = document.createElement('button');
card.type = 'button';
card.className = 'result-card';
card.setAttribute('data-copy', t);
card.innerHTML = '';
const s1 = document.createElement('span'); s1.className = 'result-text'; s1.textContent = t;
const s2 = document.createElement('span'); s2.className = 'result-tag'; s2.textContent = st.name;
card.appendChild(s1); card.appendChild(s2);
grid.appendChild(card);
});
sec.appendChild(grid);
wrap.appendChild(sec);
});
}
if (sampleInput) sampleInput.addEventListener('input', draw);
draw();
}

/* ---------- Harf tabloları (Şekilli Harfler sayfası) ---------- */
function initLetterTables() {
const wrap = document.getElementById('letter-tables');
if (!wrap) return;
const letters = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789'.split('');
const tableStyles = ['bold','script','fraktur','doublestruck','circled','smallcaps','superscript','sansbold','mono','fullwidth'];
tableStyles.forEach(sid => {
const st = STYLES.find(x => x.id === sid);
const sec = document.createElement('section');
sec.className = 'lib-group';
const h = document.createElement('h2');
h.textContent = st.name + ' Harfler';
sec.appendChild(h);
const grid = document.createElement('div');
grid.className = 'letter-grid';
letters.forEach(L => {
const t = st.fn(L);
const b = document.createElement('button');
b.type = 'button';
b.className = 'letter-cell';
b.setAttribute('data-copy', t);
const s1 = document.createElement('span'); s1.className = 'letter-big'; s1.textContent = t;
const s2 = document.createElement('span'); s2.className = 'letter-small'; s2.textContent = L;
b.appendChild(s1); b.appendChild(s2);
grid.appendChild(b);
});
sec.appendChild(grid);
wrap.appendChild(sec);
});
}

/* ---------- Sembol / emoji / kaomoji ızgaraları ---------- */
function fillSymbolGrids() {
document.querySelectorAll('[data-symbol-grid]').forEach(box => {
const src = box.getAttribute('data-symbol-grid');
let data = [];
if (src === 'all') data = SYMBOLS;
else if (src === 'safe') data = [{ cat: 'Oyunda Sorunsuz Çalışanlar', items: SAFE_SYMBOLS}];
else if (src === 'emoji') data = EMOJIS;
else if (src === 'kaomoji') data = KAOMOJI;
data.forEach(group => {
const sec = document.createElement('section');
sec.className = 'lib-group';
const h = document.createElement('h2');
h.textContent = group.cat;
sec.appendChild(h);
const grid = document.createElement('div');
grid.className = src === 'kaomoji'? 'kaomoji-grid': 'symbol-grid';
group.items.forEach(sym => {
const b = document.createElement('button');
b.type = 'button';
b.className = src === 'kaomoji'? 'kaomoji-cell': 'symbol-cell';
b.setAttribute('data-copy', sym);
b.textContent = sym;
b.title = 'Kopyala: ' + sym;
grid.appendChild(b);
});
sec.appendChild(grid);
box.appendChild(sec);
});
});
document.querySelectorAll('[data-symbol-count]').forEach(el => { el.textContent = SYMBOLS.totalCount;});
document.querySelectorAll('[data-emoji-count]').forEach(el => { el.textContent = EMOJIS.totalCount;});
document.querySelectorAll('[data-kaomoji-count]').forEach(el => { el.textContent = KAOMOJI.totalCount;});
}

/* ---------- Hazır nick listeleri ---------- */
function initNickLists() {
document.querySelectorAll('[data-nick-list]').forEach(box => {
const names = box.getAttribute('data-nick-list').split('|').map(s => s.trim()).filter(Boolean);
const styleIds = (box.getAttribute('data-list-styles') || 'bold,sansbold').split(',');
const wraps = (box.getAttribute('data-list-wraps') || 'none,star').split(',');
const grid = document.createElement('div');
grid.className = 'results-grid';
names.forEach((name, i) => {
const st = STYLES.find(x => x.id === styleIds[i % styleIds.length]) || STYLES[0];
const wr = WRAPPERS.find(x => x.id === wraps[i % wraps.length]) || WRAPPERS[0];
const t = wr.pre + st.fn(name) + wr.post;
const card = document.createElement('button');
card.type = 'button';
card.className = 'result-card';
card.setAttribute('data-copy', t);
const s1 = document.createElement('span'); s1.className = 'result-text'; s1.textContent = t;
const s2 = document.createElement('span'); s2.className = 'result-tag'; s2.textContent = name;
card.appendChild(s1); card.appendChild(s2);
grid.appendChild(card);
});
box.appendChild(grid);
});
}

/* ---------- Klan etiketi mini aracı ---------- */
function initClanTool() {
const input = document.getElementById('clan-input');
const out = document.getElementById('clan-results');
if (!input ||!out) return;
const templates = [
t => '', t => '『' + t + '』', t => '꧁' + t + '꧂',
t => '★' + t + '★', t => t + '・', t => '〆' + t, t => '♛' + t + '♛',
t => t + '࿐', t => '•' + t + '•', t => '༺' + t + '༻'
];
function draw() {
const v = input.value.trim() || 'EKİP';
out.innerHTML = '';
templates.forEach((tpl, i) => {
const t = tpl(v.toUpperCase());
const card = document.createElement('button');
card.type = 'button';
card.className = 'result-card';
card.setAttribute('data-copy', t);
const s1 = document.createElement('span'); s1.className = 'result-text'; s1.textContent = t;
const s2 = document.createElement('span'); s2.className = 'result-tag'; s2.textContent = 'Etiket şablonu ' + (i + 1);
card.appendChild(s1); card.appendChild(s2);
out.appendChild(card);
});
}
input.addEventListener('input', draw);
draw();
}

/* ---------- Boşluk aracı ---------- */
function initSpaceTool() {
const genBtn = document.getElementById('space-generate');
if (!genBtn) return;
const countInput = document.getElementById('space-count');
const typeSel = document.getElementById('space-type');
const outBox = document.getElementById('space-output');
genBtn.addEventListener('click', () => {
const n = Math.max(1, Math.min(500, parseInt(countInput.value, 10) || 10));
const ch = typeSel.value;
const text = ch.repeat(n);
outBox.value = text;
copyText(text, genBtn);
});
}

/* ---------- Başlat ---------- */
document.addEventListener('DOMContentLoaded', function () {
initGenerator();
initStyleLibrary();
initLetterTables();
fillSymbolGrids();
initNickLists();
initClanTool();
initSpaceTool();
});
