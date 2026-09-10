from kit_build import build, PALETTES
SEC=r'''
<section class="tab" id="t1" role="tabpanel" aria-labelledby="tab1">
  <h1>Kimse atom görmedi; yine de içini biliyoruz</h1>
  <p class="lead">Atom o kadar küçük ki en güçlü ışık mikroskobu bile onu gösteremez. Peki elektronun negatif, çekirdeğin küçük ve ağır olduğunu nereden biliyoruz? Görmeyerek — <em>ölçerek</em>: bir ışın manyetik alanda sapıyor, alfa parçacıkları altın yapraktan geri sekiyor. Bu hafta üç deneyin üç modeli nasıl doğurduğunu ve her modelin nerede çöktüğünü izleyeceğiz.</p>
  <div class="card">
    <p><b>Bilimsel model</b> gerçeğin fotoğrafı değil, gözlemleri açıklayan en iyi haritadır. Dalton'un topu, Thomson'un üzümlü keki, Rutherford'un güneş sistemi… Her biri kendi zamanının verisiyle doğruydu; yeni bir deney yeni bir harita gerektirdi. Sınav bu zinciri "kim ne demiş" diye değil, "hangi deney hangi modeli neden değiştirdi" diye sorar.</p>
  </div>
  <div class="box life"><div class="t">Merak sorusu</div>Evdeki duman dedektörü içinde minik bir radyoaktif kaynak (amerikyum-241) var ve sürekli alfa parçacığı yayıyor. Rutherford 1909'da tam bu parçacıkları altın yaprağa fırlattı ve 8000'de 1'i geri sekince "hayatımın en inanılmaz olayı" dedi. Neden bu kadar şaşırdı? 3. sekmede.</div>
  <div class="box def"><div class="t">Bu haftanın hedefleri (MEB Ünite 1 · Etkileşim → Atomdan Periyodik Tabloya)</div>Dalton, Thomson ve Rutherford atom modellerini deneysel dayanaklarıyla açıklamak · her modelin açıkladığı ve açıklayamadığı olguları ayırt etmek · bilimsel bilginin deneyle değişebilir doğasını atom modelleri üzerinden gerekçelendirmek.</div>
  <div class="nextbtn"><button class="btn" data-done="1" data-go="2">Anladım, hatırlatmaya geç →</button></div>
</section>
<section class="tab" id="t2" role="tabpanel" aria-labelledby="tab2">
  <h2>Hatırlatma ve aralıklı tekrar</h2>
  <div class="grid2">
    <div class="card"><b>Ortaokuldan atom</b><p>Atom; çekirdekte proton (+) ve nötron (0), çevresinde elektron (−). Element tek tür atomdan oluşur. Bu hafta bu bilginin nasıl <em>kazanıldığını</em> öğreneceğiz.</p></div>
    <div class="card"><b>Fizik H1 köprüsü</b><p>Model sınama: öngörü → deney → yanlışlama → yeni model. Galileo Aristo'yu böyle devirdi; Rutherford Thomson'u aynı yolla devirecek.</p></div>
    <div class="card"><b>Elektrik yükü</b><p>Zıt yükler çeker, aynı yükler iter. Yüklü parçacık elektrik ve manyetik alanda sapar; sapma yönü yükün işaretini söyler.</p></div>
    <div class="card"><b>Geçen haftadan</b><p>Kimya, maddenin yapısı ve dönüşümüdür; atom bu yapının en küçük "kimyasal" birimidir.</p></div>
  </div>
  <h3>Aralıklı tekrar (3 soru, anında geri bildirim)</h3>
  <div id="miniQuiz"></div>
  <div class="nextbtn"><button class="btn" data-done="2" data-go="3">Konu anlatımına geç →</button></div>
</section>
<section class="tab" id="t3" role="tabpanel" aria-labelledby="tab3">
  <h2>Konu anlatımı</h2>
  <h3>3.1 Antik fikir: Demokritos ve Aristo</h3>
  <p>MÖ 400'lerde Demokritos, maddenin bölünemez taneciklerden ("atomos") oluştuğunu ileri sürdü; Aristo ise maddenin sürekli ve dört elementten (toprak, su, hava, ateş) oluştuğunu savundu. Aristo kazandı — 2000 yıl boyunca. Sebep: ikisi de <em>deney yapmadı</em>; tartışma felsefiydi. Atom fikri ancak ölçülebilir sonuçlar verdiğinde bilim oldu.</p>
  <h3>3.2 Dalton (1803): atom bir küredir</h3>
  <div class="box def"><div class="t">Dalton atom teorisi</div>1) Madde, bölünemez ve içi dolu küre şeklindeki atomlardan oluşur. 2) Bir elementin tüm atomları özdeştir (kütle ve özellik). 3) Farklı elementlerin atomları farklıdır. 4) Bileşikler, atomların tam sayılı oranlarla birleşmesiyle oluşur. 5) Kimyasal tepkimede atomlar yok olmaz, yaratılmaz; yeniden düzenlenir.</div>
  <p><b>Neyi açıkladı?</b> Kütlenin korunumu (5. madde) ve <b>sabit oranlar yasası</b>: su hep 1 g H'ye 8 g O ile oluşur — çünkü atomlar tam sayı oranlarında birleşir (4. madde). Dalton'un teorisi <em>ölçülebilir öngörü</em> veriyordu; bu yüzden Demokritos'un fikrinden farklıydı.</p>
  <p><b>Nerede çöktü?</b> Atomun bölünemez olduğu (1) ve bir elementin tüm atomlarının özdeş olduğu (2) yanlış çıktı: elektron ve izotoplar keşfedildi.</p>
  <h3>3.3 Thomson (1897): atomun içinden bir şey çıkıyor</h3>
  <p>Havası boşaltılmış cam tüpe yüksek gerilim uygulanınca katottan anoda görünmez bir ışın akar (katot ışınları). Thomson bu ışını elektrik ve manyetik alanlardan geçirdi.</p>
  <div class="sim">
    <h3>Katot ışını tüpü</h3>
    <div class="hint">Elektrik alanı ve manyetik alanı aç-kapat; ışının sapma yönünü izle. Sonra katot metalini değiştir: sapma değişiyor mu? Bu tek soru, elektronun evrenselliğini kanıtladı.</div>
    <div class="ctrl">
      <label><input type="checkbox" id="crtE"> Elektrik alanı (+ plaka üstte)</label>
      <label><input type="checkbox" id="crtB"> Manyetik alan</label>
      <label>Katot metali <select id="crtM" style="font:inherit;padding:6px;border-radius:8px"><option>Alüminyum</option><option>Bakır</option><option>Platin</option></select></label>
      <label>Alan şiddeti <input type="range" id="crtS" min="1" max="5" value="3" style="width:90px"></label>
    </div>
    <div class="svgwrap"><svg id="crtSvg" viewBox="0 0 720 220" role="img" aria-label="Katot ışını tüpü"></svg></div>
    <div class="readout" id="crtOut" style="display:block">Alanlar kapalı: ışın düz gidiyor, ekranda orta noktada parlıyor.</div>
  </div>
  <p><b>Sonuçlar:</b> Işın (+) plakaya doğru sapar → <b>negatif yüklü taneciklerden</b> oluşur. Sapma miktarından yük/kütle (e/m) oranı ölçüldü: hidrojen iyonunun ~1800 katı büyük → tanecik atomdan <b>çok daha hafif</b>. Katot metali ne olursa olsun aynı e/m → bu tanecik <b>her atomda var</b>: <b>elektron</b>.</p>
  <div class="box def"><div class="t">Thomson modeli ("üzümlü kek")</div>Atom, pozitif yüklü ve kütlesi homojen dağılmış bir küredir; elektronlar bu kürenin içine kek üzümleri gibi gömülüdür. Toplam yük sıfır. Atom artık <em>bölünebilir</em>: Dalton'un 1. maddesi düştü.</div>
  <h3>3.4 Rutherford (1909-1911): çekirdek</h3>
  <p>Geiger ve Marsden, Rutherford'un yönetiminde, çok ince altın yaprağa (yaklaşık 1000 atom kalınlığında) alfa parçacıkları (helyum çekirdeği, +2 yüklü, hızlı ve ağır) gönderdi. Thomson modeline göre beklenen: pozitif yük atoma yayılmış ve seyrek olduğundan alfa parçacıkları <em>neredeyse hiç sapmadan</em> geçmeli.</p>
  <div class="sim">
    <h3>Altın yaprak deneyi</h3>
    <div class="hint">Önce Thomson modeliyle (yayılmış yük) alfa parçacıkları gönder; sonra Rutherford modeline (küçük yoğun çekirdek) geç. Geri seken parçacık oranını karşılaştır. Çekirdek boyutunu büyütüp neyin değiştiğine bak.</div>
    <div class="ctrl">
      <label>Model <select id="gfM" style="font:inherit;padding:6px;border-radius:8px"><option value="t">Thomson (yayılmış +)</option><option value="r" selected>Rutherford (çekirdek)</option></select></label>
      <label>Çekirdek boyutu <input type="range" id="gfR" min="1" max="6" value="1" style="width:90px"></label>
      <button id="gfGo">▶ 200 parçacık gönder</button><button id="gfReset" class="alt">Sıfırla</button>
    </div>
    <div class="svgwrap"><svg id="gfSvg" viewBox="0 0 720 260" role="img" aria-label="Altın yaprak deneyi"></svg></div>
    <div class="readout" id="gfOut" style="display:block">Parçacık göndermek için düğmeye bas.</div>
  </div>
  <p><b>Gözlem:</b> Parçacıkların büyük çoğunluğu sapmadan geçti; az bir kısmı büyük açıyla saptı; yaklaşık 8000'de 1'i <b>geri sekti</b>. Rutherford: "Bir kâğıt mendile top mermisi atıp merminin geri gelmesi gibiydi." Thomson modelinde geri sekme imkânsızdı.</p>
  <div class="box def"><div class="t">Rutherford (çekirdekli) atom modeli</div>1) Atomun kütlesinin neredeyse tamamı ve tüm pozitif yükü, merkezdeki çok küçük <b>çekirdek</b>te toplanmıştır. 2) Atomun büyük kısmı <b>boşluktur</b> (çoğu parçacık sapmadan geçti). 3) Elektronlar çekirdeğin çevresinde, güneş çevresindeki gezegenler gibi dolanır. Ölçek: çekirdek bir stadyumun ortasındaki nohut kadardır.</div>
  <p><b>Nerede çöktü?</b> Klasik fiziğe göre çekirdek çevresinde dolanan elektron sürekli ışıma yapıp enerji kaybetmeli ve saniyenin milyarda birinde çekirdeğe düşmeli. Atomlar kararlı; öyleyse model eksik. Bu soruyu gelecek hafta Bohr cevaplayacak.</p>
  <div class="sim">
    <h3>Üç modeli karşılaştır</h3>
    <div class="hint">Modeller arasında geçiş yap; her birinin açıkladığı ve açıklayamadığı olguyu oku.</div>
    <div class="ctrl"><button class="alt" data-m="0">Dalton</button><button class="alt" data-m="1">Thomson</button><button class="alt" data-m="2">Rutherford</button></div>
    <div class="svgwrap"><svg id="mdSvg" viewBox="0 0 720 220" role="img" aria-label="Atom modelleri"></svg></div>
    <div class="readout" id="mdOut" style="display:block"></div>
  </div>
  <h3>3.5 Bilimin doğası: model ne değildir?</h3>
  <div class="box warn"><div class="t">Tuzak: "Rutherford doğru, öncekiler yanlış"</div>Her model, kendi verisiyle tutarlıydı ve yeni bir deneyle <em>genişletildi</em>. Dalton'un "atomlar tepkimede korunur" ilkesi bugün de kimyanın temelidir. Yanlışlanan, modelin belirli bir iddiasıdır; bütünü değil.</div>
  <div class="box warn"><div class="t">Tuzak: sıralama ve deney karışması</div>Katot ışını → Thomson → elektron. Altın yaprak → Rutherford → çekirdek. Sınavların en sık çeldiricisi bu ikisini çaprazlamaktır.</div>
  <div class="nextbtn"><button class="btn" data-done="3" data-go="4">Günlük yaşam örneklerine geç →</button></div>
</section>
<section class="tab" id="t4" role="tabpanel" aria-labelledby="tab4">
  <h2>Günlük yaşamdan örnekler</h2>
  <div class="card"><h3 style="margin-top:0">1 · Eski tüplü televizyon: evdeki katot ışını tüpü</h3>
    <p><b>Durum:</b> Büyükannenin tüplü TV'si aslında dev bir Thomson deneyidir.</p>
    <p><b>Kavramla bağ:</b> Arkadaki katottan çıkan elektron demeti, manyetik bobinlerle saptırılarak ekranı satır satır tarar; fosfor kaplı ekran elektron çarpınca parlar. Görüntü, sapmanın kontrollü hâlidir.</p>
    <p><b>Analiz:</b> Ekrana mıknatıs yaklaştırınca görüntü çarpılır — çünkü elektronlar manyetik alanda sapar. Thomson'un 1897'de ölçtüğü şeyin tam kendisi.</p>
    <p><b>Sonuç:</b> Elektronun negatif olduğunu "gören" ilk cihaz, 20. yüzyılın en yaygın ev aleti oldu.</p></div>
  <div class="card"><h3 style="margin-top:0">2 · Duman dedektörü: Rutherford'un parçacıkları tavanda</h3>
    <p><b>Durum:</b> Dedektörde amerikyum-241 kaynağı alfa parçacıkları yayar; parçacıklar havayı iyonlaştırır, küçük bir akım oluşur.</p>
    <p><b>Kavramla bağ:</b> Duman parçacıkları alfa parçacıklarını soğurur → akım düşer → alarm. Alfa parçacığı Rutherford'un "mermisi"; havadaki atomlarla etkileşimi altın yaprak deneyindeki saçılmanın yumuşak hâlidir.</p>
    <p><b>Sonuç:</b> Alfa parçacıkları kâğıtla bile durur; dedektör güvenlidir. Ama dedektörü söküp içini açmak akıllıca değildir.</p></div>
  <div class="card"><h3 style="margin-top:0">3 · Neon tabelalar ve floresan: elektronlar gazı parlatıyor</h3>
    <p><b>Durum:</b> İzmit çarşısındaki kırmızı "AÇIK" tabelası neon gazıyla dolu bir tüp.</p>
    <p><b>Kavramla bağ:</b> Yüksek gerilim elektronları fırlatır; elektronlar neon atomlarına çarpar, atomlar enerji alıp ışık yayar. Işığın rengi gaza bağlı: neon kırmızı, cıva buharı mor-ötesi (floresanda fosforla beyaza çevrilir).</p>
    <p><b>Sonuç:</b> "Atom neden belirli renkte ışır?" sorusu Rutherford modelinin cevaplayamadığı sorudur — gelecek haftanın Bohr modeli tam bunun için doğdu.</p></div>
  <div class="card"><h3 style="margin-top:0">4 · Röntgen: Rutherford'dan önce keşfedilen "görünmez ışın"</h3>
    <p><b>Durum:</b> 1895'te Röntgen, katot ışını tüpüyle çalışırken karanlıkta parlayan bir ekran fark etti; elini tüp ile ekran arasına koyunca kemiklerini gördü.</p>
    <p><b>Kavramla bağ:</b> Hızlı elektronlar metale çarpınca X-ışını çıkar. Bu, katot ışını tüpünün beklenmedik bir yan ürünüydü; tıp görüntülemesini başlattı ve ilk Nobel Fizik Ödülü'nü aldı (1901).</p>
    <p><b>Sonuç:</b> Aynı cihaz iki yıl arayla iki devrim yaptı: X-ışını (1895) ve elektron (1897). Merakla yapılan temel araştırma, kimin ne bulacağını önceden bilmez.</p></div>
  <div class="nextbtn"><button class="btn" data-done="4" data-go="5">Etkileşimli materyale geç →</button></div>
</section>
<section class="tab" id="t5" role="tabpanel" aria-labelledby="tab5">
  <h2>Etkileşimli materyal</h2>
  <div class="sim">
    <h3>Deney → gözlem → sonuç eşleştirme</h3>
    <div class="hint">Her ifadeyi doğru bilim insanına ata. 12 ifade; çeldiriciler sınavların tipik çaprazlamaları.</div>
    <div id="game"></div>
    <div class="ctrl"><button id="gmReset" class="alt">Oyunu sıfırla</button></div>
  </div>
  <div class="sim">
    <h3>Model tahmin makinesi</h3>
    <div class="hint">Bir deney sonucu verilir; "Bu sonucu hangi model(ler) açıklayabilir?" seç. Birden fazla doğru olabilir.</div>
    <div id="pgame"></div>
    <div class="ctrl"><button id="pgReset" class="alt">Yeniden başla</button></div>
  </div>
  <div class="box def"><div class="t">Gözlem soruları</div>1) Altın yaprak simülasyonunda çekirdek boyutunu 6'ya çıkarınca geri seken oranı ne oldu? Gerçek atomda bu oran neden bu kadar küçük? &nbsp; 2) Katot ışını deneyinde metali değiştirmek neden önemliydi? &nbsp; 3) Rutherford modeli neden "elektron çekirdeğe düşmeli" der? Bir sonraki hafta için tahminin ne?</div>
  <div class="nextbtn"><button class="btn" data-done="5" data-go="6">Çözümlü örneklere geç →</button></div>
</section>
<section class="tab" id="t6" role="tabpanel" aria-labelledby="tab6">
  <h2>Çözümlü örnekler</h2>
  <div class="card"><h3 style="margin-top:0">Temel · Dalton'un hangi maddeleri bugün de geçerli, hangileri değil?</h3>
    <ol class="steps"><li>Geçerli: 3 (farklı elementlerin atomları farklı), 4 (tam sayılı oranlar), 5 (tepkimede korunum).</li><li>Geçersiz: 1 (bölünemez → elektron, proton, nötron var), 2 (tüm atomlar özdeş → izotoplar farklı kütleli).<div class="why">"Hangi madde hangi keşifle düştü" biçiminde sorulur.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Temel · Katot ışınları neden (+) plakaya doğru sapar? Bu ne kanıtlar?</h3>
    <ol class="steps"><li>Zıt yükler çeker; (+) plakaya doğru sapan ışın negatif yüklüdür.</li><li>Sonuç: katottan çıkan tanecikler negatiftir → elektron.<div class="why">Manyetik alanda da sapması, ışının yüklü tanecik olduğunu ayrıca gösterir (nötr ışık sapmaz).</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · Thomson modeline göre altın yaprak deneyinde ne beklenirdi, ne gözlendi?</h3>
    <ol class="steps"><li>Beklenti: pozitif yük atoma yayılmış ve zayıf → alfa parçacıkları küçük sapmalarla geçer, geri sekme yok.</li><li>Gözlem: çoğu sapmadan geçti (atom çoğunlukla boş), az kısmı büyük açıyla saptı, ~1/8000 geri sekti.</li><li>Yorum: pozitif yük ve kütle çok küçük bir hacimde yoğunlaşmış olmalı → çekirdek.<div class="why">Beklenti–gözlem farkı, modeli değiştiren şeydir; bunu yazmadan "Rutherford çekirdeği buldu" demek eksik cevaptır.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Orta · Katot metali değiştirilince e/m oranı değişmedi. Bu neden önemli?</h3>
    <ol class="steps"><li>Işın metale özgü olsaydı farklı metallerde farklı tanecikler beklenirdi.</li><li>Aynı e/m → aynı tanecik → elektron <b>bütün atomların ortak bileşeni</b>.<div class="why">Tek bir kontrol deneyi, "elektron evrenseldir" sonucunu verdi.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · Geri sekme oranından çekirdek boyutunu kestirmek</h3>
    <p>Altın atomunun yarıçapı ≈ 1,4 × 10⁻¹⁰ m. 8000 parçacıktan 1'i geri sekiyorsa çekirdek yarıçapı yaklaşık kaç? (Kabaca: geri sekme olasılığı ≈ çekirdek kesit alanı / atom kesit alanı; yaprak ~1000 atom kalınlığında.)</p>
    <ol class="steps"><li>Tek atom katmanı için olasılık ≈ (1/8000)/1000 ≈ 1,25 × 10⁻⁷.</li><li>Alan oranı = (r_çek / r_atom)² ≈ 1,25 × 10⁻⁷ → r_çek / r_atom ≈ 3,5 × 10⁻⁴.</li><li>r_çek ≈ 3,5 × 10⁻⁴ × 1,4 × 10⁻¹⁰ ≈ <b>5 × 10⁻¹⁴ m</b>. (Gerçek değer ~7 × 10⁻¹⁵ m; kaba tahmin, doğru büyüklük mertebesinde.)<div class="why">Basit bir oran, çekirdeğin atomdan 10 000 kat küçük olduğunu verdi. Rutherford tam bu akıl yürütmeyi yaptı.</div></li></ol></div>
  <div class="card"><h3 style="margin-top:0">Fen lisesi · Rutherford modelinin iç çelişkisi</h3>
    <p>Klasik elektromanyetizmaya göre ivmeli yük ışıma yapar. Dolanan elektron için bu ne demektir ve model neden yine de kabul gördü?</p>
    <ol class="steps"><li>Dairesel hareket ivmelidir → elektron sürekli ışır → enerji kaybeder → spiral çizerek çekirdeğe düşer (~10⁻¹⁰ s).</li><li>Atomlar kararlı ve belirli renklerde (çizgi spektrumu) ışır; model bunu açıklayamaz.</li><li>Yine de kabul gördü çünkü çekirdek gerçekti (deney bunu kanıtladı); eksik olan elektronların davranış kuralıydı. Bohr (1913) bu boşluğu "izinli yörüngeler" fikriyle dolduracak.<div class="why">Bilimde bir model, doğru kısmı korunup yanlış kısmı düzeltilerek ilerler.</div></li></ol></div>
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
    <div class="card"><b>Dalton 1803</b>İçi dolu, bölünmez küre. Sabit oranlar ve kütle korunumunu açıkladı. Elektron ve izotoplarla iki maddesi düştü.</div>
    <div class="card"><b>Thomson 1897</b>Katot ışını: (+) plakaya sapma → negatif elektron; e/m metalden bağımsız → evrensel. Üzümlü kek modeli.</div>
    <div class="card"><b>Rutherford 1911</b>Altın yaprak: çoğu geçti, 1/8000 geri sekti → küçük, yoğun, (+) çekirdek; atom çoğunlukla boşluk. Elektron kararlılığını açıklayamadı.</div>
    <div class="card"><b>Bilimin doğası</b>Model = gözlemleri açıklayan harita; yeni deney → yeni harita. Yanlışlanan iddia, korunan çekirdek fikir.</div>
  </div>
  <h3>Sık yapılan 5 hata</h3>
  <ol>
    <li>Katot ışını deneyini Rutherford'a, altın yaprağı Thomson'a bağlamak.</li>
    <li>"Thomson elektronu keşfetti, dolayısıyla çekirdeği de biliyordu" sanmak. Thomson modelinde çekirdek yoktur.</li>
    <li>Alfa parçacıklarını elektron sanmak. Alfa = helyum çekirdeği, +2 yüklü, ağır.</li>
    <li>"Atomun çoğu boşluk" sonucunu geri sekmeye bağlamak. Boşluk → sapmadan geçenlerden; çekirdek → geri sekenlerden.</li>
    <li>Dalton'u tümden yanlış saymak. Tam sayılı oranlar ve korunum ilkeleri bugün de geçerli.</li>
  </ol>
  <div class="box life"><div class="t">Gelecek haftaya köprü</div>Rutherford'un elektronu çekirdeğe düşmeli ama düşmüyor; neon tabelası neden yalnız kırmızı ışır? Gelecek hafta: <b>Bohr modeli, modern atom modeli ve atom altı parçacıklar</b> — proton, nötron, izotop.</div>
  <div class="nextbtn"><button class="btn" data-done="8" data-go="1">Haftayı tamamladım ✓</button></div>
</section>'''
MINI="""const MINI=[
 {s:'<span class="tag">Geçen hafta</span> Bir numunede "hangi madde ne kadar var?" sorusunu inceleyen alt disiplin hangisidir?',o:['Analitik kimya','Organik kimya','Polimer kimyası','Fizikokimya'],a:0,e:'Miktar ve bileşim belirleme analitik kimyadır.'},
 {s:'<span class="tag">Geçen hafta</span> Derişik asit seyreltilirken doğru sıra hangisidir?',o:['Asit yavaşça suya eklenir','Su aside eklenir','Aynı anda dökülür','Fark etmez'],a:0,e:'Seyrelme ekzotermik; su aside dökülürse sıçrar.'},
 {s:'<span class="tag">Fizik H1</span> Galileo\\'nun düşme deneyi hangi bilimsel adımın örneğidir?',o:['Öngörünün deneyle yanlışlanması','Yasanın matematiksel ifadesi','Rastgele gözlem','Otoriteye başvurma'],a:0,e:'Aristo\\'nun iddiası deneyle çürütüldü; bu hafta Thomson modeli aynı yolla çürütülecek.'}];"""
QUIZ="""const QUIZ=[
 {s:'Katot ışınlarının elektrik alanda (+) plakaya doğru sapması neyi kanıtlar?',o:['Işının negatif yüklü taneciklerden oluştuğunu','Atomun çekirdeği olduğunu','Işının kütlesiz olduğunu','Atomun bölünemez olduğunu'],a:0,e:'Zıt yükler çeker; (+) plakaya yönelen tanecik negatiftir.'},
 {s:'Altın yaprak deneyinde alfa parçacıklarının çoğunun sapmadan geçmesi hangi sonucu verir?',o:['Atomun büyük kısmı boşluktur','Elektronlar negatiftir','Atom bölünemez','Çekirdek negatiftir'],a:0,e:'Geri sekenler çekirdeği, geçenler boşluğu gösterir.'},
 {s:'Dalton atom teorisinin hangi maddesi izotopların keşfiyle yanlışlanmıştır?',o:['Bir elementin tüm atomları özdeştir','Atomlar tepkimede korunur','Bileşikler tam sayılı oranlarla oluşur','Farklı elementlerin atomları farklıdır'],a:0,e:'İzotoplar aynı elementin farklı kütleli atomlarıdır.'},
 {s:'"Üzümlü kek" modeli hangi bilim insanına aittir ve pozitif yük bu modelde nerededir?',o:['Thomson – atoma homojen yayılmış','Rutherford – merkezdeki çekirdekte','Dalton – kürenin yüzeyinde','Bohr – yörüngelerde'],a:0,e:'Thomson modelinde pozitif yük tüm atoma yayılmıştır; çekirdek yoktur.'},
 {s:'Thomson deneyinde katot metalinin değiştirilmesine rağmen e/m oranının aynı kalması neyi gösterir?',o:['Elektronun bütün atomların ortak bileşeni olduğunu','Metallerin aynı olduğunu','Işının ışık olduğunu','Elektronun kütlesiz olduğunu'],a:0,e:'Aynı tanecik her metalden çıkıyor → evrensel parçacık.'},
 {tag:'bağlam',s:'<b>Bilgi:</b> Tüplü televizyonda elektron demeti manyetik bobinlerle saptırılarak ekranı tarar.<br>Ekrana güçlü bir mıknatıs yaklaştırılınca görüntünün çarpılması, aşağıdaki deneylerden hangisinin ilkesiyle açıklanır?',o:['Thomson\\'un katot ışını deneyi','Rutherford\\'un altın yaprak deneyi','Dalton\\'un sabit oranlar çalışması','Röntgen\\'in X-ışını keşfi'],a:0,e:'Yüklü taneciklerin manyetik alanda sapması, Thomson\\'un ölçtüğü olgudur.'},
 {s:'Aşağıdakilerden hangisi Thomson modelinin açıklayamadığı, Rutherford modelinin açıkladığı bir gözlemdir?',o:['Alfa parçacıklarının bir kısmının geri sekmesi','Katot ışınlarının sapması','Kütlenin korunumu','Elementlerin farklı oluşu'],a:0,e:'Yayılmış zayıf pozitif yük geri sektiremez; yoğun çekirdek sektirir.'},
 {tag:'bağlam',s:'Bir öğrenci "Rutherford deneyinde alfa parçacıklarının çoğu geri sekti, bu yüzden çekirdek büyüktür" diyor. Bu ifadedeki hata nedir?',o:['Çoğu parçacık sapmadan geçti; geri seken çok azdı, bu yüzden çekirdek çok küçüktür','Alfa parçacıkları negatiftir','Deney gümüş yaprakla yapılmıştır','Geri sekme elektronlardan kaynaklanır'],a:0,e:'Yaklaşık 8000\\'de 1 geri sekti; bu azlık çekirdeğin küçüklüğünü gösterir.'},
 {s:'Rutherford modelinin klasik fizikle çelişen yönü hangisidir?',o:['Dolanan elektronun ışıma yapıp çekirdeğe düşmesi gerekir','Çekirdeğin negatif olması gerekir','Atomun bölünemez olması gerekir','Elektronların çekirdekte olması gerekir'],a:0,e:'İvmeli yük ışır; model atomun kararlılığını açıklayamaz.'},
 {tag:'bağlam',s:'<b>Bilgi:</b> Duman dedektöründeki amerikyum-241 alfa parçacıkları yayar; alfa parçacığı helyum çekirdeğidir (+2 yüklü).<br>Bu parçacıklar ince bir metal yaprağa gönderilse aşağıdakilerden hangisi beklenir?',o:['Çoğu geçer, çok azı çekirdeklerden geri seker','Hepsi geri seker','Hepsi metalde soğurulur','Elektrik alanında (+) plakaya sapar'],a:0,e:'Rutherford deneyinin aynısı; pozitif parçacık (+) plakaya değil (−) plakaya sapar.'},
 {s:'Altın atomunun yarıçapı çekirdeğinin yaklaşık 10⁴ katıysa, atom hacminin çekirdek hacmine oranı yaklaşık kaçtır?',o:['10¹²','10⁴','10⁸','10¹⁶'],a:0,e:'Hacim yarıçapın küpüyle orantılı: (10⁴)³ = 10¹².'},
 {s:'Bilimsel modellerle ilgili aşağıdaki ifadelerden hangisi doğrudur?',o:['Model, eldeki gözlemleri açıklayan en iyi temsildir; yeni gözlemle değişebilir','Model gerçeğin birebir fotoğrafıdır','Yeni model eskisinin her iddiasını geçersiz kılar','Model deneyden bağımsızdır'],a:0,e:'Dalton\\'un korunum ilkesi Rutherford\\'da da geçerlidir; değişen, yanlışlanan iddiadır.'},
 {open:true,s:'Thomson modeline göre altın yaprak deneyinde beklenen sonucu ve gerçekte gözleneni yaz; gözlemin modeli neden değiştirdiğini iki cümleyle açıkla.',ans:'Beklenen: küçük sapmalar, geri sekme yok. Gözlenen: çoğu geçti, azı büyük açıyla saptı, ~1/8000 geri sekti. Geri sekme için yoğun ve küçük bir pozitif merkez gerekir → çekirdek.',e:'Beklenti-gözlem-yorum üçlüsü aranır.'},
 {open:true,s:'"Modeller değiştiği için bilim güvenilmezdir" iddiasını atom modelleri örneğiyle değerlendir.',ans:'Değişim, deneye dayalı düzeltmedir; her model öncekinin doğru kısmını korur (korunum, elektron, çekirdek). Değişebilirlik bilimin zayıflığı değil, öz-düzeltme mekanizmasıdır.',e:'Korunan ilkeler + yanlışlanan iddia ayrımı beklenir.'}];"""
SIM=r"""
/* --- Katot ışını tüpü --- */
function drawCRT(){const E=$('#crtE').checked,B=$('#crtB').checked,S=+$('#crtS').value;const svg=$('#crtSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');
  svg.appendChild(el('rect',{x:40,y:60,width:640,height:100,rx:40,fill:css('--sky'),stroke:ink,'stroke-width':2}));
  svg.appendChild(el('rect',{x:60,y:95,width:14,height:30,fill:ink}));svg.appendChild(el('text',{x:67,y:180,'text-anchor':'middle','font-size':'12',fill:ink},'katot (−)'));
  svg.appendChild(el('rect',{x:160,y:80,width:6,height:60,fill:css('--ink2')}));svg.appendChild(el('rect',{x:160,y:104,width:6,height:12,fill:css('--sky')}));svg.appendChild(el('text',{x:163,y:180,'text-anchor':'middle','font-size':'12',fill:ink},'anot (+) delikli'));
  if(E){svg.appendChild(el('rect',{x:300,y:66,width:140,height:6,fill:css('--bad')}));svg.appendChild(el('text',{x:370,y:58,'text-anchor':'middle','font-size':'12',fill:css('--bad')},'+ plaka'));svg.appendChild(el('rect',{x:300,y:148,width:140,height:6,fill:nv}));svg.appendChild(el('text',{x:370,y:172,'text-anchor':'middle','font-size':'12',fill:nv},'− plaka'));}
  if(B){for(let i=0;i<5;i++)svg.appendChild(el('text',{x:310+i*30,y:115,'text-anchor':'middle','font-size':'16',fill:css('--ink2')},'⊗'));}
  const dy=(E?-9*S:0)+(B?9*S:0);
  let d='M74 110 L300 110';if(dy){d+=' Q440 110 660 '+(110+dy*2.2);}else d+=' L660 110';
  svg.appendChild(el('path',{d,stroke:gd,'stroke-width':4,fill:'none',opacity:.9}));
  svg.appendChild(el('circle',{cx:660,cy:Math.max(66,Math.min(154,110+dy*2.2)),r:6,fill:gd}));
  let msg;if(!E&&!B)msg='Alanlar kapalı: ışın düz gidiyor.';else if(E&&!B)msg='Elektrik alanı açık: ışın <b>(+) plakaya doğru</b> saptı → tanecikler <b>negatif</b>.';else if(!E&&B)msg='Manyetik alan açık: ışın saptı → ışın yüklü taneciklerden oluşuyor (ışık sapmazdı).';else msg='İki alan birden: alan şiddetleri ayarlanınca ışın düzleşir; bu dengeden hızı, sonra e/m oranı ölçülür.';
  $('#crtOut').innerHTML=msg+' Katot: <b>'+$('#crtM').value+'</b> — sapma metalden bağımsız: aynı e/m, aynı tanecik.';}
['#crtE','#crtB','#crtM','#crtS'].forEach(s=>$(s).addEventListener('input',drawCRT));
/* --- Altın yaprak --- */
let GF={n:0,thru:0,def:0,back:0};
function drawGF(){const m=$('#gfM').value,R=+$('#gfR').value;const svg=$('#gfSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');
  svg.appendChild(el('rect',{x:20,y:100,width:50,height:60,rx:6,fill:css('--ink2')}));svg.appendChild(el('text',{x:45,y:180,'text-anchor':'middle','font-size':'11',fill:ink},'alfa kaynağı'));
  svg.appendChild(el('rect',{x:355,y:20,width:6,height:220,fill:gd}));svg.appendChild(el('text',{x:358,y:255,'text-anchor':'middle','font-size':'11',fill:ink},'altın yaprak'));
  for(let i=0;i<4;i++)for(let j=0;j<5;j++){const cx=330+i*18,cy=45+j*42;if(m==='t')svg.appendChild(el('circle',{cx,cy,r:16,fill:'#f7d6a0',opacity:.6}));else{svg.appendChild(el('circle',{cx,cy,r:16,fill:'none',stroke:'#e2b46a','stroke-dasharray':'2 2'}));svg.appendChild(el('circle',{cx,cy,r:1.5+R*0.8,fill:css('--bad')}));}}
  svg.appendChild(el('path',{d:'M560 20 A120 120 0 0 1 560 240',stroke:ink,'stroke-width':4,fill:'none'}));svg.appendChild(el('text',{x:640,y:130,'text-anchor':'middle','font-size':'11',fill:ink},'dedektör'));
  svg.appendChild(el('path',{d:'M160 20 A120 120 0 0 0 160 240',stroke:ink,'stroke-width':4,fill:'none',opacity:.5}));svg.appendChild(el('text',{x:105,y:40,'text-anchor':'middle','font-size':'11',fill:ink},'geri sekme dedektörü'));
  const N=Math.min(GF.n,200);for(let i=0;i<N;i++){const y=40+(i*37)%180;const r=Math.random();let path;
    if(m==='t'){path='M70 '+y+' L355 '+y+' L560 '+(y+(Math.random()-.5)*6);}
    else{const pBack=0.002*R*R,pDef=0.03*R;if(r<pBack){path='M70 '+y+' L355 '+y+' L160 '+(y+(Math.random()-.5)*120);GF.back++;}else if(r<pBack+pDef){path='M70 '+y+' L355 '+y+' L560 '+(y+(Math.random()>.5?1:-1)*(40+Math.random()*80));GF.def++;}else{path='M70 '+y+' L355 '+y+' L560 '+(y+(Math.random()-.5)*8);GF.thru++;}}
    svg.appendChild(el('path',{d:path,stroke:nv,'stroke-width':1,fill:'none',opacity:.55}));}
  if(GF.n){const tot=GF.thru+GF.def+GF.back;$('#gfOut').innerHTML=m==='t'?'<b>Thomson modeli:</b> '+GF.n+' parçacığın hepsi küçük sapmalarla geçti; geri sekme <b>0</b>. Model geri sekmeyi öngöremez.':'<b>Rutherford modeli</b> (çekirdek boyutu '+R+'): geçen '+GF.thru+' · büyük açıyla sapan '+GF.def+' · geri seken <b>'+GF.back+'</b> / '+tot+'. '+(R>=4?'Çekirdek büyüdükçe geri sekme artıyor; gerçek atomda ~1/8000 olması çekirdeğin ne kadar küçük olduğunu söyler.':'Gerçek deneyde oran ~1/8000; küçük ama sıfır değil — Thomson ile fark budur.');}}
$('#gfGo').onclick=()=>{GF.n=200;if($('#gfM').value==='t'){GF.thru=200;GF.def=0;GF.back=0;}else{GF.thru=0;GF.def=0;GF.back=0;}drawGF();};
$('#gfReset').onclick=()=>{GF={n:0,thru:0,def:0,back:0};drawGF();$('#gfOut').textContent='Parçacık göndermek için düğmeye bas.';};
['#gfM','#gfR'].forEach(s=>$(s).addEventListener('input',()=>{GF={n:0,thru:0,def:0,back:0};drawGF();}));
/* --- Üç model --- */
const MD=[{n:'Dalton (1803)',ok:'Sabit oranlar, kütle korunumu, elementlerin farklılığı.',no:'Elektrik yükü, katot ışınları, izotoplar.'},{n:'Thomson (1897)',ok:'Elektronun varlığı ve negatifliği, atomun nötrlüğü.',no:'Alfa parçacıklarının geri sekmesi.'},{n:'Rutherford (1911)',ok:'Geri sekme, atomun boşluğu, yoğun pozitif çekirdek.',no:'Atomun kararlılığı ve çizgi spektrumları (elektron neden düşmüyor?).'}];
let selM=0;
function drawMD(){const svg=$('#mdSvg');svg.innerHTML='';const ink=css('--ink'),nv=css('--navy2'),gd=css('--gold');const cx=360,cy=110;
  if(selM===0){svg.appendChild(el('circle',{cx,cy,r:80,fill:nv}));svg.appendChild(el('text',{x:cx,y:cy+5,'text-anchor':'middle','font-size':'14',fill:'#fff'},'içi dolu, bölünmez'));}
  else if(selM===1){svg.appendChild(el('circle',{cx,cy,r:80,fill:'#f2c6c6'}));svg.appendChild(el('text',{x:cx,y:cy-90,'text-anchor':'middle','font-size':'12',fill:ink},'+ yük yayılmış'));[[-40,-20],[30,-35],[0,20],[-25,45],[45,30],[-5,-55]].forEach(([dx,dy])=>{svg.appendChild(el('circle',{cx:cx+dx,cy:cy+dy,r:8,fill:nv}));svg.appendChild(el('text',{x:cx+dx,y:cy+dy+4,'text-anchor':'middle','font-size':'10',fill:'#fff'},'−'));});}
  else{svg.appendChild(el('circle',{cx,cy,r:85,fill:'none',stroke:css('--line'),'stroke-dasharray':'4 4'}));svg.appendChild(el('circle',{cx,cy,r:55,fill:'none',stroke:css('--line'),'stroke-dasharray':'4 4'}));svg.appendChild(el('circle',{cx,cy,r:6,fill:css('--bad')}));svg.appendChild(el('text',{x:cx,y:cy+24,'text-anchor':'middle','font-size':'11',fill:ink},'çekirdek (+), küçük ve ağır'));[[85,0],[-55,0],[0,-85]].forEach(([dx,dy])=>{svg.appendChild(el('circle',{cx:cx+dx,cy:cy+dy,r:7,fill:nv}));});svg.appendChild(el('text',{x:cx+100,y:cy+30,'font-size':'11',fill:ink},'boşluk'));}
  svg.appendChild(el('text',{x:cx,y:210,'text-anchor':'middle','font-size':'15','font-weight':'700',fill:gd},MD[selM].n));
  $('#mdOut').innerHTML='<b>Açıkladı:</b> '+MD[selM].ok+'<br><b>Açıklayamadı:</b> '+MD[selM].no;}
$$('[data-m]').forEach(b=>b.onclick=()=>{selM=+b.dataset.m;drawMD();});
/* --- Eşleştirme oyunu --- */
const GB=['Dalton','Thomson','Rutherford'];const GQ=[['Katot ışınlarının (+) plakaya sapması',1,'Negatif tanecik → elektron.'],['Alfa parçacıklarının 1/8000\'inin geri sekmesi',2,'Yoğun pozitif çekirdek.'],['Atomlar tam sayılı oranlarla birleşir',0,'Sabit oranlar yasasının açıklaması.'],['Üzümlü kek modeli',1,'Pozitif yük yayılmış, elektronlar gömülü.'],['Atomun büyük kısmı boşluktur',2,'Sapmadan geçen parçacıklar.'],['Atom içi dolu, bölünmez küredir',0,'Dalton\'un ilk maddesi.'],['e/m oranı metale bağlı değildir',1,'Elektron evrensel parçacık.'],['Elektronlar çekirdek çevresinde dolanır',2,'Güneş sistemi benzetmesi.'],['Kimyasal tepkimede atomlar korunur',0,'Kütlenin korunumu.'],['Altın yaprak deneyi',2,'Geiger–Marsden, 1909.'],['Elektronun keşfi (1897)',1,'Katot ışını tüpü.'],['İzotopların keşfiyle yanlışlanan "tüm atomlar özdeştir"',0,'Dalton\'un ikinci maddesi.']];
let GM={i:0,s:0,log:[]};
function drawGame(){const box=$('#game');if(GM.i>=GQ.length){box.innerHTML='<div class="readout">Puan: '+GM.s+' / '+GQ.length+'</div>'+GM.log.map(l=>'<div class="q '+(l.ok?'right':'wrong')+'"><div class="stem">'+l.q+'</div><div class="fb">'+(l.ok?'✔ ':'✘ Doğru: <b>'+l.d+'</b> · ')+l.e+'</div></div>').join('');return;}
  const q=GQ[GM.i];box.innerHTML='<div class="readout">'+(GM.i+1)+' / '+GQ.length+' · Puan '+GM.s+'</div><div class="q"><div class="stem">'+q[0]+'</div><div class="ctrl">'+GB.map((b,j)=>'<button class="btn alt" data-v="'+j+'">'+b+'</button>').join('')+'</div><div class="fb" id="gmFb"></div></div>';
  box.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{const ok=+b.dataset.v===q[1];if(ok)GM.s++;GM.log.push({q:q[0],ok,d:GB[q[1]],e:q[2]});box.querySelector('.q').classList.add(ok?'right':'wrong');box.querySelectorAll('[data-v]').forEach(x=>x.disabled=true);$('#gmFb').innerHTML=(ok?'✔ Doğru. ':'✘ Doğru: <b>'+GB[q[1]]+'</b>. ')+q[2]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="gmNext">Sonraki →</button>';$('#gmNext').onclick=()=>{GM.i++;drawGame();};});}
$('#gmReset').onclick=()=>{GM={i:0,s:0,log:[]};drawGame();};
/* --- Model tahmin makinesi (çoklu seçim) --- */
const PQ=[['Atomlar tepkimede yok olmaz',[0,1,2],'Korunum ilkesi üç modelde de vardır.'],['Katottan negatif tanecik çıkar',[1,2],'Dalton\'da elektron yok.'],['Alfa parçacıkları geri seker',[2],'Yalnız çekirdekli model.'],['Su daima 1:8 kütle oranında H ve O içerir',[0,1,2],'Sabit oranlar; hepsi açıklar.'],['Atom elektriksel olarak nötrdür',[1,2],'Dalton yükten söz etmez.'],['Neon gazı yalnız belirli renklerde ışır',[],'Hiçbiri; Bohr gerekir (gelecek hafta).']];
let PG={i:0,s:0};
function drawPG(){const box=$('#pgame');if(PG.i>=PQ.length){box.innerHTML='<div class="readout">Puan: '+PG.s+' / '+PQ.length+'</div>';return;}
  const q=PQ[PG.i];box.innerHTML='<div class="readout">'+(PG.i+1)+' / '+PQ.length+' · Puan '+PG.s+'</div><div class="q"><div class="stem">Gözlem: '+q[0]+'<br><span class="note" style="font-weight:400;font-size:14px;color:var(--ink2)">Hangi model(ler) açıklar? (birden çok seçilebilir, hiçbiri de olabilir)</span></div><div class="opts">'+GB.map((b,j)=>'<label><input type="checkbox" value="'+j+'"> <span>'+b+'</span></label>').join('')+'</div><div class="ctrl"><button class="btn" id="pgGo">Kontrol et</button></div><div class="fb" id="pgFb"></div></div>';
  $('#pgGo').onclick=()=>{const sel=[...box.querySelectorAll('input:checked')].map(i=>+i.value);const ok=sel.length===q[1].length&&sel.every(v=>q[1].includes(v));if(ok)PG.s++;box.querySelector('.q').classList.add(ok?'right':'wrong');$('#pgGo').disabled=true;$('#pgFb').innerHTML=(ok?'✔ Doğru. ':'✘ Doğru: <b>'+(q[1].length?q[1].map(i=>GB[i]).join(', '):'hiçbiri')+'</b>. ')+q[2]+' <button class="btn" style="margin-left:8px;min-height:32px;padding:4px 10px" id="pgNext">Sonraki →</button>';$('#pgNext').onclick=()=>{PG.i++;drawPG();};};}
$('#pgReset').onclick=()=>{PG={i:0,s:0};drawPG();};
function stopAll(){}
"""
build({'TITLE':'Kimya 9 · Hafta 2 · Atom Teorileri I','CRUMB':'Kimya · Ünite 1 Etkileşim · Atomdan Periyodik Tabloya · Hafta 2','SUBTITLE':'Dalton, Thomson ve Rutherford atom modelleri','PALETTE':PALETTES['kim'],'FOOT':'Fen Lisesi 9 · Kimya · Ünite 1 · Hafta 2','KEY':'ah9-kim-h02','PACKAGE':'Kimya 9 · Ünite 1 · Hafta 2 · Atom teorileri I (Dalton, Thomson, Rutherford)','PAKET':'kim-h02','HAFTA':'2','SECTIONS':SEC,'MINI':MINI,'QUIZ':QUIZ,'SIMJS':SIM,'INIT':'drawCRT();drawGF();drawMD();drawGame();drawPG();'},'kim-h02.html')
