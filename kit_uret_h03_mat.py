import json
from kit_build import build, PALETTES
J=lambda x:json.dumps(x,ensure_ascii=False)
SEC=r'''
<section class="tab" id="t1" role="tabpanel" aria-labelledby="tab1">
  <h1>Sayıların soyağacı: doğaldan gerçeğe</h1>
  <p class="lead">Geçen hafta 7 ile 8 arasında sonsuz sayı olduğunu gördük. Bu hafta o sayıların <em>kimliğini</em> soruyoruz: hangileri kesir olarak yazılabilir, hangileri asla yazılamaz; toplama-çarpma gibi işlemler hangi kümelerde "içeride kalır", hangilerinde dışarı taşar. Cevaplar yalnızca sınav için değil: A4 kâğıdından telefonun hesap makinesine kadar her yerde bu ayrım iş görüyor.</p>
  <div class="card">
    <p>Sayı kümeleri iç içe kutulardır: <b>ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</b>. Her yeni kutu, bir öncekinde <em>çözümü olmayan</em> bir denklemi çözmek için açılmıştır: x + 5 = 2 doğal sayılarda çözülemez (tam sayılar gerekir); 2x = 1 tam sayılarda çözülemez (kesirler gerekir); x² = 2 kesirlerde çözülemez (irrasyoneller gerekir). Bu hafta bu kutuların içini, sınırlarını ve içinde geçerli olan işlem kurallarını inceleyeceğiz; sonunda "x² = 2'nin çözümü kesir olamaz" cümlesini <em>ispat</em> edeceğiz.</p>
  </div>
  <div class="box life"><div class="t">Merak sorusu</div>Bir A4 kâğıdını uzun kenarından ikiye katla: A5 elde edersin ve şekil "aynı" kalır — kenar oranı değişmez. Bunun için oranın <b>√2</b> olması gerekir. Peki 210 mm × 297 mm ölçülerindeki kâğıdın oranı gerçekten √2 mi? Yoksa matbaacılar yaklaşık bir değere mi razı oluyor? 4. sekmede; cevabın içinde bu haftanın ana fikri var: √2 hiçbir kesire eşit değildir.</div>
  <div class="box def"><div class="t">Bu haftanın hedefleri (MEB Ünite 1 · Sayılar)</div>Doğal, tam, rasyonel, irrasyonel ve gerçek sayı kümelerinin kapsama ilişkisini ve elemanlarını ayırt etmek · sıralama ve "arada olma" (yoğunluk) özelliklerini gerekçelendirmek · rasyonel sayıları ondalık açılımlarından (sonlu / devirli) tanımak ve devirli ondalığı kesre çevirmek · toplama ve çarpmanın işlem özelliklerini (kapalılık, değişme, birleşme, etkisiz ve ters eleman, dağılma) cebirsel olarak ifade etmek, karşı örnekle sınamak · √2'nin irrasyonel olduğunu çelişkiyle ispat sezgisiyle görmek.</div>
  <div class="nextbtn"><button class="btn" data-done="1" data-go="2">Anladım, hatırlatmaya geç →</button></div>
</section>
<section class="tab" id="t2" role="tabpanel" aria-labelledby="tab2">
  <h2>Hatırlatma ve aralıklı tekrar</h2>
  <div class="grid2">
    <div class="card"><b>Ortaokuldan sayı kümeleri</b><p>Doğal sayılar ℕ = {0, 1, 2, 3, …} (MEB'de 0 dahildir; 1'den başlayana "sayma sayıları" denir). Tam sayılar ℤ = {…, −2, −1, 0, 1, 2, …}. Rasyonel sayılar ℚ: a/b biçiminde yazılabilenler (a, b tam sayı, b ≠ 0).</p></div>
    <div class="card"><b>Kesir ↔ ondalık</b><p>3/8 = 0,375 (payda 8, bölme biter). 1/3 = 0,333… (bölme hiç bitmez, 3 tekrar eder). Ondalıktan kesre: 0,75 = 75/100 = 3/4. Devirli ondalığı kesre çevirmeyi bu hafta öğreneceğiz.</p></div>
    <div class="card"><b>Geçen haftadan: aralıklar</b><p>[a, b] uçlar dahil, (a, b) hariç. ∩ "ve", ∪ "veya". (2, 6) aralığında sonsuz gerçek sayı ama yalnız 3 tam sayı vardır: 3, 4, 5. Bu hafta o "sonsuz sayının" hangi kümelerden geldiğini soracağız.</p></div>
    <div class="card"><b>Dersler arası köprü</b><p>Fizik H2'de her ölçüm sonucunu sonlu basamakla yazdın: 14,3 cm, 2,50 × 10³ m. Sonlu ondalık daima rasyoneldir; yani hiçbir ölçüm aleti irrasyonel bir sayı "okuyamaz". π ve √2 ancak <em>tanımla</em> yakalanır, cetvelle değil.</p></div>
  </div>
  <h3>Aralıklı tekrar (3 soru, anında geri bildirim)</h3>
  <div id="miniQuiz"></div>
  <div class="nextbtn"><button class="btn" data-done="2" data-go="3">Konu anlatımına geç →</button></div>
</section>
<section class="tab" id="t3" role="tabpanel" aria-labelledby="tab3">
  <h2>Konu anlatımı</h2>
  <h3>3.1 Kutular neden açıldı? Sayı kümelerinin gerekçesi</h3>
  <p>Her sayı kümesi bir sorunun cevabıdır. Doğal sayılar <em>saymak</em> için yeter; ama "5 liram vardı, 8 lira harcadım" borç ister: negatif sayılar ve ℤ. "3 ekmeği 4 kişiye böl" kesir ister: ℚ. Peki "kenarı 1 olan karenin köşegeni kaç?" Pisagor'la x² = 2. Bu denklemin çözümü olan √2, göreceğimiz gibi, hiçbir kesire eşit değildir; işte irrasyoneller ve ℝ.</p>
  <table>
    <tr><th>Küme</th><th>Sembol</th><th>Elemanları</th><th>Çözdüğü denklem</th><th>Örnek</th></tr>
    <tr><td>Doğal sayılar</td><td>ℕ</td><td>0, 1, 2, 3, …</td><td>x + 2 = 5</td><td>7, √16 = 4, 0</td></tr>
    <tr><td>Tam sayılar</td><td>ℤ</td><td>…, −2, −1, 0, 1, 2, …</td><td>x + 5 = 2</td><td>−3, −√25 = −5</td></tr>
    <tr><td>Rasyonel sayılar</td><td>ℚ</td><td>a/b, (a, b ∈ ℤ, b ≠ 0)</td><td>2x = 1</td><td>1/2, −7/3, 0,75, 0,(3)</td></tr>
    <tr><td>İrrasyonel sayılar</td><td>ℚ′ (ℝ − ℚ)</td><td>kesir olarak yazılamayanlar</td><td>x² = 2</td><td>√2, √10, π, 0,1010010001…</td></tr>
    <tr><td>Gerçek sayılar</td><td>ℝ = ℚ ∪ ℚ′</td><td>sayı doğrusunun tüm noktaları</td><td>—</td><td>hepsi</td></tr>
  </table>
  <div class="box def"><div class="t">Kapsama zinciri</div><b>ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</b> ve ℚ ∩ ℚ′ = ∅, ℚ ∪ ℚ′ = ℝ. Bir sayı ℕ'deyse otomatik olarak ℤ, ℚ ve ℝ'dedir; ama tersi doğru değil. Soru "hangi kümenin elemanıdır?" diye sorarsa <em>en dar</em> kutuyu bulmak yeterlidir; "hangi kümelerin?" diye sorarsa o kutudan dışarıya doğru hepsini say.</div>
  <div class="box warn"><div class="t">Tuzak: görünüşe aldanmak</div>√16 kök işaretli ama irrasyonel değil: 4. 12/4 kesir gibi ama tam sayı: 3. 0,999… ondalık gibi ama 1'e eşit (geçen hafta ispatladık). Kimliği <b>değer</b> belirler, yazılış değil.</div>
  <div class="sim">
    <h3>Sayı yerleştirici</h3>
    <div class="hint">Bir sayı yaz ya da hazır örneklerden birine dokun; simülasyon sayıyı en dar kümesine yerleştirsin. Devirli ondalığı parantezle yaz: 0,(3). Kök için √10 ya da kok10 yazabilirsin.</div>
    <div class="ctrl">
      <label>Sayı <input type="text" id="nyIn" placeholder="örn. −3, 7/2, 0,75, √10" style="width:170px"></label>
      <button id="nyGo">Yerleştir</button>
    </div>
    <div class="ctrl" id="nyChips"><button class="alt nychip" data-n="−3">−3</button><button class="alt nychip" data-n="0">0</button><button class="alt nychip" data-n="7/2">7/2</button><button class="alt nychip" data-n="12/4">12/4</button><button class="alt nychip" data-n="0,75">0,75</button><button class="alt nychip" data-n="0,(3)">0,(3)</button><button class="alt nychip" data-n="√9">√9</button><button class="alt nychip" data-n="√10">√10</button><button class="alt nychip" data-n="−√25">−√25</button><button class="alt nychip" data-n="π">π</button><button class="alt nychip" data-n="3,14">3,14</button><button class="alt nychip" data-n="0,999…">0,999…</button></div>
    <div class="svgwrap"><svg id="nySvg" viewBox="0 0 720 300" role="img" aria-label="İç içe sayı kümeleri"></svg></div>
    <div class="readout" id="nyOut" style="display:block">Bir sayı yaz ya da örnek seç.</div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Bir sayının kimliğini yazılışı değil <em>değeri</em> belirler: √9 kök işaretine rağmen doğal sayıdır, 12/4 kesir çizgisine rağmen tam sayıdır. Kutular iç içe olduğundan bir sayı en dar kutusuna yerleşince dışarıdaki tüm kutuların da elemanıdır. 0,999… örneğini dene: 1'e eşit olduğu için ℕ'ye gider.</div>

  <h3>3.2 Sıralama ve "arada olma": tam sayılar seyrek, kesirler yoğun</h3>
  <p>Tam sayılarda "bir sonraki" vardır: 3'ten sonra 4 gelir, arada tam sayı yoktur. Rasyonel sayılarda böyle bir şey yoktur: 1/3 ile 1/2 arasında 5/12 vardır; 1/3 ile 5/12 arasında 3/8; ve bu hiç bitmez. Genel kural: a &lt; b iki rasyonel sayıysa ortalamaları (a + b)/2 de rasyoneldir ve tam aralarındadır. Aynı işlemi tekrarlayınca <b>iki rasyonel arasında sonsuz rasyonel</b> bulunur. Bu özelliğe <em>yoğunluk</em> denir.</p>
  <div class="formula"><div class="m">a &lt; <span class="frac"><span>a + b</span><span>2</span></span> &lt; b</div><div class="why">İki sayının ortalaması ikisinin arasındadır; ℚ toplama ve 2'ye bölmeye kapalı olduğundan ortalama yine rasyoneldir.</div></div>
  <p><b>Fen lisesi notu:</b> irrasyoneller de yoğundur; hatta iki rasyonel arasında daima bir irrasyonel vardır (örneğin a ile b arasına a + (b − a)/√2 sayısını yerleştir; √2 irrasyonel olduğundan bu sayı da irrasyoneldir). Sayı doğrusunda rasyoneller ve irrasyoneller birbirinin "içine işlemiş" durumdadır; yine de irrasyoneller, sayılamayacak kadar daha çoktur (Cantor, 1874) — bu, üniversitede karşılaşacağın en şaşırtıcı sonuçlardan biridir.</p>
  <div class="box warn"><div class="t">Tuzak: "ardışık kesir"</div>"1/3'ten sonra gelen kesir 2/3'tür" cümlesi anlamsızdır; kesirlerde <em>ardışık</em> kavramı yoktur. Sınavda "a ile b arasında kaç rasyonel sayı vardır?" sorusunun cevabı, a ≠ b olduğu sürece daima <b>sonsuz</b>tur; "kaç tam sayı" diye sorarsa sayılır.</div>

  <h3>3.3 Ondalık açılım: bir sayının parmak izi</h3>
  <p>Bir kesri bölme yaparak ondalığa çevirdiğinde üç şeyden biri olur:</p>
  <table>
    <tr><th>Açılım türü</th><th>Örnek</th><th>Ne oluyor?</th><th>Küme</th></tr>
    <tr><td>Sonlu</td><td>3/8 = 0,375</td><td>Kalan bir noktada 0 olur, bölme biter.</td><td>ℚ</td></tr>
    <tr><td>Sonsuz devirli</td><td>5/11 = 0,4545… = 0,(45)</td><td>Bir kalan tekrar eder, basamaklar döngüye girer.</td><td>ℚ</td></tr>
    <tr><td>Sonsuz devirsiz</td><td>√2 = 1,41421356…</td><td>Hiçbir blok sonsuza dek tekrar etmez.</td><td>ℚ′</td></tr>
  </table>
  <div class="box def"><div class="t">Neden rasyonel sayının açılımı ya biter ya devreder?</div>a/b bölmesinde her adımdaki kalan 0, 1, 2, …, b − 1 sayılarından biridir: yalnızca <b>b tane</b> seçenek. En geç b adım sonra ya kalan 0 olur (biter) ya da daha önce çıkmış bir kalan yeniden çıkar; o andan itibaren basamaklar aynen tekrar eder. Bu yüzden 1/7'nin devir uzunluğu en fazla 6 olabilir (gerçekten de 0,(142857), altı basamak). Tersi de doğrudur: devirli her ondalık bir kesirdir — aşağıdaki simülasyon bunu hesaplıyor.</div>
  <p><b>Devirli ondalığı kesre çevirme yöntemi:</b> sayıya x de; virgülü devir bloğunun sonuna taşıyacak kadar 10 ile çarp; devirsiz kısım varsa bir de virgülü devrin başına taşıyacak kadar çarp; iki eşitliği çıkar — sonsuz kuyruklar birbirini götürür.</p>
  <div class="formula"><div class="m">x = 0,(27) &nbsp;⇒&nbsp; 100x − x = 27,(27) − 0,(27) = 27 &nbsp;⇒&nbsp; x = <span class="frac"><span>27</span><span>99</span></span> = <span class="frac"><span>3</span><span>11</span></span></div><div class="why">Devir 2 basamak → 10² ile çarp. Kuyruklar özdeş olduğu için fark tam sayı çıkar.</div></div>
  <div class="formula"><div class="m">x = 2,1(6) &nbsp;⇒&nbsp; 100x − 10x = 216,(6) − 21,(6) = 195 &nbsp;⇒&nbsp; x = <span class="frac"><span>195</span><span>90</span></span> = <span class="frac"><span>13</span><span>6</span></span></div><div class="why">Devirsiz kısım 1 basamak, devir 1 basamak: 10x ile 100x'i çıkar. Kısayol: (216 − 21)/90.</div></div>
  <div class="sim">
    <h3>Devirli ondalık ↔ kesir dönüştürücü</h3>
    <div class="hint">İki yönde çalışır. "Kesir → ondalık" modunda bölmedeki kalanları izle: bir kalan tekrar ettiği anda devir başlar. "Ondalık → kesir" modunda tam kısım, devirsiz kısım ve devreden bloğu ayrı ayrı gir; simülasyon 10 ile çarpma ve çıkarma adımlarını yazsın.</div>
    <div class="ctrl">
      <label>Mod <select id="dvMode" style="font:inherit;padding:6px;border-radius:8px"><option value="a">Kesir → ondalık</option><option value="b">Ondalık → kesir</option></select></label>
      <span id="dvA"><label>Pay <input type="number" id="dvP" value="5" min="0" max="99999" style="width:80px"></label><label>Payda <input type="number" id="dvQ" value="11" min="1" max="9999" style="width:80px"></label></span>
      <span id="dvB" style="display:none"><label>Tam kısım <input type="number" id="dvT" value="2" min="0" max="9999" style="width:70px"></label><label>Devirsiz kısım <input type="text" id="dvN" value="1" maxlength="4" style="width:70px" placeholder="boş olabilir"></label><label>Devreden <input type="text" id="dvR" value="6" maxlength="4" style="width:70px"></label></span>
      <button id="dvGo">Hesapla</button>
    </div>
    <div class="readout" id="dvOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Kesirden ondalığa giderken kalanların sayısı sınırlı olduğundan bölme ya biter ya döngüye girer: 1/7'de altı farklı kalandan sonra 1 yeniden gelir. Ondalıktan kesre giderken "10 ile çarp ve çıkar" adımı sonsuz kuyruğu yok eder; sonuç daima iki tam sayının oranıdır. İki yön birlikte şu cümleyi kanıtlar: <b>bir sayı rasyoneldir ⇔ ondalık açılımı sonlu ya da devirlidir.</b></div>

  <h3>3.4 İşlem özellikleri: kurallar ve kuralların bozulduğu yerler</h3>
  <p>Toplama ve çarpma gerçek sayılarda "uslu" işlemlerdir: sıra fark etmez, gruplama fark etmez, birbirlerine dağılırlar. Çıkarma ve bölme öyle değildir. Bu farkları ezberlemek yerine <em>cebirsel olarak yazmayı</em> ve <em>karşı örnekle sınamayı</em> öğreneceğiz — çünkü MEB'in bu haftaki hedefi tam olarak budur.</p>
  <table>
    <tr><th>Özellik</th><th>Toplama (her a, b, c ∈ ℝ)</th><th>Çarpma (her a, b, c ∈ ℝ)</th><th>Çıkarma / bölmede?</th></tr>
    <tr><td>Kapalılık</td><td>a + b ∈ ℝ</td><td>a · b ∈ ℝ</td><td>ℝ'de evet (bölmede b ≠ 0); alt kümelerde her zaman değil</td></tr>
    <tr><td>Değişme</td><td>a + b = b + a</td><td>a · b = b · a</td><td>Hayır: 5 − 3 ≠ 3 − 5, 8 ÷ 2 ≠ 2 ÷ 8</td></tr>
    <tr><td>Birleşme</td><td>(a + b) + c = a + (b + c)</td><td>(a · b) · c = a · (b · c)</td><td>Hayır: (8 − 4) − 2 ≠ 8 − (4 − 2)</td></tr>
    <tr><td>Etkisiz eleman</td><td>a + 0 = a</td><td>a · 1 = a</td><td>Yalnız sağdan: a − 0 = a ama 0 − a ≠ a</td></tr>
    <tr><td>Ters eleman</td><td>a + (−a) = 0</td><td>a · (1/a) = 1 (a ≠ 0)</td><td>0'ın çarpmaya göre tersi yoktur</td></tr>
    <tr><td>Dağılma</td><td colspan="2">a · (b + c) = a · b + a · c &nbsp;(çarpma toplama üzerine dağılır)</td><td>Toplama çarpma üzerine dağılmaz: a + (b·c) ≠ (a+b)(a+c)</td></tr>
  </table>
  <div class="box def"><div class="t">Kapalılık: işlem kümenin içinde kalıyor mu?</div>Bir küme bir işleme <b>kapalıdır</b> demek, kümeden alınan <em>her</em> iki eleman için sonucun yine kümede olması demektir. Tek bir kaçak (karşı örnek) kapalılığı bozar.
  <table style="margin-top:8px">
    <tr><th>Küme</th><th>+</th><th>−</th><th>×</th><th>÷ (b ≠ 0)</th></tr>
    <tr><td>ℕ</td><td>✓</td><td>✗ 3 − 5 = −2</td><td>✓</td><td>✗ 3 ÷ 2 = 1,5</td></tr>
    <tr><td>ℤ</td><td>✓</td><td>✓</td><td>✓</td><td>✗ 3 ÷ 2 = 1,5</td></tr>
    <tr><td>ℚ</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
    <tr><td>ℚ′ (irrasyoneller)</td><td>✗ √2 + (−√2) = 0</td><td>✗ √2 − √2 = 0</td><td>✗ √2 · √2 = 2</td><td>✗ √2 ÷ √2 = 1</td></tr>
    <tr><td>ℝ</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
  </table></div>
  <div class="box warn"><div class="t">Tuzak: "irrasyonel × irrasyonel = irrasyonel"</div>√2 · √8 = √16 = 4. İki irrasyonelin çarpımı, toplamı, farkı rasyonel <em>olabilir</em>; hiçbir garanti yoktur. Buna karşılık <b>rasyonel + irrasyonel daima irrasyoneldir</b> ve <b>sıfırdan farklı rasyonel × irrasyonel daima irrasyoneldir</b>: toplam r rasyonel olsaydı, irrasyonel = r − rasyonel = rasyonel olurdu; çelişki.</div>
  <div class="sim">
    <h3>İşlem özelliği sınayıcı</h3>
    <div class="hint">Bir eşitlik seç, a, b, c kaydırıcılarını oynat; iki taraf teraziye konur. Doğru özellikler her değerde dengede kalır; sahte özellikler bazı değerlerde şans eseri denk gelse bile tek bir dengesizlik iddiayı çürütür.</div>
    <div class="ctrl">
      <label>Eşitlik <select id="opSel" style="font:inherit;padding:6px;border-radius:8px;max-width:260px"></select></label>
      <label>a <input type="range" id="opa" min="-6" max="6" value="5"><output id="opao">5</output></label>
      <label>b <input type="range" id="opb" min="-6" max="6" value="3"><output id="opbo">3</output></label>
      <label>c <input type="range" id="opc" min="-6" max="6" value="2"><output id="opco">2</output></label>
    </div>
    <div class="svgwrap"><svg id="opSvg" viewBox="0 0 720 170" role="img" aria-label="Terazi"></svg></div>
    <div class="readout" id="opOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>"Her a, b, c için" iddiası ile "bazı a, b, c için" gözlemi arasındaki farkı. a − b = b − a eşitliği a = b iken tutar; ama özellik olması için <em>her</em> değerde tutması gerekir. Terazinin bir kez bile eğilmesi iddiayı düşürür; hiç eğilmemesi ise ispat değildir — ispat, cebirsel gerekçeyle yapılır (örneğin toplamanın değişme özelliği sayıların tanımından gelir).</div>

  <h3>3.5 √2 neden kesir olamaz? Çelişkiyle ispat</h3>
  <p>Şimdiye kadar "√2 irrasyoneldir" dedik; bunu nereden biliyoruz? Hesap makinesi 1,41421356… gösteriyor, devir görünmüyor — ama görünmemesi olmaması demek değil; devir milyonuncu basamakta başlıyor olabilir. Kesin bilgi ancak ispatla gelir. Yöntem: tersini varsay, çelişkiye ulaş.</p>
  <ol class="steps">
    <li><b>Varsayım:</b> √2 rasyonel olsun: √2 = a/b, a ve b aralarında asal tam sayılar (kesir sadeleştirilmiş).<div class="why">Her kesir sadeleştirilebilir; bu yüzden "ortak böleni yok" demek serbest.</div></li>
    <li>İki tarafın karesini al: 2 = a²/b² → <b>a² = 2b²</b>.<div class="why">a² çift sayıdır (2 ile bir tam sayının çarpımı).</div></li>
    <li>a² çiftse a da çifttir (tek sayının karesi tektir: (2k+1)² = 4k² + 4k + 1). Öyleyse a = 2k yazılabilir.<div class="why">Buradaki mantık: "a tek olsaydı a² tek olurdu" — bir karşı olasılığı eliyoruz.</div></li>
    <li>Yerine koy: (2k)² = 2b² → 4k² = 2b² → <b>b² = 2k²</b> → b² çift → b de çift.</li>
    <li><b>Çelişki:</b> a da b de çift; ama "aralarında asal" demiştik. Varsayım yanlış: √2 rasyonel değildir. ∎<div class="why">İspat, a/b'nin hangi kesir olduğuna hiç bakmadı; bu yüzden <em>hiçbir</em> kesir √2'ye eşit olamaz. "Denedim, bulamadım"dan çok daha güçlü bir sonuç.</div></li>
  </ol>
  <div class="box def"><div class="t">Aynı kalıp başka nerede işler?</div>√3, √5, √6 ve tam kare olmayan her doğal sayının kökü için aynı ispat (2 yerine ilgili asal ile) çalışır. Ayrıca √2 + 1, 3√2, √2/5 gibi türevler de irrasyoneldir: rasyonel olsalardı, rasyonel işlemlerle √2'yi rasyonel yapabilirdik. π'nin irrasyonelliği ise çok daha zor bir ispat ister (1761, Lambert).</div>

  <h3>3.6 Sık karışan noktalar</h3>
  <div class="grid2">
    <div class="card"><b>0 doğal sayı mıdır?</b><p>MEB programında evet: ℕ = {0, 1, 2, …}. Sayma sayıları {1, 2, 3, …} ayrıca adlandırılır. Soruda "pozitif tam sayı" deniyorsa 0 dışarıdadır.</p></div>
    <div class="card"><b>22/7 ve 3,14</b><p>İkisi de rasyoneldir; π'nin yaklaşık değerleridir, kendisi değil. "π ≈ 22/7" işareti eşitlik değil, yakınlık bildirir.</p></div>
    <div class="card"><b>Kök her zaman irrasyonel değildir</b><p>√49 = 7, √0,25 = 0,5, ∛8 = 2. Kök altındaki sayının uygun bir kuvvet olup olmadığına bak.</p></div>
    <div class="card"><b>Örüntü ≠ devir</b><p>0,1010010001… bir kurala göre yazılıyor ama hiçbir blok aynen tekrar etmiyor; devirsizdir, dolayısıyla irrasyoneldir.</p></div>
  </div>
  <div class="nextbtn"><button class="btn" data-done="3" data-go="4">Günlük yaşam örneklerine geç →</button></div>
</section>
<section class="tab" id="t4" role="tabpanel" aria-labelledby="tab4">
  <h2>Günlük yaşamdan örnekler</h2>
  <div class="card"><h3 style="margin-top:0">1 · A4 kâğıdı: √2'ye "yaklaşan" matbaa</h3>
    <p><b>Durum:</b> A serisi kâğıtlar ikiye katlanınca aynı biçimi korur; bunun için uzun kenar / kısa kenar oranının √2 olması gerekir (oran r ise katlanınca kısa/uzun = (r/2)/1 → r/2 = 1/r → r² = 2).</p>
    <p><b>Kavramla bağ:</b> Kâğıt tam milimetreyle kesilir; iki tam sayının oranı rasyoneldir, √2 ise irrasyonel. Öyleyse hiçbir gerçek A4 kâğıdı tam olarak √2 oranında olamaz; standart, √2'ye <em>en yakın</em> tam milimetre çiftini seçer.</p>
    <p><b>Hesap:</b> 297/210 = 99/70 = 1,4142857… (devirli: 142857 bloğu döner). √2 = 1,4142135… Fark yaklaşık 0,00007; 297 mm üzerinde 0,02 mm'den küçük — gözle görülmez. Kontrol: (99/70)² = 9801/4900 = 2,0002…; tam 2 değil.</p>
    <p><b>Sonuç:</b> Mühendislik irrasyonel sayıyı "yeterince yakın" bir rasyonelle temsil eder; matematik ise aradaki farkın sıfır <em>olamayacağını</em> bilir. İzmit'teki bir matbaa da, uluslararası standart da bu uzlaşmayla çalışır.</p></div>
  <div class="card"><h3 style="margin-top:0">2 · Bisiklet dişli oranı: devirli ondalığın gizli anlamı</h3>
    <p><b>Durum:</b> Krank dişlisi 48, arka dişli 18 dişli. Bir pedal turunda arka tekerlek kaç tur döner? 48/18.</p>
    <p><b>Kavramla bağ:</b> Diş sayıları tam sayı olduğundan oran daima rasyoneldir. Sadeleştir: 48/18 = 8/3 = 2,(6). Devirli açılım, bölmenin hiç bitmediğini söyler: pedal ile tekerlek "tam tur" hizasına ancak 3 pedal turu sonra (8 tekerlek turu) yeniden gelir.</p>
    <p><b>Hesap:</b> Sadeleşmiş kesrin paydası 3 → zincirdeki belirli bir bakla, arka dişlideki aynı dişe her 3 pedal turunda bir oturur. Sabit vitesli bisikletlerde bu sayı, arka lastikte aşınan "kayma noktası" sayısını verir: 48/18 için 3 nokta; 48/16 = 3/1 için tek nokta (lastik tek yerden aşınır, kötü seçim).</p>
    <p><b>Sonuç:</b> "Sadeleştirilmiş kesrin paydası" soyut bir kural değil; lastiğin nerede aşınacağını söyler.</p></div>
  <div class="card"><h3 style="margin-top:0">3 · Telefonun hesap makinesi neden 0,1 + 0,2 = 0,30000000000000004 der?</h3>
    <p><b>Durum:</b> Bazı hesap makinesi ve programlama uygulamalarında 0,1 + 0,2 sonucu tam 0,3 çıkmaz.</p>
    <p><b>Kavramla bağ:</b> Devirli olmak sayının değil, <em>tabanın</em> özelliğidir. 1/3 onluk tabanda devirlidir (0,333…) ama üçlük tabanda sonludur (0,1). Bilgisayar ikilik taban kullanır; 1/10 ikilikte devirlidir: 0,0001100110011… Sonlu bellek bu kuyruğu keser; kesilen sayı artık tam 0,1 değildir.</p>
    <p><b>Analiz:</b> Kesme hatası her sayıda küçüktür ama toplamda birikir ve son basamakta görünür. Bankacılık yazılımları bu yüzden lirayı ondalıkla değil, <em>kuruş cinsinden tam sayıyla</em> tutar: tam sayılar ikilikte hep sonludur.</p>
    <p><b>Sonuç:</b> 0,1 ve 0,2 rasyoneldir, toplamları tam 0,3'tür; hata matematikte değil, temsildedir. "Rasyonel sayı = sonlu ya da devirli açılım" kuralı tabanla birlikte düşünülmelidir.</p></div>
  <div class="card"><h3 style="margin-top:0">4 · Mutfakta tarif ölçekleme: ℚ neden dört işleme kapalı?</h3>
    <p><b>Durum:</b> 3 kişilik tarifte 2/3 su bardağı süt var; 4 kişilik yapılacak. Ölçü kabı 1/4 bardak hassasiyetinde.</p>
    <p><b>Kavramla bağ:</b> Ölçek çarpanı 4/3 rasyonel; 2/3 × 4/3 = 8/9 rasyonel — ℚ çarpmaya kapalı olduğu için sonuç yine bir kesir, yani ölçülebilir bir miktar. Hiçbir tarif ölçeklemesi seni kesir dünyasının dışına atamaz.</p>
    <p><b>Hesap:</b> 8/9 = 0,(8) bardak. Ölçü kabındaki en yakın çizgi: 3/4 = 0,75 mi, 1 mi? |8/9 − 3/4| = 5/36 ≈ 0,139; |1 − 8/9| = 1/9 ≈ 0,111 → 1 bardak daha yakın. Aradaki 1/9 bardak fark (yaklaşık 25 mL) pişirmede fark etmez, kimyada eder.</p>
    <p><b>Sonuç:</b> Sonuç ℚ'da kaldı ama ölçü kabının "çözünürlüğü" ondalık kesirlerle sınırlı; yuvarlama hatası burada da vardı — tıpkı telefondaki gibi.</p></div>
  <div class="nextbtn"><button class="btn" data-done="4" data-go="5">Etkileşimli materyale geç →</button></div>
</section>
<section class="tab" id="t5" role="tabpanel" aria-labelledby="tab5">
  <h2>Etkileşimli materyal</h2>
  <div class="sim">
    <h3>Küme yerleştirme oyunu</h3>
    <div class="hint">12 sayı; her biri için <em>en dar</em> kümeyi seç. Kök, kesir ve devirli ondalık kılığındaki tam sayılar tuzak olarak sık gelir. Sonunda hangi kılığa aldandığını görürsün.</div>
    <div id="game"></div>
    <div class="ctrl"><button id="gmReset" class="alt">Oyunu sıfırla</button></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Sayının kimliği için önce <em>değerini</em> hesaplamak gerektiğini: √16'yı 4'e, 12/4'ü 3'e, 0,999…'u 1'e indirmeden karar verilmez. Ayrıca "en dar küme" düşüncesi kapsama zincirini pekiştirir: ℕ'de olan her sayı ℤ, ℚ ve ℝ'de de vardır.</div>
  <div class="sim">
    <h3>Karşı örnek avcısı</h3>
    <div class="hint">Bir kapalılık iddiası verilir; dört aday arasından <em>geçerli</em> karşı örneği bul ya da iddianın doğru olduğuna karar ver. Geçerli karşı örnek: iki eleman da kümede, sonuç kümenin dışında. Elemanlardan biri kümede değilse örnek geçersizdir.</div>
    <div id="cegame"></div>
    <div class="ctrl"><button id="ceReset" class="alt">Yeniden başla</button></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Bir iddiayı çürütmek için tek karşı örnek yeter, ama karşı örneğin kurallara uyması gerekir. "√2 + 1 rasyonel değil, öyleyse ℚ toplamaya kapalı değil" demek hatalıdır: √2 zaten ℚ'da değildir. Kapalılık yalnızca kümenin <em>kendi</em> elemanlarıyla sınanır.</div>
  <div class="box def"><div class="t">Gözlem soruları</div>1) Yerleştirme oyununda en çok hangi kılığa aldandın: kök mü, kesir mi, devirli ondalık mı? &nbsp; 2) Avcıda "karşı örnek yok" dediğin iddialar hangi kümelerdeydi? Bu kümelerin ortak yanı ne? &nbsp; 3) İrrasyoneller kümesi dört işlemin hiçbirine kapalı değil; peki "rasyonel + irrasyonel" neden daima irrasyonel? (3.4'teki gerekçeyi kendi cümlenle yaz.)</div>
  <div class="nextbtn"><button class="btn" data-done="5" data-go="6">Çözümlü örneklere geç →</button></div>
</section>
<section class="tab" id="t6" role="tabpanel" aria-labelledby="tab6">
  <h2>Çözümlü örnekler</h2>
  <div class="card"><h3 style="margin-top:0">Temel · −7, 0, 2/5, √16, √17, 0,12 ve 1,2020020002… sayılarını kümelerine yerleştir</h3>
    <ol class="steps"><li>Önce değerleri sadeleştir: √16 = 4; 0,12 = 12/100 = 3/25; diğerleri olduğu gibi.</li><li>ℕ: 0, √16. &nbsp; ℤ (ℕ dışı): −7. &nbsp; ℚ (ℤ dışı): 2/5, 0,12. &nbsp; ℚ′: √17 (17 tam kare değil), 1,2020020002… (devirsiz).<div class="why">Hepsi ℝ'nin elemanı; soru "hangi kümelerin" derse zinciri dışa doğru say: 0 ∈ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Temel · 0,4545… sayısını kesre çevir</h3>
    <ol class="steps"><li>x = 0,(45); devir 2 basamak → 100x = 45,(45).</li><li>100x − x = 45 → 99x = 45 → x = 45/99 = <b>5/11</b>.<div class="why">Kontrol: 5 ÷ 11 = 0,4545… ✓. Kısayol: devreden blok / (devir uzunluğu kadar 9).</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · 2,1666… sayısını kesre çevir</h3>
    <ol class="steps"><li>x = 2,1(6): tam kısım 2, devirsiz kısım "1" (1 basamak), devreden "6" (1 basamak).</li><li>Virgülü devrin başına: 10x = 21,(6). Virgülü devrin sonuna: 100x = 216,(6).</li><li>100x − 10x = 216 − 21 = 195 → 90x = 195 → x = 195/90 = <b>13/6</b>.<div class="why">Kısayol: (216 − 21) / 90: paydada devir kadar 9, devirsiz kısım kadar 0. Kontrol: 13 ÷ 6 = 2,1666… ✓.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · Aşağıdaki kümeler verilen işleme kapalı mı? a) ℤ, bölme b) ℚ′, toplama c) tek sayılar, toplama d) çift sayılar, çarpma</h3>
    <ol class="steps"><li>a) Hayır: 3 ÷ 2 = 1,5 ∉ ℤ. (6 ÷ 3 = 2 örneği kapalılığı <em>kanıtlamaz</em>; tek kaçak yeter.)</li><li>b) Hayır: √2 + (−√2) = 0 ∉ ℚ′. İki eleman da irrasyonel, toplam rasyonel.</li><li>c) Hayır: 3 + 5 = 8 tek değil.</li><li>d) Evet: çift sayılar 2m ve 2n ise çarpım 2m · 2n = 2(2mn), yine çift. Genel gösterim gerekir; örnek yetmez.<div class="why">"Kapalı" demek için genel bir gerekçe, "kapalı değil" demek için tek bir karşı örnek yeterlidir: iki iddianın ispat yükü farklıdır.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · √2 ispatındaki mantığı kullanarak √2 + 1'in irrasyonel olduğunu göster</h3>
    <ol class="steps"><li>Tersini varsay: √2 + 1 = r rasyonel olsun.</li><li>O hâlde √2 = r − 1. ℚ çıkarmaya kapalıdır; r ve 1 rasyonel → r − 1 rasyonel → √2 rasyonel.</li><li>Ama √2'nin irrasyonel olduğunu ispatlamıştık: çelişki. Öyleyse √2 + 1 irrasyoneldir. ∎<div class="why">Yeni bir ispat yazmadık; bilinen sonucu ve ℚ'nun kapalılığını birleştirdik. Aynı yol 3√2, √2/5, √2 − 7 için de işler; ama √2 · √2 için işlemez — çünkü orada ikinci çarpan rasyonel değil.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · "Her rasyonel sayının ondalık açılımı sonlu ya da devirlidir" — neden? 1/7 üzerinden gerekçele</h3>
    <ol class="steps"><li>1 ÷ 7 bölmesinde kalanlar: 1 → 3 → 2 → 6 → 4 → 5 → 1. Yedinci adımda kalan 1 yeniden çıktı; basamaklar 142857 bloğuyla tekrar eder: 1/7 = 0,(142857).</li><li>Genel gerekçe: a ÷ b bölmesinde kalan daima {0, 1, …, b − 1} kümesindendir; b tane olasılık var. En geç b adımda ya 0 gelir (biter) ya bir kalan tekrar eder (devir). "Sınırlı sayıda kutuya sınırsız sayıda top koyarsan bir kutuya iki top düşer" — güvercin yuvası ilkesi.</li><li>Sonuç: devir uzunluğu en fazla b − 1 olabilir. 1/7 için 6 (en uzun olası); 1/11 için 2; 1/3 için 1.<div class="why">Bu gerekçe, devirsiz sonsuz açılımı olan her sayının (π, √2) rasyonel olamayacağını da söyler: kalanlar sınırlıysa devir kaçınılmazdır.</div></li></ol></div>
  <div class="nextbtn"><button class="btn" data-done="6" data-go="7">Kendini sına →</button></div>
</section>
<section class="tab" id="t7" role="tabpanel" aria-labelledby="tab7">
  <h2>Kendini sına</h2>
  <p>12 soru: 4 temel, 5 orta, 3 fen lisesi. Cevaplarını işaretle ve sonunda kaydet; değerlendirme öğretmenine iletilir.</p>
  <div id="quiz"></div><div class="score" id="scoreBox"></div>
  <div class="nextbtn"><button class="btn" id="quizCheck">Cevapları kaydet</button><button class="btn alt" id="quizReset">Testi temizle</button><button class="btn" data-done="7" data-go="8">Özete geç →</button></div>
</section>
<section class="tab" id="t8" role="tabpanel" aria-labelledby="tab8">
  <h2>Özet ve tuzaklar</h2>
  <div class="summary">
    <div class="card"><b>Kümeler</b>ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ; ℝ = ℚ ∪ ℚ′. Kimliği değer belirler: √16 = 4 ∈ ℕ, 12/4 = 3 ∈ ℕ. En dar kümeyi bul, dışa doğru say.</div>
    <div class="card"><b>Ondalık açılım</b>Sonlu ya da devirli ⇔ rasyonel. Devirsiz sonsuz ⇔ irrasyonel. Devirliyi kesre: 10ᵏ ile çarp, çıkar; kısayol 0,(ab) = ab/99.</div>
    <div class="card"><b>İşlem özellikleri</b>+ ve ×: değişme, birleşme, etkisiz (0, 1), ters (−a, 1/a), dağılma a(b+c) = ab+ac. − ve ÷: değişme ve birleşme yok. Kapalılık: tek kaçak bozar.</div>
    <div class="card"><b>İspat</b>√2 = a/b varsay → a² = 2b² → a çift → b çift → çelişki. Rasyonel + irrasyonel = irrasyonel (ℚ'nun kapalılığından).</div>
  </div>
  <h3>Sık yapılan 5 hata</h3>
  <ol>
    <li>Kök işareti görünce "irrasyonel" demek: √49 = 7 doğal sayıdır.</li>
    <li>İki irrasyonelin toplamının ya da çarpımının irrasyonel olduğunu sanmak: √2 · √8 = 4, √2 + (−√2) = 0.</li>
    <li>"a − b = b − a" gibi yanlış bir özelliği tek örnekle (a = b) doğru sanmak: özellik <em>her</em> değerde tutmalı.</li>
    <li>0,(27) sayısını 27/100 yazmak: 27/100 = 0,27 sonludur. Devirli için payda 99'dur: 27/99 = 3/11.</li>
    <li>Örüntüyü devir sanmak: 0,1010010001… bir kurala göre yazılır ama tekrar eden blok yoktur; irrasyoneldir.</li>
  </ol>
  <div class="box life"><div class="t">Gelecek haftaya köprü</div>Bu hafta (√2 + 1)(√2 − 1) = 1 çıktı; çünkü (a + b)(a − b) = a² − b². Bu "iki kare farkı" özdeşliği ve tam kare özdeşlikleri gelecek haftanın konusu: 99² = (100 − 1)² gibi hızlı hesaplar, alan modeliyle ispat ve köklü ifadelerde eşlenikle bağ. Hazırlık: (a + b)² = a² + b² <em>neden</em> yanlış, bir örnekle göster.</div>
  <div class="nextbtn"><button class="btn" data-done="8" data-go="1">Haftayı tamamladım ✓</button></div>
</section>'''
MINI_L=[
 {"s":'<span class="tag">Geçen hafta</span> A = [−2, 3) ve B = (0, 5] ise A ∩ B hangisidir?',"o":['(0, 3)','[0, 3]','[−2, 5]','(0, 3]'],"a":0,"e":'Örtüşen bölge 0 ile 3 arası. 0, B\'de hariç; 3, A\'da hariç → her iki uç yuvarlak: (0, 3).'},
 {"s":'<span class="tag">2 hafta önce</span> √18 ifadesinin en sade biçimi hangisidir?',"o":['3√2','2√3','9√2','6'],"a":0,"e":'18 = 9 · 2 → √18 = √9 · √2 = 3√2. Tam kare çarpanı dışarı çıkar; 18 tam kare olmadığı için sonuç irrasyoneldir — bu hafta bunun neden böyle olduğunu ispatlayacağız.'},
 {"s":'<span class="tag">Fizik H2 köprüsü</span> Bir cetvelle ölçülen 14,3 cm değeri için hangisi doğrudur?',"o":['Sonlu ondalık olduğu için rasyoneldir','Tam sayı olmadığı için irrasyoneldir','Doğal sayıdır','Ölçüm sonuçları sayı kümelerine girmez'],"a":0,"e":'14,3 = 143/10; iki tam sayının oranı → rasyonel. Her ölçüm sonlu basamakla yazıldığından daima rasyoneldir.'}]
QUIZ_L=[
 {"s":'Aşağıdakilerden hangisi tam sayı olduğu hâlde doğal sayı değildir?',"o":['−4','√25','0','7/1'],"a":0,"e":'ℕ = {0, 1, 2, …}; −4 ∈ ℤ ama ∉ ℕ. √25 = 5 ve 7/1 = 7 doğal sayıdır; MEB programında 0 da doğal sayıdır.'},
 {"s":'Aşağıdakilerden hangisi irrasyoneldir?',"o":['√8','√9','0,(8)','8/√4'],"a":0,"e":'√8 = 2√2; 8 tam kare olmadığından irrasyonel. √9 = 3, 0,(8) = 8/9 ve 8/√4 = 8/2 = 4 rasyoneldir.'},
 {"s":'0,272727… sayısının kesir olarak eşiti hangisidir?',"o":['3/11','27/100','27/90','3/10'],"a":0,"e":'x = 0,(27) → 100x − x = 27 → x = 27/99 = 3/11. 27/100 = 0,27 (sonlu), 27/90 = 3/10 = 0,3: farklı sayılar.'},
 {"s":'Doğal sayılar kümesi aşağıdaki işlemlerden hangisine kapalı DEĞİLDİR?',"o":['Çıkarma','Toplama','Çarpma','Toplama ve çarpma'],"a":0,"e":'3 − 5 = −2 ∉ ℕ: tek karşı örnek yeter. İki doğal sayının toplamı ve çarpımı daima doğal sayıdır.'},
 {"tag":'bağlam',"s":'<b>Bilgi:</b> A4 kâğıdı 210 mm × 297 mm boyutundadır; tasarımda hedeflenen kenar oranı √2\'dir.<br>297/210 oranı için hangisi doğrudur?',"o":['Rasyoneldir; √2\'nin yaklaşık değeridir, kendisine eşit değildir','İrrasyoneldir, çünkü √2\'ye eşittir','Tam sayıdır, çünkü ölçüler tam sayıdır','Sonsuz ve devirsiz ondalık açılımı vardır'],"a":0,"e":'297/210 = 99/70: iki tam sayının oranı → rasyonel, açılımı devirli (1,4(142857)). √2 irrasyoneldir; hiçbir kesire tam eşit olamaz, kâğıt ölçüleri yalnızca yaklaştırır.'},
 {"tag":'bağlam',"s":'Bir bisiklette krank dişlisi 48, arka dişli 18 dişlidir. Bir pedal turunda arka tekerleğin kaç tur döndüğünü veren 48/18 oranı için hangisi doğrudur?',"o":['8/3 = 2,666… → rasyonel, devirli ondalık','2,67 → sonlu ondalık','2,666… → devirsiz olduğu için irrasyonel','Ondalık açılımı yoktur'],"a":0,"e":'Sadeleştir: 48/18 = 8/3. 8 ÷ 3 = 2,(6) devirli, dolayısıyla rasyonel. 2,67 yalnızca yuvarlanmış değeridir.'},
 {"s":'(√2 + 1)(√2 − 1) = 2 − 1 = 1 işlemine göre aşağıdakilerden hangisi kesinlikle doğrudur?',"o":['İki irrasyonel sayının çarpımı rasyonel olabilir','İki irrasyonel sayının çarpımı daima irrasyoneldir','√2 + 1 rasyoneldir','İrrasyonel sayılar kümesi çarpmaya kapalıdır'],"a":0,"e":'Tek bir örnek "daima irrasyonel" ve "kapalı" iddialarını çürütür. √2 + 1 irrasyoneldir: rasyonel olsaydı 1 çıkarınca √2 rasyonel olurdu.'},
 {"s":'x rasyonel, y irrasyonel bir sayı ise x + y toplamı için hangisi doğrudur?',"o":['Daima irrasyoneldir','Daima rasyoneldir','x\'in işaretine bağlıdır','Bazen rasyonel, bazen irrasyoneldir'],"a":0,"e":'x + y = r rasyonel olsaydı y = r − x olurdu; ℚ çıkarmaya kapalı olduğundan y rasyonel çıkardı — çelişki. Toplam daima irrasyoneldir.'},
 {"s":'Aşağıdaki eşitliklerden hangisi her a, b, c gerçek sayısı için doğru DEĞİLDİR?',"o":['a − (b − c) = (a − b) − c','a · (b + c) = a·b + a·c','a + b = b + a','(a · b) · c = a · (b · c)'],"a":0,"e":'Çıkarmanın birleşme özelliği yoktur: a = 5, b = 3, c = 1 için 5 − (3 − 1) = 3 ama (5 − 3) − 1 = 1. Diğerleri dağılma, değişme ve birleşme özellikleridir.'},
 {"tag":'bağlam',"s":'<b>Bilgi:</b> Bilgisayar ve telefonlar sayıları ikilik tabanda saklar; 0,1 sayısının ikilik açılımı 0,000110011… biçiminde devirlidir ve sonlu sayıda basamakla saklanır.<br>Bir hesap makinesi uygulamasının 0,1 + 0,2 için 0,30000000000000004 vermesi en iyi nasıl açıklanır?',"o":['Devirli açılım sonlu basamakta kesildiği için küçük bir yuvarlama hatası oluşur','0,1 ve 0,2 irrasyonel sayılardır','Rasyonel sayılar toplamaya kapalı değildir','Onluk tabanda da 0,1 + 0,2 tam olarak 0,3 etmez'],"a":0,"e":'0,1 ve 0,2 rasyoneldir ve toplamları tam 0,3\'tür; hata, ikilikte devirli olan açılımın kesilmesinden gelir. Aynı sayı bir tabanda sonlu, başka tabanda devirli olabilir (1/3 onlukta devirli, üçlükte 0,1).'},
 {"s":'√2\'nin irrasyonel olduğu ispatında "√2 = a/b, a ile b aralarında asal" varsayımından a² = 2b² elde edilir. Doğru devam hangisidir?',"o":['a² çift olduğundan a çifttir; a = 2k yazılıp b\'nin de çift olduğu gösterilir','b² çift olduğundan b tek sayıdır','a² = 2b² olduğundan a = 2b\'dir','a ve b\'nin ikisi de tek sayı olmalıdır'],"a":0,"e":'Tek sayının karesi tektir; a² çiftse a çifttir. a = 2k → 4k² = 2b² → b² = 2k² → b de çift. İkisi de çift olunca "aralarında asal" varsayımı çöker: çelişki.'},
 {"s":'0,101001000100001… (birler arasındaki sıfır sayısı her seferinde bir artıyor) sayısı için hangisi doğrudur?',"o":['İrrasyoneldir, çünkü açılımı sonsuz ve devirsizdir','Rasyoneldir, çünkü belirli bir örüntüsü vardır','Rasyoneldir, çünkü yalnızca 0 ve 1 rakamlarından oluşur','Sonlu ondalığa dönüştürülebilir'],"a":0,"e":'Örüntü olması devir olması demek değildir: devirde aynı blok sonsuza dek aynen tekrar eder. Burada bloklar sürekli uzadığından açılım devirsizdir → irrasyonel.'},
 {"open":True,"s":'√3\'ün irrasyonel olduğunu, √2 ispatındaki adımları izleyerek çelişkiyle ispatla. (İpucu: a² = 3b² ise a, 3\'e bölünür; çünkü 3\'e bölünmeyen bir sayının karesi de 3\'e bölünmez.)',"ans":'√3 = a/b (aralarında asal) varsay → a² = 3b² → a², 3\'ün katı → a, 3\'ün katı; a = 3k → 9k² = 3b² → b² = 3k² → b de 3\'ün katı → "aralarında asal" varsayımıyla çelişki → √3 irrasyoneldir.',"e":'Çelişki adımı ve "a, 3\'ün katı" gerekçesi beklenir.'},
 {"open":True,"s":'"İrrasyonel sayılar kümesi çarpmaya kapalıdır" iddiasını değerlendir: doğruysa gerekçele, yanlışsa geçerli bir karşı örnek ver ve karşı örneğin neden geçerli olduğunu açıkla.',"ans":'Yanlış. √2 · √2 = 2 (veya √2 · √8 = 4): çarpanların ikisi de irrasyonel (kümede), çarpım rasyonel (küme dışında). Geçerli karşı örneğin iki koşulu da sağlanıyor; tek karşı örnek kapalılığı bozar.',"e":'Geçerli karşı örnek + iki koşulun kontrolü beklenir.'}]
MINI="const MINI="+J(MINI_L)+";"
QUIZ="const QUIZ="+J(QUIZ_L)+";"
SIM=r"""
/* --- yardımcılar --- */
function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b];}return a;}
function fmtN(v){if(v==null||!isFinite(v))return 'tanımsız';if(Number.isInteger(v))return String(v).replace('-','−');return (Math.round(v*1000)/1000).toString().replace('.',',').replace('-','−');}
/* --- Sayı yerleştirici --- */
function parseNum(str){let s=str.trim().replace(/,/g,'.').replace(/−/g,'-').replace(/\s+/g,'').replace(/…/g,'...');if(!s)return null;let m;
  if(/^-?(π|pi)$/i.test(s))return {set:'I',label:'π',note:'π irrasyoneldir (Lambert, 1761); 3,14 ve 22/7 yalnızca yaklaşık değerleridir.'};
  if(m=s.match(/^(-?)(√|kok|sqrt)\(?(\d+)\)?$/i)){const n=+m[3],r=Math.sqrt(n);if(Number.isInteger(r)){const v=(m[1]?-1:1)*r;return {set:v>=0?'N':'Z',label:m[1].replace('-','−')+'√'+n+' = '+fmtN(v),note:n+' tam kare olduğundan kök "kaybolur": sonuç tam sayı.'};}return {set:'I',label:m[1].replace('-','−')+'√'+n,note:n+' tam kare değil → √'+n+' irrasyonel (√2 ispatının aynısı işler).'};}
  if(m=s.match(/^(-?\d+)$/)){const v=+m[1];return {set:v>=0?'N':'Z',label:fmtN(v),note:v>=0?'Doğal sayı (0 dahil).':'Negatif tam sayı: ℤ\'de var, ℕ\'de yok.'};}
  if(m=s.match(/^(-?)(\d+)\/(\d+)$/)){let p=+m[2],q=+m[3];if(!q)return {set:null,label:s,note:'Payda 0 olamaz: tanımsız.'};const g=gcd(p,q);p/=g;q/=g;if(q===1){const v=(m[1]?-1:1)*p;return {set:v>=0?'N':'Z',label:s.replace('-','−')+' = '+fmtN(v),note:'Sadeleşince tam sayı çıktı; kesir çizgisi kimliği değiştirmez.'};}return {set:'Q',label:m[1].replace('-','−')+p+'/'+q+(g>1?' (sadeleşmiş)':''),note:'İki tam sayının oranı: rasyonel. Ondalık açılımı sonlu ya da devirlidir.'};}
  if(m=s.match(/^(-?)(\d+)\.(\d*)\((\d+)\)$/)){const T=m[2],N=m[3],R=m[4],k=N.length,mm=R.length;const num=+(T+N+R)-+(T+N),den=Math.pow(10,k)*(Math.pow(10,mm)-1),g=gcd(num,den);return {set:'Q',label:m[1].replace('-','−')+T+','+N+'('+R+') = '+m[1].replace('-','−')+(num/g)+'/'+(den/g),note:'Devirli ondalık daima rasyoneldir (10 ile çarp, çıkar).'};}
  if(m=s.match(/^(-?)(\d+)\.(\d+)$/)){const dec=m[3];if(/^0+$/.test(dec)){const v=(m[1]?-1:1)*+m[2];return {set:v>=0?'N':'Z',label:s.replace('.',',').replace('-','−')+' = '+fmtN(v),note:'Ondalık kısmı sıfır: aslında tam sayı.'};}const den=Math.pow(10,dec.length),num=+(m[2]+dec),g=gcd(num,den);return {set:'Q',label:m[1].replace('-','−')+m[2]+','+dec+' = '+m[1].replace('-','−')+(num/g)+'/'+(den/g),note:'Sonlu ondalık = paydası 10\'un kuvveti olan kesir → rasyonel.'};}
  if(/^(-?)0\.9+\.\.\.$/.test(s))return {set:'N',label:'0,999… = 1',note:'Sonsuz dokuz tam olarak 1\'dir (10x − x = 9 → x = 1). Yazılış ondalık, değer doğal sayı.'};
  if(/\.\.\.$/.test(s))return {set:null,label:s,note:'Sonsuz açılım: devir varsa parantezle yaz (0,(3)); devir yoksa sayı irrasyoneldir ama bunu üç noktayla değil, tanımla belirleriz.'};
  return {set:null,label:s,note:'Anlayamadım. Örnekler: −3 · 7/2 · 0,75 · 0,(3) · √10 · π'};}
const NYCHAIN={N:'ℕ → dolayısıyla ℤ, ℚ ve ℝ\'nin de elemanı.',Z:'ℤ (ℕ değil) → dolayısıyla ℚ ve ℝ\'nin elemanı.',Q:'ℚ (ℤ değil) → dolayısıyla ℝ\'nin elemanı.',I:'ℚ′ irrasyonel → ℝ\'nin elemanı; ℚ\'nun elemanı değil.'};
function drawNY(res){const svg=$('#nySvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold'),paper=css('--paper');
  const R=[['R',10,10,700,280,'ℝ gerçek sayılar'],['Q',30,50,430,220,'ℚ rasyonel sayılar'],['Z',50,92,300,160,'ℤ tam sayılar'],['N',70,134,170,100,'ℕ doğal sayılar'],['I',490,50,200,220,'ℚ′ irrasyoneller']];
  R.forEach(([k,x,y,w,h,t])=>{const on=res&&res.set===k;svg.appendChild(el('rect',{x,y,width:w,height:h,rx:14,fill:on?gd:paper,'fill-opacity':on?.35:1,stroke:k==='I'?gd:nv,'stroke-width':on?3:1.5,'stroke-dasharray':k==='I'?'6 4':'none'}));svg.appendChild(el('text',{x:x+10,y:y+20,'font-size':'14','font-weight':'700',fill:ink},t));});
  if(res&&res.set){const pos={N:[110,215],Z:[170,235],Q:[310,250],I:[560,170]}[res.set];svg.appendChild(el('circle',{cx:pos[0],cy:pos[1],r:6,fill:css('--bad')}));svg.appendChild(el('text',{x:pos[0]+10,y:pos[1]+5,'font-size':'15','font-weight':'700',fill:css('--bad')},res.label.split(' = ')[0]));}}
function runNY(){const r=parseNum($('#nyIn').value);if(!r){drawNY(null);$('#nyOut').textContent='Bir sayı yaz ya da örnek seç.';return;}drawNY(r);$('#nyOut').innerHTML=r.set?'<b>'+r.label+'</b> → '+NYCHAIN[r.set]+' <span style="color:var(--ink2)">'+r.note+'</span>':'<b>'+r.label+'</b>: '+r.note;}
$('#nyGo').onclick=runNY;$('#nyIn').addEventListener('keydown',e=>{if(e.key==='Enter')runNY();});
$$('.nychip').forEach(b=>b.onclick=()=>{$('#nyIn').value=b.dataset.n;runNY();});
/* --- Devirli ondalık ↔ kesir --- */
function longDiv(p,q){const intPart=Math.floor(p/q);let r=p%q;const digits=[],seen={},rems=[];let repStart=-1;while(r!==0&&digits.length<300){if(seen[r]!==undefined){repStart=seen[r];break;}seen[r]=digits.length;rems.push(r);r*=10;digits.push(Math.floor(r/q));r=r%q;}return {intPart,digits,repStart,rems,ended:r===0};}
$('#dvMode').addEventListener('change',()=>{const a=$('#dvMode').value==='a';$('#dvA').style.display=a?'':'none';$('#dvB').style.display=a?'none':'';dvRun();});
function dvRun(){const out=$('#dvOut');if($('#dvMode').value==='a'){const p=Math.abs(Math.floor(+$('#dvP').value||0)),q=Math.floor(+$('#dvQ').value||0);if(!q){out.textContent='Payda 0 olamaz.';return;}const d=longDiv(p,q);let dec;
    if(d.ended)dec=d.digits.length?d.intPart+','+d.digits.join(''):String(d.intPart);
    else if(d.repStart>=0)dec=d.intPart+','+d.digits.slice(0,d.repStart).join('')+'('+d.digits.slice(d.repStart).join('')+')';
    else dec=d.intPart+','+d.digits.join('')+'… (devir 300 basamaktan uzun; yine de vardır)';
    const g=gcd(p,q);let h='<b>'+p+'/'+q+' = '+dec+'</b>';if(g>1)h+=' &nbsp;(sadeleşmiş: '+(p/g)+'/'+(q/g)+')';
    h+='<br>'+(d.ended?'Kalan 0 oldu → <b>sonlu</b> açılım.':d.repStart>=0?'Kalanlar: '+d.rems.join(' → ')+' → <b>'+d.rems[d.repStart]+' tekrar etti</b> → devir uzunluğu '+(d.digits.length-d.repStart)+' (en fazla '+(q-1)+' olabilirdi).':'')+'<br><span style="color:var(--ink2)">Her adım: kalan × 10, paydaya böl, bölüm basamak olur, yeni kalan bir sonrakine geçer. Kalan '+q+' değerden birini alabildiği için döngü kaçınılmazdır.</span>';out.innerHTML=h;}
  else{const T=Math.abs(Math.floor(+$('#dvT').value||0)),N=($('#dvN').value||'').replace(/\D/g,''),R=($('#dvR').value||'').replace(/\D/g,'');if(!R){out.textContent='Devreden blok gerekli (örn. 6 ya da 45).';return;}const k=N.length,m=R.length;const big=+(T+''+N+R),small=+(T+''+N);const num=big-small,den=Math.pow(10,k)*(Math.pow(10,m)-1),g=gcd(num,den);
    let h='<b>x = '+T+','+N+'('+R+')</b><br>';
    if(k)h+='10<sup>'+k+'</sup>x = '+(+(T+''+N))+','+'('+R+') &nbsp;<span style="color:var(--ink2)">(virgül devrin başına)</span><br>';
    h+='10<sup>'+(k+m)+'</sup>x = '+big+',('+R+') &nbsp;<span style="color:var(--ink2)">(virgül devrin sonuna)</span><br>';
    h+='Çıkar: ('+Math.pow(10,k+m)+' − '+Math.pow(10,k)+')x = '+big+' − '+small+' = '+num+' → x = '+num+'/'+den+(g>1?' = <b>'+(num/g)+'/'+(den/g)+'</b>':'');
    h+='<br><span style="color:var(--ink2)">Kontrol: '+(num/g)+' ÷ '+(den/g)+' = '+(num/den).toFixed(6).replace('.',',')+'… Kısayol: paydada devir kadar 9, devirsiz kısım kadar 0.</span>';out.innerHTML=h;}}
$('#dvGo').onclick=dvRun;['#dvP','#dvQ','#dvT','#dvN','#dvR'].forEach(s=>$(s).addEventListener('keydown',e=>{if(e.key==='Enter')dvRun();}));
/* --- İşlem özelliği sınayıcı --- */
const OPS=[['a + b = b + a',(a,b,c)=>a+b,(a,b,c)=>b+a,true,'Toplamanın değişme özelliği'],['a − b = b − a',(a,b,c)=>a-b,(a,b,c)=>b-a,false,'Çıkarmada değişme yoktur'],['a · b = b · a',(a,b,c)=>a*b,(a,b,c)=>b*a,true,'Çarpmanın değişme özelliği'],['a ÷ b = b ÷ a',(a,b,c)=>b?a/b:NaN,(a,b,c)=>a?b/a:NaN,false,'Bölmede değişme yoktur'],['(a + b) + c = a + (b + c)',(a,b,c)=>(a+b)+c,(a,b,c)=>a+(b+c),true,'Toplamanın birleşme özelliği'],['(a − b) − c = a − (b − c)',(a,b,c)=>(a-b)-c,(a,b,c)=>a-(b-c),false,'Çıkarmada birleşme yoktur'],['(a · b) · c = a · (b · c)',(a,b,c)=>(a*b)*c,(a,b,c)=>a*(b*c),true,'Çarpmanın birleşme özelliği'],['(a ÷ b) ÷ c = a ÷ (b ÷ c)',(a,b,c)=>(b&&c)?(a/b)/c:NaN,(a,b,c)=>(c&&b)?a/(b/c):NaN,false,'Bölmede birleşme yoktur'],['a · (b + c) = a·b + a·c',(a,b,c)=>a*(b+c),(a,b,c)=>a*b+a*c,true,'Çarpmanın toplama üzerine dağılma özelliği'],['a + (b · c) = (a + b) · (a + c)',(a,b,c)=>a+b*c,(a,b,c)=>(a+b)*(a+c),false,'Toplama çarpma üzerine dağılmaz'],['(b + c) ÷ a = b÷a + c÷a',(a,b,c)=>a?(b+c)/a:NaN,(a,b,c)=>a?b/a+c/a:NaN,true,'Bölme, bölünen tarafta toplama üzerine dağılır (a ≠ 0)'],['a ÷ (b + c) = a÷b + a÷c',(a,b,c)=>(b+c)?a/(b+c):NaN,(a,b,c)=>(b&&c)?a/b+a/c:NaN,false,'Bölme, bölen tarafta dağılmaz']];
OPS.forEach((o,i)=>{const op=document.createElement('option');op.value=i;op.textContent=o[0];$('#opSel').appendChild(op);});
function drawOP(){const a=+$('#opa').value,b=+$('#opb').value,c=+$('#opc').value;$('#opao').value=a;$('#opbo').value=b;$('#opco').value=c;const o=OPS[+$('#opSel').value];const L=o[1](a,b,c),Rv=o[2](a,b,c);const svg=$('#opSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');
  const und=!isFinite(L)||!isFinite(Rv);const eq=!und&&Math.abs(L-Rv)<1e-9;const ang=und?0:Math.max(-12,Math.min(12,(Rv-L)*2));
  svg.appendChild(el('path',{d:'M340 150 L380 150 L360 110 Z',fill:css('--ink2')}));
  const g=el('g',{transform:'rotate('+ang+' 360 110)'});g.appendChild(el('line',{x1:120,y1:110,x2:600,y2:110,stroke:ink,'stroke-width':5,'stroke-linecap':'round'}));
  [[120,'Sol taraf',L,nv],[600,'Sağ taraf',Rv,gd]].forEach(([x,t,v,col])=>{g.appendChild(el('line',{x1:x,y1:110,x2:x,y2:60,stroke:ink,'stroke-width':2}));g.appendChild(el('rect',{x:x-70,y:22,width:140,height:40,rx:8,fill:col,opacity:.85}));g.appendChild(el('text',{x,y:48,'text-anchor':'middle','font-size':'18','font-weight':'700',fill:'#fff'},fmtN(v)));g.appendChild(el('text',{x,y:135,'text-anchor':'middle','font-size':'12',fill:css('--ink2')},t));});svg.appendChild(g);
  let msg='<b>'+o[0]+'</b> için a = '+fmtN(a)+', b = '+fmtN(b)+', c = '+fmtN(c)+': sol = <b>'+fmtN(L)+'</b>, sağ = <b>'+fmtN(Rv)+'</b> → '+(und?'bölen 0: tanımsız':eq?'eşit':'<span style="color:var(--bad)">eşit değil</span>')+'.<br>';
  msg+=o[3]?'<span style="color:var(--ok)">Bu bir özelliktir: '+o[4]+' — her değerde dengede kalır (bölmede bölen 0 olamaz).</span>':(eq?'<span style="color:var(--gold)">Bu değerlerde şans eseri eşit çıktı; ama '+o[4]+'. Kaydırıcıları değiştir: tek bir dengesizlik iddiayı çürütür.</span>':'<span style="color:var(--bad)">Karşı örnek buldun: '+o[4]+'.</span>');
  $('#opOut').innerHTML=msg;}
['#opSel','#opa','#opb','#opc'].forEach(s=>$(s).addEventListener('input',drawOP));
/* --- Küme yerleştirme oyunu --- */
const GB=['ℕ','ℤ (ℕ değil)','ℚ (ℤ değil)','ℚ′ irrasyonel'];
const GQ=[['√16',0,'√16 = 4, doğal sayı. Kök işareti kimlik değildir.'],['−√25',1,'−√25 = −5: tam sayı ama negatif, ℕ dışı.'],['0,75',2,'0,75 = 3/4: sonlu ondalık, rasyonel; tam sayı değil.'],['√12',3,'12 tam kare değil → √12 = 2√3 irrasyonel.'],['0,(6)',2,'0,(6) = 6/9 = 2/3: devirli ondalık rasyoneldir.'],['0',0,'MEB programında 0 doğal sayıdır.'],['3,14',2,'3,14 = 314/100 rasyoneldir; π\'nin yaklaşık değeridir, π değildir.'],['π',3,'π irrasyoneldir: devirsiz sonsuz açılım.'],['−7/2',2,'−3,5: rasyonel, tam sayı değil.'],['0,1010010001…',3,'Örüntü var, devir yok → irrasyonel.'],['√2 · √8',0,'√16 = 4: iki irrasyonelin çarpımı doğal sayı çıktı.'],['0,999…',0,'0,999… = 1 (geçen hafta ispatladık): doğal sayı.']];
let GM={i:0,s:0,log:[]};
function drawGame(){const box=$('#game');if(GM.i>=GQ.length){box.innerHTML='<div class="readout">Puan: '+GM.s+' / '+GQ.length+'</div>'+GM.log.map(l=>'<div class="q '+(l.ok?'right':'wrong')+'"><div class="stem">'+l.q+'</div><div class="fb">'+(l.ok?'✔ ':'✘ Doğru: <b>'+l.d+'</b> · ')+l.e+'</div></div>').join('');return;}
  const q=GQ[GM.i];box.innerHTML='<div class="readout">'+(GM.i+1)+' / '+GQ.length+' · Puan '+GM.s+'</div><div class="q"><div class="stem" style="font-size:22px">'+q[0]+' &nbsp;<span style="font-weight:400;font-size:15px;color:var(--ink2)">en dar küme?</span></div><div class="ctrl">'+GB.map((b,j)=>'<button class="btn alt" data-v="'+j+'">'+b+'</button>').join('')+'</div><div class="fb" id="gmFb"></div></div>';
  box.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{const ok=+b.dataset.v===q[1];if(ok)GM.s++;GM.log.push({q:q[0],ok,d:GB[q[1]],e:q[2]});box.querySelector('.q').classList.add(ok?'right':'wrong');box.querySelectorAll('[data-v]').forEach(x=>x.disabled=true);$('#gmFb').innerHTML=(ok?'✔ Doğru. ':'✘ Doğru: <b>'+GB[q[1]]+'</b>. ')+q[2]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="gmNext">Sonraki →</button>';$('#gmNext').onclick=()=>{GM.i++;drawGame();};});}
$('#gmReset').onclick=()=>{GM={i:0,s:0,log:[]};drawGame();};
/* --- Karşı örnek avcısı --- */
const CE=[['ℕ (doğal sayılar) çıkarmaya kapalıdır.',['3 − 5 = −2','5 − 3 = 2','3 − (−5) = 8','Karşı örnek yok; iddia doğru'],0,'3 ve 5 doğal, fark −2 doğal değil: geçerli karşı örnek. 5 − 3 kümede kalır; −5 zaten ℕ\'de olmadığından üçüncü aday geçersizdir.'],
 ['ℤ (tam sayılar) bölmeye kapalıdır.',['6 ÷ 3 = 2','0 ÷ 5 = 0','3 ÷ 2 = 1,5','Karşı örnek yok; iddia doğru'],2,'3 ve 2 tam sayı, bölüm 1,5 tam sayı değil. Diğer bölmeler kümede kalıyor; kalmaları kapalılığı kanıtlamaz, tek kaçak bozar.'],
 ['ℚ (rasyonel sayılar) toplamaya kapalıdır.',['1/2 + 1/3 = 5/6','√2 + 1','0,5 + 0,25 = 0,75','Karşı örnek yok; iddia doğru'],3,'a/b + c/d = (ad + bc)/bd yine kesirdir: her durumda kümede kalır. √2 + 1 geçersiz aday: √2 ∈ ℚ değil.'],
 ['İrrasyonel sayılar kümesi toplamaya kapalıdır.',['√2 + √3','√2 + (−√2) = 0','1 + √2','Karşı örnek yok; iddia doğru'],1,'√2 ve −√2 irrasyonel, toplam 0 rasyonel: geçerli karşı örnek. √2 + √3 irrasyoneldir (bozmaz); 1 irrasyonel değildir (geçersiz).'],
 ['İrrasyonel sayılar kümesi çarpmaya kapalıdır.',['√2 · √8 = 4','√2 · √3 = √6','2 · √2','Karşı örnek yok; iddia doğru'],0,'√2 ve √8 irrasyonel, çarpım 4 rasyonel: geçerli. √6 irrasyonel kalır; 2 rasyonel olduğundan üçüncü aday geçersiz.'],
 ['Tek sayılar kümesi toplamaya kapalıdır.',['3 · 5 = 15','3 + 4 = 7','3 + 5 = 8','Karşı örnek yok; iddia doğru'],2,'İki tek sayının toplamı çifttir: 3 + 5 = 8. 3 · 5 çarpmadır (konu dışı); 4 tek değildir (geçersiz).'],
 ['Çift sayılar kümesi çarpmaya kapalıdır.',['2 · 4 = 8','2 · 3 = 6','4 ÷ 2 = 2','Karşı örnek yok; iddia doğru'],3,'2m · 2n = 2(2mn) daima çift: iddia doğru, karşı örnek olamaz. 3 çift değil (geçersiz), 4 ÷ 2 bölmedir (konu dışı).'],
 ['Negatif tam sayılar kümesi çarpmaya kapalıdır.',['(−2) · 3 = −6','(−2) · (−3) = 6','(−2) + (−3) = −5','Karşı örnek yok; iddia doğru'],1,'İki negatifin çarpımı pozitif: 6 kümede değil → geçerli karşı örnek. 3 negatif değil (geçersiz); toplama konu dışı.']];
let CG={i:0,s:0};
function drawCE(){const box=$('#cegame');if(CG.i>=CE.length){box.innerHTML='<div class="readout">Puan: '+CG.s+' / '+CE.length+'</div><p>Kural: "kapalı değil" için bir geçerli karşı örnek; "kapalı" için genel gerekçe gerekir.</p>';return;}
  const q=CE[CG.i];box.innerHTML='<div class="readout">'+(CG.i+1)+' / '+CE.length+' · Puan '+CG.s+'</div><div class="q"><div class="stem">İddia: '+q[0]+'</div><div class="opts">'+q[1].map((o,j)=>'<label><input type="radio" name="ce" value="'+j+'"> <span>'+o+'</span></label>').join('')+'</div><div class="ctrl"><button class="btn" id="ceGo">Kontrol et</button></div><div class="fb" id="ceFb"></div></div>';
  $('#ceGo').onclick=()=>{const v=box.querySelector('input:checked');if(!v)return;const ok=+v.value===q[2];if(ok)CG.s++;box.querySelector('.q').classList.add(ok?'right':'wrong');$('#ceGo').disabled=true;box.querySelectorAll('input').forEach(i=>i.disabled=true);$('#ceFb').innerHTML=(ok?'✔ Doğru. ':'✘ Doğru seçenek: <b>'+q[1][q[2]]+'</b>. ')+q[3]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="ceNext">Sonraki →</button>';$('#ceNext').onclick=()=>{CG.i++;drawCE();};};}
$('#ceReset').onclick=()=>{CG={i:0,s:0};drawCE();};
function stopAll(){}
"""
build({'TITLE':'Matematik 9 · Hafta 3 · Sayı Kümeleri ve İşlem Özellikleri','CRUMB':'Matematik · Ünite 1 Sayılar · Hafta 3','SUBTITLE':'Sayı kümeleri, ondalık açılım, işlem özellikleri ve √2 ispatı','PALETTE':PALETTES['mat'],'FOOT':'Fen Lisesi 9 · Matematik · Ünite 1 · Hafta 3','KEY':'ah9-mat-h03','PACKAGE':'Matematik 9 · Ünite 1 · Hafta 3 · Sayı kümeleri ve işlem özellikleri','PAKET':'mat-h03','HAFTA':'3','SECTIONS':SEC,'MINI':MINI,'QUIZ':QUIZ,'SIMJS':SIM,'INIT':'drawNY(null);dvRun();drawOP();drawGame();drawCE();'},'mat-h03.html')
