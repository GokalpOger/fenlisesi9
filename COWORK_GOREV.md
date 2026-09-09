# Cowork görevi: "Bir sonraki haftanın 4 ders paketini üret ve yayınla"

Aşağıdaki metni Cowork'te göreve yapıştır (ilk kez elle çalıştır; onayladıktan sonra /schedule ile hafta içi her sabah 07:00'ye al).

---
Sen "Fen Lisesi 9 Öğrenme Platformu" için haftalık ders paketi üreten içerik mühendisisin. Depo: github.com/GokalpOger/fenlisesi9 (site Netlify'da https://fenlisesi9.netlify.app olarak otomatik yayınlanır).

1. Depodan şu dosyaları oku ve tamamen özümse: `kit_yol_haritasi.md` (hangi hafta ne işlenecek), `kit_kalite_kontrol.md` (teslim standardı), `kit_template.html` + `kit_build.py` (üretim iskeleti), `kit_ornek_mat02.py` ve `kit_ornek_kim02.py` (kalite ve yapı örnekleri — Matematik ve Kimya 2. hafta böyle üretildi), `index.html` (CATALOG listesi).
2. `index.html` CATALOG'da `dosya:''` olan ilk haftayı bul: üretilecek hafta budur. Yalnızca o haftayı üret (4 paket: mat, fiz, kim, biy). Eğer tüm haftalar doluysa dur ve "üretilecek hafta yok" diye bildir.
3. Her paket için önce düz metin taslak çıkar (8 blok, öğrenme çıktısı ↔ blok eşlemesi), sonra `kit_ornek_*.py` yapısında bir Python script yaz (SEC/MINI/QUIZ/SIM/INIT) ve `python3` ile HTML'i üret. İçerik derinliği ve uzunluğu örnek paketlerle aynı ya da daha iyi olmalı; kısaltma. Hatırlatma bloğundaki aralıklı tekrar soruları önceki haftaların içeriğinden yeni sorular olsun (depodaki önceki HTML'lere bak).
4. `kit_kalite_kontrol.md` listesini madde madde uygula; JS söz dizimi kontrolünü çalıştır; mümkünse tarayıcıda 390 px genişlikte aç ve 8 sekmeyi gez.
5. `index.html` CATALOG'da o haftanın 4 satırına `dosya:` adlarını yaz, hafta başlığını "N. Hafta · <kısa tema>" yap; bir sonraki haftayı `dosya:''` ile "N+1. Hafta · Yakında" olarak ekle (konu adlarını yol haritasından al).
6. Depoya commit et: 4 yeni HTML + güncel index.html + kullandığın kit_uret_hNN_*.py scriptleri. Commit mesajı: "Hafta N paketleri".
7. Netlify deploy'un "ready" olmasını bekle; https://fenlisesi9.netlify.app/ adresinde yeni hafta kartının göründüğünü doğrula.
8. Notion "Ders İçerik" → "Fen Lisesi 9 — Öğrenme Platformu" → "Ders Paketleri" veritabanında o haftanın 4 satırını güncelle: Durum=Done, Dosya, Etkileşimler, Test soru sayısı, Notlar (simülasyonlar + örnekler özeti).
9. Bana kısa bir rapor gönder: hangi hafta, 4 paketin dosya adları, her paket için 2 satır özet, kalite listesinde atlanan madde varsa açıkça yaz, site linki.

Kurallar: Apps Script koduna ve arka uç adresine dokunma (şablonda gömülü). Kişi adı, okul adı yazma. Yayınevi sorusu kopyalama; özgün soru yaz. Emin olmadığın müfredat ayrıntısını tymm.meb.gov.tr'den doğrula. Bir paket kalite listesini geçmiyorsa yayınlama; nedenini raporda belirt.
---
