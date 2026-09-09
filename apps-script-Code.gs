/**
 * Fen Lisesi Öğrenme Platformu — arka uç (Google Apps Script) · sürüm 4.0
 * Öğrenci kaydı (e-posta doğrulama + veli onayı), veli hesapları, PIN sıfırlama,
 * ilerleme/XP/rozet/liderlik, test kilidi, öğretmen paneli, haftalık özet ve hatırlatma mailleri.
 */

const VELI_PIN = '1999';   // ÖĞRETMEN / yönetici PIN'i (tüm öğrencileri görür). Değiştirirsen New version ile dağıt.
const TO = '';             // boş: yönetici raporları scripti dağıtan hesaba gider
const SITE_URL = 'https://fenlisesi9.netlify.app';
const EXEC_URL = 'https://script.google.com/macros/s/AKfycbw8VTyagXZXHCfXm4SAO73OP6yTJWAshco_J7Yhiptx7QrNQC-NFwAMXmG-ELhO2PLpuQ/exec';
const KOD_GECERLILIK_DK = 20, MAX_DENEME = 5, GUNLUK_KAYIT_LIMITI = 20;
const HATIRLATMA_GUN = 3;  // bu kadar gün girmeyen öğrenciye hatırlatma
const MAIL_EVENTS = ['quiz', 'week_done', 'kurulum_denemesi'];
const LEVELS = [[0, 'Çırak'], [200, 'Kalfa'], [600, 'Usta'], [1200, 'Fen Lisesi Şampiyonu']];
const WEEK_BONUS = 50, WEEK_SUBJECTS = 4;

/* ============ HTTP ============ */
function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.onay) return onayPage(p.onay);
  if (!p.d) return infoPage();
  let out; try { out = route(JSON.parse(p.d)); } catch (err) { out = { ok: false, error: String(err) }; }
  if (p.cb) return ContentService.createTextOutput(p.cb + '(' + JSON.stringify(out) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
  return ContentService.createTextOutput(JSON.stringify(out)).setMimeType(ContentService.MimeType.JSON);
}
function doPost(e) {
  const d = JSON.parse(e.postData.contents);
  if (d.action) return ContentService.createTextOutput(JSON.stringify(route(d))).setMimeType(ContentService.MimeType.JSON);
  handleReport(d); return ContentService.createTextOutput('ok');
}
function route(d) {
  switch (d.action) {
    case 'register': return register(d);
    case 'verify': return verify(d);
    case 'resend': return resend(d);
    case 'status': return regStatus(d);
    case 'login': return login(d);
    case 'progress': return saveProgress(d);
    case 'board': return { ok: true, board: leaderboard() };
    case 'forgot': return forgot(d);
    case 'resetpin': return resetPin(d);
    case 'velipin': return veliPinSet(d);
    case 'velilogin': return veliLogin(d);
    case 'veli': return veli(d);
    case 'velirapor': return veliRapor(d);
    case 'ogretmen': return ogretmenIslem(d);
    default: return { ok: false, error: 'bilinmeyen işlem' };
  }
}
function infoPage() { return html('Servis çalışıyor', 'Bu adres arka uç servisidir. Öğrenci sayfası: <a href="' + SITE_URL + '">' + SITE_URL + '</a>'); }
function html(title, body) {
  return HtmlService.createHtmlOutput('<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + title + '</title></head><body style="font-family:system-ui,Arial;max-width:520px;margin:40px auto;padding:20px;color:#14213d;line-height:1.5"><h2 style="color:#1b2f6e">' + title + '</h2><div style="font-size:16px">' + body + '</div></body></html>').setTitle(title);
}

/* ============ E-Tablo ============ */
const SCHEMA = {
  ogrenciler: ['id', 'ad', 'adKey', 'pinHash', 'kayit', 'sonGiris', 'eposta', 'veliEposta', 'epostaOnay', 'veliOnay', 'durum', 'sonHatirlatma'],
  bekleyen: ['id', 'ad', 'adKey', 'pinHash', 'eposta', 'veliEposta', 'kod', 'kodHash', 'token', 'epostaOnay', 'veliOnay', 'deneme', 'olusma'],
  veliler: ['eposta', 'pinHash', 'olusma', 'sonGiris'],
  tokenler: ['token', 'tur', 'ref', 'olusma'],
  ilerleme: ['key', 'id', 'paket', 'hafta', 'done', 'quizScore', 'quizOf', 'quizSubmitted', 'mini', 'miniOf', 'activeSec', 'ctxBonus', 'updated', 'kilit'],
  gunler: ['id', 'gun'],
  raporlar: ['zaman', 'id', 'ad', 'paket', 'event', 'json']
};
let _ss = null;
function db() {
  if (_ss) return _ss;
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('SHEET_ID'), ss = null;
  if (id) { try { ss = SpreadsheetApp.openById(id); } catch (e) { ss = null; } }
  if (!ss) { ss = SpreadsheetApp.create('Fen Lisesi 9 - Ogrenci Verileri'); props.setProperty('SHEET_ID', ss.getId()); }
  for (const name in SCHEMA) {
    let sh = ss.getSheetByName(name);
    if (!sh) { sh = ss.insertSheet(name); sh.appendRow(SCHEMA[name]); continue; }
    const have = sh.getRange(1, 1, 1, Math.max(1, sh.getLastColumn())).getValues()[0].filter(String);
    const missing = SCHEMA[name].filter(c => have.indexOf(c) < 0);
    if (missing.length) sh.getRange(1, have.length + 1, 1, missing.length).setValues([missing]);
  }
  _ss = ss; return ss;
}
function rows(name) {
  const sh = db().getSheetByName(name), lr = sh.getLastRow(), lc = sh.getLastColumn();
  if (lr < 1) return [];
  const v = sh.getRange(1, 1, lr, lc).getValues(), h = v[0];
  return v.slice(1).map((r, i) => { const o = { _row: i + 2 }; h.forEach((k, j) => { if (k) o[k] = r[j]; }); return o; });
}
function headers(name) { const sh = db().getSheetByName(name); return sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]; }
function appendRow(name, obj) { const h = headers(name); db().getSheetByName(name).appendRow(h.map(k => obj[k] == null ? '' : obj[k])); }
function updateRow(name, rowNo, obj) { const h = headers(name); db().getSheetByName(name).getRange(rowNo, 1, 1, h.length).setValues([h.map(k => obj[k] == null ? '' : obj[k])]); }
function clearRow(name, rowNo) { const h = headers(name); db().getSheetByName(name).getRange(rowNo, 1, 1, h.length).clearContent(); }
function hash(s) { return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, 'ah9|' + s).map(b => ('0' + (b & 255).toString(16)).slice(-2)).join(''); }
function today() { return Utilities.formatDate(new Date(), 'Europe/Istanbul', 'yyyy-MM-dd'); }
function trTime(x) { return x ? new Date(x).toLocaleString('tr-TR', { timeZone: 'Europe/Istanbul' }) : '—'; }
function normName(s) { return String(s || '').trim().replace(/\s+/g, ' ').slice(0, 24); }
function normMail(s) { return String(s || '').trim().toLowerCase(); }
function validMail(s) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(s); }
function validPin(p) { return /^\d{4,6}$/.test(String(p || '')); }
function newCode() { return String(Math.floor(100000 + Math.random() * 900000)); }
function newToken() { return Utilities.getUuid().replace(/-/g, '') + Utilities.getUuid().replace(/-/g, '').slice(0, 8); }
function expired(iso) { return (Date.now() - new Date(iso).getTime()) > KOD_GECERLILIK_DK * 60000; }
function esc(x) { return String(x == null ? '' : x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function mail(to, subject, body) { MailApp.sendEmail({ to, subject, htmlBody: '<div style="font-family:system-ui,Arial;font-size:16px;color:#14213d;line-height:1.5">' + body + '<p style="color:#888;font-size:12px;margin-top:24px">Fen Lisesi Öğrenme Platformu · ' + SITE_URL + '</p></div>' }); }
function btn(url, text) { return '<p><a href="' + url + '" style="display:inline-block;background:#2f4aa8;color:#fff;padding:12px 20px;border-radius:8px;text-decoration:none;font-weight:700">' + text + '</a></p>'; }
function makeToken(tur, ref) { const t = newToken(); appendRow('tokenler', { token: t, tur, ref, olusma: new Date().toISOString() }); return t; }
function useToken(token, tur) {
  const r = rows('tokenler').find(x => x.token === token && x.tur === tur);
  if (!r) return null;
  clearRow('tokenler', r._row);
  if (expired(r.olusma)) return null;
  return r.ref;
}

/* ============ Kayıt ============ */
function register(d) {
  const ad = normName(d.ad), pin = String(d.pin || ''), ep = normMail(d.eposta), vep = normMail(d.veliEposta);
  if (ad.length < 2) return { ok: false, error: 'Takma ad en az 2 karakter olmalı.' };
  if (!/^\d{4}$/.test(pin)) return { ok: false, error: 'PIN 4 rakam olmalı.' };
  if (!validMail(ep)) return { ok: false, error: 'Geçerli bir e-posta adresi yaz.' };
  if (!validMail(vep)) return { ok: false, error: 'Geçerli bir veli e-posta adresi yaz.' };
  if (ep === vep) return { ok: false, error: 'Veli e-postası kendi adresinden farklı olmalı.' };
  const lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    const key = ad.toLocaleLowerCase('tr-TR'), ogr = rows('ogrenciler').filter(r => r.id);
    if (ogr.some(r => r.adKey === key)) return { ok: false, error: 'Bu takma ad alınmış. Başka bir ad seç.' };
    if (ogr.some(r => normMail(r.eposta) === ep)) return { ok: false, error: 'Bu e-posta ile zaten bir hesap var. Giriş yap ya da "PIN\'imi unuttum"u kullan.' };
    const bek = rows('bekleyen').filter(r => r.ad), t = today();
    if (bek.filter(r => normMail(r.veliEposta) === vep && String(r.olusma).slice(0, 10) === t).length >= GUNLUK_KAYIT_LIMITI) return { ok: false, error: 'Bu veli adresiyle bugün çok fazla kayıt denendi.' };
    bek.filter(r => r.adKey === key || normMail(r.eposta) === ep).forEach(r => clearRow('bekleyen', r._row));
    const id = Utilities.getUuid().slice(0, 8), kod = newCode(), token = newToken();
    appendRow('bekleyen', { id, ad, adKey: key, pinHash: hash(pin), eposta: ep, veliEposta: vep, kod: '', kodHash: hash(kod), token, epostaOnay: '', veliOnay: '', deneme: 0, olusma: new Date().toISOString() });
    mailKod(ep, ad, kod); mailVeli(vep, ad, ep, token);
    return { ok: true, pending: true, id, eposta: ep, veliEposta: vep };
  } finally { lock.releaseLock(); }
}
function pendingOf(id) { return rows('bekleyen').find(r => r.id === id && r.ad); }
function verify(d) {
  const p = pendingOf(d.id); if (!p) return { ok: false, error: 'Kayıt bulunamadı. Yeniden kayıt ol.' };
  if (expired(p.olusma) || Number(p.deneme) >= MAX_DENEME) return { ok: false, error: 'Kodun süresi doldu ya da deneme hakkı bitti. "Yeniden gönder"e bas.', expired: true };
  if (hash(String(d.kod || '').trim()) !== p.kodHash) { updateRow('bekleyen', p._row, Object.assign(p, { deneme: Number(p.deneme) + 1 })); return { ok: false, error: 'Kod hatalı. (' + (MAX_DENEME - Number(p.deneme) - 1) + ' hak kaldı)' }; }
  updateRow('bekleyen', p._row, Object.assign(p, { epostaOnay: new Date().toISOString() }));
  return finalize(p.id);
}
function resend(d) {
  const p = pendingOf(d.id); if (!p) return { ok: false, error: 'Kayıt bulunamadı.' };
  const kod = newCode(), upd = { kodHash: hash(kod), deneme: 0, olusma: new Date().toISOString() };
  if (!p.epostaOnay) mailKod(p.eposta, p.ad, kod);
  if (!p.veliOnay) { upd.token = newToken(); mailVeli(p.veliEposta, p.ad, p.eposta, upd.token); }
  updateRow('bekleyen', p._row, Object.assign(p, upd));
  return { ok: true, epostaOnay: !!p.epostaOnay, veliOnay: !!p.veliOnay };
}
function regStatus(d) {
  const p = pendingOf(d.id);
  if (!p) return rows('ogrenciler').some(r => r.id === d.id) ? { ok: true, done: true } : { ok: false, error: 'Kayıt bulunamadı.' };
  return { ok: true, done: false, epostaOnay: !!p.epostaOnay, veliOnay: !!p.veliOnay, expired: expired(p.olusma) };
}
function finalize(id) {
  const p = pendingOf(id); if (!p) return { ok: true, done: true };
  if (!(p.epostaOnay && p.veliOnay)) return { ok: true, done: false, epostaOnay: !!p.epostaOnay, veliOnay: !!p.veliOnay };
  if (!rows('ogrenciler').some(r => r.id === id)) {
    appendRow('ogrenciler', { id, ad: p.ad, adKey: p.adKey, pinHash: p.pinHash, kayit: new Date().toISOString(), sonGiris: new Date().toISOString(), eposta: p.eposta, veliEposta: p.veliEposta, epostaOnay: p.epostaOnay, veliOnay: p.veliOnay, durum: 'aktif', sonHatirlatma: '' });
    touchDay(id);
    mail(p.eposta, 'Hoş geldin, ' + p.ad + '!', '<p>Hesabın açıldı. Takma adın: <b>' + esc(p.ad) + '</b>. PIN\'ini hatırlayamazsan giriş ekranındaki "PIN\'imi unuttum" bağlantısı sana yardımcı olur.</p>' + btn(SITE_URL, 'Platforma git'));
  }
  clearRow('bekleyen', p._row);
  return { ok: true, done: true };
}
function onayPage(token) {
  const p = rows('bekleyen').find(r => r.token === token && r.ad);
  if (!p) return html('Bağlantı geçersiz', 'Bu onay bağlantısı kullanılmış ya da süresi dolmuş. Öğrenci "Yeniden gönder" derse yeni bağlantı gelir.');
  if (expired(p.olusma)) return html('Bağlantının süresi dolmuş', 'Öğrenci kayıt ekranından "Yeniden gönder" derse yeni bağlantı gelir.');
  updateRow('bekleyen', p._row, Object.assign(p, { veliOnay: new Date().toISOString(), token: 'kullanildi' }));
  const r = finalize(p.id);
  const vep = normMail(p.veliEposta), hasAcc = rows('veliler').some(v => normMail(v.eposta) === vep);
  let body = '<b>' + esc(p.ad) + '</b> (' + esc(p.eposta) + ') için veli onayı alındı.' + (r.done ? ' Hesap açıldı; öğrenci artık giriş yapabilir.' : ' Öğrenci e-postasına gelen kodu girdiğinde hesap açılacak.');
  if (hasAcc) body += '<p>Veli panelinde e-postan ve veli PIN\'inle bu öğrenciyi de göreceksin.</p>' + btn(SITE_URL + '/veli.html', 'Veli paneline git');
  else { const t = makeToken('velipin', vep); body += '<p><b>Son adım:</b> veli paneline girmek için kendine bir PIN belirle. Bu panelde yalnızca onayladığın öğrencileri görürsün; test sonuçları da bu adrese gelir.</p>' + btn(SITE_URL + '/veli.html?kur=' + t, 'Veli PIN\'imi belirle') + '<p style="color:#666;font-size:13px">Bağlantı ' + KOD_GECERLILIK_DK + ' dakika geçerli. Süresi dolarsa veli panelinde "PIN\'imi unuttum" ile yenisini alırsın.</p>'; }
  return html('Onaylandı — teşekkürler', body);
}
function mailKod(to, ad, kod) { mail(to, 'Doğrulama kodun: ' + kod, '<p>Merhaba <b>' + esc(ad) + '</b>,</p><p>Kaydını tamamlamak için bu kodu kayıt ekranına gir:</p><p style="font-size:34px;letter-spacing:8px;font-weight:700;color:#1b2f6e">' + kod + '</p><p style="color:#666;font-size:13px">Kod ' + KOD_GECERLILIK_DK + ' dakika geçerli. Bu kaydı sen yapmadıysan bu e-postayı yok say.</p>'); }
function mailVeli(to, ad, ep, token) { mail(to, 'Veli onayı: ' + ad + ' kaydoluyor', '<p>Merhaba,</p><p><b>' + esc(ad) + '</b> takma adlı öğrenci (' + esc(ep) + ') 9. sınıf Fen Lisesi Öğrenme Platformu\'na kaydolurken sizi veli olarak belirtti.</p><p>Onaylıyorsanız bağlantıya tıklayın; hesap ancak onayınızla açılır ve test sonuçları bu adrese gelir:</p>' + btn(EXEC_URL + '?onay=' + token, 'Onaylıyorum') + '<p style="color:#666;font-size:13px">Bağlantı ' + KOD_GECERLILIK_DK + ' dakika geçerli. Bu öğrenciyi tanımıyorsanız hiçbir şey yapmayın; hesap açılmaz.</p>'); }

/* ============ Giriş, PIN sıfırlama ============ */
function auth(d) {
  const list = rows('ogrenciler').filter(r => r.id);
  const r = d.id ? list.find(r => r.id === d.id) : list.find(r => r.adKey === normName(d.ad).toLocaleLowerCase('tr-TR') || (validMail(normMail(d.ad)) && normMail(r.eposta) === normMail(d.ad)));
  return r && r.pinHash === hash(String(d.pin || '')) ? r : null;
}
function login(d) {
  const r = auth(d); if (!r) return { ok: false, error: 'Takma ad / e-posta veya PIN hatalı.' };
  updateRow('ogrenciler', r._row, Object.assign(r, { sonGiris: new Date().toISOString() }));
  touchDay(r.id);
  return Object.assign({ ok: true }, profile(r.id, r.ad));
}
function forgot(d) {
  const ep = normMail(d.eposta); if (!validMail(ep)) return { ok: false, error: 'Geçerli bir e-posta yaz.' };
  const st = rows('ogrenciler').find(r => r.id && normMail(r.eposta) === ep);
  const vl = rows('veliler').find(r => normMail(r.eposta) === ep);
  if (st) { const t = makeToken('reset-ogr', st.id); mail(ep, 'PIN sıfırlama', '<p>Merhaba <b>' + esc(st.ad) + '</b>, PIN\'ini yenilemek için:</p>' + btn(SITE_URL + '/?sifirla=' + t, 'Yeni PIN belirle') + '<p style="color:#666;font-size:13px">' + KOD_GECERLILIK_DK + ' dakika geçerli. Sen istemediysen yok say.</p>'); }
  if (!vl && rows('ogrenciler').some(r => r.id && normMail(r.veliEposta) === ep)) { const t = makeToken('velipin', ep); mail(ep, 'Veli PIN belirleme', '<p>Veli panelinde onayladığın öğrencileri görmek için bir PIN belirle:</p>' + btn(SITE_URL + '/veli.html?kur=' + t, 'Veli PIN\'imi belirle') + '<p style="color:#666;font-size:13px">' + KOD_GECERLILIK_DK + ' dakika geçerli.</p>'); }
  if (vl) { const t = makeToken('reset-veli', ep); mail(ep, 'Veli PIN sıfırlama', '<p>Veli paneli PIN\'ini yenilemek için:</p>' + btn(SITE_URL + '/veli.html?sifirla=' + t, 'Yeni veli PIN\'i belirle') + '<p style="color:#666;font-size:13px">' + KOD_GECERLILIK_DK + ' dakika geçerli.</p>'); }
  return { ok: true, message: 'Bu adrese kayıtlı bir hesap varsa sıfırlama bağlantısı gönderildi.' };
}
function resetPin(d) {
  if (!validPin(d.pin)) return { ok: false, error: 'PIN 4-6 rakam olmalı.' };
  let ref = useToken(d.token, 'reset-ogr');
  if (ref) { const st = rows('ogrenciler').find(r => r.id === ref); if (!st) return { ok: false, error: 'Hesap bulunamadı.' }; updateRow('ogrenciler', st._row, Object.assign(st, { pinHash: hash(d.pin) })); return { ok: true, tur: 'ogrenci', ad: st.ad }; }
  ref = useToken(d.token, 'reset-veli');
  if (ref) { const v = rows('veliler').find(r => normMail(r.eposta) === ref); if (!v) return { ok: false, error: 'Hesap bulunamadı.' }; updateRow('veliler', v._row, Object.assign(v, { pinHash: hash(d.pin) })); return { ok: true, tur: 'veli', eposta: ref }; }
  return { ok: false, error: 'Bağlantı geçersiz ya da süresi dolmuş. "PIN\'imi unuttum" ile yenisini iste.' };
}

/* ============ Veli hesapları ============ */
function veliPinSet(d) {
  if (!validPin(d.pin)) return { ok: false, error: 'PIN 4-6 rakam olmalı.' };
  const ep = useToken(d.token, 'velipin'); if (!ep) return { ok: false, error: 'Bağlantı geçersiz ya da süresi dolmuş. Veli panelinde "PIN\'imi unuttum"u kullan.' };
  const v = rows('veliler').find(r => normMail(r.eposta) === ep);
  if (v) updateRow('veliler', v._row, Object.assign(v, { pinHash: hash(d.pin) })); else appendRow('veliler', { eposta: ep, pinHash: hash(d.pin), olusma: new Date().toISOString(), sonGiris: '' });
  return { ok: true, eposta: ep };
}
function veliAuth(d) {
  const ep = normMail(d.eposta), v = rows('veliler').find(r => normMail(r.eposta) === ep);
  return v && v.pinHash === hash(String(d.pin || '')) ? v : null;
}
function veliLogin(d) {
  const v = veliAuth(d); if (!v) return { ok: false, error: 'E-posta veya veli PIN hatalı.' };
  updateRow('veliler', v._row, Object.assign(v, { sonGiris: new Date().toISOString() }));
  return { ok: true, tur: 'veli', eposta: v.eposta, students: studentList(s => normMail(s.veliEposta) === normMail(v.eposta)) };
}
function isTeacher(d) { return String(d.vpin || '') === VELI_PIN; }
function veli(d) {
  if (isTeacher(d)) return { ok: true, tur: 'ogretmen', students: studentList(() => true) };
  const v = veliAuth(d); if (!v) return { ok: false, error: 'Yetki yok.' };
  return { ok: true, tur: 'veli', eposta: v.eposta, students: studentList(s => normMail(s.veliEposta) === normMail(v.eposta)) };
}
function canSee(d, id) { if (isTeacher(d)) return true; const v = veliAuth(d); if (!v) return false; const s = rows('ogrenciler').find(r => r.id === id); return !!s && normMail(s.veliEposta) === normMail(v.eposta); }
function veliRapor(d) {
  if (!canSee(d, d.id)) return { ok: false, error: 'Yetki yok.' };
  const list = rows('raporlar').filter(r => r.id === d.id && r.event === 'quiz').slice(-30).map(r => { const j = JSON.parse(r.json); return { zaman: r.zaman, paket: r.paket, score: j.quiz.score, of: j.quiz.of, items: j.quiz.items, session: j.session }; });
  return { ok: true, reports: list };
}
function studentList(pred) {
  const all = rows('ilerleme').filter(p => p.key), days = rows('gunler');
  return rows('ogrenciler').filter(o => o.id && pred(o)).map(o => {
    const s = computeStats(o.id, all, days), p = {};
    all.filter(x => x.id === o.id).forEach(x => p[x.paket] = { done: String(x.done || '').split(',').filter(Boolean).length, quizScore: Number(x.quizScore || 0), quizOf: Number(x.quizOf || 0), quizSubmitted: x.quizSubmitted, kilit: !!x.quizSubmitted, mini: Number(x.mini || 0), activeMin: Math.round(Number(x.activeSec || 0) / 60), updated: x.updated });
    return { id: o.id, ad: o.ad, eposta: o.eposta, veliEposta: o.veliEposta, kayit: o.kayit, sonGiris: o.sonGiris, xp: s.xp, level: s.level, streak: s.streak, badges: s.badges, totalMin: s.totalMin, progress: p };
  });
}
/* Öğretmen işlemleri: op = reopen | resetpin | delete */
function ogretmenIslem(d) {
  if (!isTeacher(d)) return { ok: false, error: 'Yetki yok.' };
  const st = rows('ogrenciler').find(r => r.id === d.id); if (!st) return { ok: false, error: 'Öğrenci bulunamadı.' };
  if (d.op === 'reopen') { const p = rows('ilerleme').find(x => x.key === st.id + '|' + d.paket); if (!p) return { ok: false, error: 'Kayıt yok.' }; updateRow('ilerleme', p._row, Object.assign(p, { quizSubmitted: '', kilit: '' })); return { ok: true, message: 'Test yeniden açıldı; öğrenci yeniden kaydedebilir. Eski puanı, yeni puan yüksekse güncellenir.' }; }
  if (d.op === 'resetpin') { forgot({ eposta: st.eposta }); return { ok: true, message: 'Öğrenciye PIN sıfırlama bağlantısı gönderildi.' }; }
  if (d.op === 'delete') {
    rows('ilerleme').filter(x => x.id === st.id).forEach(x => clearRow('ilerleme', x._row));
    rows('gunler').filter(x => x.id === st.id).forEach(x => clearRow('gunler', x._row));
    clearRow('ogrenciler', st._row); return { ok: true, message: 'Öğrenci ve ilerlemesi silindi (raporlar arşivde kaldı).' };
  }
  return { ok: false, error: 'bilinmeyen işlem' };
}

/* ============ İlerleme, puan, kilit ============ */
function touchDay(id) { const t = today(); if (!rows('gunler').some(g => g.id === id && String(g.gun) === t)) appendRow('gunler', { id, gun: t }); }
function streak(id, days) {
  const set = new Set(days.filter(g => g.id === id).map(g => String(g.gun))); let n = 0; const dt = new Date();
  for (; ;) { const s = Utilities.formatDate(dt, 'Europe/Istanbul', 'yyyy-MM-dd'); if (!set.has(s)) break; n++; dt.setDate(dt.getDate() - 1); }
  return n;
}
function saveProgress(d) {
  const r = auth(d); if (!r) return { ok: false, error: 'Giriş gerekli.' };
  const lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    const key = r.id + '|' + d.paket, cur = rows('ilerleme').find(x => x.key === key) || {};
    const locked = !!cur.quizSubmitted;
    const done = Array.from(new Set(String(cur.done || '').split(',').filter(Boolean).map(Number).concat(d.done || []))).sort((a, b) => a - b).join(',');
    const rec = { key, id: r.id, paket: d.paket, hafta: d.hafta || cur.hafta || '', done,
      quizScore: locked ? Number(cur.quizScore || 0) : Math.max(Number(cur.quizScore || 0), Number(d.quizScore || 0)), quizOf: d.quizOf || cur.quizOf || 10,
      quizSubmitted: locked ? cur.quizSubmitted : (d.quizSubmitted || ''), kilit: (locked || !!d.quizSubmitted) ? 'evet' : '',
      mini: Math.max(Number(cur.mini || 0), Number(d.mini || 0)), miniOf: d.miniOf || cur.miniOf || 3,
      activeSec: Math.max(Number(cur.activeSec || 0), Number(d.activeSec || 0)), ctxBonus: locked ? Number(cur.ctxBonus || 0) : Math.max(Number(cur.ctxBonus || 0), Number(d.ctxBonus || 0)), updated: new Date().toISOString() };
    if (cur._row) updateRow('ilerleme', cur._row, rec); else appendRow('ilerleme', rec);
    touchDay(r.id);
    return Object.assign({ ok: true, locked: !!rec.quizSubmitted, rejected: locked && !!d.quizSubmitted && d.quizSubmitted !== cur.quizSubmitted }, profile(r.id, r.ad));
  } finally { lock.releaseLock(); }
}
function packageXp(p) { const done = String(p.done || '').split(',').filter(Boolean).length; const quiz = Number(p.quizOf) ? Math.round(100 * Number(p.quizScore) / Number(p.quizOf)) : 0; return done * 10 + quiz + Number(p.mini || 0) * 5 + Number(p.ctxBonus || 0) * 5; }
function computeStats(id, all, days) {
  const mine = all.filter(p => p.id === id); let xp = 0; const weeks = {};
  mine.forEach(p => { xp += packageXp(p); if (p.quizSubmitted) weeks[p.hafta] = (weeks[p.hafta] || 0) + 1; });
  const fullWeeks = Object.keys(weeks).filter(w => weeks[w] >= WEEK_SUBJECTS); xp += fullWeeks.length * WEEK_BONUS;
  const st = streak(id, days), badges = [];
  if (mine.some(p => String(p.done).split(',').filter(Boolean).length >= 8)) badges.push({ k: 'ilk-adim', n: 'İlk Adım', d: 'Bir paketi baştan sona bitirdin.' });
  if (mine.some(p => Number(p.quizOf) && Number(p.quizScore) / Number(p.quizOf) >= 0.9)) badges.push({ k: 'tuzak-avcisi', n: 'Tuzak Avcısı', d: 'Bir testte %90 ve üzeri.' });
  if (fullWeeks.length) badges.push({ k: 'dort-dortluk', n: 'Dört Dörtlük', d: 'Bir haftanın dört dersini de tamamladın.' });
  if (st >= 3) badges.push({ k: 'seri', n: 'Seri Çalışan', d: st + ' gün üst üste çalıştın.' });
  const totalMin = mine.reduce((a, p) => a + Number(p.activeSec || 0), 0) / 60;
  if (totalMin >= 300) badges.push({ k: 'maratoncu', n: 'Maratoncu', d: '5 saatten fazla aktif çalışma.' });
  if (mine.filter(p => p.quizSubmitted).length >= 8) badges.push({ k: 'sinav-kurdu', n: 'Sınav Kurdu', d: '8 test kaydettin.' });
  let level = LEVELS[0][1], next = null; for (let i = 0; i < LEVELS.length; i++) if (xp >= LEVELS[i][0]) { level = LEVELS[i][1]; next = LEVELS[i + 1] ? LEVELS[i + 1][0] : null; }
  return { xp, level, next, streak: st, badges, fullWeeks, totalMin: Math.round(totalMin) };
}
function profile(id, ad) {
  const all = rows('ilerleme').filter(p => p.key), days = rows('gunler'), s = computeStats(id, all, days), progress = {};
  all.filter(p => p.id === id).forEach(p => progress[p.paket] = { done: String(p.done || '').split(',').filter(Boolean).map(Number), quizScore: Number(p.quizScore || 0), quizOf: Number(p.quizOf || 0), quizSubmitted: p.quizSubmitted || '', locked: !!p.quizSubmitted, mini: Number(p.mini || 0), activeSec: Number(p.activeSec || 0), xp: packageXp(p), hafta: p.hafta });
  return { id, ad, xp: s.xp, level: s.level, next: s.next, streak: s.streak, badges: s.badges, totalMin: s.totalMin, progress, board: leaderboard(all, days) };
}
function leaderboard(all, days) {
  all = all || rows('ilerleme').filter(p => p.key); days = days || rows('gunler');
  return rows('ogrenciler').filter(o => o.id).map(o => { const s = computeStats(o.id, all, days); return { id: o.id, ad: o.ad, xp: s.xp, level: s.level, streak: s.streak, badges: s.badges.length }; }).sort((a, b) => b.xp - a.xp).slice(0, 50);
}

/* ============ Rapor (paketten POST) ============ */
function handleReport(d) {
  const st = d.studentId ? rows('ogrenciler').find(r => r.id === d.studentId) : null, ad = st ? st.ad : (d.student || 'Bilinmeyen');
  let locked = false;
  if (st && d.paket) {
    const cur = rows('ilerleme').find(x => x.key === st.id + '|' + d.paket) || {};
    locked = !!cur.quizSubmitted && d.event === 'quiz' && d.quiz.submitted !== cur.quizSubmitted;
    appendRow('raporlar', { zaman: new Date().toISOString(), id: st.id, ad, paket: d.paket, event: locked ? 'quiz_reddedildi' : d.event, json: JSON.stringify(d) });
    if (!locked) { const ctx = (d.quiz.items || []).filter(i => i.tip === 'bağlam' && i.puan === 1).length; saveProgress({ id: st.id, pin: d.studentPin, paket: d.paket, hafta: d.hafta, done: d.session.done, quizScore: d.quiz.score, quizOf: d.quiz.of, quizSubmitted: d.quiz.submitted, mini: d.mini.score, miniOf: d.mini.of, activeSec: d.session.activeSec, ctxBonus: ctx }); }
  } else appendRow('raporlar', { zaman: new Date().toISOString(), id: '', ad, paket: d.paket || d.package, event: d.event, json: JSON.stringify(d) });
  if (!locked && MAIL_EVENTS.indexOf(d.event) >= 0) sendMail(d, ad, st);
}
function sendMail(d, ad, st) {
  const admin = TO || Session.getEffectiveUser().getEmail(); const tos = [admin];
  if (st && st.veliEposta && normMail(st.veliEposta) !== normMail(admin)) tos.push(st.veliEposta);
  const s = d.session, q = d.quiz, m = d.mini, pct = q.of ? Math.round(100 * q.score / q.of) : 0;
  const title = (d.event === 'quiz' ? 'Test kaydedildi' : d.event === 'week_done' ? 'Hafta tamamlandı' : 'Kurulum denemesi') + ' · ' + ad + ' · ' + d.package;
  const tabRows = (s.tabs || []).map(t => `<tr><td>${t.tab}</td><td style="text-align:right">${t.dk} dk</td></tr>`).join('');
  const qRows = (q.items || []).map(i => { const ok = i.puan === 1, open = i.tip === 'açık uçlu'; const bg = open ? '#eef2ff' : ok ? '#e6f6ec' : (i.cevap ? '#fde8e6' : '#f3f3f3'); return `<tr style="background:${bg}"><td>${i.n}</td><td>${esc(i.soru)}</td><td><b>${esc(i.cevap) || '—'}</b></td><td>${esc(i.dogru)}</td><td>${open ? 'elle değerlendir' : ok ? '✔' : (i.cevap ? '✘' : 'boş')}</td><td>${i.tip}</td></tr>`; }).join('');
  const body = `<h2 style="color:#1b2f6e">${title}</h2><table cellpadding="6" style="border-collapse:collapse"><tr><td><b>Öğrenci</b></td><td>${esc(ad)}</td></tr><tr><td><b>Başlangıç</b></td><td>${trTime(s.start)}</td></tr><tr><td><b>Son etkinlik</b></td><td>${trTime(s.lastActive || d.sent)}</td></tr><tr><td><b>Aktif çalışma</b></td><td>${s.active}</td></tr><tr><td><b>Tamamlanan bölümler</b></td><td>${(s.done || []).join(', ') || '—'} / 8</td></tr><tr><td><b>Mini test</b></td><td>${m.score} / ${m.of}</td></tr><tr><td><b>Test</b></td><td><b>${q.score} / ${q.of}</b> (%${pct})</td></tr></table>
  <h3 style="color:#1b2f6e">Bölümlere harcanan süre</h3><table cellpadding="5" border="1" style="border-collapse:collapse;border-color:#d5dbe8">${tabRows}</table>
  <h3 style="color:#1b2f6e">Cevaplar</h3><table cellpadding="5" border="1" style="border-collapse:collapse;border-color:#d5dbe8;font-size:13px"><tr style="background:#dfe7ff"><th>#</th><th>Soru</th><th>Öğrenci</th><th>Doğru</th><th></th><th>Tür</th></tr>${qRows}</table>`;
  tos.forEach(to => mail(to, title, body));
}

/* ============ Zamanlanmış: haftalık özet + hatırlatma ============ */
function haftalikOzet() {
  const ogr = rows('ogrenciler').filter(o => o.id), all = rows('ilerleme').filter(p => p.key), days = rows('gunler'), rap = rows('raporlar');
  const since = Date.now() - 7 * 86400000, byVeli = {};
  ogr.forEach(o => {
    const s = computeStats(o.id, all, days), dayCount = days.filter(g => g.id === o.id && new Date(g.gun).getTime() >= since - 86400000).length;
    const tests = rap.filter(r => r.id === o.id && r.event === 'quiz' && new Date(r.zaman).getTime() >= since).map(r => { const j = JSON.parse(r.json); return { paket: j.package, score: j.quiz.score, of: j.quiz.of }; });
    const line = `<tr><td><b>${esc(o.ad)}</b></td><td>${s.level} · ${s.xp} puan</td><td>${dayCount} gün</td><td>${s.streak}🔥</td><td>${tests.length ? tests.map(t => esc(t.paket.split('·')[0]) + ' ' + t.score + '/' + t.of).join('<br>') : '—'}</td></tr>`;
    const v = normMail(o.veliEposta); if (v) (byVeli[v] = byVeli[v] || []).push(line);
  });
  for (const v in byVeli) mail(v, 'Haftalık özet · ' + today(), '<p>Bu haftaki çalışma özeti:</p><table cellpadding="6" border="1" style="border-collapse:collapse;border-color:#d5dbe8"><tr style="background:#dfe7ff"><th>Öğrenci</th><th>Seviye</th><th>Çalışılan gün</th><th>Seri</th><th>Bu haftaki testler</th></tr>' + byVeli[v].join('') + '</table>' + btn(SITE_URL + '/veli.html', 'Veli paneli'));
}
function hatirlatma() {
  const ogr = rows('ogrenciler').filter(o => o.id), days = rows('gunler'), now = Date.now();
  ogr.forEach(o => {
    const last = days.filter(g => g.id === o.id).map(g => new Date(g.gun).getTime()).sort((a, b) => b - a)[0] || new Date(o.kayit).getTime();
    const idle = (now - last) / 86400000, sinceRem = o.sonHatirlatma ? (now - new Date(o.sonHatirlatma).getTime()) / 86400000 : 99;
    if (idle >= HATIRLATMA_GUN && sinceRem >= HATIRLATMA_GUN && o.eposta) {
      mail(o.eposta, 'Seni özledik, ' + o.ad, '<p>' + Math.floor(idle) + ' gündür platforma girmedin. 25 dakikalık bir bölüm serini geri getirir; her bölüm +10 puan.</p>' + btn(SITE_URL, 'Bugün bir bölüm bitir'));
      updateRow('ogrenciler', o._row, Object.assign(o, { sonHatirlatma: new Date().toISOString() }));
    }
  });
}
function kurTetikleyiciler() {
  ScriptApp.getProjectTriggers().forEach(t => { if (['haftalikOzet', 'hatirlatma'].indexOf(t.getHandlerFunction()) >= 0) ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('haftalikOzet').timeBased().onWeekDay(ScriptApp.WeekDay.SUNDAY).atHour(19).inTimezone('Europe/Istanbul').create();
  ScriptApp.newTrigger('hatirlatma').timeBased().everyDays(1).atHour(18).inTimezone('Europe/Istanbul').create();
  Logger.log('Tetikleyiciler kuruldu: Pazar 19:00 haftalık özet, her gün 18:00 hatırlatma.');
}

/* ============ Kurulum testi ============ */
function kurulumTesti() {
  const ss = db(); kurTetikleyiciler();
  mail(TO || Session.getEffectiveUser().getEmail(), 'Fen Lisesi Öğrenme Platformu kuruldu (s4.0)', 'Veri tablosu: <a href="' + ss.getUrl() + '">' + ss.getUrl() + '</a><br>Site: ' + SITE_URL + '<br>Öğretmen PIN: <b>' + VELI_PIN + '</b><br>Tetikleyiciler: Pazar 19:00 haftalık özet · her gün 18:00 hatırlatma.');
}
