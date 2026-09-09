# Paket kalite kontrol listesi (her paket yayınlanmadan önce)

## İçerik
- [ ] Ünite/konu adı ve sırası `kit_yol_haritasi.md` ile birebir; MEB Maarif Modeli 9. sınıf programına uygun; uydurma kazanım kodu yok
- [ ] 8 sekme eksiksiz: Neden → Hatırlatma → Konu → Günlük yaşam → Etkileşim → Çözümlü → Kendini sına → Özet
- [ ] Hatırlatma: 3 aralıklı tekrar sorusu (geçen hafta / 2 hafta önce / köprü), `<span class="tag">…</span>` etiketiyle, anında geri bildirimli
- [ ] Konu anlatımında en az 1 simülasyon; Etkileşim sekmesinde en az 2; her simülasyonun `hint` metni ve "Bu simülasyon neyi gösteriyor?" kutusu var
- [ ] En az 3 (tercihen 4) günlük yaşam örneği: Durum → Kavramla bağ → Hesap/Analiz → Sonuç; Kocaeli/İzmit, bisiklet, mutfak, telefon, deprem bağlamları; kişi adı YOK ("bir öğrenci", "bir bisikletli")
- [ ] Çözümlü örnekler: 2 temel + 2 orta + 2 fen lisesi; her adımda "neden" (`<div class="why">`)
- [ ] Test: 12 çoktan seçmeli (4 temel · 5 orta · 3 fen lisesi) + 2 açık uçlu; en az 3 `tag:'bağlam'`; konu anlatımında geçmeyen olgu gerekiyorsa soru içinde `<b>Bilgi:</b>` bloğu; çeldiriciler tipik hatalardan; `a:0` doğru cevap (şablon karıştırır)
- [ ] Özet: 4 kart + "Sık yapılan 5 hata" + "Gelecek haftaya köprü"
- [ ] Sayısal hesaplar iki kez doğrulandı; birimler SI; TDK yazımı; "Ali Han" veya okul adı geçmiyor

## Teknik
- [ ] `python3 kit_ornek_*.py` benzeri script ile `kit_template.html` üzerinden üretildi; yer tutucu kalmadı
- [ ] JS söz dizimi: `node -e "const h=require('fs').readFileSync('X.html','utf8');const i=h.lastIndexOf('<script>');new Function(h.slice(i+8).split('</script>')[0])"` hatasız
- [ ] Dosya adı `ders-hNN.html` (mat/fiz/kim/biy), PAKET ve KEY aynı kodla; HAFTA doğru
- [ ] Tarayıcıda (390 px) 8 sekme açıldı, simülasyonlar hata vermedi, "Cevapları kaydet" kilitlendi
- [ ] `index.html` içindeki CATALOG'da haftanın 4 satırında `dosya:` dolduruldu; bir sonraki hafta "Yakında" satırlarıyla eklendi
- [ ] Depoya commit edildi; Netlify deploy "ready"; https://fenlisesi9.netlify.app/ açılıyor, yeni hafta kartı görünüyor
- [ ] Notion "Ders Paketleri" satırları: Durum=Done, Dosya, Etkileşimler, Test soru sayısı, Notlar
