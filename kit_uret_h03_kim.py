import json
from kit_build import build, PALETTES
J=lambda x:json.dumps(x,ensure_ascii=False)
SEC=r'''
<section class="tab" id="t1" role="tabpanel" aria-labelledby="tab1">
  <h1>Elektron neden çekirdeğe düşmüyor?</h1>
  <p class="lead">Geçen hafta Rutherford'un modelini bir soruyla bıraktık: klasik fiziğe göre çekirdek çevresinde dolanan elektron sürekli ışıyıp saniyenin milyarda birinde çekirdeğe düşmeli. Düşmüyor. Üstelik neon tabelası yalnız kırmızı, sodyum lambası yalnız sarı ışık veriyor — her element kendi renklerinde. Bu iki bilmeceyi 1913'te Bohr, 1920'lerde kuantum fiziği çözdü. Bu hafta o çözümü, sonra atomun "kimlik kartını" öğreneceğiz: proton, nötron, elektron sayıları; izotoplar; iyonlar.</p>
  <div class="card">
    <p><b>İki bölüm:</b> Önce atom teorilerinin son iki halkası — Bohr modeli (enerji seviyeleri, ışık soğurma ve yayma) ve modern (bulut) model (belirsizlik, orbital). Sonra atomu sayılarla tanımlamak: atom numarası Z, kütle numarası A, izotop / izoton / izobar / izoelektronik tanecikler ve iyon oluşumu. Bu sayılar gelecek haftaların (elektron dizilimi, periyodik tablo) alfabesidir.</p>
  </div>
  <div class="box life"><div class="t">Merak sorusu</div>Bayram gecesi İzmit sahilinde havai fişekler: kırmızı, yeşil, mavi, sarı. Renkleri "boya" vermez — stronsiyum kırmızı, baryum yeşil, bakır mavi-yeşil, sodyum sarı ışır. Isı aynı, barut aynı; renk neden elemente göre değişiyor? Cevap Bohr modelinin tam kalbinde: 3. sekmede.</div>
  <div class="box def"><div class="t">Bu haftanın hedefleri (MEB Ünite 1 · Etkileşim → Atomdan Periyodik Tabloya)</div>Bohr atom teorisinin varsayımlarını ve eksikliklerini açıklamak; modern atom teorisiyle ilişkilendirmek (belirsizlik ilkesi, orbital kavramı) · elektron, proton ve nötronun yük, kütle ve keşif verilerini kullanmak · atom numarası ve kütle numarasından tanecik sayılarını hesaplamak · izotop, izoton, izobar ve izoelektronik tanecikleri ayırt etmek · iyon oluşumunu elektron alışverişiyle açıklamak · bilimsel bilginin değişebilirliğini atom modelleri üzerinden değerlendirmek.</div>
  <div class="nextbtn"><button class="btn" data-done="1" data-go="2">Anladım, hatırlatmaya geç →</button></div>
</section>
<section class="tab" id="t2" role="tabpanel" aria-labelledby="tab2">
  <h2>Hatırlatma ve aralıklı tekrar</h2>
  <div class="grid2">
    <div class="card"><b>Geçen haftadan: üç model</b><p>Dalton (dolu küre) → Thomson (üzümlü kek, elektron) → Rutherford (küçük yoğun çekirdek, boşluk). Her model bir deneyle düzeltildi; yanlışlanan iddia, korunan çekirdek fikir.</p></div>
    <div class="card"><b>Rutherford'un açık sorusu</b><p>Dolanan elektron ivmelidir; klasik fizik "ivmeli yük ışır" der → enerji kaybı → çekirdeğe düşme. Atom kararlı olduğuna göre modelde eksik bir kural var.</p></div>
    <div class="card"><b>Ortaokuldan: yük ve ışık</b><p>Zıt yükler çeker. Işık enerji taşır; rengi enerjisine bağlıdır: mor ışık kırmızıdan daha enerjiktir. Bu hafta "renk = enerji farkı" olacak.</p></div>
    <div class="card"><b>Dersler arası köprü</b><p>Matematik H1 bilimsel gösterim: elektronun kütlesi 9,1 × 10⁻³¹ kg, protonunki 1,67 × 10⁻²⁷ kg. Fizik H2: yükün SI birimi coulomb (C = A·s); elektronun yükü −1,6 × 10⁻¹⁹ C.</p></div>
  </div>
  <h3>Aralıklı tekrar (3 soru, anında geri bildirim)</h3>
  <div id="miniQuiz"></div>
  <div class="nextbtn"><button class="btn" data-done="2" data-go="3">Konu anlatımına geç →</button></div>
</section>
<section class="tab" id="t3" role="tabpanel" aria-labelledby="tab3">
  <h2>Konu anlatımı</h2>
  <h3>3.1 Bohr atom modeli (1913): elektron her yerde olamaz</h3>
  <p>Bohr, Rutherford'un çekirdeğini korudu; elektronlara ise cesur bir kural koydu: elektron çekirdek çevresinde <em>yalnızca belirli</em> uzaklıklardaki dairesel yörüngelerde bulunabilir. Her yörüngenin belirli bir enerjisi vardır (n = 1, 2, 3, … ya da K, L, M, N kabukları); araları yasaktır — merdiven basamakları gibi, rampa gibi değil.</p>
  <div class="box def"><div class="t">Bohr'un varsayımları</div>1) Elektronlar, çekirdek çevresinde belirli enerjili dairesel yörüngelerde (enerji seviyelerinde) dolanır; çekirdeğe en yakın seviye (n = 1) en düşük enerjilidir. 2) Elektron bir yörüngede dolanırken <b>ışıma yapmaz</b>; atom kararlıdır (<em>temel hâl</em>). 3) Elektron dışarıdan tam olarak iki seviye arasındaki fark kadar enerji alırsa üst seviyeye çıkar (<b>absorpsiyon</b>, <em>uyarılmış hâl</em>); geri dönerken aradaki enerji farkını bir ışık paketi (foton) olarak yayar (<b>emisyon</b>). Fotonun enerjisi, dolayısıyla rengi, seviye farkına eşittir: E<sub>foton</sub> = E<sub>üst</sub> − E<sub>alt</sub>.</div>
  <p><b>Neyi açıkladı?</b> Kararlılığı (2. varsayım, kuralla) ve <b>çizgi spektrumunu</b>: hidrojen gazı uyarılınca yalnız belirli renkler yayar — 656 nm kırmızı, 486 nm mavi-yeşil, 434 ve 410 nm mor. Bohr bu dört çizgiyi hesapla, ondalık basamağına kadar tutturdu. Her elementin seviye enerjileri farklı olduğundan çizgileri de farklıdır: ışık, elementin <em>parmak izi</em>dir.</p>
  <div class="sim">
    <h3>Bohr atomu: uyar ve ışı</h3>
    <div class="hint">Hidrojen atomunun elektronu n = 1'de. Enerji vererek üst seviyeye çıkar (absorpsiyon), sonra aşağı indir (emisyon): yayılan fotonun dalga boyu ve rengi hesaplansın, spektrum şeridinde çizgi olarak birikin. Hangi geçişlerin görünür ışık verdiğini bul.</div>
    <div class="ctrl"><span>Uyar →</span><button class="alt" data-up="2">n=2</button><button class="alt" data-up="3">n=3</button><button class="alt" data-up="4">n=4</button><button class="alt" data-up="5">n=5</button><button class="alt" data-up="6">n=6</button></div>
    <div class="ctrl"><span>Işı (geri dön) →</span><button data-dn="1">n=1</button><button data-dn="2">n=2</button><button data-dn="3">n=3</button><button id="bhReset" class="alt">Sıfırla</button></div>
    <div class="svgwrap"><svg id="bhSvg" viewBox="0 0 720 330" role="img" aria-label="Bohr atomu ve spektrum"></svg></div>
    <div class="readout" id="bhOut" style="display:block">Elektron temel hâlde (n = 1). Önce uyar.</div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Renk, elektronun "nereden nereye" indiğiyle belirlenir: n = 2'ye inişler görünür ışık (Balmer serisi), n = 1'e inişler daha büyük enerji farkıyla mor ötesi, n = 3'e inişler kızıl ötesi verir. Seviyeler yukarı çıktıkça sıklaşır; bu yüzden n = 6 → 2 ile n = 5 → 2 çizgileri birbirine yakındır. Basamaklar sabit olduğundan aynı element her zaman aynı çizgileri verir.</div>
  <div class="box warn"><div class="t">Bohr modelinin eksikleri</div>1) Yalnız tek elektronlu taneciklerin (H, He⁺, Li²⁺) spektrumunu açıklar; çok elektronlu atomlarda çizgiler tutmaz. 2) Elektronu belirli yörüngede belirli hızla dolanan bir <em>parçacık</em> sayar; oysa elektronun konumu ve hızı aynı anda kesin bilinemez (belirsizlik ilkesi). 3) Spektrum çizgilerinin ince yapısını ve manyetik alanda yarılmasını açıklayamaz. Yine de "enerji seviyeleri" ve "foton = seviye farkı" fikirleri bugün de geçerlidir — model tümden çöpe gitmedi, genişletildi.</div>

  <h3>3.2 Modern (kuantum) atom modeli: yörünge yerine bulut</h3>
  <p>1924'te de Broglie elektronun dalga gibi de davrandığını öne sürdü; 1926'da Schrödinger bu dalganın denklemini yazdı; 1927'de Heisenberg <b>belirsizlik ilkesi</b>ni ortaya koydu: bir elektronun konumu ve hızı aynı anda istenen kesinlikte ölçülemez. Öyleyse "elektron şu yörüngede şu hızla dolanıyor" cümlesi anlamsızdır. Bunun yerine elektronun <em>nerede bulunma olasılığının yüksek olduğu</em> söylenir.</p>
  <div class="box def"><div class="t">Orbital</div>Elektronun bulunma olasılığının yüksek (yaklaşık %90) olduğu uzay bölgesine <b>orbital</b> denir. Bohr'un keskin çemberi, modern modelde yoğunluğu merkezden uzaklaştıkça azalan bir <em>elektron bulutu</em>na dönüşür. Enerji seviyeleri fikri korunur; ama her seviyede farklı biçimlerde orbitaller (s, p, d, f) vardır — bunları gelecek hafta ayrıntısıyla göreceğiz.</div>
  <div class="sim">
    <h3>Yörünge mi, bulut mu?</h3>
    <div class="hint">Bohr modunda elektron tek bir çemberdedir. Modern moda geç ve "ölçüm ekle": her nokta, elektronun bir anlık ölçümde bulunduğu yer. Noktalar birikince orbitalin sınırını (noktaların %90'ını içine alan daire) izle. En yoğun halka nerede?</div>
    <div class="ctrl">
      <label>Model <select id="clMode" style="font:inherit;padding:6px;border-radius:8px"><option value="b">Bohr (yörünge)</option><option value="m" selected>Modern (bulut)</option></select></label>
      <button id="clAdd">+100 ölçüm</button><button id="clClear" class="alt">Temizle</button>
    </div>
    <div class="svgwrap"><svg id="clSvg" viewBox="0 0 720 300" role="img" aria-label="Elektron bulutu"></svg></div>
    <div class="readout" id="clOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Modern modelde elektronun "yeri" bir nokta değil, bir olasılık dağılımıdır. Noktaların en sık toplandığı uzaklık, Bohr'un hesapladığı yarıçapa (a₀ ≈ 53 pm) denk gelir: Bohr yanılmadı, yalnızca "kesin yörünge" yerine "en olası uzaklık" demek gerekiyordu. Bilimsel bilgi böyle değişir: eski modelin doğru kısmı yeni modelin içinde yaşar.</div>

  <h3>3.3 Atom altı parçacıklar: hazır veri seti</h3>
  <table>
    <tr><th>Parçacık</th><th>Keşif</th><th>Bağıl yük</th><th>Gerçek yük (C)</th><th>Kütle (kg)</th><th>Kütle (akb)</th><th>Yeri</th></tr>
    <tr><td>Elektron (e⁻)</td><td>1897, Thomson</td><td>−1</td><td>−1,602 × 10⁻¹⁹</td><td>9,109 × 10⁻³¹</td><td>≈ 0,00055 (1/1836)</td><td>Çekirdek çevresi</td></tr>
    <tr><td>Proton (p⁺)</td><td>1919, Rutherford</td><td>+1</td><td>+1,602 × 10⁻¹⁹</td><td>1,673 × 10⁻²⁷</td><td>1,0073 ≈ 1</td><td>Çekirdek</td></tr>
    <tr><td>Nötron (n⁰)</td><td>1932, Chadwick</td><td>0</td><td>0</td><td>1,675 × 10⁻²⁷</td><td>1,0087 ≈ 1</td><td>Çekirdek</td></tr>
  </table>
  <p>Akb (atomik kütle birimi): karbon-12 atomunun kütlesinin 1/12'si ≈ 1,66 × 10⁻²⁷ kg. Proton ve nötron yaklaşık 1 akb, elektron ihmal edilecek kadar hafif: atom kütlesinin %99,9'undan fazlası çekirdektedir. Atomun boyutu ise elektron bulutuyla belirlenir: çekirdek atomdan yaklaşık 10⁴ kat küçüktür (geçen hafta hesaplamıştık).</p>
  <div class="box warn"><div class="t">Bilimin doğası: keşif sırası</div>Elektron (1897) → çekirdek (1911) → proton (1919) → nötron (1932). Nötron en son bulundu, çünkü yüksüzdür: elektrik ve manyetik alanla saptırılıp izlenemez. Chadwick onu ancak berilyuma alfa parçacığı çarptırıp ortaya çıkan "görünmez ışının" parafinden proton kopardığını gözleyerek buldu — dolaylı kanıt.</div>

  <h3>3.4 Atomun kimlik kartı: atom numarası ve kütle numarası</h3>
  <div class="formula"><div class="m"><sup>A</sup><sub>Z</sub>X &nbsp;·&nbsp; Z = proton sayısı &nbsp;·&nbsp; A = proton + nötron &nbsp;·&nbsp; nötron = A − Z</div><div class="why">Z elementin kimliğidir: 6 protonlu her atom karbondur. Nötr atomda elektron sayısı = Z.</div></div>
  <p>Örnekler: <sup>12</sup><sub>6</sub>C: 6 p, 6 n, 6 e. &nbsp;<sup>23</sup><sub>11</sub>Na: 11 p, 12 n, 11 e. &nbsp;<sup>35</sup><sub>17</sub>Cl: 17 p, 18 n, 17 e. Kütle numarası bir <em>sayım</em>dır: tam sayıdır ve tek bir atoma aittir.</p>
  <div class="box warn"><div class="t">Tuzak: kütle numarası ≠ atom kütlesi</div>Periyodik tabloda klor için 35,45 yazar; ama hiçbir klor atomunda 35,45 tanecik yoktur. Bu sayı, doğadaki klor atomlarının (%76 ³⁵Cl, %24 ³⁷Cl) bollukla ağırlıklı <b>ortalama kütlesi</b>dir (akb). Kütle numarası tek atomun p + n sayısı; atom kütlesi, izotop karışımının ortalaması.</div>
  <div class="sim">
    <h3>İzotop kurucu</h3>
    <div class="hint">Bir element seç, nötron sayısını kaydır. Proton sayısı sabit kaldığı sürece element aynı kalır; kütle numarası değişir. Hangi nötron sayılarının doğada bulunan izotoplara karşılık geldiğini simülasyon söyler.</div>
    <div class="ctrl">
      <label>Element <select id="izEl" style="font:inherit;padding:6px;border-radius:8px"></select></label>
      <label>Nötron sayısı <input type="range" id="izN" min="0" max="20" value="6"><output id="izNo">6</output></label>
    </div>
    <div class="svgwrap"><svg id="izSvg" viewBox="0 0 720 220" role="img" aria-label="Çekirdek"></svg></div>
    <div class="readout" id="izOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Nötron eklemek elementi değiştirmez, kütlesini değiştirir: karbonun 6, 7 ve 8 nötronlu üç doğal izotopu vardır. Nötron sayısı protona göre çok az ya da çok fazla olan çekirdekler kararsızdır (radyoaktif) ya da hiç oluşmaz; doğadaki izotoplar dar bir "kararlılık şeridi"nde yaşar.</div>

  <h3>3.5 İzo-kavramlar: neyi paylaşıyorlar?</h3>
  <table>
    <tr><th>Kavram</th><th>Aynı olan</th><th>Farklı olan</th><th>Örnek</th><th>Ezber anahtarı</th></tr>
    <tr><td><b>İzotop</b></td><td>Proton sayısı (Z) — aynı element</td><td>Nötron sayısı, kütle numarası</td><td>¹H, ²H (döteryum), ³H (trityum); ¹²C, ¹³C, ¹⁴C; ³⁵Cl, ³⁷Cl</td><td>izo<b>top</b> → pro<b>ton</b></td></tr>
    <tr><td><b>İzoton</b></td><td>Nötron sayısı</td><td>Proton sayısı, kütle numarası</td><td>¹³₆C ve ¹⁴₇N (7 nötron); ²³₁₁Na ve ²⁴₁₂Mg (12 nötron)</td><td>izo<b>ton</b> → nö<b>tron</b></td></tr>
    <tr><td><b>İzobar</b></td><td>Kütle numarası (A)</td><td>Proton ve nötron sayıları</td><td>¹⁴₆C ve ¹⁴₇N; ⁴⁰₁₈Ar ve ⁴⁰₂₀Ca</td><td>izo<b>bar</b> → A ("ağırlık")</td></tr>
    <tr><td><b>İzoelektronik</b></td><td>Elektron sayısı (ve dizilimi)</td><td>Proton sayısı, yük</td><td>Na⁺, Ne, F⁻, Mg²⁺, O²⁻ (10 e)</td><td>izo<b>elektron</b>ik → elektron</td></tr>
  </table>
  <div class="box def"><div class="t">İzotoplar neden kimyasal olarak aynıdır?</div>Kimyasal davranışı elektronlar belirler; izotopların proton ve elektron sayıları aynıdır. Farklı olan kütledir: yoğunluk, kaynama noktası, difüzyon hızı gibi <em>fiziksel</em> özellikler azıcık değişir. Ağır su (D₂O) 101,4 °C'de kaynar, normal su 100 °C'de; ama ikisi de sudur, aynı tepkimelere girer.</div>
  <div class="box warn"><div class="t">Tuzak: izotop ≠ allotrop</div>Allotrop, <em>aynı elementin farklı yapıda maddeleri</em>dir: elmas ve grafit (karbon), O₂ ve O₃ (oksijen). Atomlar aynı, dizilişleri farklı. İzotop ise tek bir atomun nötron sayısıyla ilgilidir. Biri madde düzeyi, öbürü çekirdek düzeyi.</div>

  <h3>3.6 İyon oluşumu: elektron alıp vermek</h3>
  <p>Nötr atomda proton = elektron. Atom elektron <b>verirse</b> proton fazlası oluşur: pozitif yüklü <b>katyon</b> (Na → Na⁺ + e⁻). Elektron <b>alırsa</b> negatif yüklü <b>anyon</b> (Cl + e⁻ → Cl⁻). Yük = proton sayısı − elektron sayısı. İyonlaşmada çekirdek hiç değişmez: proton, nötron ve kütle numarası aynı kalır; element aynı kalır.</p>
  <div class="formula"><div class="m">Na (11 p, 11 e) → Na⁺ (11 p, 10 e) &nbsp;·&nbsp; Cl (17 p, 17 e) → Cl⁻ (17 p, 18 e)</div><div class="why">Na⁺ ile Ne (10 e) izoelektroniktir; Cl⁻ ile Ar (18 e) izoelektroniktir. Atomlar soy gaz elektron sayısına ulaşacak kadar verir ya da alır — nedenini elektron diziliminde göreceğiz.</div></div>
  <div class="sim">
    <h3>İyon yapıcı</h3>
    <div class="hint">Bir element seç, elektron sayısını değiştir; yük, iyon türü ve hangi soy gazla izoelektronik olduğu hesaplansın. Elementin doğada oluşturduğu tipik iyonu bul: ipucu, en dış kabuğu tam dolu ya da tam boş yapmak.</div>
    <div class="ctrl">
      <label>Element <select id="ioEl" style="font:inherit;padding:6px;border-radius:8px"></select></label>
      <label>Elektron sayısı <input type="range" id="ioE" min="0" max="23" value="11"><output id="ioEo">11</output></label>
    </div>
    <div class="svgwrap"><svg id="ioSvg" viewBox="0 0 720 240" role="img" aria-label="İyon"></svg></div>
    <div class="readout" id="ioOut" style="display:block"></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Yükün yalnızca elektron sayısıyla değiştiğini; proton sayısının (elementin) sabit kaldığını. Na'nın 1 elektron verip Ne'ye, Cl'nin 1 elektron alıp Ar'a benzemesi rastlantı değildir: iyonlar soy gaz elektron sayısında "rahat eder". Bu örüntü, gelecek haftaların elektron dizilimi konusunun kapısıdır.</div>
  <div class="box warn"><div class="t">Tuzak: iyonda nötron sayısı</div>"⁴⁰Ca²⁺ iyonunun nötron sayısı?" → 40 − 20 = 20; yükün nötronla ilgisi yoktur. Elektron sayısı ise 20 − 2 = 18. En sık hata: yükü nötrona ya da protona uygulamak.</div>
  <div class="nextbtn"><button class="btn" data-done="3" data-go="4">Günlük yaşam örneklerine geç →</button></div>
</section>
<section class="tab" id="t4" role="tabpanel" aria-labelledby="tab4">
  <h2>Günlük yaşamdan örnekler</h2>
  <div class="card"><h3 style="margin-top:0">1 · Havai fişek ve sokak lambası: emisyonun renkleri</h3>
    <p><b>Durum:</b> Bayram gecesi İzmit sahilinde kırmızı, yeşil ve sarı havai fişekler; yolda turuncu-sarı sodyum buharlı lambalar.</p>
    <p><b>Kavramla bağ:</b> Barutun ısısı metal tuzlarındaki atomların elektronlarını üst seviyelere uyarır; geri dönüşte her element kendi seviye farklarına eşit enerjili fotonlar yayar: stronsiyum kırmızı, baryum yeşil, bakır mavi-yeşil, sodyum 589 nm sarı. Sodyum lambasında uyarılma elektrik akımıyla olur; sonuç aynı çizgi.</p>
    <p><b>Analiz:</b> Aynı ilke laboratuvarda <em>alev testi</em> olarak kullanılır: bilinmeyen tuz aleve tutulur, renk elementi söyler. Astronomlar yıldız ışığındaki çizgilerden yıldızın bileşimini okur — helyum Dünya'da bulunmadan önce Güneş spektrumunda keşfedildi (1868).</p>
    <p><b>Sonuç:</b> Renk, elementin enerji merdiveninin fotoğrafıdır; Bohr'un "basamaklar sabit" fikri her havai fişekte doğrulanır.</p></div>
  <div class="card"><h3 style="margin-top:0">2 · Karbon-14 ile yaş tayini: izotop olarak saat</h3>
    <p><b>Durum:</b> Bir kazıda bulunan ahşap kalıntının kaç yıllık olduğu soruluyor.</p>
    <p><b>Kavramla bağ:</b> Karbonun üç doğal izotopu vardır: ¹²C (%98,9), ¹³C (%1,1) ve eser miktarda radyoaktif ¹⁴C. Canlı, havadaki CO₂'yi aldığı sürece ¹⁴C/¹²C oranı sabittir; öldüğünde alım durur ve ¹⁴C her 5730 yılda yarıya iner.</p>
    <p><b>Hesap:</b> Kalıntıdaki ¹⁴C oranı canlıdakinin 1/4'ü ise iki yarılanma geçmiştir: 2 × 5730 = 11 460 yıl. Kimyasal olarak ¹⁴C ve ¹²C aynı davranır (aynı elektron sayısı); bu yüzden canlı dokuya ayrım yapmadan girerler — yöntem tam da izotopların kimyasal aynılığına dayanır.</p>
    <p><b>Sonuç:</b> Nötron sayısındaki fark kimyayı değiştirmez ama çekirdeğin kararlılığını değiştirir; bu fark bir saat olarak kullanılır.</p></div>
  <div class="card"><h3 style="margin-top:0">3 · Nükleer santral yakıtı: ²³⁵U'yu ²³⁸U'dan ayırmak</h3>
    <p><b>Durum:</b> Doğal uranyumun %99,3'ü ²³⁸U, yalnız %0,7'si zincirleme tepkime verebilen ²³⁵U'dur. Reaktör yakıtı için oran %3-5'e çıkarılır ("zenginleştirme").</p>
    <p><b>Kavramla bağ:</b> İki izotopun proton ve elektron sayıları aynı (92); kimyasal özellikleri özdeş. Hiçbir çözücü, hiçbir tepkime birini seçemez. Fark yalnızca kütlede: 235 ile 238, yaklaşık %1,3.</p>
    <p><b>Analiz:</b> Uranyum önce gaz hâline (UF₆) getirilir; sonra binlerce santrifüjde döndürülür: ağır molekül dışa, hafif olan merkeze eğilim gösterir. Her kademe küçücük bir zenginleşme verir, kademeler art arda bağlanır — tamamen <em>fiziksel</em> bir ayırma.</p>
    <p><b>Sonuç:</b> "İzotopların kimyasal özellikleri aynıdır" cümlesi, dünyanın en pahalı endüstriyel süreçlerinden birinin nedenidir.</p></div>
  <div class="card"><h3 style="margin-top:0">4 · Telefonun pili: Li⁺ iyonlarının yolculuğu</h3>
    <p><b>Durum:</b> Lityum iyon pil boşalırken telefonu çalıştırır, şarj olurken tersine döner. Adı "iyon" — neden?</p>
    <p><b>Kavramla bağ:</b> Lityum atomu (3 p, 3 e) kolayca bir elektron verir: Li → Li⁺ + e⁻. Li⁺ (2 e) helyumla izoelektroniktir. Boşalırken Li⁺ iyonları elektrolit içinden bir elektrottan öbürüne geçer; elektronlar ise dış devreden — yani telefonun devresinden — akar ve iş yapar.</p>
    <p><b>Analiz:</b> Şarj aleti elektronları geri pompalar, Li⁺ iyonları grafit katmanlarına geri döner. Pilin kapasitesi, kaç iyonun gidip gelebildiğiyle ölçülür (mAh). İyonun küçük ve hafif olması (kütle numarası 7) lityumu pil için ideal yapar: az kütleyle çok yük.</p>
    <p><b>Sonuç:</b> "Elektron vermek" soyut bir kural değil; cebindeki cihazın enerjisi bu alışverişin ta kendisidir.</p></div>
  <div class="nextbtn"><button class="btn" data-done="4" data-go="5">Etkileşimli materyale geç →</button></div>
</section>
<section class="tab" id="t5" role="tabpanel" aria-labelledby="tab5">
  <h2>Etkileşimli materyal</h2>
  <div class="sim">
    <h3>p-n-e hesap oyunu</h3>
    <div class="hint">Bir tanecik verilir (atom ya da iyon); proton, nötron ve elektron sayılarını yaz. 10 tur. Yükü doğru tarafa uygula: katyon elektron <em>vermiştir</em>, anyon <em>almıştır</em>; nötron yükten etkilenmez.</div>
    <div id="pngame"></div>
    <div class="ctrl"><button id="pnReset" class="alt">Yeniden başla</button></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>Üç sayının üç ayrı kaynaktan geldiğini: p alt indisten, n üst indis − alt indisten, e ise p − yükten. Hata çoğunlukla yükün yanlış sayıya uygulanmasından çıkar; oyun bunu her turda ayrı ayrı gösterir.</div>
  <div class="sim">
    <h3>İzo-eşleştirme</h3>
    <div class="hint">İki tanecik verilir; aralarındaki ilişkiyi seç: izotop, izoton, izobar, izoelektronik ya da hiçbiri. Önce her ikisinin p, n, e sayısını zihinde çıkar, sonra karşılaştır. 10 tur.</div>
    <div id="isgame"></div>
    <div class="ctrl"><button id="isReset" class="alt">Yeniden başla</button></div>
  </div>
  <div class="box def"><div class="t">Bu simülasyon neyi gösteriyor?</div>"İzo-" kavramlarının her birinin tek bir sayıyı karşılaştırdığını: p (izotop), n (izoton), A (izobar), e (izoelektronik). İki tanecik aynı anda hem izobar hem izotop olamaz; ama bir iyon çifti izoelektronik olduğu hâlde farklı elementlerden olabilir.</div>
  <div class="box def"><div class="t">Gözlem soruları</div>1) Bohr simülasyonunda n = 6 → 2 ile n = 3 → 2 geçişlerinden hangisi daha kısa dalga boylu (daha enerjik) ışık verdi; neden? &nbsp; 2) Bulut simülasyonunda %90 dairesinin yarıçapı ölçüm sayısı arttıkça sabitleşti mi? Bu sınır neden "kesin" değil? &nbsp; 3) İyon yapıcıda Mg için 2 elektron çıkarınca hangi soy gazla izoelektronik oldu; Al için kaç elektron gerekir?</div>
  <div class="nextbtn"><button class="btn" data-done="5" data-go="6">Çözümlü örneklere geç →</button></div>
</section>
<section class="tab" id="t6" role="tabpanel" aria-labelledby="tab6">
  <h2>Çözümlü örnekler</h2>
  <div class="card"><h3 style="margin-top:0">Temel · <sup>23</sup><sub>11</sub>Na atomunun proton, nötron ve elektron sayıları</h3>
    <ol class="steps"><li>Alt indis Z = 11 → 11 proton. Nötr atom → 11 elektron.</li><li>Nötron = A − Z = 23 − 11 = 12.<div class="why">Sıra hep aynı: alt indis proton, üst eksi alt nötron, nötr atomda elektron = proton.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Temel · <sup>24</sup><sub>12</sub>Mg²⁺ iyonunda tanecik sayıları</h3>
    <ol class="steps"><li>p = 12; n = 24 − 12 = 12 (yükten bağımsız).</li><li>Yük +2 → 2 elektron verilmiş: e = 12 − 2 = 10. Ne ile izoelektronik.<div class="why">"2+" proton eklendi demek değil; elektron eksildi demek.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · Hidrojende n = 3 → 2, n = 4 → 2 ve n = 2 → 1 geçişlerinden hangileri görünür ışık verir?</h3>
    <p>Veri: seviye enerjileri E₁ = −13,6 eV, E₂ = −3,40 eV, E₃ = −1,51 eV, E₄ = −0,85 eV; görünür ışık yaklaşık 1,8-3,1 eV aralığıdır.</p>
    <ol class="steps"><li>3 → 2: −1,51 − (−3,40) = 1,89 eV → görünür (kırmızı, 656 nm).</li><li>4 → 2: −0,85 − (−3,40) = 2,55 eV → görünür (mavi-yeşil, 486 nm).</li><li>2 → 1: −3,40 − (−13,6) = 10,2 eV → görünür aralığın çok üstünde: mor ötesi (122 nm).<div class="why">Foton enerjisi seviye farkıdır; fark büyüdükçe dalga boyu kısalır. n = 1'e inişler her zaman mor ötesidir.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · <sup>14</sup><sub>6</sub>C, <sup>14</sup><sub>7</sub>N, <sup>13</sup><sub>6</sub>C ve <sup>15</sup><sub>7</sub>N tanecikleri arasındaki izo-ilişkileri bul</h3>
    <ol class="steps"><li>Sayıları çıkar: ¹⁴C (6 p, 8 n), ¹⁴N (7 p, 7 n), ¹³C (6 p, 7 n), ¹⁵N (7 p, 8 n).</li><li>İzotop: aynı p → ¹⁴C–¹³C (karbon), ¹⁴N–¹⁵N (azot).</li><li>İzoton: aynı n → ¹⁴N–¹³C (7 n), ¹⁴C–¹⁵N (8 n).</li><li>İzobar: aynı A → ¹⁴C–¹⁴N.<div class="why">Her çift yalnız bir sayıyı paylaşır; tablo yapmak karışıklığı önler.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · Klorun ortalama atom kütlesi: ³⁵Cl (%75,8; 34,97 akb) ve ³⁷Cl (%24,2; 36,97 akb)</h3>
    <ol class="steps"><li>Bollukla ağırlıklı ortalama: 0,758 × 34,97 + 0,242 × 36,97.</li><li>= 26,51 + 8,95 = <b>35,46 akb</b> (tabloda 35,45).</li><li>Sonuç 35'e daha yakın; çünkü ³⁵Cl daha bol. Ortalama, izotop kütlelerinin aritmetik ortalaması (35,97) değildir.<div class="why">Kütle numarası tam sayı (35, 37); ortalama atom kütlesi ondalık. Bir de izotop kütlesinin tam olarak 35,00 olmadığına dikkat: bağlanma enerjisi (üniversite konusu).</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · Bilinmeyen iyon: X²⁺ iyonunun 18 elektronu ve 20 nötronu var. X nedir, hangi soy gazla izoelektroniktir?</h3>
    <ol class="steps"><li>Katyon 2 elektron vermiş → nötr atomda e = 18 + 2 = 20 → Z = 20: kalsiyum.</li><li>A = Z + n = 20 + 20 = 40 → <sup>40</sup><sub>20</sub>Ca²⁺.</li><li>18 elektron → argon (Z = 18) ile izoelektronik; K⁺, Cl⁻, S²⁻ de aynı ailede.<div class="why">Geriye doğru çözerken önce yükü elektrona uygula, sonra Z'ye ulaş; nötron yalnız A için gerekir.</div></li></ol></div>
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
    <div class="card"><b>Bohr 1913</b>Belirli enerjili yörüngeler; yörüngede ışıma yok; absorpsiyon yukarı, emisyon aşağı; foton enerjisi = seviye farkı → çizgi spektrumu. Eksik: çok elektronlu atomlar, belirsizlik.</div>
    <div class="card"><b>Modern model</b>de Broglie dalga, Heisenberg belirsizlik, Schrödinger denklemi. Orbital: elektronun %90 olasılıkla bulunduğu bölge; yörünge yerine bulut.</div>
    <div class="card"><b>Tanecikler ve sayılar</b>e⁻ (1897, −1, ~0), p⁺ (1919, +1, 1 akb), n⁰ (1932, 0, 1 akb). Z = p; A = p + n; n = A − Z; nötr atomda e = p. Kütle numarası ≠ ortalama atom kütlesi.</div>
    <div class="card"><b>İzo-kavramlar ve iyon</b>İzotop: p aynı · izoton: n aynı · izobar: A aynı · izoelektronik: e aynı. Yük = p − e; katyon verir (+), anyon alır (−); çekirdek değişmez.</div>
  </div>
  <h3>Sık yapılan 5 hata</h3>
  <ol>
    <li>Kütle numarasını (tam sayı, tek atom) periyodik tablodaki atom kütlesiyle (ondalık, izotop ortalaması) karıştırmak.</li>
    <li>İzotop ile izobarı çaprazlamak: izo<b>top</b> proton, izo<b>bar</b> kütle numarası paylaşır.</li>
    <li>İyon yükünü nötron ya da proton sayısına uygulamak: yük yalnız elektron sayısını değiştirir.</li>
    <li>"Elektron enerji alınca ışık yayar" demek: alınca <em>yukarı çıkar</em> (absorpsiyon), inince yayar (emisyon).</li>
    <li>Modern modeli "Bohr yanlıştı" diye özetlemek: seviyeler ve foton fikri korundu; değişen, kesin yörünge yerine olasılık bölgesi.</li>
  </ol>
  <div class="box life"><div class="t">Gelecek haftaya köprü</div>Bulut simülasyonunda tek bir küresel bölge gördün. Peki 11 elektronlu sodyumun elektronları nerede, hangi sırayla dizilir; neden sodyum 1, magnezyum 2 elektron verir? Gelecek hafta: <b>orbitaller (s, p, d, f) ve elektron dizilimi</b> — Aufbau, Hund, Pauli kuralları. Hazırlık: Ne (10 e), Ar (18 e) ve Kr (36 e) sayılarını aklında tut; dizilim bu sayılarda "tam dolu" olacak.</div>
  <div class="nextbtn"><button class="btn" data-done="8" data-go="1">Haftayı tamamladım ✓</button></div>
</section>'''
MINI_L=[
 {"s":'<span class="tag">Geçen hafta</span> Altın yaprak deneyinde alfa parçacıklarının çok azının geri sekmesi hangi sonucu verdi?',"o":['Pozitif yük ve kütle, çok küçük bir çekirdekte toplanmıştır','Atom bölünemez bir küredir','Elektronlar negatif yüklüdür','Atomun büyük kısmı dolu maddedir'],"a":0,"e":'Geri sekme için yoğun ve küçük bir pozitif merkez gerekir; azlığı çekirdeğin ne kadar küçük olduğunu gösterir.'},
 {"s":'<span class="tag">2 hafta önce</span> Kimyasal madde etiketindeki kuru kafa (kafatası) piktogramı neyi belirtir?',"o":['Akut zehirlilik','Tahriş edici','Yanıcı','Çevre için tehlikeli'],"a":0,"e":'Kuru kafa akut zehirliliktir; ünlem işareti tahriş/orta tehlike, alev yanıcı, ağaç-balık çevre tehlikesidir.'},
 {"s":'<span class="tag">Matematik H1 köprüsü</span> Protonun kütlesi 1,67 × 10⁻²⁷ kg, elektronun kütlesi 9,1 × 10⁻³¹ kg\'dır. Proton, elektronun yaklaşık kaç katıdır?',"o":['Yaklaşık 1800','Yaklaşık 18','Yaklaşık 180 000','Yaklaşık 2'],"a":0,"e":'(1,67 / 9,1) × 10⁻²⁷⁺³¹ ≈ 0,18 × 10⁴ = 1800. Üsleri çıkar, katsayıları böl. Bu yüzden atom kütlesinde elektron ihmal edilir.'}]
QUIZ_L=[
 {"s":'Bohr atom modeline göre elektron için hangisi doğrudur?',"o":['Belirli enerjili yörüngelerde bulunur ve bu yörüngelerde dolanırken ışıma yapmaz','Çekirdeğin içinde bulunur','Çekirdekten her uzaklıkta bulunabilir ve sürekli ışıma yapar','Yalnızca tek bir yörüngede bulunabilir, uyarılamaz'],"a":0,"e":'Bohr\'un 1. ve 2. varsayımları: izinli seviyeler ve kararlı yörünge. Elektron enerji alarak üst seviyelere çıkabilir (uyarılma).'},
 {"s":'<sup>16</sup><sub>8</sub>O atomunda proton, nötron ve elektron sayıları sırasıyla nedir?',"o":['8, 8, 8','8, 16, 8','16, 8, 8','8, 8, 16'],"a":0,"e":'Z = 8 → 8 proton; nötron = A − Z = 16 − 8 = 8; nötr atomda elektron = proton = 8.'},
 {"s":'Bir atom elektron verdiğinde oluşan tanecik ve yükü nedir?',"o":['Katyon; pozitif','Anyon; negatif','Katyon; negatif','İzotop; nötr'],"a":0,"e":'Elektron negatiftir; verilince proton fazlalığı oluşur → pozitif yüklü katyon (Na → Na⁺ + e⁻). Elektron alan atom anyon olur.'},
 {"s":'İzotop atomlar için hangisi doğrudur?',"o":['Proton sayıları aynı, nötron sayıları farklıdır','Nötron sayıları aynı, proton sayıları farklıdır','Kütle numaraları aynı, proton sayıları farklıdır','Proton sayıları aynı, elektron sayıları farklıdır'],"a":0,"e":'İzoTOP → proTon aynı; nötron ve dolayısıyla kütle numarası farklı (¹²C, ¹³C, ¹⁴C). Elektron sayısı farklı olan tanecik iyondur, izotop değil.'},
 {"tag":'bağlam',"s":'<b>Bilgi:</b> Havai fişeklerde stronsiyum tuzları kırmızı, bakır tuzları mavi-yeşil ışık verir.<br>Bu renklerin oluşumu Bohr modeline göre en iyi nasıl açıklanır?',"o":['Isıyla uyarılan elektronlar üst seviyeye çıkar; geri dönerken seviye farkına eşit enerjili, elemente özgü renkte foton yayar','Elektronlar çekirdeğe düşerken ışık yayar','Protonlar ısıyla parçalanarak ışık üretir','Renk, tuzun kristal şekline bağlıdır'],"a":0,"e":'Emisyon: foton enerjisi = E_üst − E_alt. Seviyeler elemente özgü olduğundan renk de özgüdür; Bohr\'un seviyeleri her elementin parmak izidir.'},
 {"s":'<sup>32</sup><sub>16</sub>S²⁻ iyonunda proton, nötron ve elektron sayıları sırasıyla nedir?',"o":['16, 16, 18','16, 16, 14','18, 16, 16','16, 18, 16'],"a":0,"e":'p = Z = 16; n = 32 − 16 = 16; yük −2 → 2 elektron fazlası: e = 18. İyonlaşma proton ve nötronu değiştirmez.'},
 {"s":'Aşağıdaki çiftlerden hangisi izobardır?',"o":['<sup>14</sup><sub>6</sub>C ve <sup>14</sup><sub>7</sub>N','<sup>12</sup><sub>6</sub>C ve <sup>14</sup><sub>6</sub>C','<sup>13</sup><sub>6</sub>C ve <sup>14</sup><sub>7</sub>N','Na⁺ ve Ne'],"a":0,"e":'İzoBAR → kütle numarası (A) aynı, proton farklı: ikisinde de A = 14. ¹²C–¹⁴C izotop, ¹³C–¹⁴N izoton (7 nötron), Na⁺–Ne izoelektronik (10 elektron).'},
 {"s":'Klorun periyodik tablodaki atom kütlesi 35,45 akb\'dir; oysa hiçbir klor atomunun kütle numarası 35,45 değildir. Bu durum nasıl açıklanır?',"o":['Doğal klor, ³⁵Cl (%76) ve ³⁷Cl (%24) izotoplarının karışımıdır; 35,45 bollukla ağırlıklı ortalama kütledir','Klor atomunda 0,45 nötron bulunur','Kütle numarası ölçüm hatası nedeniyle ondalıklı çıkar','Elektronların toplam kütlesi 0,45 akb\'dir'],"a":0,"e":'Kütle numarası tek atomun p + n sayısıdır (tam sayı); atom kütlesi izotop bolluklarıyla alınan ortalamadır: 0,76·35 + 0,24·37 ≈ 35,5.'},
 {"tag":'bağlam',"s":'<b>Bilgi:</b> Lityum iyon pil boşalırken lityum, grafit elektrottan elektrolit içinden karşı elektroda geçer; elektronlar ise telefonun devresi üzerinden akar.<br>Elektrolit içinden geçen tanecik hangisidir ve nedeni nedir?',"o":['Li⁺ katyonu; lityum atomu bir elektron vererek pozitif iyon hâline gelir','Li⁻ anyonu; lityum bir elektron alır','Nötr Li atomu; iyonlaşma gerekmez','Lityum çekirdeği; proton verir'],"a":0,"e":'Li (3 p, 3 e) bir elektron verir → Li⁺ (3 p, 2 e; He ile izoelektronik). Elektron dış devreden, iyon elektrolitten gider; şarjda yön tersine döner.'},
 {"tag":'bağlam',"s":'<b>Bilgi:</b> Doğal uranyumun %99,3\'ü ²³⁸U, %0,7\'si ²³⁵U\'dur; reaktör yakıtı için ²³⁵U oranının artırılması gerekir.<br>Bu iki izotop neden kimyasal yöntemlerle (tepkime, çözme, çöktürme) birbirinden ayrılamaz?',"o":['Proton ve elektron sayıları aynı olduğundan kimyasal özellikleri aynıdır; yalnız kütleleri farklıdır (fiziksel yöntem: santrifüj)','Kimyasal olarak farklıdırlar ama tepkimeleri tehlikelidir','İkisi de soy gazlar gibi tepkimeye girmez','Nötron sayıları aynı olduğu için'],"a":0,"e":'Kimyasal davranış elektron sayısı ve dizilimiyle belirlenir; izotoplarda bu aynıdır. Kütle farkı (%1,3) ancak fiziksel yöntemlerle (gaz santrifüjü) kullanılabilir.'},
 {"s":'Modern atom teorisinin Bohr modelinden temel farkı hangisidir?',"o":['Elektronun konumu ve hızı aynı anda kesin bilinemez (Heisenberg); yörünge yerine bulunma olasılığının yüksek olduğu bölge (orbital) tanımlanır','Elektronlar çekirdeğin içinde kabul edilir','Enerji seviyeleri fikri tamamen terk edilmiştir','Atomun çekirdeği olmadığı kabul edilir'],"a":0,"e":'Belirsizlik ilkesi kesin yörüngeyi anlamsız kılar; enerji seviyeleri korunur ama elektron bir olasılık bulutu (orbital) ile tanımlanır.'},
 {"s":'X²⁺ iyonunun 10 elektronu ve 12 nötronu vardır. X\'in atom numarası ve kütle numarası sırasıyla nedir?',"o":['12 ve 24','10 ve 22','12 ve 22','10 ve 24'],"a":0,"e":'Katyon 2 elektron vermiş: p = 10 + 2 = 12 → Z = 12 (magnezyum). A = p + n = 12 + 12 = 24. İyon Ne ile izoelektroniktir.'},
 {"open":True,"s":'Bohr\'un iki temel varsayımını yaz; bu varsayımların Rutherford modelindeki "elektron çekirdeğe düşmeli" çelişkisini nasıl giderdiğini ve modelin hangi noktada yetersiz kaldığını açıkla.',"ans":'Varsayımlar: elektron yalnız belirli enerjili yörüngelerde bulunur; bu yörüngelerde dolanırken ışıma yapmaz, yalnız seviyeler arası geçişte foton soğurur/yayar. Çelişki, "yörüngede ışıma yok" kuralıyla giderildi (kararlılık). Yetersizlik: çok elektronlu atomların spektrumu, belirsizlik ilkesi (kesin yörünge olamaz), çizgilerin ince yapısı.',"e":'İki varsayım + kararlılık gerekçesi + en az bir eksik beklenir.'},
 {"open":True,"s":'"İzotopların kimyasal özellikleri aynı, fiziksel özellikleri farklıdır." Bu ifadeyi elektron ve kütle kavramlarıyla gerekçelendir; ağır su (D₂O) örneğini kullan.',"ans":'Kimyasal davranışı elektron sayısı ve dizilimi belirler; izotoplarda proton ve elektron sayısı aynı olduğundan tepkimeleri aynıdır. Kütle farkı (nötron) yoğunluk, kaynama noktası, difüzyon hızı gibi fiziksel özellikleri değiştirir: D₂O 101,4 °C\'de kaynar, daha yoğundur; ama su gibi tepkime verir.',"e":'Elektron → kimya, kütle → fizik ayrımı ve ağır su verisi beklenir.'}]
MINI="const MINI="+J(MINI_L)+";"
QUIZ="const QUIZ="+J(QUIZ_L)+";"
SIM=r"""
/* --- yardımcılar --- */
let TIMERS=[];function later(fn,ms){const t=setTimeout(fn,ms);TIMERS.push(t);return t;}
function fmtN(v,d){return (d!=null?v.toFixed(d):String(v)).replace('.',',').replace('-','−');}
function wl2rgb(l){let r=0,g=0,b=0;if(l<380||l>750)return null;if(l<440){r=-(l-440)/60;b=1;}else if(l<490){g=(l-440)/50;b=1;}else if(l<510){g=1;b=-(l-510)/20;}else if(l<580){r=(l-510)/70;g=1;}else if(l<645){r=1;g=-(l-645)/65;}else{r=1;}return 'rgb('+Math.round(r*255)+','+Math.round(g*255)+','+Math.round(b*255)+')';}
function colorName(l){if(l<380)return 'mor ötesi (görünmez)';if(l<450)return 'mor';if(l<495)return 'mavi-yeşil';if(l<570)return 'yeşil';if(l<590)return 'sarı';if(l<620)return 'turuncu';if(l<=750)return 'kırmızı';return 'kızıl ötesi (görünmez)';}
/* --- Bohr atomu --- */
const EN=n=>-13.6/(n*n);
let BH={n:1,lines:[],msg:''};
function drawBH(){const svg=$('#bhSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold'),ln=css('--line'),ink2=css('--ink2');const cx=150,cy=125;
  for(let n=1;n<=6;n++){svg.appendChild(el('circle',{cx,cy,r:18*n,fill:'none',stroke:n===BH.n?nv:ln,'stroke-width':n===BH.n?2.5:1,'stroke-dasharray':n===BH.n?'none':'4 3'}));svg.appendChild(el('text',{x:cx+18*n*Math.cos(-1.1)+3,y:cy+18*n*Math.sin(-1.1)-2,'font-size':'9',fill:ink2},'n='+n));}
  svg.appendChild(el('circle',{cx,cy,r:7,fill:css('--bad')}));svg.appendChild(el('text',{x:cx,y:cy+3,'text-anchor':'middle','font-size':'8',fill:'#fff'},'p⁺'));
  const ang=Math.PI/4;svg.appendChild(el('circle',{cx:cx+18*BH.n*Math.cos(ang),cy:cy+18*BH.n*Math.sin(ang),r:6,fill:nv}));
  svg.appendChild(el('text',{x:cx,y:11,'text-anchor':'middle','font-size':'11',fill:ink},'Hidrojen atomu · elektron n = '+BH.n));
  /* enerji merdiveni */
  const lx=330,ly=n=>30+(-EN(n))*15;const labY={6:36,5:50,4:64,3:78,2:98,1:ly(1)+4};
  svg.appendChild(el('text',{x:lx,y:18,'font-size':'12','font-weight':'700',fill:ink},'Enerji seviyeleri'));
  for(let n=1;n<=6;n++){svg.appendChild(el('line',{x1:lx,y1:ly(n),x2:lx+90,y2:ly(n),stroke:n===BH.n?nv:ink,'stroke-width':n===BH.n?4:2}));if(n>2)svg.appendChild(el('line',{x1:lx+90,y1:ly(n),x2:lx+112,y2:labY[n]-3,stroke:ln}));svg.appendChild(el('text',{x:lx+116,y:labY[n],'font-size':'10',fill:n===BH.n?nv:ink2,'font-weight':n===BH.n?'700':'400'},'n='+n+'  '+fmtN(EN(n),2)+' eV'));}
  svg.appendChild(el('text',{x:lx,y:ly(1)+18,'font-size':'10',fill:ink2},'temel hâl'));
  svg.appendChild(el('text',{x:lx+116,y:150,'font-size':'10',fill:ink2},'Görünür: n=2\'ye inişler (Balmer)'));svg.appendChild(el('text',{x:lx+116,y:164,'font-size':'10',fill:ink2},'UV: n=1\'e inişler (Lyman)'));svg.appendChild(el('text',{x:lx+116,y:178,'font-size':'10',fill:ink2},'IR: n=3\'e inişler (Paschen)'));
  /* spektrum şeridi */
  const sx=90,sw=540,sy=272;const X=l=>sx+(l-380)/(750-380)*sw;
  svg.appendChild(el('text',{x:sx-46,y:236,'font-size':'12','font-weight':'700',fill:ink},'Spektrum: yayılan çizgiler (nm)'));
  for(let l=380;l<750;l+=4)svg.appendChild(el('rect',{x:X(l),y:sy,width:X(l+4)-X(l)+0.6,height:30,fill:wl2rgb(l),opacity:.8}));
  svg.appendChild(el('rect',{x:sx-46,y:sy,width:40,height:30,fill:css('--sky')}));svg.appendChild(el('text',{x:sx-26,y:sy+19,'text-anchor':'middle','font-size':'10',fill:ink},'UV'));
  svg.appendChild(el('rect',{x:sx+sw+6,y:sy,width:40,height:30,fill:css('--sky')}));svg.appendChild(el('text',{x:sx+sw+26,y:sy+19,'text-anchor':'middle','font-size':'10',fill:ink},'IR'));
  [400,450,500,550,600,650,700].forEach(l=>svg.appendChild(el('text',{x:X(l),y:sy+44,'text-anchor':'middle','font-size':'10',fill:ink2},l)));
  BH.lines.forEach(L=>{const x=L.l<380?sx-26:L.l>750?sx+sw+26:X(L.l);svg.appendChild(el('line',{x1:x,y1:sy-4,x2:x,y2:sy+34,stroke:ink,'stroke-width':2}));svg.appendChild(el('text',{x,y:sy-8-((L.k%2)*11),'text-anchor':'middle','font-size':'9',fill:ink},L.from+'→'+L.to));});}
$$('[data-up]').forEach(b=>b.onclick=()=>{const n=+b.dataset.up;if(n<=BH.n){$('#bhOut').innerHTML='Elektron zaten n = '+BH.n+'\'de; uyarılma yalnız <b>üst</b> seviyeye olur. Enerji vermek için daha yüksek n seç ya da önce ışı.';return;}const dE=EN(n)-EN(BH.n);const l=1239.8/dE;BH.n=n;drawBH();$('#bhOut').innerHTML='<b>Absorpsiyon:</b> elektron n = '+n+'\'e çıktı. Gereken enerji tam olarak '+fmtN(dE,2)+' eV ('+fmtN(l,0)+' nm\'lik foton). Daha azı ya da fazlası kabul edilmez: seviyeler arası "yasak".';});
$$('[data-dn]').forEach(b=>b.onclick=()=>{const n=+b.dataset.dn;if(n>=BH.n){$('#bhOut').innerHTML='Elektron n = '+BH.n+'\'de; ışıma için daha <b>alt</b> bir seviye seç (ya da önce uyar).';return;}const from=BH.n,dE=EN(from)-EN(n),l=1239.8/dE;BH.n=n;BH.lines.push({l,from,to:n,k:BH.lines.length});drawBH();
  const col=wl2rgb(l);$('#bhOut').innerHTML='<b>Emisyon:</b> n = '+from+' → n = '+n+'. Foton enerjisi = E'+from+' − E'+n+' = '+fmtN(dE,2)+' eV → dalga boyu <b>'+fmtN(l,1)+' nm</b>: <b style="color:'+(col||'inherit')+'">'+colorName(l)+'</b>. '+(n===2?'Balmer serisi — gözle görülür çizgi.':n===1?'Lyman serisi — büyük enerji farkı, mor ötesi.':'Paschen serisi — küçük enerji farkı, kızıl ötesi.');
  if(motionOn()){const svg=$('#bhSvg');const ph=el('circle',{cx:180,cy:150,r:5,fill:col||css('--gold')});svg.appendChild(ph);let i=0;const step=()=>{i++;ph.setAttribute('cx',180+i*11);ph.setAttribute('cy',150+i*6);if(i<20)later(step,25);else ph.remove();};later(step,25);}});
$('#bhReset').onclick=()=>{BH={n:1,lines:[],msg:''};drawBH();$('#bhOut').textContent='Elektron temel hâlde (n = 1). Önce uyar.';};
/* --- Yörünge mi bulut mu --- */
let CL={pts:[]};
function drawCL(){const svg=$('#clSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold'),ink2=css('--ink2');const cx=200,cy=150,a0=38;const mode=$('#clMode').value;
  svg.appendChild(el('circle',{cx,cy,r:5,fill:css('--bad')}));
  if(mode==='b'){svg.appendChild(el('circle',{cx,cy,r:a0,fill:'none',stroke:nv,'stroke-width':2.5}));svg.appendChild(el('circle',{cx:cx+a0,cy,r:6,fill:nv}));svg.appendChild(el('text',{x:cx,y:cy+a0+22,'text-anchor':'middle','font-size':'12',fill:ink},'Bohr: elektron kesin bir çemberde, r = a₀'));$('#clOut').innerHTML='<b>Bohr modeli:</b> elektron tam olarak a₀ = 53 pm uzaklıkta dolanır. Modern moda geçip ölçüm ekle: gerçekte ne görülüyor?';return;}
  CL.pts.forEach(p=>svg.appendChild(el('circle',{cx:cx+p[0]*a0,cy:cy+p[1]*a0,r:1.6,fill:nv,opacity:.7})));
  svg.appendChild(el('circle',{cx,cy,r:a0,fill:'none',stroke:gd,'stroke-width':1.5,'stroke-dasharray':'4 3'}));svg.appendChild(el('text',{x:cx+a0+4,y:cy-4,'font-size':'10',fill:gd},'a₀'));
  let r90=null;if(CL.pts.length>=20){const rs=CL.pts.map(p=>p[2]).sort((a,b)=>a-b);r90=rs[Math.floor(rs.length*0.9)];svg.appendChild(el('circle',{cx,cy,r:r90*a0,fill:'none',stroke:nv,'stroke-width':2}));svg.appendChild(el('text',{x:cx,y:cy+r90*a0+16,'text-anchor':'middle','font-size':'11',fill:nv},'%90 sınırı: orbital'));}
  /* radyal histogram */
  const hx=430,hy=250,hw=260,hh=170;svg.appendChild(el('line',{x1:hx,y1:hy,x2:hx+hw,y2:hy,stroke:ink}));svg.appendChild(el('line',{x1:hx,y1:hy,x2:hx,y2:hy-hh,stroke:ink}));svg.appendChild(el('text',{x:hx+hw/2,y:hy+22,'text-anchor':'middle','font-size':'11',fill:ink2},'çekirdeğe uzaklık (a₀ birimi)'));svg.appendChild(el('text',{x:hx,y:hy-hh-8,'font-size':'11',fill:ink2},'kaç ölçüm?'));
  const bins=new Array(12).fill(0);CL.pts.forEach(p=>{const r=p[2];const b=Math.min(11,Math.floor(r/0.5));bins[b]++;});const mx=Math.max(1,...bins);bins.forEach((c,i)=>{const h=c/mx*(hh-10);svg.appendChild(el('rect',{x:hx+i*(hw/12)+2,y:hy-h,width:hw/12-4,height:h,fill:nv,opacity:.8}));if(i%2===0)svg.appendChild(el('text',{x:hx+i*(hw/12),y:hy+12,'font-size':'9',fill:ink2},(i*0.5).toString().replace('.',',')));});
  const peak=bins.indexOf(mx);
  $('#clOut').innerHTML=CL.pts.length?'<b>'+CL.pts.length+' ölçüm.</b> Noktaların %90\'ı r &lt; <b>'+fmtN(r90,2)+' a₀</b> içinde → orbitalin sınırı bu daire. En sık görülen uzaklık: '+fmtN(peak*0.5,1)+'-'+fmtN(peak*0.5+0.5,1)+' a₀ — Bohr yarıçapı (1 a₀) civarı. Sınır kesin değil: birkaç nokta dışarıda kalır, çünkü olasılık hiçbir uzaklıkta tam sıfır olmaz.':'Henüz ölçüm yok. "+100 ölçüm"e bas.';}
function clAdd(){for(let i=0;i<100;i++){const r=-0.5*Math.log(Math.random()*Math.random()*Math.random());const t=Math.random()*2*Math.PI;const ph=Math.acos(2*Math.random()-1);const rr=r*Math.sin(ph);CL.pts.push([rr*Math.cos(t),rr*Math.sin(t),r]);}if(CL.pts.length>1500)CL.pts=CL.pts.slice(-1500);drawCL();}
$('#clAdd').onclick=()=>{if($('#clMode').value==='b')$('#clMode').value='m';clAdd();};$('#clClear').onclick=()=>{CL.pts=[];drawCL();};$('#clMode').addEventListener('change',drawCL);
/* --- İzotop kurucu --- */
const ELEM=[{s:'H',z:1,n:{0:'protyum ¹H — %99,98, kararlı',1:'döteryum ²H (D) — %0,02, kararlı; ağır su',2:'trityum ³H — radyoaktif (12,3 yıl), eser'}},{s:'He',z:2,n:{1:'³He — %0,0002, kararlı',2:'⁴He — %99,9998, kararlı; alfa parçacığı'}},{s:'C',z:6,n:{6:'¹²C — %98,9, kararlı; akb tanımı',7:'¹³C — %1,1, kararlı',8:'¹⁴C — radyoaktif (5730 yıl); yaş tayini'}},{s:'N',z:7,n:{7:'¹⁴N — %99,6, kararlı',8:'¹⁵N — %0,4, kararlı'}},{s:'O',z:8,n:{8:'¹⁶O — %99,76, kararlı',9:'¹⁷O — %0,04, kararlı',10:'¹⁸O — %0,20, kararlı; iklim arşivleri'}},{s:'Na',z:11,n:{12:'²³Na — %100, kararlı (tek doğal izotop)'}},{s:'Mg',z:12,n:{12:'²⁴Mg — %79, kararlı',13:'²⁵Mg — %10, kararlı',14:'²⁶Mg — %11, kararlı'}},{s:'Cl',z:17,n:{18:'³⁵Cl — %75,8, kararlı',20:'³⁷Cl — %24,2, kararlı'}},{s:'K',z:19,n:{20:'³⁹K — %93,3, kararlı',21:'⁴⁰K — %0,012, radyoaktif (1,25 milyar yıl); kaya yaşı',22:'⁴¹K — %6,7, kararlı'}},{s:'Ca',z:20,n:{20:'⁴⁰Ca — %97, kararlı',22:'⁴²Ca — kararlı',24:'⁴⁴Ca — kararlı'}},{s:'Fe',z:26,n:{28:'⁵⁴Fe — %5,8, kararlı',30:'⁵⁶Fe — %91,8, kararlı; en kararlı çekirdeklerden',31:'⁵⁷Fe — %2,1',32:'⁵⁸Fe — %0,3'}},{s:'U',z:92,n:{143:'²³⁵U — %0,7, radyoaktif (704 milyon yıl); reaktör yakıtı',146:'²³⁸U — %99,3, radyoaktif (4,5 milyar yıl)'}}];
ELEM.forEach((e,i)=>{const o=document.createElement('option');o.value=i;o.textContent=e.s+' (Z = '+e.z+')';$('#izEl').appendChild(o);});$('#izEl').value=2;
function izSetup(){const e=ELEM[+$('#izEl').value];const keys=Object.keys(e.n).map(Number);const lo=Math.max(0,Math.min(...keys)-3),hi=Math.max(...keys)+3;$('#izN').min=lo;$('#izN').max=hi;$('#izN').value=keys[0];drawIZ();}
function drawIZ(){const e=ELEM[+$('#izEl').value],n=+$('#izN').value;$('#izNo').value=n;const svg=$('#izSvg');svg.innerHTML='';const ink=css('--ink'),ink2=css('--ink2');const cx=180,cy=110;const A=e.z+n;
  const parts=[];for(let i=0;i<e.z;i++)parts.push('p');for(let i=0;i<n;i++)parts.push('n');const show=parts.length<=60?parts:parts.filter((p,i)=>i%Math.ceil(parts.length/60)===0);
  show.forEach((p,i)=>{const r=6*Math.sqrt(i+0.5),t=i*2.4;svg.appendChild(el('circle',{cx:cx+r*Math.cos(t),cy:cy+r*Math.sin(t),r:7,fill:p==='p'?css('--bad'):ink2,stroke:css('--paper'),'stroke-width':1}));});
  if(parts.length>60)svg.appendChild(el('text',{x:cx,y:cy+95,'text-anchor':'middle','font-size':'10',fill:ink2},'(temsilî; '+parts.length+' nükleon)'));
  svg.appendChild(el('circle',{cx:400,cy:60,r:7,fill:css('--bad')}));svg.appendChild(el('text',{x:414,y:64,'font-size':'13',fill:ink},'proton × '+e.z));svg.appendChild(el('circle',{cx:400,cy:90,r:7,fill:ink2}));svg.appendChild(el('text',{x:414,y:94,'font-size':'13',fill:ink},'nötron × '+n));
  svg.appendChild(el('text',{x:400,y:150,'font-size':'30','font-weight':'700',fill:ink},e.s));svg.appendChild(el('text',{x:386,y:132,'text-anchor':'end','font-size':'16',fill:ink},A));svg.appendChild(el('text',{x:386,y:160,'text-anchor':'end','font-size':'16',fill:ink},e.z));svg.appendChild(el('text',{x:400,y:185,'font-size':'12',fill:ink2},'A = '+e.z+' + '+n+' = '+A));
  const known=e.n[n];$('#izOut').innerHTML='<b>'+e.s+'-'+A+'</b>: '+e.z+' proton, '+n+' nötron → kütle numarası '+A+'. '+(known?'<span style="color:var(--ok)">Bilinen izotop: '+known+'.</span>':'<span style="color:var(--gold)">Bu nötron sayısıyla doğal bir izotop yok: çekirdek ya çok kararsızdır ya da hiç oluşmaz.</span>')+' Proton sayısı değişmediği için element hâlâ <b>'+e.s+'</b>; nötr atomda elektron sayısı '+e.z+'.';}
$('#izEl').addEventListener('change',izSetup);$('#izN').addEventListener('input',drawIZ);
/* --- İyon yapıcı --- */
const IEL=[{s:'Li',z:3,t:1},{s:'N',z:7,t:-3},{s:'O',z:8,t:-2},{s:'F',z:9,t:-1},{s:'Na',z:11,t:1},{s:'Mg',z:12,t:2},{s:'Al',z:13,t:3},{s:'S',z:16,t:-2},{s:'Cl',z:17,t:-1},{s:'K',z:19,t:1},{s:'Ca',z:20,t:2}];
const NOBLE={2:'He',10:'Ne',18:'Ar'};
IEL.forEach((e,i)=>{const o=document.createElement('option');o.value=i;o.textContent=e.s+' (Z = '+e.z+')';$('#ioEl').appendChild(o);});$('#ioEl').value=4;
function ioSetup(){const e=IEL[+$('#ioEl').value];$('#ioE').min=Math.max(0,e.z-3);$('#ioE').max=e.z+3;$('#ioE').value=e.z;drawIO();}
function shells(e){const cap=[2,8,8,8];const out=[];let left=e;for(const c of cap){const k=Math.min(c,left);out.push(k);left-=k;if(!left)break;}return out;}
function drawIO(){const e=IEL[+$('#ioEl').value],ne=+$('#ioE').value;$('#ioEo').value=ne;const svg=$('#ioSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),ink2=css('--ink2'),ln=css('--line');const cx=170,cy=120;
  svg.appendChild(el('circle',{cx,cy,r:14,fill:css('--bad')}));svg.appendChild(el('text',{x:cx,y:cy+4,'text-anchor':'middle','font-size':'10',fill:'#fff'},e.z+'p'));
  const sh=shells(ne);sh.forEach((k,i)=>{const r=32+i*24;svg.appendChild(el('circle',{cx,cy,r,fill:'none',stroke:ln}));for(let j=0;j<k;j++){const t=j/k*2*Math.PI-Math.PI/2;svg.appendChild(el('circle',{cx:cx+r*Math.cos(t),cy:cy+r*Math.sin(t),r:5,fill:nv}));}});
  const q=e.z-ne;const qs=q===0?'':(Math.abs(q)>1?Math.abs(q):'')+(q>0?'+':'−');
  svg.appendChild(el('text',{x:400,y:110,'font-size':'34','font-weight':'700',fill:ink},e.s));svg.appendChild(el('text',{x:400+(e.s.length>1?42:22),y:92,'font-size':'16',fill:ink},qs));
  svg.appendChild(el('text',{x:400,y:145,'font-size':'13',fill:ink2},'proton '+e.z+' · elektron '+ne+' · yük = '+e.z+' − '+ne+' = '+(q>0?'+':'')+q));
  let msg='<b>'+e.s+qs+'</b>: '+(q===0?'nötr atom':q>0?'<b>katyon</b> ('+q+' elektron vermiş)':'<b>anyon</b> ('+(-q)+' elektron almış)')+'. ';
  if(NOBLE[ne])msg+='<span style="color:var(--ok)">'+ne+' elektron: <b>'+NOBLE[ne]+'</b> ile izoelektronik.</span> ';
  if(q===e.t)msg+='<span style="color:var(--ok)">Bu, '+e.s+'\'nin doğada oluşturduğu tipik iyondur.</span>';else if(q!==0)msg+='<span style="color:var(--gold)">Tipik iyon '+e.s+(Math.abs(e.t)>1?Math.abs(e.t):'')+(e.t>0?'⁺':'⁻')+': en dış kabuk tam dolu/boş olunca.</span>';
  msg+='<br><span style="color:var(--ink2)">Nötron sayısı ve kütle numarası değişmedi; çekirdek iyonlaşmaya karışmaz.</span>';$('#ioOut').innerHTML=msg;}
$('#ioEl').addEventListener('change',ioSetup);$('#ioE').addEventListener('input',drawIO);
/* --- p-n-e oyunu --- */
const PN=[['Na','23','11','+',11,12,10],['Cl','35','17','−',17,18,18],['Ca','40','20','2+',20,20,18],['O','16','8','2−',8,8,10],['Al','27','13','3+',13,14,10],['C','14','6','',6,8,6],['Fe','56','26','3+',26,30,23],['S','32','16','2−',16,16,18],['H','1','1','+',1,0,0],['K','39','19','+',19,20,18]];
let PG={i:0,s:0};
function symHTML(q){return '<span style="font-size:24px"><sup>'+q[1]+'</sup><sub>'+q[2]+'</sub>'+q[0]+'<sup>'+q[3]+'</sup></span>';}
function drawPN(){const box=$('#pngame');if(PG.i>=PN.length){box.innerHTML='<div class="readout">Puan: '+PG.s+' / '+PN.length+'</div>';return;}const q=PN[PG.i];
  box.innerHTML='<div class="readout">'+(PG.i+1)+' / '+PN.length+' · Puan '+PG.s+'</div><div class="q"><div class="stem">'+symHTML(q)+' &nbsp;taneciği için:</div><div class="ctrl"><label>p <input type="number" id="pnP" style="width:70px"></label><label>n <input type="number" id="pnN" style="width:70px"></label><label>e <input type="number" id="pnE" style="width:70px"></label><button class="btn" id="pnGo">Kontrol et</button></div><div class="fb" id="pnFb"></div></div>';
  $('#pnGo').onclick=()=>{const p=+$('#pnP').value,n=+$('#pnN').value,e=+$('#pnE').value;const okp=p===q[4],okn=n===q[5],oke=e===q[6];const ok=okp&&okn&&oke;if(ok)PG.s++;box.querySelector('.q').classList.add(ok?'right':'wrong');$('#pnGo').disabled=true;
    $('#pnFb').innerHTML=(ok?'✔ Doğru. ':'✘ ')+'p = '+q[4]+' (alt indis)'+(okp?' ✔':' ✘')+' · n = '+q[1]+' − '+q[2]+' = '+q[5]+(okn?' ✔':' ✘')+' · e = '+q[4]+(q[3]?(q[3].includes('+')?' − '+(parseInt(q[3])||1):' + '+(parseInt(q[3])||1)):'')+' = '+q[6]+(oke?' ✔':' ✘')+(q[0]==='H'&&q[3]==='+'?' — H⁺ çıplak bir protondur.':'')+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="pnNext">Sonraki →</button>';$('#pnNext').onclick=()=>{PG.i++;drawPN();};};}
$('#pnReset').onclick=()=>{PG={i:0,s:0};drawPN();};
/* --- İzo-eşleştirme --- */
const ISB=['İzotop','İzoton','İzobar','İzoelektronik','Hiçbiri'];
const IS=[['<sup>12</sup><sub>6</sub>C','<sup>14</sup><sub>6</sub>C',0,'Proton 6 = 6, nötron 6 ≠ 8.'],['<sup>14</sup><sub>6</sub>C','<sup>14</sup><sub>7</sub>N',2,'Kütle numarası 14 = 14, proton 6 ≠ 7.'],['<sup>13</sup><sub>6</sub>C','<sup>14</sup><sub>7</sub>N',1,'Nötron 13 − 6 = 7 ve 14 − 7 = 7.'],['Na⁺ (Z = 11)','Ne (Z = 10)',3,'Elektron 10 = 10; proton farklı.'],['<sup>40</sup><sub>18</sub>Ar','<sup>40</sup><sub>20</sub>Ca',2,'A = 40 = 40; proton 18 ≠ 20.'],['<sup>35</sup><sub>17</sub>Cl','<sup>37</sup><sub>17</sub>Cl',0,'Aynı element (17 p), nötron 18 ≠ 20.'],['O²⁻ (Z = 8)','Mg²⁺ (Z = 12)',3,'Elektron 8 + 2 = 10 ve 12 − 2 = 10.'],['<sup>31</sup><sub>15</sub>P','<sup>32</sup><sub>16</sub>S',1,'Nötron 31 − 15 = 16 ve 32 − 16 = 16.'],['<sup>1</sup><sub>1</sub>H','<sup>4</sup><sub>2</sub>He',4,'p 1 ≠ 2, n 0 ≠ 2, A 1 ≠ 4, e 1 ≠ 2: hiçbir sayı ortak değil.'],['K⁺ (Z = 19)','Cl⁻ (Z = 17)',3,'Elektron 19 − 1 = 18 ve 17 + 1 = 18: argon ailesi.']];
let ISG={i:0,s:0};
function drawIS(){const box=$('#isgame');if(ISG.i>=IS.length){box.innerHTML='<div class="readout">Puan: '+ISG.s+' / '+IS.length+'</div>';return;}const q=IS[ISG.i];
  box.innerHTML='<div class="readout">'+(ISG.i+1)+' / '+IS.length+' · Puan '+ISG.s+'</div><div class="q"><div class="stem" style="font-size:22px">'+q[0]+' &nbsp;ile&nbsp; '+q[1]+'</div><div class="ctrl">'+ISB.map((b,j)=>'<button class="btn alt" data-v="'+j+'">'+b+'</button>').join('')+'</div><div class="fb" id="isFb"></div></div>';
  box.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{const ok=+b.dataset.v===q[2];if(ok)ISG.s++;box.querySelector('.q').classList.add(ok?'right':'wrong');box.querySelectorAll('[data-v]').forEach(x=>x.disabled=true);$('#isFb').innerHTML=(ok?'✔ Doğru. ':'✘ Doğru: <b>'+ISB[q[2]]+'</b>. ')+q[3]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="isNext">Sonraki →</button>';$('#isNext').onclick=()=>{ISG.i++;drawIS();};});}
$('#isReset').onclick=()=>{ISG={i:0,s:0};drawIS();};
function stopAll(){TIMERS.forEach(clearTimeout);TIMERS=[];}
"""
build({'TITLE':'Kimya 9 · Hafta 3 · Atom Teorileri II ve Atom Altı Parçacıklar','CRUMB':'Kimya · Ünite 1 Etkileşim · Atomdan Periyodik Tabloya · Hafta 3','SUBTITLE':'Bohr ve modern atom modeli, proton-nötron-elektron, izotoplar ve iyonlar','PALETTE':PALETTES['kim'],'FOOT':'Fen Lisesi 9 · Kimya · Ünite 1 · Hafta 3','KEY':'ah9-kim-h03','PACKAGE':'Kimya 9 · Ünite 1 · Hafta 3 · Atom teorileri II ve atom altı parçacıklar','PAKET':'kim-h03','HAFTA':'3','SECTIONS':SEC,'MINI':MINI,'QUIZ':QUIZ,'SIMJS':SIM,'INIT':'drawBH();drawCL();izSetup();ioSetup();drawPN();drawIS();'},'kim-h03.html')
