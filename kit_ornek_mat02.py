from kit_build import build, PALETTES
SEC=r'''
<section class="tab" id="t1" role="tabpanel" aria-labelledby="tab1">
  <h1>"7 ile 8 arasındaki en büyük sayı" diye bir şey yoktur</h1>
  <p class="lead">Geçen hafta √50'yi 7 ile 8 arasına sıkıştırdık. Bu hafta o "ara"nın kendisini inceliyoruz: 7 ile 8 arasında kaç sayı var, hangisi en büyük, "7'den büyük ve 8'den küçük" ile "7 ya da daha büyük" arasında ne fark var? Cevaplar sandığından daha şaşırtıcı — ve kombi termostatından deprem sınıflarına kadar her yerde.</p>
  <div class="card">
    <p><b>Aralık</b>, sayı doğrusunda kesintisiz bir parçadır: "18 °C ile 21 °C arası", "50 km/sa ve altı", "4,0-4,9 büyüklüğünde deprem". Bu hafta aralıkları üç dilde yazmayı öğreneceğiz — <b>eşitsizlik</b>, <b>aralık gösterimi</b>, <b>sayı doğrusu</b> — ve aralıklarla işlem yapmayı: iki koşulu birden sağlayan sayılar (kesişim), en az birini sağlayanlar (birleşim).</p>
  </div>
  <div class="box life"><div class="t">Merak sorusu</div>Evdeki kombi 20 °C'ye ayarlı ama sürekli 19,5-20,5 arasında salınıyor; "tam 20" hiç olmuyor. Termostat neden tek bir sayıya değil, bir aralığa göre çalışır? Cevap 4. sekmede — ve cevabın içinde bu haftanın en önemli fikri var: aralık uçlarının "dahil" olup olmaması.</div>
  <div class="box def"><div class="t">Bu haftanın hedefleri (MEB Ünite 1 · Sayılar)</div>Gerçek sayı aralıklarını eşitsizlik, aralık gösterimi ve sayı doğrusuyla ifade etmek · açık/kapalı/yarı açık ve sonsuz aralıkları ayırt etmek · aralıklarda kesişim, birleşim ve fark işlemleri yapmak · aralıkların uç davranışını (en büyük/en küçük eleman) gerekçelendirmek.</div>
  <div class="nextbtn"><button class="btn" data-done="1" data-go="2">Anladım, hatırlatmaya geç →</button></div>
</section>
<section class="tab" id="t2" role="tabpanel" aria-labelledby="tab2">
  <h2>Hatırlatma ve aralıklı tekrar</h2>
  <div class="grid2">
    <div class="card"><b>Eşitsizlik işaretleri (ortaokul)</b><p>x &lt; 3: 3'ten küçük · x ≤ 3: 3 veya daha küçük · x &gt; 3 · x ≥ 3. Sayı doğrusunda "dahil" için dolu nokta, "hariç" için boş nokta.</p></div>
    <div class="card"><b>Eşitsizlik çözme temelleri</b><p>İki tarafa aynı sayı eklenir/çıkarılır; pozitifle çarpılır/bölünür. Negatifle çarpınca işaret <b>yön değiştirir</b>: −2x &lt; 6 → x &gt; −3.</p></div>
    <div class="card"><b>Geçen haftadan: sıkıştırma</b><p>49 &lt; 50 &lt; 64 → 7 &lt; √50 &lt; 8. Yani √50, "7'den büyük 8'den küçük sayılar" kümesinin bir elemanı.</p></div>
    <div class="card"><b>Dersler arası köprü</b><p>Fizik H2'de ölçüm hatası göreceksin: "5,0 ± 0,2 cm" demek 4,8 ≤ uzunluk ≤ 5,2 — yani kapalı bir aralık.</p></div>
  </div>
  <h3>Aralıklı tekrar (3 soru, anında geri bildirim)</h3>
  <div id="miniQuiz"></div>
  <div class="nextbtn"><button class="btn" data-done="2" data-go="3">Konu anlatımına geç →</button></div>
</section>
<section class="tab" id="t3" role="tabpanel" aria-labelledby="tab3">
  <h2>Konu anlatımı</h2>
  <h3>3.1 Sayı doğrusu "dolu"dur</h3>
  <p>Gerçek sayılar sayı doğrusunun her noktasını doldurur: iki farklı gerçek sayı arasında daima başka bir gerçek sayı vardır (ortalamaları). O yüzden 7 ile 8 arasında sonsuz sayı var: 7,1; 7,01; 7,001; √50; 7,999… Bu "yoğunluk" özelliği, aralıkların neden liste değil <em>parça</em> olarak düşünülmesi gerektiğini açıklar.</p>
  <div class="box def"><div class="t">Tanım</div>a &lt; b olmak üzere, a ile b arasındaki (uçlar dahil ya da hariç) tüm gerçek sayıların kümesine <b>aralık</b> denir. Uç nokta dahilse <b>köşeli ayraç [ ]</b>, hariçse <b>yuvarlak ayraç ( )</b> kullanılır.</div>
  <h3>3.2 Dört tür aralık ve sonsuz aralıklar</h3>
  <table>
    <tr><th>Eşitsizlik</th><th>Aralık</th><th>Adı</th><th>Sayı doğrusu</th></tr>
    <tr><td>a ≤ x ≤ b</td><td>[a, b]</td><td>kapalı</td><td>● ——— ●</td></tr>
    <tr><td>a &lt; x &lt; b</td><td>(a, b)</td><td>açık</td><td>○ ——— ○</td></tr>
    <tr><td>a ≤ x &lt; b</td><td>[a, b)</td><td>yarı açık (sağdan açık)</td><td>● ——— ○</td></tr>
    <tr><td>a &lt; x ≤ b</td><td>(a, b]</td><td>yarı açık (soldan açık)</td><td>○ ——— ●</td></tr>
    <tr><td>x &gt; a</td><td>(a, ∞)</td><td>sonsuz aralık</td><td>○ ———→</td></tr>
    <tr><td>x ≤ b</td><td>(−∞, b]</td><td>sonsuz aralık</td><td>←——— ●</td></tr>
    <tr><td>her x</td><td>(−∞, ∞) = ℝ</td><td>gerçek sayılar</td><td>←———→</td></tr>
  </table>
  <div class="box warn"><div class="t">Tuzak: ∞ bir sayı değildir</div>Sonsuzluk tarafı <b>her zaman yuvarlak</b> ayraçla yazılır: [3, ∞) doğru, [3, ∞] yanlış. "Sonsuza kadar" demek, bir yerde durup onu dahil etmek demek değildir.</div>
  <div class="sim">
    <h3>Aralık oluşturucu</h3>
    <div class="hint">Uçları kaydır, dahil/hariç anahtarlarını değiştir; üç gösterim (eşitsizlik, aralık, sayı doğrusu) birlikte güncellenir. Uçları eşitleyince ne olduğuna dikkat et.</div>
    <div class="ctrl">
      <label>a <input type="range" id="ia" min="-6" max="8" value="-2"><output id="iao">-2</output></label>
      <label><input type="checkbox" id="ial" checked> a dahil</label>
      <label>b <input type="range" id="ib" min="-6" max="8" value="5"><output id="ibo">5</output></label>
      <label><input type="checkbox" id="ibl"> b dahil</label>
      <label><input type="checkbox" id="iinf"> sağ uç ∞</label>
    </div>
    <div class="svgwrap"><svg id="iSvg" viewBox="0 0 720 130" role="img" aria-label="Aralık sayı doğrusu"></svg></div>
    <div class="readout" id="iOut" style="display:block"></div>
  </div>
  <h3>3.3 Üç dil, tek anlam</h3>
  <p>Sınavda üç gösterim arasında geçiş istenir. Yöntem: önce uçları ve dahil/hariç durumunu belirle, sonra çevir. Örnek: "En az 3, 9'dan küçük" → 3 ≤ x &lt; 9 → [3, 9) → sayı doğrusunda 3'te dolu, 9'da boş nokta.</p>
  <div class="formula"><div class="m">x ≥ −1 &nbsp;⇔&nbsp; [−1, ∞) &nbsp;⇔&nbsp; ● ———→</div><div class="why">"−1 ve üzeri": −1 dahil, sağa sonsuz.</div></div>
  <div class="formula"><div class="m">−4 &lt; x ≤ 2 &nbsp;⇔&nbsp; (−4, 2] &nbsp;⇔&nbsp; ○ ——— ●</div><div class="why">−4 hariç, 2 dahil. Hangi uç dahil, ona bak; sıra değil.</div></div>
  <h3>3.4 Aralıklarda işlemler: kesişim, birleşim, fark</h3>
  <p>Aralıklar kümedir; küme işlemleri aynen geçerlidir. <b>Kesişim (∩)</b>: her iki koşulu birden sağlayan sayılar ("ve"). <b>Birleşim (∪)</b>: en az birini sağlayanlar ("veya"). <b>Fark (A − B)</b>: A'da olup B'de olmayanlar.</p>
  <div class="sim">
    <h3>Kesişim ve birleşim laboratuvarı</h3>
    <div class="hint">İki aralığı kaydır; kesişim (koyu) ve birleşimi (açık) izle. Aralıklar birbirinden ayrılınca kesişim boş kümeye, birleşim iki parçaya dönüşür — birleşim her zaman tek aralık değildir.</div>
    <div class="ctrl">
      <label>A: [<input type="number" id="a1" value="-3" style="width:64px">, <input type="number" id="a2" value="4" style="width:64px">]</label>
      <label>B: (<input type="number" id="b1" value="1" style="width:64px">, <input type="number" id="b2" value="7" style="width:64px">)</label>
      <button id="kReset" class="alt">Sıfırla</button>
    </div>
    <div class="svgwrap"><svg id="kSvg" viewBox="0 0 720 200" role="img" aria-label="Kesişim ve birleşim"></svg></div>
    <div class="readout" id="kOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Uç noktalarda kural</div>Kesişimde bir uç, <em>her iki</em> aralıkta dahilse dahildir. [1, 5] ∩ (1, 5) = (1, 5). Birleşimde bir uç, aralıklardan <em>en az birinde</em> dahilse dahildir: [1, 5) ∪ (3, 5] = [1, 5].</div>
  <h3>3.5 Sınırda ne olur? En büyük eleman meselesi</h3>
  <p>[2, 5] aralığının en büyük elemanı 5'tir. Peki (2, 5) aralığının? 5 dahil değil; 4,9 var ama 4,99 daha büyük; 4,999 daha da büyük… Hangi sayıyı seçersen seç, onunla 5'in ortalaması hem aralıktadır hem de daha büyüktür. <b>Açık uçlu bir aralığın o uçta en büyük (ya da en küçük) elemanı yoktur.</b> 5, aralığın "üst sınırı"dır ama elemanı değildir. Bu fikir, ileride limit ve sürekliliğin temelidir.</p>
  <div class="box warn"><div class="t">Tuzak: 0,999… = 1</div>"(2, 5)'in en büyük elemanı 4,999…'dur" demek yanlıştır; çünkü 4,999… (sonsuz dokuz) tam olarak 5'e eşittir. Kanıt: x = 4,999…, 10x = 49,999…, 10x − x = 45 → x = 5. Yani 4,999… aralıkta değildir. Sonlu sayıda dokuz (4,999) ise aralıktadır ama en büyük değildir.</div>
  <h3>3.6 Tek noktalı ve boş aralıklar</h3>
  <div class="formula"><div class="m">[3, 3] = {3} &nbsp;·&nbsp; (3, 3) = ∅ &nbsp;·&nbsp; [3, 3) = ∅</div><div class="why">Uçlar eşitse yalnızca kapalı aralık bir eleman içerir. Simülasyonda a = b yaparak gör.</div></div>
  <div class="box warn"><div class="t">Tuzak: "aralık" ile "tam sayılar" karışması</div>(2, 6) aralığında sonsuz sayı vardır; ama (2, 6) ∩ ℤ = {3, 4, 5} yalnızca 3 elemanlıdır. Soru "kaç tam sayı" diyorsa ayraç türü sayıyı doğrudan değiştirir: [2, 6] ∩ ℤ = {2, 3, 4, 5, 6}.</div>
  <div class="nextbtn"><button class="btn" data-done="3" data-go="4">Günlük yaşam örneklerine geç →</button></div>
</section>
<section class="tab" id="t4" role="tabpanel" aria-labelledby="tab4">
  <h2>Günlük yaşamdan örnekler</h2>
  <div class="card"><h3 style="margin-top:0">1 · Kombi termostatı: neden tek sayı değil, aralık?</h3>
    <p><b>Durum:</b> Termostat 20 °C'ye ayarlı. Kombi 19,5 °C'de yanıyor, 20,5 °C'de sönüyor.</p>
    <p><b>Kavramla bağ:</b> Cihaz "sıcaklık = 20" koşuluyla çalışsa, 20'nin çevresindeki minicik dalgalanmalarda saniyede yüzlerce kez açılıp kapanırdı. Onun yerine bir aralık tanımlanır: t ≤ 19,5 ise yan, t ≥ 20,5 ise sön. Bu, [19,5, 20,5] aralığının dışına çıkınca müdahale demektir; mühendisler buna <em>histerezis</em> der.</p>
    <p><b>Analiz:</b> "Rahat aralık" = [19,5, 20,5]. Kombi yanma koşulu = (−∞, 19,5], sönme koşulu = [20,5, ∞). İkisinin kesişimi ∅ — asla aynı anda hem yanıp hem sönmez. Birleşimleri ise ℝ − (19,5, 20,5): kombinin karar verdiği bölge.</p>
    <p><b>Sonuç:</b> Termostat, aralıkların kesişim ve farkıyla tasarlanmış küçük bir mantık devresidir.</p></div>
  <div class="card"><h3 style="margin-top:0">2 · Bisiklet lastiği basıncı</h3>
    <p><b>Durum:</b> Lastiğin yanında "35-50 psi" yazıyor. 34 psi'ye şişirsen ne olur, 51'e şişirsen?</p>
    <p><b>Kavramla bağ:</b> Üreticinin güvenli aralığı [35, 50] (psi). Alt sınırın altı "jant vuruğu ve patlak" riski, üst sınırın üstü "patlama" riski: (−∞, 35) ∪ (50, ∞) tehlike bölgesi — bir birleşim.</p>
    <p><b>Hesap:</b> Pompan 0,1 psi hassasiyetle okuyor. Hedef: yolda konfor için aralığın alt yarısı, [35, 42,5]. Bu, [35, 50] aralığının orta noktası 42,5 alınarak bulunan alt yarısı; uzunluğu 7,5 psi.</p>
    <p><b>Sonuç:</b> Aralığın uçları güvenlik sınırıdır; "orta nokta" ve "yarı" kavramları aralık aritmetiğidir.</p></div>
  <div class="card"><h3 style="margin-top:0">3 · Deprem büyüklük sınıfları — uçlar kime ait?</h3>
    <p><b>Durum:</b> Sismolojide sınıflar: hafif 4,0-4,9 · orta 5,0-5,9 · kuvvetli 6,0-6,9 · büyük 7,0-7,9. 1999 İzmit depremi 7,4 → "büyük".</p>
    <p><b>Kavramla bağ:</b> Bu sınıflar aslında yarı açık aralıklardır: hafif = [4, 5), orta = [5, 6), kuvvetli = [6, 7), büyük = [7, 8). Neden? 4,95 büyüklüğündeki bir deprem "4,0-4,9" listesinde görünmez ama "5,0-5,9"da da yoktur; yarı açık aralıklar bu boşluğu kapatır ve her sayıyı tam bir sınıfa koyar.</p>
    <p><b>Analiz:</b> Sınıfların birleşimi [4, 8) kesintisizdir; ikili kesişimleri boştur. Bu iki özellik ("örtme" ve "ayrıklık") iyi bir sınıflandırmanın tanımıdır.</p>
    <p><b>Sonuç:</b> Gazetedeki "4,0-4,9" yazımı bir kısaltmadır; matematiksel karşılığı [4, 5)'tir.</p></div>
  <div class="card"><h3 style="margin-top:0">4 · Hava kalitesi indeksi (Kocaeli sanayi bölgesi)</h3>
    <p><b>Durum:</b> Belediye ölçüm ekranı: 0-50 "iyi", 51-100 "orta", 101-150 "hassas gruplar için sağlıksız"… İndeks 100,4 çıktı; hangi sınıf?</p>
    <p><b>Kavramla bağ:</b> Tam sayı sınırlarla yazılmış sınıflarda 100 ile 101 arasındaki ondalıklar açıkta kalır. Resmî tanımda indeks tam sayıya yuvarlanır (100,4 → 100 → "orta"); yani sınıflar aslında [0, 50], [51, 100] gibi <em>tam sayı</em> aralıklarıdır: ℤ ile kesişim alınmış hâlleri.</p>
    <p><b>Sonuç:</b> Bir aralığın ondalıklara mı tam sayılara mı ait olduğu, sınırların anlamını değiştirir. Soru "kaç değer var?" dediğinde ilk sorulacak şey budur.</p></div>
  <div class="nextbtn"><button class="btn" data-done="4" data-go="5">Etkileşimli materyale geç →</button></div>
</section>
<section class="tab" id="t5" role="tabpanel" aria-labelledby="tab5">
  <h2>Etkileşimli materyal</h2>
  <div class="sim">
    <h3>Aralıkta mı? — hızlı karar oyunu</h3>
    <div class="hint">Bir aralık ve bir sayı verilir; "içinde" ya da "dışında" seç. 12 tur; uç noktalar ve ∞ tuzakları sık gelir. Sonunda hangi tür hatayı yaptığını görürsün.</div>
    <div id="game"></div>
    <div class="ctrl"><button id="gmReset" class="alt">Oyunu sıfırla</button></div>
  </div>
  <div class="sim">
    <h3>En büyük eleman avcısı</h3>
    <div class="hint">(7, 8) aralığında en büyük sayıyı bulmaya çalış: bir sayı yaz, simülasyon aralıkta ondan büyük bir sayı üretsin. Kaç turda pes edeceksin?</div>
    <div class="ctrl"><label>Sayın <input type="text" id="supIn" placeholder="örn. 7,99" style="width:140px"></label><button id="supGo">Dene</button><button id="supReset" class="alt">Sıfırla</button></div>
    <div class="svgwrap"><svg id="supSvg" viewBox="0 0 720 120" role="img" aria-label="En büyük eleman avı"></svg></div>
    <div class="readout" id="supOut" style="display:block">7 ile 8 arasında bir sayı yaz.</div>
  </div>
  <div class="box def"><div class="t">Gözlem soruları</div>1) Oyunda en çok hangi tuzağa düştün: uç nokta mı, ∞ mi, tam sayı sayma mı? &nbsp; 2) "Avcı"da yazdığın her sayıya karşılık verilen sayı nasıl üretiliyor olabilir? (İpucu: ortalama.) &nbsp; 3) [7, 8] aralığında aynı oyun oynansa ne olurdu?</div>
  <div class="nextbtn"><button class="btn" data-done="5" data-go="6">Çözümlü örneklere geç →</button></div>
</section>
<section class="tab" id="t6" role="tabpanel" aria-labelledby="tab6">
  <h2>Çözümlü örnekler</h2>
  <div class="card"><h3 style="margin-top:0">Temel · "3'ten büyük, 10 veya daha küçük" sayılar</h3>
    <ol class="steps"><li>Uçlar: 3 (hariç: "büyük"), 10 (dahil: "veya daha küçük").</li><li>Eşitsizlik: 3 &lt; x ≤ 10. Aralık: <b>(3, 10]</b>. Sayı doğrusu: 3'te boş, 10'da dolu nokta.<div class="why">"Veya eşit" gördüğün yer köşeli ayraçtır.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Temel · [−2, 4) aralığını eşitsizlik ve sayı doğrusuyla göster; kaç tam sayı içerir?</h3>
    <ol class="steps"><li>−2 ≤ x &lt; 4; −2'de dolu, 4'te boş nokta.</li><li>Tam sayılar: −2, −1, 0, 1, 2, 3 → <b>6 tane</b>. 4 dahil değil.<div class="why">Sayarken uç ayraçlarına bak: sağ uç yuvarlak, 4 sayılmaz.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · A = [−2, 5), B = (1, 8] için A ∩ B, A ∪ B, A − B</h3>
    <ol class="steps"><li>Sayı doğrusuna ikisini de çiz; kesişim ikisinin örtüştüğü bölge: 1'den 5'e. 1 hangi ayraçla? B'de hariç → hariç. 5? A'da hariç → hariç. <b>A ∩ B = (1, 5)</b>.</li><li>Birleşim: −2'den 8'e kesintisiz (aralıklar örtüşüyor). −2 A'da dahil → dahil; 8 B'de dahil → dahil. <b>A ∪ B = [−2, 8]</b>.</li><li>Fark A − B: A'da olup B'de olmayan: B'ye girmeyen kısım 1 ve altı. 1, B'de yok → A − B'de var. <b>A − B = [−2, 1]</b>.<div class="why">Fark alırken çıkarılan kümenin uç ayracı tersine döner: B'de 1 hariçti, farkta 1 dahil oldu.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · 3 ≤ 2x − 1 &lt; 9 eşitsizliğinin çözüm aralığı</h3>
    <ol class="steps"><li>Her tarafa 1 ekle: 4 ≤ 2x &lt; 10.</li><li>2'ye böl (pozitif, yön değişmez): 2 ≤ x &lt; 5 → <b>[2, 5)</b>.</li><li>Kontrol: x = 2 → 2·2−1 = 3 ✓ (dahil); x = 5 → 9, "&lt; 9" sağlanmaz ✓ (hariç).<div class="why">Uç kontrolü, ayraç türünü doğrulamanın en güvenli yolu.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · A = (−∞, 3], B = [3, ∞) için A ∩ B ve A ∪ B; sonra B yerine (3, ∞) alınırsa?</h3>
    <ol class="steps"><li>A ∩ B: yalnız 3 her ikisinde de var → <b>{3}</b> = [3, 3]. A ∪ B = <b>ℝ</b>.</li><li>B = (3, ∞) olursa: 3 artık B'de yok → A ∩ B = <b>∅</b>; A ∪ B yine ℝ (3, A'dan geliyor).<div class="why">Tek bir ayraç değişikliği kesişimi bir elemandan boş kümeye indirdi; birleşim etkilenmedi.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · İç içe aralıklar: I₁ = (0, 1), I₂ = (0, ½), I₃ = (0, ⅓), … Tüm I_n'lerin ortak elemanı var mı?</h3>
    <ol class="steps"><li>Aday: 0 mı? Hiçbirinde yok (açık uç).</li><li>Pozitif herhangi bir x alalım, örn. x = 0,001. n = 1001 için 1/n = 0,000999 &lt; x → x ∉ I₁₀₀₁. Her pozitif x için böyle bir n bulunur (Arşimet özelliği).</li><li>Sonuç: ortak eleman <b>yok</b>, kesişim ∅. Oysa kapalı hâlleri [0, 1/n] alınsaydı kesişim {0} olurdu.<div class="why">Açık/kapalı ayrımı burada "sonsuz kesişim" sorusunun cevabını tamamen değiştiriyor — analiz derslerinin kapısı.</div></li></ol></div>
  <div class="nextbtn"><button class="btn" data-done="6" data-go="7">Kendini sına →</button></div>
</section>
<section class="tab" id="t7" role="tabpanel" aria-labelledby="tab7">
  <h2>Kendini sına</h2>
  <p>12 çoktan seçmeli (4 temel, 5 orta, 3 fen lisesi) + 2 açık uçlu. Cevaplarını işaretle ve sonunda kaydet; değerlendirme öğretmenine iletilir.</p>
  <div id="quiz"></div><div class="score" id="scoreBox"></div>
  <div class="nextbtn"><button class="btn" id="quizCheck">Cevapları kaydet</button><button class="btn alt" id="quizReset">Testi temizle</button><button class="btn" data-done="7" data-go="8">Özete geç →</button></div>
</section>
<section class="tab" id="t8" role="tabpanel" aria-labelledby="tab8">
  <h2>Özet ve tuzaklar</h2>
  <div class="summary">
    <div class="card"><b>Ayraçlar</b>[ ] dahil · ( ) hariç · ∞ tarafı daima ( ) · [a,a] = {a}, (a,a) = ∅</div>
    <div class="card"><b>Üç dil</b>a ≤ x &lt; b ⇔ [a, b) ⇔ ● — ○. Önce uçlar ve dahil/hariç, sonra çevir; uç kontrolüyle doğrula.</div>
    <div class="card"><b>İşlemler</b>∩ "ve": ikisinde de · ∪ "veya": en az birinde · A − B: A'da olup B'de olmayan (B'nin ayracı tersine döner)</div>
    <div class="card"><b>Sınır davranışı</b>Açık uçta en büyük/en küçük eleman yoktur; 0,999… = 1; tam sayı sayarken ayraca bak.</div>
  </div>
  <h3>Sık yapılan 5 hata</h3>
  <ol>
    <li>[3, ∞] yazmak. Sonsuz tarafı her zaman yuvarlak.</li>
    <li>(2, 6) aralığında "4 sayı var" demek. Sonsuz gerçek sayı var; 3 tam sayı var.</li>
    <li>Kesişimde ucu "kapalı olandan" almak. Uç, ancak <em>her iki</em> kümede dahilse dahildir.</li>
    <li>İki ayrık aralığın birleşimini tek aralık yazmak: [1, 2] ∪ [4, 5] = [1, 5] <b>değildir</b>.</li>
    <li>(a, b) aralığının en büyük elemanını "b'ye çok yakın bir sayı" sanmak. Yoktur.</li>
  </ol>
  <div class="box life"><div class="t">Gelecek haftaya köprü</div>Bu hafta "7 ile 8 arasında sonsuz sayı var" dedik. Peki bunların kaçı kesir olarak yazılabilir, kaçı yazılamaz? √50 yazılamaz — bunu nasıl <em>kanıtlarız</em>? Gelecek hafta: <b>sayı kümeleri (ℕ, ℤ, ℚ, ℝ) ve işlem özellikleri</b>.</div>
  <div class="nextbtn"><button class="btn" data-done="8" data-go="1">Haftayı tamamladım ✓</button></div>
</section>'''
MINI="""const MINI=[
 {s:'<span class="tag">Geçen hafta</span> 2<sup>−3</sup> · 4<sup>2</sup> işleminin sonucu kaçtır?',o:['2','−2','1/2','32'],a:0,e:'2⁻³ = 1/8, 4² = 16; 16/8 = 2. Negatif üs işaret değil, ters çevirme.'},
 {s:'<span class="tag">Geçen hafta</span> √40 hangi iki ardışık tam sayı arasındadır?',o:['6 ile 7','5 ile 6','7 ile 8','4 ile 5'],a:0,e:'36 < 40 < 49 → 6 < √40 < 7. Yani √40 ∈ (6, 7).'},
 {s:'<span class="tag">Ortaokul</span> −3x > 12 eşitsizliğinin çözümü hangisidir?',o:['x < −4','x > −4','x < 4','x > 4'],a:0,e:'−3 ile bölünce yön değişir: x < −4. Bu hafta bunu (−∞, −4) diye yazacağız.'}];"""
QUIZ="""const QUIZ=[
 {s:'"−5 veya daha büyük, 2\\'den küçük" sayılar kümesi hangi aralıktır?',o:['[−5, 2)','(−5, 2]','(−5, 2)','[−5, 2]'],a:0,e:'"Veya daha büyük" → −5 dahil (köşeli); "küçük" → 2 hariç (yuvarlak).'},
 {s:'x ≤ 4 eşitsizliğinin aralık gösterimi hangisidir?',o:['(−∞, 4]','(−∞, 4)','[−∞, 4]','[4, ∞)'],a:0,e:'4 dahil → köşeli; sonsuz tarafı daima yuvarlak. [−∞, 4] yazımı hatalıdır.'},
 {s:'(−3, 5] aralığında kaç tam sayı vardır?',o:['8','9','7','Sonsuz'],a:0,e:'−2, −1, 0, 1, 2, 3, 4, 5 → 8 tane. −3 hariç. "Sonsuz" cevabı gerçek sayılar için doğrudur, tam sayılar için değil.'},
 {s:'Sayı doğrusunda 1\\'de dolu nokta, 6\\'da boş nokta ve arası taralı olan gösterim hangi aralıktır?',o:['[1, 6)','(1, 6]','[1, 6]','(1, 6)'],a:0,e:'Dolu nokta dahil, boş nokta hariç.'},
 {s:'A = [−1, 6), B = (2, 9] ise A ∩ B kaçtır?',o:['(2, 6)','[2, 6]','[−1, 9]','(2, 6]'],a:0,e:'Örtüşen bölge 2\\'den 6\\'ya; 2 B\\'de hariç, 6 A\\'da hariç → (2, 6).'},
 {s:'A = (−∞, 2], B = [2, ∞) ise A ∪ B ve A ∩ B sırasıyla nedir?',o:['ℝ ve {2}','ℝ ve ∅','(−∞, ∞) ve (2, 2)','[2, 2] ve ℝ'],a:0,e:'Her sayı ya 2 ve altı ya 2 ve üstü → birleşim ℝ. İkisinde de olan tek sayı 2 → kesişim {2}.'},
 {tag:'bağlam',s:'Bir bisiklet lastiğinde "35-50 psi" yazıyor; üretici sınır değerlerin de güvenli olduğunu belirtiyor. Tehlikeli basınç değerleri kümesi hangisidir?',o:['(−∞, 35) ∪ (50, ∞)','(−∞, 35] ∪ [50, ∞)','(35, 50)','[35, 50]'],a:0,e:'Güvenli aralık [35, 50]; tümleyeni iki parçalı birleşimdir ve uçlar tehlikede değildir (yuvarlak).'},
 {s:'2 < 3x + 1 ≤ 10 eşitsizliğinin çözüm kümesi hangisidir?',o:['(1/3, 3]','[1/3, 3)','(1, 3]','[1, 3]'],a:0,e:'1 çıkar: 1 < 3x ≤ 9; 3\\'e böl: 1/3 < x ≤ 3. Uç kontrolü: x = 3 → 10 ✓ dahil.'},
 {tag:'bağlam',s:'<b>Bilgi:</b> Deprem sınıfları "orta: 5,0-5,9", "kuvvetli: 6,0-6,9" biçiminde yazılır; her büyüklük tam bir sınıfa ait olmalıdır.<br>5,97 büyüklüğündeki bir deprem için doğru matematiksel sınıf aralığı hangisidir?',o:['[5, 6) → orta','[5, 5,9] → orta','(5,9, 6) → sınıfsız','[6, 7) → kuvvetli'],a:0,e:'Boşluk kalmaması için sınıflar yarı açık [5, 6) biçimindedir; 5,97 bu aralıktadır.'},
 {s:'A = [1, 4], B = (1, 4) için A − B hangisidir?',o:['{1, 4}','∅','[1, 4]','(1, 4)'],a:0,e:'A\\'da olup B\\'de olmayanlar yalnızca uçlar: 1 ve 4. İki elemanlı küme.'},
 {tag:'bağlam',s:'Bir termostat, sıcaklık 19,5 °C ve altına düşünce ısıtıcıyı açıyor; 20,5 °C ve üstüne çıkınca kapatıyor. Isıtıcının ne açılıp ne kapandığı ("bekleme") sıcaklık aralığı hangisidir?',o:['(19,5, 20,5)','[19,5, 20,5]','(−∞, 19,5] ∪ [20,5, ∞)','{20}'],a:0,e:'19,5 ve 20,5 karar noktalarıdır (açma/kapama); bekleme bölgesi bu iki değeri içermez → açık aralık.'},
 {s:'Aşağıdaki ifadelerden hangisi doğrudur?',o:['(2, 5) aralığının en büyük elemanı yoktur','(2, 5) aralığının en büyük elemanı 4,999…\\'dur','[2, 5) aralığının en büyük elemanı 5\\'tir','(2, 5) aralığında 5\\'e en yakın sayı 4,99\\'dur'],a:0,e:'Her elemandan büyük bir eleman daha vardır (ortalama al). 4,999… = 5 olduğundan aralıkta değildir.'},
 {open:true,s:'A = [−4, 2) ve B = [0, 6] için A ∪ B, A ∩ B ve B − A kümelerini bul; her sonuçta uçların neden dahil/hariç olduğunu bir cümleyle açıkla.',ans:'A ∪ B = [−4, 6] (−4 A\\'da dahil, 6 B\\'de dahil); A ∩ B = [0, 2) (0 her ikisinde dahil, 2 A\\'da hariç); B − A = [2, 6] (2 A\\'da olmadığı için farkta kalır).',e:'Uç gerekçeleri beklenir.'},
 {open:true,s:'"(0, 1) aralığında en küçük pozitif sayı vardır" iddiasını çürüt.',ans:'x en küçük olsun; x/2 de aralıktadır ve x\\'ten küçüktür → çelişki. Dolayısıyla en küçük eleman yoktur.',e:'Çelişkiyle ispat sezgisi; "yarısını al" adımı yeterli.'}];"""
SIM=r"""
/* --- Aralık oluşturucu --- */
function fmtI(a,b,al,bl,inf){if(inf)return (al?'[':'(')+a+', ∞)';if(a>b)return '∅ (a > b)';if(a===b)return (al&&bl)?'{'+a+'}':'∅';return (al?'[':'(')+a+', '+b+(bl?']':')');}
function drawI(){const a=+$('#ia').value,b=+$('#ib').value,al=$('#ial').checked,bl=$('#ibl').checked,inf=$('#iinf').checked;$('#iao').value=a;$('#ibo').value=b;
  const svg=$('#iSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),X=v=>60+(v+7)*40;
  svg.appendChild(el('line',{x1:20,y1:70,x2:700,y2:70,stroke:ink,'stroke-width':2}));svg.appendChild(el('path',{d:'M700 70 l-8 -5 v10 z',fill:ink}));
  for(let v=-7;v<=9;v++){svg.appendChild(el('line',{x1:X(v),y1:64,x2:X(v),y2:76,stroke:ink}));svg.appendChild(el('text',{x:X(v),y:98,'text-anchor':'middle','font-size':'12',fill:css('--ink2')},v));}
  const bad=!inf&&(a>b||(a===b&&!(al&&bl)));
  if(!bad){svg.appendChild(el('rect',{x:X(a),y:62,width:(inf?X(9.5):X(b))-X(a),height:16,fill:nv,opacity:.35}));
    svg.appendChild(el('circle',{cx:X(a),cy:70,r:7,fill:al?nv:css('--paper'),stroke:nv,'stroke-width':3}));
    if(!inf)svg.appendChild(el('circle',{cx:X(b),cy:70,r:7,fill:bl?nv:css('--paper'),stroke:nv,'stroke-width':3}));}
  const ineq=inf?(a+(al?' ≤ ':' < ')+'x'):(a>b?'çözüm yok':a+(al?' ≤ ':' < ')+'x'+(bl?' ≤ ':' < ')+b);
  $('#iOut').innerHTML='<b>Aralık:</b> '+fmtI(a,b,al,bl,inf)+' &nbsp;·&nbsp; <b>Eşitsizlik:</b> '+ineq+(a===b&&!inf?' &nbsp;<span style="color:var(--gold)">Uçlar eşit: yalnız kapalı aralık bir eleman içerir.</span>':'')+(inf?' &nbsp;<span style="color:var(--gold)">∞ tarafı her zaman yuvarlak.</span>':'');}
['#ia','#ib','#ial','#ibl','#iinf'].forEach(s=>$(s).addEventListener('input',drawI));
/* --- Kesişim / birleşim --- */
function drawK(){const a1=+$('#a1').value,a2=+$('#a2').value,b1=+$('#b1').value,b2=+$('#b2').value;const svg=$('#kSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');
  const lo=Math.min(a1,b1,-1)-1,hi=Math.max(a2,b2,1)+1,X=v=>40+(v-lo)/(hi-lo)*640;
  const row=(y,l,r,lc,rc,color,label)=>{svg.appendChild(el('line',{x1:40,y1:y,x2:680,y2:y,stroke:css('--line')}));if(l<=r){svg.appendChild(el('rect',{x:X(l),y:y-7,width:Math.max(2,X(r)-X(l)),height:14,fill:color,opacity:.5}));svg.appendChild(el('circle',{cx:X(l),cy:y,r:6,fill:lc?color:css('--paper'),stroke:color,'stroke-width':2.5}));svg.appendChild(el('circle',{cx:X(r),cy:y,r:6,fill:rc?color:css('--paper'),stroke:color,'stroke-width':2.5}));}svg.appendChild(el('text',{x:10,y:y+5,'font-size':'13','font-weight':'700',fill:ink},label));};
  row(30,a1,a2,true,true,nv,'A');row(70,b1,b2,false,false,gd,'B');
  // kesişim (A kapalı, B açık)
  const il=Math.max(a1,b1),ir=Math.min(a2,b2);const inB=v=>v>b1&&v<b2;let inter='∅';
  if(il<ir){const ilc=inB(il),irc=inB(ir);inter=(ilc?'[':'(')+il+', '+ir+(irc?']':')');row(110,il,ir,ilc,irc,css('--ok'),'A∩B');}
  else if(il===ir&&inB(il)){inter='{'+il+'}';row(110,il,ir,true,true,css('--ok'),'A∩B');}
  else{svg.appendChild(el('text',{x:10,y:115,'font-size':'13','font-weight':'700',fill:ink},'A∩B'));svg.appendChild(el('text',{x:360,y:115,'text-anchor':'middle','font-size':'13',fill:css('--ink2')},'∅ — ortak eleman yok'));}
  // birleşim
  let uni;const overlap=(a1<=b2&&b1<=a2);
  if(overlap){const ul=Math.min(a1,b1),ur=Math.max(a2,b2),ulc=a1<=b1,urc=a2>=b2;uni=(ulc?'[':'(')+ul+', '+ur+(urc?']':')');row(150,ul,ur,ulc,urc,nv,'A∪B');}
  else{uni='['+a1+', '+a2+'] ∪ ('+b1+', '+b2+')';svg.appendChild(el('text',{x:10,y:155,'font-size':'13','font-weight':'700',fill:ink},'A∪B'));svg.appendChild(el('rect',{x:X(a1),y:143,width:Math.max(2,X(a2)-X(a1)),height:14,fill:nv,opacity:.5}));svg.appendChild(el('rect',{x:X(b1),y:143,width:Math.max(2,X(b2)-X(b1)),height:14,fill:gd,opacity:.5}));svg.appendChild(el('text',{x:360,y:185,'text-anchor':'middle','font-size':'12',fill:css('--ink2')},'iki ayrı parça — tek aralık olarak yazılamaz'));}
  for(let v=Math.ceil(lo);v<=Math.floor(hi);v++)svg.appendChild(el('text',{x:X(v),y:196,'text-anchor':'middle','font-size':'10',fill:css('--ink2')},v));
  $('#kOut').innerHTML='A = ['+a1+', '+a2+'] · B = ('+b1+', '+b2+')<br><b>A ∩ B = '+inter+'</b> &nbsp;·&nbsp; <b>A ∪ B = '+uni+'</b>';}
['#a1','#a2','#b1','#b2'].forEach(s=>$(s).addEventListener('input',drawK));
$('#kReset').onclick=()=>{$('#a1').value=-3;$('#a2').value=4;$('#b1').value=1;$('#b2').value=7;drawK();};
/* --- Aralıkta mı? oyunu --- */
const GQ=[['[2, 7]',7,true,'Kapalı uç: 7 dahil.'],['(2, 7)',2,false,'Açık uç: 2 hariç.'],['[−3, ∞)',1000,true,'Sonsuz aralık; büyük sayılar da dahil.'],['(−∞, 4]',4,true,'4 dahil (köşeli).'],['(0, 1)',0.5,true,'0,5 aralıktadır; ondalıklar da gerçek sayıdır.'],['(0, 1)',1,false,'1 hariç.'],['[5, 5]',5,true,'{5} tek elemanlı küme.'],['(5, 5)',5,false,'Boş küme: hiçbir sayı içermez.'],['[−2, 3)',-2,true,'−2 dahil.'],['[−2, 3)',2.999,true,'3 altındaki her sayı dahil.'],['(1, 4] ∩ [4, 9)',4,true,'4 her ikisinde de var → kesişimde.'],['(1, 4) ∪ (4, 9)',4,false,'İki aralıkta da 4 yok; birleşimde de yoktur.']];
let GM={i:0,s:0,log:[]};
function drawGame(){const box=$('#game');if(GM.i>=GQ.length){box.innerHTML='<div class="readout">Puan: '+GM.s+' / '+GQ.length+'</div>'+GM.log.map(l=>'<div class="q '+(l.ok?'right':'wrong')+'"><div class="stem">'+l.q+'</div><div class="fb">'+(l.ok?'✔ ':'✘ ')+l.e+'</div></div>').join('');return;}
  const q=GQ[GM.i];box.innerHTML='<div class="readout">'+(GM.i+1)+' / '+GQ.length+' · Puan '+GM.s+'</div><div class="q"><div class="stem" style="font-size:20px">'+String(q[1]).replace('.',',')+' &nbsp;∈&nbsp; '+q[0]+' &nbsp;?</div><div class="ctrl"><button class="btn" data-v="1">İçinde</button><button class="btn alt" data-v="0">Dışında</button></div><div class="fb" id="gmFb"></div></div>';
  box.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{const ok=(b.dataset.v==='1')===q[2];if(ok)GM.s++;GM.log.push({q:String(q[1]).replace('.',',')+' ∈ '+q[0]+' ?',ok,e:q[3]});box.querySelector('.q').classList.add(ok?'right':'wrong');box.querySelectorAll('[data-v]').forEach(x=>x.disabled=true);$('#gmFb').innerHTML=(ok?'✔ Doğru. ':'✘ ')+q[3]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="gmNext">Sonraki →</button>';$('#gmNext').onclick=()=>{GM.i++;drawGame();};});}
$('#gmReset').onclick=()=>{GM={i:0,s:0,log:[]};drawGame();};
/* --- En büyük eleman avcısı --- */
let SUP={tries:0,pts:[]};
function drawSup(){const svg=$('#supSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');const X=v=>40+(v-7)*640;
  svg.appendChild(el('line',{x1:40,y1:60,x2:680,y2:60,stroke:ink,'stroke-width':2}));svg.appendChild(el('circle',{cx:40,cy:60,r:7,fill:css('--paper'),stroke:nv,'stroke-width':3}));svg.appendChild(el('circle',{cx:680,cy:60,r:7,fill:css('--paper'),stroke:nv,'stroke-width':3}));
  svg.appendChild(el('text',{x:40,y:90,'text-anchor':'middle','font-size':'14',fill:ink},'7'));svg.appendChild(el('text',{x:680,y:90,'text-anchor':'middle','font-size':'14',fill:ink},'8'));
  SUP.pts.forEach((p,i)=>{svg.appendChild(el('circle',{cx:X(p.u),cy:60,r:5,fill:nv}));svg.appendChild(el('circle',{cx:X(p.m),cy:40,r:5,fill:gd}));svg.appendChild(el('line',{x1:X(p.u),y1:60,x2:X(p.m),y2:40,stroke:gd,'stroke-dasharray':'3 3'}));});}
$('#supGo').onclick=()=>{const v=parseFloat($('#supIn').value.replace(',','.'));if(isNaN(v)){$('#supOut').textContent='Bir sayı yaz.';return;}
  if(!(v>7&&v<8)){$('#supOut').innerHTML=v.toString().replace('.',',')+' aralıkta değil: (7, 8) yalnız 7\'den büyük 8\'den küçük sayıları içerir.';return;}
  const m=(v+8)/2;SUP.tries++;SUP.pts.push({u:v,m});drawSup();
  const ms=m.toFixed(Math.min(12,(v.toString().split('.')[1]||'').length+1)).replace('.',',');
  $('#supOut').innerHTML='Senin sayın: <b>'+v.toString().replace('.',',')+'</b>. Daha büyüğü: <b>'+ms+'</b> = (senin sayın + 8) / 2 — o da aralıkta.'+(SUP.tries>=3?'<br><span style="color:var(--gold)">Her adımda 8\'e olan uzaklık yarıya iniyor ama hiçbir zaman sıfır olmuyor: en büyük eleman yok, 8 yalnızca üst sınır.</span>':'');};
$('#supIn').addEventListener('keydown',e=>{if(e.key==='Enter')$('#supGo').click();});
$('#supReset').onclick=()=>{SUP={tries:0,pts:[]};drawSup();$('#supOut').textContent='7 ile 8 arasında bir sayı yaz.';$('#supIn').value='';};
function stopAll(){}
"""
build({'TITLE':'Matematik 9 · Hafta 2 · Gerçek Sayı Aralıkları','CRUMB':'Matematik · Ünite 1 Sayılar · Hafta 2','SUBTITLE':'Gerçek sayı aralıkları ve aralıklarda işlemler','PALETTE':PALETTES['mat'],'FOOT':'Fen Lisesi 9 · Matematik · Ünite 1 · Hafta 2','KEY':'ah9-mat-h02','PACKAGE':'Matematik 9 · Ünite 1 · Hafta 2 · Gerçek sayı aralıkları','PAKET':'mat-h02','HAFTA':'2','SECTIONS':SEC,'MINI':MINI,'QUIZ':QUIZ,'SIMJS':SIM,'INIT':'drawI();drawK();drawGame();drawSup();'},'mat-h02.html')
