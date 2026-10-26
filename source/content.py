# -*- coding: utf-8 -*-
"""
NickUstası — sayfa içerikleri (tamamı özgün Türkçe metinlerdir).
Her sayfa: başlık, açıklama, araç ayarı, giriş metni, bölümler, SSS.
"""

PAGES = [

# ============================================================ 1. ANA SAYFA
{
 "slug": "index", "file": "index.html",
 "title": "Nick Yazma — Şekilli Nick Oluşturucu ve Şekilli İsim Yazma",
 "desc": "Nick yazma aracı ile ismini yaz, 100'den fazla şekilli nick stilini tek tıkla kopyala. Türkçe harfleri bozmayan şekilli nick oluşturucu: semboller, süslemeler ve havalı yazı stilleri.",
 "h1": "Şekilli <span class='hl'>Nick Yazma</span> Aracı",
 "lead": "İsmini ya da oyun nickini yaz, saniyeler içinde yüzlerce şekilli nick önerisi üret. Beğendiğin stile tek tıkla kopyala; PUBG, Instagram, Discord ve dilediğin her yerde kullan.",
 "badge": "Türkçe harfleri bozmayan üreteç",
 "tool": "generator",
 "cfg": {"limit": 0, "sample": "Şahin", "placeholder": "Nickini veya ismini yaz...",
         "label": "Nickini yaz, stiller anında üretilsin"},
 "chips": ["AslanKral", "GeceKuşu", "Şahin", "KaraŞimşek", "YalnızKurt", "AyIşığı"],
 "intro": [
   "<p>Şekilli nick, sıradan harflerin Unicode adı verilen evrensel karakter setindeki süslü karşılıklarıyla değiştirilmesiyle oluşur. Yani gördüğün süslü yazı aslında bir resim ya da özel bir yazı tipi değildir; telefonunun ve oyunun zaten tanıdığı gerçek karakterlerdir. Bu yüzden kopyaladığın şekilli nick, yapıştırdığın her yerde aynı şekilde görünür.</p>",
   "<p>Bu sayfadaki nick yazma aracı, yazdığın metni 30 temel yazı stilinde dönüştürür; üstüne süsleme ve ayraç seçenekleriyle birlikte 100'den fazla farklı sonuç üretir. Kalın, italik ve el yazısından gotik, balon ve kare harflere kadar her tarz burada. Üstelik araç, Türkçe harfleri özel olarak destekler: ğ, ü, ş, ı, ö, ç ve İ harfleri silinmez ya da başka harfe dönüştürülmez; ait oldukları stilde düzgün biçimde üretilir.</p>",
 ],
 "sections": [
   ("Şekilli Nick Nasıl Yapılır?",
    "<p>Üç adım yeterli: <strong>1)</strong> Üstteki kutuya nickini veya ismini yaz. <strong>2)</strong> Üretilen stiller arasında gezin; istersen süsleyici menüsünden yıldız, taç, kalp gibi bir çerçeve seç, ayraç menüsünden harflerin arasına girecek işareti belirle. <strong>3)</strong> Beğendiğin kartın üzerine tıkla; nick panona kopyalanır. Sonra oyununa ya da sosyal medya uygulamana yapıştırman yeterli.</p>"
    "<p>Kararsız kaldıysan önce sade stillerden başla. Kalabalık semboller dikkat çeker ama okunabilirliği azaltır; özellikle oyun içinde hızlı tanınmak istiyorsan kalın ya da modern stiller üzerine tek bir süsleme eklemek genelde en iyi sonucu verir.</p>"),
   ("Hangi Stil Nerede Kullanılır?",
    "<ul>"
    "<li><strong>Oyun nickleri:</strong> Kalın, gotik, çift çizgili ve siyah kare stilleri lobide en çok fark edilenlerdir. Karakter sınırı olan oyunlar için sayfadaki özel oyun araçlarını kullan: <a href='pubg-sekilli-nick.html'>PUBG şekilli nick</a>, <a href='free-fire-sekilli-nick.html'>Free Fire şekilli nick</a>, <a href='brawl-stars-sekilli-nick.html'>Brawl Stars şekilli nick</a>.</li>"
    "<li><strong>Instagram ve TikTok:</strong> El yazısı, italik ve minik üst yazı stilleri biyografi alanında zarif durur. Ayrıntılar için <a href='instagram-sekilli-yazi.html'>Instagram şekilli yazı</a> sayfasına bak.</li>"
    "<li><strong>Discord ve WhatsApp:</strong> Modern ve daktilo stilleri sohbet içinde okunaklı kalır. <a href='discord-sekilli-nick.html'>Discord</a> ve <a href='whatsapp-sekilli-nick.html'>WhatsApp</a> sayfalarında platforma özel sınırlar da anlatılıyor.</li>"
    "</ul>"),
   ("Türkçe Harf Desteği Neden Önemli?",
    "<p>Birçok şekilli yazı aracı İngilizce alfabe için hazırlanmıştır; ğ, ş, ı gibi harfleri ya atar ya da düz harfe çevirir. Sonuçta 'Şahin' yazmak isterken elinde 'Sahin' kalır. Bu üreteçte her Türkçe harfin, seçtiğin stildeki karşılığı özenle eşleştirilir; karşılığı bulunmayan stillerde harf, birleşik işaret tekniğiyle aslına sadık üretilir. Adın neyse, nickin de o olur.</p>"),
 ],
 "faqs": [
   ("Şekilli nick yazmak ücretli mi?",
    "Hayır. Bu sayfadaki üreteç ve sitedeki tüm araçlar tamamen ücretsizdir; üyelik ya da uygulama indirme gerekmez."),
   ("Yaptığım şekilli nick her oyunda çalışır mı?",
    "Şekilli harfler Unicode karakterler olduğu için çoğu oyun ve uygulama bunları gösterir. Ancak bazı oyunlar belirli sembolleri engeller ya da kendi yazı tipinde karşılığı olmayan karakterleri kutu (□) olarak gösterir. Oyuna özel güvenli sembol listesi için rehberdeki 'hata vermeyen semboller' yazısına göz at."),
   ("Nickim neden bazı yerlerde kutu kutu görünüyor?",
    "Kullandığın cihazın veya oyunun yazı tipinde o karakterin çizimi yoksa yerine kutu gösterilir. Bu, nickinin bozuk olduğu anlamına gelmez; başka bir cihazda düzgün görünebilir. Çözüm olarak daha yaygın stilleri (kalın, modern, balon) dene."),
   ("Şekilli nick kullanmak ban sebebi midir?",
    "Şekilli harflerin kendisi genelde yasak değildir; fakat her oyunun kendi isim kuralları vardır. Küfürlü, taklit amaçlı ya da reklam içeren isimler şekilli de olsa cezalandırılabilir. Kurallara uygun bir isim seçtiğin sürece şekilli nick güvenlidir."),
   ("Türkçe harfler (ğ, ü, ş, ı, ö, ç) neden bazı sitelerde bozuluyor?",
    "Çünkü o araçlar yalnızca İngilizce harfleri dönüştürür, Türkçe harfleri tanımaz. Bu sitedeki motor Türkçe harfleri özellikle destekler; harf atlamadan dönüşüm yapar."),
   ("Beğendiğim stili nasıl kaybedmeden saklarım?",
    "Kartın üzerine tıklayıp kopyaladıktan sonra telefonunun not uygulamasına yapıştırarak saklayabilirsin. Aynı metni bu sayfaya tekrar yazarsan aynı sonuçlar yeniden üretilir."),
 ],
},

# ============================================================ 2. ŞEKİLLİ YAZI YAZMA
{
 "slug": "sekilli-yazi-yazma", "file": "sekilli-yazi-yazma.html",
 "title": "Şekilli Yazı Yazma — Süslü ve Değişik Yazı Stilleri Oluşturucu",
 "desc": "Şekilli yazı yazma aracı: cümlelerini kalın, italik, el yazısı, gotik ve onlarca süslü yazı stiline çevir, tek tıkla kopyala. Türkçe karakter destekli değişik yazılar.",
 "h1": "Şekilli <span class='hl'>Yazı Yazma</span>",
 "lead": "Bir cümle, bir durum mesajı ya da profil yazısı... Yazını yaz; onlarca süslü yazı stiline anında dönüşsün. Beğendiğini tıkla, kopyala, istediğin yerde kullan.",
 "tool": "generator",
 "cfg": {"limit": 0, "sample": "Merhaba Dünya", "placeholder": "Şekilli yazıya çevirmek istediğin metni yaz...",
         "label": "Metnini yaz, şekilli hallerini gör"},
 "chips": ["Merhaba Dünya", "İyi ki varsın", "Hayat kısa", "Günaydın", "Teşekkürler"],
 "intro": [
   "<p>Şekilli yazı, düz metni herkesin telefonunda bulunan Unicode karakterlerle süsleme sanatıdır. Durum mesajlarında, biyografilerde, yorumlarda ve başlıklarda yazının kalabalığın arasından sıyrılmasını sağlar. Bu araç; kalın, italik, el yazısı, gotik, çift çizgili, balon, kare ve daha pek çok stili tek sayfada toplar.</p>",
   "<p>Nick üretecinden farkı, bu sayfanın uzun metinlere göre düşünülmüş olmasıdır: cümleler, sözler ve kısa paragraflar da sorunsuz dönüşür. Türkçe harfler aynen korunur; 'Bugün çok güzel bir gün' yazdığında sonucun içinde ğ, ü, ş, ı, ö, ç harflerinin hepsi yerli yerinde olur.</p>",
 ],
 "sections": [
   ("Şekilli Yazıyı Nerede Kullanabilirsin?",
    "<ul>"
    "<li><strong>WhatsApp durumu ve hakkında:</strong> Kısa bir sözü el yazısı ya da minik üst yazı stiliyle paylaşmak profili anında farklılaştırır.</li>"
    "<li><strong>Instagram biyografisi:</strong> Satır satır bilgileri farklı stillerle ayırmak biyografiyi düzenli ve dikkat çekici gösterir.</li>"
    "<li><strong>Oyun içi mesajlar ve klan duyuruları:</strong> Kalın ve altı çizili stiller duyuruların okunmasını kolaylaştırır.</li>"
    "<li><strong>Yorumlar ve gönderiler:</strong> Tek bir şekilli kelime bile yorumunun görünürlüğünü artırır.</li>"
    "</ul>"),
   ("Okunabilirliği Korumak İçin İpuçları",
    "<p>Süslü yazının amacı dikkat çekmektir; ama okunamayan yazı amacına ulaşamaz. Uzun cümlelerde sade stilleri (modern, kalın, italik) seç; vurguyu kısa kelimelerde kullan. Gotik ve çift çizgili gibi yoğun stiller başlıklarda harika durur ama paragraf içinde yorucu olabilir. Bir de şunu unutma: Bazı eski cihazlar belirli stilleri gösteremeyebilir; önemli bir duyuru yazıyorsan en yaygın stilleri tercih et.</p>"),
 ],
 "faqs": [
   ("Şekilli yazı nasıl kopyalanır?",
    "Beğendiğin sonucun kartına tıklaman yeterli; metin panona kopyalanır ve ekranda 'Kopyalandı' bildirimi görürsün. Sonra istediğin uygulamaya yapıştırabilirsin."),
   ("Uzun metinler de dönüşüyor mu?",
    "Evet. Araç cümle ve kısa paragrafları da dönüştürür. Yine de en iyi görünüm kısa ve orta uzunluktaki metinlerde alınır."),
   ("Şekilli yazılar her telefonda görünür mü?",
    "Modern telefonların ve uygulamaların büyük bölümü bu karakterleri destekler. Çok eski cihazlarda bazı stiller kutu olarak görünebilir."),
   ("Hangi stil en çok okunuyor?",
    "Deneyimlerimize göre kalın ve modern (sans) stiller en okunaklı olanlardır; el yazısı ve italik de günlük kullanımda sorunsuzdur."),
   ("Yazımın arasına sembol ekleyebilir miyim?",
    "Evet. Süsleyici ve ayraç menülerini kullanabilir, ayrıca <a href='sekilli-semboller.html'>şekilli semboller</a> sayfasından dilediğin işareti kopyalayıp metnine ekleyebilirsin."),
   ("Bu yazılar yazı tipi (font) mi?",
    "Hayır. Bunlar farklı karakterlerdir; bu yüzden font yüklemeden, her uygulamaya kopyala-yapıştır ile taşınabilirler."),
 ],
},

# ============================================================ 3. ŞEKİLLİ İSİM YAZMA
{
 "slug": "sekilli-isim-yazma", "file": "sekilli-isim-yazma.html",
 "title": "Şekilli İsim Yazma — İsmini Süslü Harflerle Yaz ve Kopyala",
 "desc": "Şekilli isim yazma aracı ile kendi ismini ya da sevdiklerinin ismini süslü harflerle yaz. Türkçe isimlerdeki ğ, ü, ş, ı, ö, ç harfleri bozulmadan, tek tıkla kopyala.",
 "h1": "Şekilli <span class='hl'>İsim Yazma</span>",
 "lead": "Kendi ismini hiç bu kadar havalı görmedin. İsmini yaz; el yazısından gotiğe, balon harflerden kraliyet çerçevelerine kadar onlarca şekilli isim önerisi arasından beğen, kopyala.",
 "tool": "generator",
 "cfg": {"limit": 0, "sample": "Zeynep", "placeholder": "İsmini yaz...",
         "label": "İsmini yaz, şekilli hallerini gör"},
 "chips": ["Zeynep", "Mehmet", "Şükran", "Işıl", "Ömer", "Çağla", "Gülşen", "İbrahim"],
 "intro": [
   "<p>İsim, insanın dijital dünyadaki imzasıdır. Oyun profillerinde, sosyal medya hesaplarında ve mesajlaşma uygulamalarında isminin süslü hali hem seni yansıtır hem de akılda kalmanı sağlar. Bu sayfadaki şekilli isim yazma aracı, yazdığın ismi onlarca farklı karakter stiline çevirir.</p>",
   "<p>Türkçe isimler bu işin en kritik noktasıdır: Işıl, Şükran, Çağlar, Özgür, Gülçin gibi isimler, Türkçe harfleri desteklemeyen araçlarda tanınmaz hale gelir. Buradaki motor her harfi tek tek ve özenle dönüştürür; ismin, hangi stili seçersen seç, yine senin ismindir.</p>",
 ],
 "sections": [
   ("İsmine Uygun Stili Seçmek",
    "<p><strong>Resmî ve sade bir görünüm</strong> için modern ve kalın stiller; <strong>zarif bir imza</strong> için el yazısı ve italik; <strong>dikkat çekici bir profil</strong> için balon, kare ve taç süslemeli kombinasyonlar uygundur. İki isimliysen (örneğin Ayşe Nur) arada kalp ya da çiçek ayracı kullanmak hoş bir denge kurar.</p>"
    "<p>Soyadınla birlikte kullanacaksan toplam uzunluğa dikkat et: Bazı platformlar isim alanını sınırlar. Sınırı olan platformlar için ilgili sayfalardaki sayaçlı araçları kullanman daha doğru olur.</p>"),
   ("Şekilli İsmini Kullanabileceğin Yerler",
    "<ul>"
    "<li>Oyun profilleri ve kullanıcı adları</li>"
    "<li>Instagram, TikTok ve X görüntü adları</li>"
    "<li>WhatsApp ve Telegram profil isimleri</li>"
    "<li>Doğum günü ve tebrik görselleri için metin taslakları</li>"
    "<li>Dijital imza ve rumuzlar</li>"
    "</ul>"
    "<p>Hazır isim listeleri arıyorsan <a href='nick-listeleri.html'>nick listeleri</a> sayfasındaki Türkçe, İngilizce, kız ve erkek listelerine de göz at.</p>"),
 ],
 "faqs": [
   ("İsmimdeki Türkçe harfler bozulur mu?",
    "Hayır. ğ, ü, ş, ı, ö, ç ve İ harfleri bu araçta özel olarak desteklenir; stil ne olursa olsun ismin doğru yazılır."),
   ("İki kelimeli isim yazabilir miyim?",
    "Evet. Boşluk bırakarak tam ismini yazabilirsin; boşluklar korunur ve her kelime ayrı ayrı şekillendirilir."),
   ("Şekilli ismimi Instagram'da kullanabilir miyim?",
    "Evet, görüntü adı ve biyografi alanlarında şekilli harfler sorunsuz görünür. Ayrıntılı bilgi için <a href='instagram-sekilli-yazi.html'>Instagram şekilli yazı</a> sayfasına bak."),
   ("İsmimi kimse çalabilir mi, benzersiz olur mu?",
    "Şekilli harfler ismini görsel olarak farklılaştırır ama kullanıcı adı benzersizliği platformun kurallarına bağlıdır. Görüntü adında özgürsün; kullanıcı adında platform neye izin verirse o geçerlidir."),
   ("En zarif isim stili hangisi?",
    "El yazısı ve italik stiller isimlerde en zarif sonucu verir. Davetiye havası için kraliyet çerçevesi süslemesini de deneyebilirsin."),
 ],
},

# ============================================================ 4. YAZI STİLLERİ
{
 "slug": "yazi-stilleri", "file": "yazi-stilleri.html",
 "title": "Yazı Stilleri — Şekilli Yazı Fontları ve Yazı Tipleri Kütüphanesi",
 "desc": "Tüm yazı stilleri tek sayfada: kalın, italik, el yazısı, gotik, balon, kare, minik harfler ve efekt stilleri. Örnek metni yaz, stilleri gruplar halinde incele, tıklayıp kopyala.",
 "h1": "<span class='hl'>Yazı Stilleri</span> Kütüphanesi",
 "lead": "Bu sitede kullanılan 30 yazı stilinin tamamı, gruplar halinde burada. Örnek metni değiştir; her stilin senin metninle nasıl göründüğünü anında gör ve kopyala.",
 "tool": "styles",
 "cfg": {"limit": 0, "sample": "Şahin", "placeholder": "Örnek metin yaz...",
         "label": "Örnek metin (stiller bu metinle gösterilir)"},
 "chips": ["Şahin", "Güzellik", "Oyuncu", "Kral"],
 "intro": [
   "<p>Yazı stilleri beş grupta toplanır: <strong>Klasik</strong> stiller (kalın, italik, el yazısı, gotik) zamansızdır ve her yerde çalışır. <strong>Modern</strong> stiller (sans ve daktilo) teknoloji ve oyun profillerine yakışır. <strong>Çerçeveli</strong> stiller (balon, kare, parantezli) harfleri kutucuk içine alır, özellikle kısa nicklerde güçlü durur. <strong>Küçük</strong> stiller (küçük büyük harf ve minik üst yazı) biyografi satırlarında incelik sağlar. <strong>Efekt</strong> stilleri ise üstü çizili, altı çizili, ters ve leet gibi oyunlu dönüşümler sunar.</p>",
   "<p>Her grubun altındaki kartlar tıklanabilir; beğendiğin stili tek tıkla kopyalarsın. Tüm stillerle aynı anda çalışmak istersen <a href='index.html'>ana üreteci</a> kullan.</p>",
 ],
 "sections": [
   ("Stil Seçerken Bilmen Gerekenler",
    "<p><strong>Destek durumu:</strong> Klasik ve modern stiller neredeyse her cihazda görünür. Çerçeveli stillerden siyah balon ve siyah kare, bazı eski Android cihazlarda eksik çıkabilir. Minik üst yazıda birkaç harfin (C, F, S, Y, Z büyük halleri) Unicode'da tam karşılığı olmadığı için en yakın küçük karşılık kullanılır.</p>"
    "<p><strong>Türkçe harfler:</strong> Her stilde ğ, ü, ş, ı, ö, ç korunur. Karşılığı olmayan harfler için birleşik işaret yöntemi kullanılır; böylece örneğin gotik stilde bile 'ğ' harfi kaybolmaz.</p>"),
 ],
 "faqs": [
   ("Kaç farklı yazı stili var?",
    "Bu kütüphanede 30 temel stil bulunur. Süsleme ve ayraçlarla birlikte üreteçte 100'den fazla farklı sonuç elde edilir."),
   ("Şekilli yazı fontu indirmem gerekir mi?",
    "Hayır. Bunlar font değil, Unicode karakterlerdir. Hiçbir şey indirmeden kopyala-yapıştır ile kullanılır."),
   ("El yazısı stili her harfi destekliyor mu?",
    "Bazı el yazısı büyük harflerinin Unicode karşılığı ayrı bir blokta tanımlıdır; motor bunları otomatik kullanır. Türkçe harfler de birleşik işaretle tamamlanır."),
   ("Üstü çizili yazı nerede kullanılır?",
    "Şaka amaçlı düzeltmelerde, eski fiyatı gösterirken ya da '~~vazgeçtim~~' tarzı esprili mesajlarda sık kullanılır."),
   ("Minik harflerle uzun cümle yazılır mı?",
    "Yazılır ama okunması zorlaşır. Minik üst yazı en çok kısa vurgular ve biyografi satırlarında güzel durur."),
   ("Ters yazı nasıl okunur?",
    "Ters stil, metni baş aşağı çevirir; okumak için ekranı çevirmek ya da alışmak gerekir. Eğlence amaçlıdır, uzun metinlere uygun değildir."),
 ],
},

# ============================================================ 5. ŞEKİLLİ HARFLER
{
 "slug": "sekilli-harfler", "file": "sekilli-harfler.html",
 "title": "Şekilli Harfler — A'dan Z'ye Süslü Harf Tabloları ve Harf Yazma",
 "desc": "Şekilli harfler burada: A'dan Z'ye tüm harflerin kalın, el yazısı, gotik, balon ve diğer stillerdeki karşılıkları. Harfe tıkla kopyala; üstteki araçla kelimeni de çevir.",
 "h1": "Şekilli <span class='hl'>Harfler</span> A–Z",
 "lead": "Tek tek harf mi lazım? Aşağıdaki tablolarda her harfin 10 farklı stildeki karşılığını bulursun. Harfe tıkla, kopyala; harfleri yan yana getirip kendi kelimeni kur.",
 "tool": "letters",
 "cfg": {"limit": 0, "sample": "Harf", "placeholder": "Kelime veya harf yaz...",
         "label": "Önce kelimeni dene (istersen)"},
 "chips": ["Harf", "Kelime", "Şekil"],
 "intro": [
   "<p>Bazen bütün bir kelimeyi çevirmek yerine tek bir harfin süslü hali gerekir: nickinin baş harfi, bir kısaltma ya da monogram. Bu sayfadaki tablolar, Türkçe alfabedeki tüm harflerin ve rakamların on farklı stildeki karşılığını listeler.</p>",
   "<p>Tablolarda Türkçe harfler ayrı sıralanır; yani 'ı' ile 'i', 'ş' ile 's' birbirine karışmaz. Her hücre tıklanabilir: harfi kopyalayıp istediğin metnin içine yapıştırabilirsin. Kelime bazında çalışmak istersen üstteki üreteç de aynı sayfada seni bekliyor.</p>",
 ],
 "sections": [
   ("Harf Tablolarını Kullanma Fikirleri",
    "<ul>"
    "<li><strong>Monogram:</strong> Adının ve soyadının baş harflerini el yazısı veya kraliyet çerçevesiyle birleştir.</li>"
    "<li><strong>Kısaltmalar:</strong> Klan ve ekip kısaltmalarını (ör. takım adının baş harfleri) kare ya da balon stilde yaz.</li>"
    "<li><strong>Numaralar:</strong> Doğum yılı, forma numarası gibi rakamları çift çizgili stilde vurgula.</li>"
    "<li><strong>Karışık stiller:</strong> Kelimenin ilk harfini gotik, devamını modern stilde yazarak kendi imza stilini yarat.</li>"
    "</ul>"),
 ],
 "faqs": [
   ("Şekilli 'a' harfini nasıl kopyalarım?",
    "Tabloda istediğin stilin bölümüne git, 'a' hücresine tıkla. Harf panona kopyalanır; yapıştırmak istediğin yere basman yeterli."),
   ("Türkçe harfler tabloda var mı?",
    "Evet. ç, ğ, ı, ö, ş, ü harfleri ve büyük karşılıkları tablolarda alfabetik sırayla yer alır."),
   ("Bazı stillerde bir harf neden farklı görünüyor?",
    "Birkaç harfin (örneğin el yazısında G, üst simgede Q) Unicode'da bire bir karşılığı yoktur; motor en yakın resmi karşılığı kullanır. Bu, karakterin kaybolmasından çok daha iyi bir çözümdür."),
   ("Rakamların da şekilli halleri var mı?",
    "Evet. Çoğu stilde rakam karşılıkları bulunur; tablonun sonunda 0-9 arası rakamları görebilirsin."),
   ("Harfleri birleştirince kelime bozulur mu?",
    "Bozulmaz. Her harf bağımsız bir karakterdir; yan yana yapıştırdığında kelimen aynen korunur."),
 ],
},

# ============================================================ 6. ŞEKİLLİ SEMBOLLER
{
 "slug": "sekilli-semboller", "file": "sekilli-semboller.html",
 "title": "Şekilli Semboller — Nick Sembolleri Kopyala (Kalp, Yıldız, Taç)",
 "desc": "Şekilli semboller kütüphanesi: kalpler, yıldızlar, taçlar, oklar, çiçekler ve oyun sembolleri kategoriler halinde. Sembole tıkla, kopyala, nickine ekle.",
 "h1": "Şekilli <span class='hl'>Semboller</span>",
 "lead": "Nickini tamamlayacak son dokunuş burada. Kategorilere ayrılmış <span data-symbol-count></span> sembol arasından beğendiğine tıkla; kopyalayıp nickinin başına, sonuna ya da harf aralarına ekle.",
 "tool": "symbols",
 "cfg": {},
 "intro": [
   "<p>İyi bir sembol, nicki sıradanlıktan kurtaran imzadır. Ama doğru sembolü seçmek önemlidir: Oyunun desteklemediği bir sembol, lobide kutu olarak görünür ve bütün havanı bozar. Bu yüzden kütüphaneyi kategorilere ayırdık ve en güvenilir sembolleri başa aldık.</p>",
   "<p>Kalpler ve yıldızlar her yerde çalışır; taçlar (satranç taşları) yıllardır oyun nicklerinin vazgeçilmezidir; oklar ve köşe çerçeveleri ise nickine 'tasarım' hissi verir. Emin olamadığın sembolleri önce oyunun sohbet kısmında dene; orada görünen sembol, isim alanında da büyük ihtimalle görünür.</p>",
 ],
 "sections": [
   ("Sembol Seçim Rehberi",
    "<ul>"
    "<li><strong>Her yerde güvenli:</strong> ★ ☆ ♥ ♡ ♛ ✿ ♪ • gibi temel semboller neredeyse tüm oyun ve uygulamalarda görünür.</li>"
    "<li><strong>Dikkat isteyenler:</strong> Nadir bloklardaki süslü işaretler (bazı çerçeve ve yazı süsleri) eski cihazlarda kutu olabilir.</li>"
    "<li><strong>Azı karar:</strong> Nick başında ve sonunda birer sembol çoğu zaman yeterlidir; fazlası okunabilirliği öldürür.</li>"
    "</ul>"
    "<p>Oyunlara özel güvenli liste için <a href='pubg-sekilli-nick.html'>PUBG sayfasındaki</a> güvenli semboller bölümüne ve <a href='hata-vermeyen-sekilli-semboller.html'>rehberdeki</a> 'hata vermeyen semboller' yazısına bak.</p>"),
 ],
 "faqs": [
   ("Sembolleri nasıl kopyalarım?",
    "Sembole tıklaman yeterli; pano kopyalaması otomatik yapılır ve 'Kopyalandı' bildirimi görürsün."),
   ("TC yazısı ve bayrak sembolleri var mı?",
    "Kategoriler arasında para birimleri (₺ dahil) ve popüler nick sembolleri bulunur. 'TC' yazısı genelde harf süslemeleriyle yazılır; semboller bölümündeki köşe çerçeveleriyle birleştirip kendi TC imzanı oluşturabilirsin."),
   ("Sembol ekleyince nickim çok uzun olur mu?",
    "Her sembol genelde bir karakter sayılır; ancak bazı oyunlar çok baytlı karakterleri iki birim sayabilir. Sınırı olan oyunlarda sayfadaki sayaçlı araçları kullan."),
   ("Kalp ve yıldız sembolleri hangi oyunlarda çalışır?",
    "PUBG Mobile, Free Fire, Brawl Stars ve Mobile Legends dahil popüler oyunların tamamında temel kalp ve yıldız sembolleri sorunsuz görünür."),
   ("Semboller kopyalanınca neden bazen boş görünüyor?",
    "Bazı semboller (birleşik işaret içerenler) tek başına yapıştırıldığında görünmez gibi durabilir; bir harfin yanına yapıştırdığında ortaya çıkar."),
 ],
},

# ============================================================ 7. BOŞLUK KOPYALA
{
 "slug": "bosluk-kopyala", "file": "bosluk-kopyala.html",
 "title": "Boşluk Kopyala — Görünmez Boşluk ve Görünmez Karakter Oluşturucu",
 "desc": "Boşluk kopyala: görünmez boşluk karakterini tek tıkla kopyala. PUBG görünmez isim, WhatsApp boş mesaj ve Instagram boş satır için farklı boşluk türleri ve üretici.",
 "h1": "Boşluk <span class='hl'>Kopyala</span> (Görünmez Karakter)",
 "lead": "Görünmez isim mi yapmak istiyorsun, boş mesaj mı göndermek? İhtiyacın olan boşluk karakteri burada: türünü seç, tıkla, kopyala.",
 "tool": "space",
 "cfg": {},
 "intro": [
   "<p>Görünmez karakter, ekranda boşluk gibi görünen ama aslında gerçek bir Unicode karakteri olan işarettir. Normal boşluk tuşunun ürettiği karakteri birçok uygulama isim alanlarında kabul etmez; görünmez karakterler ise kabul edilir. Bu fark sayesinde oyunlarda boşluklu ya da tamamen görünmez isimler, WhatsApp'ta boş mesajlar ve Instagram'da boş satırlar mümkün olur.</p>",
   "<p>Aşağıda en çok kullanılan boşluk türlerini ayrı ayrı sunuyoruz; çünkü her platform her türü kabul etmez. Biri çalışmazsa diğerini dene.</p>",
 ],
 "sections": [
   ("Görünmez İsim Nasıl Yapılır?",
    "<p>PUBG Mobile gibi oyunlarda görünmez isim için genelde iki yol izlenir: Ya isim alanına yalnızca görünmez karakter yapıştırılır (tamamen boş görünen isim), ya da harflerin arasına/yanına görünmez karakter eklenerek 'ikinci satıra geçmiş' gibi görünen isimler yapılır. Adım adım anlatım ve oyunlara özel notlar için <a href='pubg-sekilli-nick.html'>PUBG şekilli nick</a> sayfasına bak.</p>"),
   ("WhatsApp'ta Boş Mesaj Gönderme",
    "<p>WhatsApp normal boşlukla mesaj göndermene izin vermez ama görünmez karakteri kabul eder. Aşağıdaki Hangul dolgu karakterini ya da Braille boşluk desenini kopyalayıp mesaj alanına yapıştır ve gönder; karşı tarafa boş bir mesaj balonu gider. Şaka amaçlı eğlencelidir; yine de ardı ardına gönderip kimseyi bunaltma.</p>"),
 ],
 "faqs": [
   ("Hangi boşluk türünü seçmeliyim?",
    "Oyun isimleri için U+3164 (Hangul dolgu) ve U+2800 (Braille boşluk) en çok işe yarayanlardır. Instagram satır boşluklarında ise genel Unicode boşlukları tercih edilir. Çalışmazsa sırayla diğerlerini dene."),
   ("Görünmez karakter kopyaladım ama yapıştırınca görünmüyor, bozuk mu?",
    "Hayır, görünmemesi normal; karakter zaten görünmezdir. Yapıştırdığın alanda imlecin ilerlediğini ya da karakter sayacının arttığını görürsen işlem tamamdır."),
   ("PUBG'de görünmez isim ban sebebi mi?",
    "Boşluk karakterinin kendisi yasaklı bir hile değildir; pek çok oyuncu kullanır. Yine de oyunun isim politikası zamanla değişebilir; görünmez isim kullanırken küfürlü ya da taklit içerikli isimlerden kaçın."),
   ("Boşluk karakteri kaç karakter sayılır?",
    "Genelde bir karakter sayılır. Bazı oyunlar çok baytlı karakterleri farklı sayabilir; emin olmak için oyunun kendi sayacını kontrol et."),
   ("Instagram biyografisinde boş satır nasıl bırakılır?",
    "Satır sonuna görünmez karakter ekleyerek ya da satır aralığı karakterini kullanarak boş satır oluşturabilirsin. Biyografi aracı için <a href='instagram-sekilli-yazi.html'>Instagram şekilli yazı</a> sayfasına bak."),
 ],
},

# ============================================================ 8. EMOJİLER
{
 "slug": "emojiler", "file": "emojiler.html",
 "title": "Emojiler Kopyala — Emoji ve Kaomoji (Yüz İfadeleri) Kütüphanesi",
 "desc": "Emojiler kopyala: yüzler, kalpler, hayvanlar, oyun ve spor emojileri kategoriler halinde; ayrıca kaomoji yazılı yüz ifadeleri. Tıkla, kopyala, her yerde kullan.",
 "h1": "Emojiler ve <span class='hl'>Kaomoji</span>",
 "lead": "Mesajına duygu katmanın en hızlı yolu. <span data-emoji-count></span> emoji ve <span data-kaomoji-count></span> kaomoji (yazılı yüz ifadesi) arasından beğendiğine tıkla, kopyala.",
 "tool": "emoji",
 "cfg": {},
 "intro": [
   "<p>Emojiler evrenseldir: Telefonun, oyunun ya da uygulaman ne olursa olsun aynı görünürler. Bu sayfadaki kütüphane, günlük hayatta ve oyun profillerinde en çok kullanılan emojileri kategorilere ayırır; aradığını kaydırmadan bulursun.</p>",
   "<p>Kaomojiler ise bambaşka bir kültürdür: Japonya'dan dünyaya yayılan bu yazılı yüz ifadeleri, klavye karakterleriyle duygu anlatır. ¯\\_(ツ)_/¯ umursamazlığı, (ง •̀_•́)ง kararlılığı tek satırda söyler. Oyun nicklerinde ve sohbetlerde hâlâ çok sevilirler; üstelik her cihazda çalışırlar çünkü sıradan karakterlerden oluşurlar.</p>",
 ],
 "sections": [
   ("Emoji ve Kaomoji Nicklerde Nasıl Kullanılır?",
    "<p>Oyunların çoğu isim alanında emoji kabul etmez ama biyografi, durum ve klan açıklamalarında serbesttir. Kaomojiler ise harf ve işaretlerden oluştuğu için isim alanında da sıkça kullanılabilir; yine de uzun kaomojiler karakter sınırını hızla doldurur. Kısa olanları seç ve önce deneme alanında test et.</p>"),
 ],
 "faqs": [
   ("Emojiyi nasıl kopyalarım?",
    "Emojiye tıklaman yeterli; panona kopyalanır ve istediğin yere yapıştırabilirsin."),
   ("Kaomoji nedir?",
    "Kaomoji, parantez, çizgi ve harf gibi sıradan karakterlerle oluşturulan yüz ifadeleridir. Telefonunun emoji klavyesine ihtiyaç duymadan her yerde çalışır."),
   ("Emojiler oyun isimlerinde neden kabul edilmiyor?",
    "Çoğu oyun, isim alanında yalnızca harf, rakam ve temel sembollere izin verir; renkli emoji karakterleri bu kurala takılır. Biyografi ve sohbet alanlarında ise genelde serbesttir."),
   ("Yeni emojiler neden bazı telefonlarda kutu görünüyor?",
    "Emoji seti her yıl genişler; eski telefonların yazı tipleri yeni emojileri içermez. Karşı taraf güncel bir cihaz kullanıyorsa sorun yaşamazsın."),
   ("Kaomoji kopyalarken bozulur mu?",
    "Hayır, düz karakterlerden oluştuğu için kopyala-yapıştırda aynen taşınır."),
 ],
},

]

PAGES += [

# ============================================================ 9. PUBG
{
"slug": "pubg-sekilli-nick", "file": "pubg-sekilli-nick.html",
"title": "PUBG Şekilli Nick Yazma — Karakter Sayaçlı PUBG Nick Oluşturucu",
"desc": "PUBG Mobile şekilli nick yazma aracı: 14 karakter sayaçlı üreteç, klan etiketi şablonları, oyunda çalışan güvenli semboller ve isim değiştirme kartı rehberi.",
"h1": "PUBG Mobile <span class='hl'>Şekilli Nick</span> Yazma",
"lead": "PUBG Mobile'da nickin, lobideki kimliğindir. Bu araç PUBG'nin 14 karakter sınırına göre çalışır: sayacı aşan stiller işaretlenir, böylece oyuna yapıştırdığında sürpriz yaşamazsın.",
"badge": "14 karakter sayaçlı",
"tool": "generator",
"cfg": {"limit": 14, "sample": "KeskinAvcı", "placeholder": "PUBG nickini yaz (en fazla 14 karakter)...",
"label": "PUBG nickini yaz"},
"chips": ["KeskinAvcı", "GeceAvcısı", "TekKişilik", "SonNefes", "KralDöndü", "SessizÖlüm"],
"extra_html": """
<section class='content'>
<h2>PUBG'de Çalışan Güvenli Semboller</h2>
<p>Her sembol her oyunda görünmez. Aşağıdaki liste, PUBG Mobile'da yıllardır sorunsuz görüntülenen ve oyuncu nicklerinde en sık rastlanan sembollerden derlendi. Yine de oyun güncellemeleri destek listesini değiştirebilir; nickini kesinleştirmeden önce bir tanesini deneme maçında ya da profil önizlemesinde kontrol et. Sembole tıklayıp kopyalayabilirsin.</p>
<div data-symbol-grid='safe'></div>
<h2>Klan Etiketi Şablonları</h2>
<p>Klan etiketi, nickinin önünde ekibini gösteren kısa imzadır. Aşağıdaki şablonları kopyalayıp etiket harflerini kendi klanının kısaltmasıyla değiştir:</p>
<div class='results-grid'>
<button type='button' class='result-card' data-copy=''><span class='result-text'></span><span class='result-tag'>Köşeli etiket</span></button>
<button type='button' class='result-card' data-copy='『TAG』'><span class='result-text'>『TAG』</span><span class='result-tag'>Japon köşeli</span></button>
<button type='button' class='result-card' data-copy='꧁TAG꧂'><span class='result-text'>꧁TAG꧂</span><span class='result-tag'>Kraliyet çerçeve</span></button>
<button type='button' class='result-card' data-copy='TAG・'><span class='result-text'>TAG・</span><span class='result-tag'>Noktalı bitiş</span></button>
<button type='button' class='result-card' data-copy='〆TAG'><span class='result-text'>〆TAG</span><span class='result-tag'>İmza başı</span></button>
<button type='button' class='result-card' data-copy='★TAG★'><span class='result-text'>★TAG★</span><span class='result-tag'>Yıldızlı</span></button>
</div>
</section>""",
"intro": [
"<p>PUBG Mobile'da isim alanı 14 karakterle sınırlıdır ve bu sınır, süslemeler dahil her karakteri sayar. Şekilli harfler tek karakter sayılır; yani kalın ya da gotik yazmak sınırı büyütmez. Ancak harf arasına eklenen ayraçlar ve çerçeveler sınırı hızla doldurur. Üstteki araç bu hesabı senin yerine yapar: 14 karakteri aşan sonuçlar soluk gösterilir ve 'limit dışı' diye işaretlenir.</p>",
"<p>Bir de görünmez karakter konusu var: PUBG oyuncularının sevdiği 'boşluklu' ve 'görünmez' isimler, <a href='bosluk-kopyala.html'>görünmez boşluk karakterleriyle</a> yapılır. İsminin arasında boşluk varmış gibi göstermek ya da tamamen görünmez bir isim kullanmak için o sayfadaki karakterleri kopyalaman yeterli.</p>",
],
"sections": [
("İyi Bir PUBG Nicki Nasıl Olmalı?",
"<ul>"
"<li><strong>Kısa ve okunaklı:</strong> Kill ekranında bir saniyede okunmalı. 8-12 karakter idealdir.</li>"
"<li><strong>Tek vurgu:</strong> Ya stil ya sembol öne çıksın; ikisini de abartmak nicki karmaşık gösterir.</li>"
"<li><strong>Takım uyumu:</strong> Klanınla aynı etiketi ve benzer stili kullanmak lobide güçlü bir görüntü verir.</li>"
"<li><strong>Türkçe karakter avantajı:</strong> Bu araç ğ, ş, ı gibi harfleri bozmadığı için 'Şahin', 'Işıl' gibi isimler aynen yazılır.</li>"
"</ul>"),
("İsim Değiştirme Kartı Hakkında",
"<p>PUBG Mobile'da nick değiştirmek için İsim Değiştirme Kartı (ID Kartı) gerekir. Kart; etkinlik ödüllerinden, görev ve ilerleme ödüllerinden ya da oyun içi mağazadan UC ile temin edilebilir. Kartın yoksa yeni nickini burada hazırlayıp sakla; kartı aldığında tek yapıştırışta uygularsın. Saklamak için nicki kopyalayıp telefonunun notlarına yapıştırman yeterli.</p>"),
],
"faqs": [
("PUBG nicki en fazla kaç karakter olabilir?",
"PUBG Mobile isim alanı 14 karakterdir. Bu sayfadaki araç 14 karakteri aşan sonuçları işaretler; böylece oyuna gitmeden hangi stillerin sığdığını görürsün."),
("Şekilli harfler karakter sınırını artırır mı?",
"Hayır. Şekilli harfler de tek karakter sayılır. Sınırı dolduranlar genelde eklenen semboller ve ayraçlardır; araçtaki sayaç harf harf (görsel birim olarak) hesap yapar."),
("PUBG'de görünmez isim nasıl yapılır?",
"İsim alanına yalnızca görünmez boşluk karakteri yapıştırılır ya da harflerin arasına bu karakter eklenir. Gerekli karakterler <a href='bosluk-kopyala.html'>boşluk kopyala</a> sayfasında; U+3164 ve U+2800 en çok işe yarayanlardır."),
("Hangi semboller PUBG'de kutu görünür?",
"Nadir Unicode bloklarındaki süsler bazı cihazlarda kutu olabilir. Sayfanın 'güvenli semboller' bölümü, oyunda yıllardır sorunsuz görünen işaretlerden oluşur; önce oradakileri dene."),
("İsim değiştirme kartı olmadan nick değişir mi?",
"Hayır, PUBG Mobile nick değişikliği için İsim Değiştirme Kartı ister. Kart etkinliklerden, görevlerden veya mağazadan UC ile alınabilir."),
("Şekilli nick kullanmak yasak mı?",
"Şekilli harf kullanmak başlı başına yasak değildir. Yasak olan; küfürlü, başka oyuncuyu taklit eden ya da hile çağrışımlı isimlerdir. Kurallara uygun bir isim seçersen sorun yaşamazsın."),
("Klan etiketi nickten sayılır mı?",
"Evet, etiketi nickinle aynı alana yazıyorsan toplam uzunluk 14 karakteri geçmemeli. Kısa etiket (2-4 harf) ve kısa nick kombinasyonu en sağlıklısıdır."),
],
},

# ============================================================ 10. BRAWL STARS
{
"slug": "brawl-stars-sekilli-nick", "file": "brawl-stars-sekilli-nick.html",
"title": "Brawl Stars Şekilli Nick — 15 Karakter Sayaçlı İsim Oluşturucu",
"desc": "Brawl Stars için şekilli nick oluşturucu: 15 karakter sınırı sayaçlı araç, hazır isim önerileri ve oyunda görünen sembol ipuçları.",
"h1": "Brawl Stars <span class='hl'>Şekilli Nick</span>",
"lead": "Brawl Stars ismin 15 karakterle sınırlı. Bu sayaçlı araçla hangi şekilli stillerin sınıra sığdığını gör, hazır listeden ilham al, tek tıkla kopyala.",
"badge": "15 karakter sayaçlı",
"tool": "generator",
"cfg": {"limit": 15, "sample": "Yıldırım", "placeholder": "Brawl Stars ismini yaz (en fazla 15 karakter)...",
"label": "Brawl Stars ismini yaz"},
"chips": ["Yıldırım", "MinikDev", "ElPrimo", "KupaAvcısı", "SüperBrawler", "GeceSavaşçısı"],
"intro": [
"<p>Brawl Stars, renkli ve hızlı bir oyun; ismin de öyle olmalı. Oyunun isim alanı 15 karakter kabul eder ve bu sayfadaki araç her sonucu bu sınıra göre denetler. Sınırı aşan kombinasyonlar işaretlenir; böylece 'bir sembol daha ekleyeyim' derken isminin yarısını kaybetmezsin.</p>",
"<p>Brawl Stars'ın isim alanında bazı yoğun süslemeler sade stillere göre daha kararsız görünebilir. Bu yüzden bu sayfada balon, kare ve kalın stiller öne çıkar; bunlar oyunun canlı arayüzünde de net okunur.</p>",
],
"sections": [
("Hazır Brawl Stars İsim Önerileri",
"<p>Kendi ismini bulamadıysan aşağıdaki özgün önerilerden birini kopyalayabilir ya da onlardan ilhamla kendi karışımını yapabilirsin. Listeler tıklayıp kopyalamaya uygundur.</p>"
"<div data-nick-list='MinikDev|KupaKraliçesi|YıldırımÇocuk|SüperNişancı|GeceBrawlerı|ElmasAvcısı|ŞimşekKız|KralBrawler' data-list-styles='sansbold,bold,circled' data-list-wraps='none,star,spark'></div>"),
("Brawl Stars'ta İsim Değiştirme",
"<p>Brawl Stars'ta ilk isim değişikliği genelde ücretsizdir; sonrakiler elmas (gem) isteyebilir ve belirli aralıklarla sınırlı olabilir. Bu yüzden değişiklik yapmadan önce nickini burada son haline getirip önizlemede kontrol etmek akıllıca olur. Ayrıca kulüp (club) arkadaşlarınla benzer etiket kullanmak, kulüp savaşlarında takım görüntüsünü güçlendirir.</p>"),
],
"faqs": [
("Brawl Stars ismi kaç karakter olabilir?",
"İsim alanı 15 karakterdir. Araç, sınırı aşan sonuçları 'limit dışı' olarak işaretler."),
("Brawl Stars'ta hangi semboller görünür?",
"Yıldız, kalp, taç gibi temel semboller sorunsuz görünür. Çok nadir süs işaretleri bazı cihazlarda kutu olabilir; önce kulüp sohbetinde deneme yap."),
("İsmimi kaç kez değiştirebilirim?",
"İlk değişiklik çoğunlukla ücretsizdir; sonraki değişiklikler elmas gerektirebilir ve oyun kurallarına göre sınırlanabilir. Güncel koşul için oyunun ayarlar bölümünü kontrol et."),
("Renkli isim yapabilir miyim?",
"Brawl Stars bazı renk kodlarını desteklediği dönemler olmuştur; bu destek sürümden sürüme değişir. Şekilli harfler ise her sürümde çalışır, daha güvenli bir seçimdir."),
("Küfürlü ya da taklit isim kullanırsam ne olur?",
"Kurallara aykırı isimler şikâyet edilirse oyun ismi sıfırlayabilir ya da yaptırım uygulayabilir. Şekilli de olsa kurallara uygun isim seç."),
],
},

# ============================================================ 11. FREE FIRE
{
"slug": "free-fire-sekilli-nick", "file": "free-fire-sekilli-nick.html",
"title": "Free Fire Şekilli Nick — 12 Karakter Sayaçlı İsim Yazma",
"desc": "Free Fire şekilli nick aracı: 12 karakter sınırı, sayaçlı üreteç, hazır Free Fire isimleri ve elmas harcamadan önce nickini hazırlama rehberi.",
"h1": "Free Fire <span class='hl'>Şekilli Nick</span>",
"lead": "Free Fire'da isim alanı sadece 12 karakter. Kısa ve vurucu olmak zorundasın. Bu araç her stili 12 karakter sınırına göre denetler; sığmayanı boşuna deneme.",
"badge": "12 karakter sayaçlı",
"tool": "generator",
"cfg": {"limit": 12, "sample": "AsiÇocuk", "placeholder": "Free Fire nickini yaz (en fazla 12 karakter)...",
"label": "Free Fire nickini yaz"},
"chips": ["AsiÇocuk", "TekAtış", "BaşKeser", "NoScope", "Hayalet", "Booyah"],
"intro": [
"<p>Free Fire, popüler oyunlar arasında en kısa isim alanına sahip olanlardan: 12 karakter. Bu kısıt, aslında iyi bir nick için fırsattır; çünkü lobi ekranında kısa isimler daha hızlı okunur ve daha akılda kalıcıdır. Üstteki araç, yazdığın nicki düzinelerce stilde üretir ve 12 karakteri aşanları işaretler.</p>",
"<p>Free Fire'da isim değişikliği elmasla alınan İsim Değiştirme Kartı gerektirir. Elması harcamadan önce nickinin son halini burada hazırlaman, kart boşa gitmesini önler.</p>",
],
"sections": [
("12 Karaktere Sığan Nick Stratejisi",
"<ul>"
"<li><strong>Kısalt:</strong> 'KeskinNişancı' yerine 'Keskin' ya da 'Nişancı' tek başına daha güçlüdür.</li>"
"<li><strong>Tek sembol kullan:</strong> Başta bir taç ya da yıldız, toplamda 2 karaktere mal olur; bütçeni koru.</li>"
"<li><strong>Ayraçtan kaçın:</strong> Harf arası ayraçlar 12 karakterlik bütçede lükstür.</li>"
"<li><strong>Sayılardan yararlan:</strong> Doğum yılı yerine tek rakamlı vurgular (ör. 7, 9) yer kaplamaz.</li>"
"</ul>"
"<div data-nick-list='Booyah|TekAtış|AsiRuh|GeceKurdu|BaşAvcısı|SonKurşun|Kabus|Fırtına' data-list-styles='bold,fraktur,sansbold' data-list-wraps='crown,none,star'></div>"),
],
"faqs": [
("Free Fire nicki en fazla kaç karakter?",
"12 karakter. Bu sayfadaki araç sınırı aşan stilleri işaretler."),
("Free Fire isim değiştirme kartı nasıl alınır?",
"Kart, oyun içi mağazadan elmas ile alınır; zaman zaman etkinlik ödülü olarak da verilir. Kartı kullanmadan önce nickini burada kesinleştir."),
("Free Fire'da görünmez isim yapılabilir mi?",
"Görünmez boşluk karakterleri Free Fire'da da sık kullanılır. Karakterleri <a href='bosluk-kopyala.html'>boşluk kopyala</a> sayfasından alıp isim alanına yapıştırarak deneyebilirsin; destek, oyun sürümüne göre değişebilir."),
("Hangi stiller 12 karaktere en rahat sığar?",
"Kalın, modern ve küçük büyük harf stilleri harf sayısını değiştirmez; önemli olan eklediğin süslemelerdir. Baş ve sonda birer sembol genelde yeterlidir."),
("Nickimde Türkçe harf kullanabilir miyim?",
"Evet. Bu araç ğ, ü, ş, ı, ö, ç harflerini korur. Oyunun yazı tipi de bu harflerin şekilli karşılıklarını gösterir."),
],
},

# ============================================================ 12. VALORANT & CS2
{
"slug": "valorant-cs2-nickleri", "file": "valorant-cs2-nickleri.html",
"title": "Valorant ve CS2 Nickleri — Şekilli Nick ve İsim Önerileri",
"desc": "Valorant şekilli nick ve CS2 nickleri için oluşturucu: Riot ID kuralları, karakter sınırı notları, Steam ismi ipuçları ve hazır havalı nick önerileri.",
"h1": "Valorant &amp; CS2 <span class='hl'>Şekilli Nickleri</span>",
"lead": "Rekabetçi oyunlarda nick, itibarındır. Valorant'ın Riot ID kurallarına ve CS2'nin Steam ismi özgürlüğüne uygun şekilli nickler üret; sayaç Riot ID oyun adı sınırı olan 16 karaktere ayarlıdır.",
"badge": "Riot ID 16 karakter sayaçlı",
"tool": "generator",
"cfg": {"limit": 16, "sample": "KeskinGöz", "placeholder": "Oyun adını yaz (Riot ID için en fazla 16 karakter)...",
"label": "Oyun adını yaz"},
"chips": ["KeskinGöz", "TekMermi", "SessizAvcı", "RadyanYolcusu", "KafaAvcısı", "GölgeOperatör"],
"intro": [
"<p>Valorant'ta görünen adın, Riot ID'nin 'oyun adı' kısmıdır; yanında bir de etiket (tagline) bulunur. Oyun adı 3-16 karakter arası olmalı ve özel karakter desteği sınırlıdır; bu yüzden Valorant'ta en güvenlisi, sade stiller ve az sayıda semboldür. CS2 tarafında ise isim Steam profilinden gelir ve çok daha özgürdür: Unicode stillerin neredeyse tamamı çalışır.</p>",
"<p>Bu sayfadaki sayaç 16 karaktere ayarlıdır; Valorant için güvenli bölgede kalırsın, CS2 içinse bol bol yerin olur.</p>",
],
"sections": [
("Valorant Riot ID Kuralları (Özet)",
"<ul>"
"<li>Oyun adı 3 ile 16 karakter arasında olmalı.</li>"
"<li>Etiket (tagline) 3-5 karakterdir; adı benzersiz yapan asıl parça budur.</li>"
"<li>Çoğu süslü sembol Riot ID'de kabul edilmez; şekilli harflerin yaygın stilleri (kalın, modern) daha güvenlidir.</li>"
"<li>İsim değişikliği belirli aralıklarla yapılabilir; acele etmeden burada son halini ver.</li>"
"</ul>"),
("Hazır Rekabetçi Nick Önerileri",
"<div data-nick-list='TekMermi|KafaAvcısı|SessizOperatör|GölgeKeskin|RadyanAsı|SonŞarjör|GeceVardiyası|BuzKıran' data-list-styles='sansbold,bold,mono' data-list-wraps='none,arrow,star'></div>"
"<p>CS2 ve Steam için daha gösterişli stiller de kullanabilirsin; Steam isimleri Unicode karakterleri geniş ölçüde destekler. <a href='sekilli-semboller.html'>Sembol kütüphanesinden</a> nişangâh ve ok işaretleriyle kendi imzanı tamamla.</p>"),
],
"faqs": [
("Valorant'ta şekilli nick neden kabul edilmiyor?",
"Riot ID sistemi, oyun adında sınırlı karakter setine izin verir. Kalın ve modern gibi yaygın stiller genelde geçer; yoğun semboller reddedilebilir. Reddedilirse süslemeyi azaltmayı dene."),
("CS2'de isim nereden değişir?",
"CS2 oyun içi isim, Steam profil adından alınır. Steam profilini düzenleyip yeni şekilli ismi yapıştırman yeterli; değişiklik ücretsizdir."),
("Steam isminde her sembol çalışır mı?",
"Steam, Unicode karakterlerin büyük bölümünü gösterir. Yine de nişangâh gibi nadir işaretler bazı yazı tiplerinde farklı görünebilir; profil önizlemesinde kontrol et."),
("Takım etiketi nasıl eklerim?",
"CS2'de klan etiketi Steam grubuna üyelikle seçilir. Valorant'ta ise etiket, Riot ID'nin ikinci parçasıdır; oyun adından ayrı ayarlanır."),
("16 karakter sınırı hangi oyun için?",
"Bu sayfadaki sayaç Valorant Riot ID oyun adı sınırına (16) göre ayarlandı. CS2/Steam tarafında pratikte çok daha uzun isimler kullanılabilir."),
],
},

# ============================================================ 13. MOBILE LEGENDS
{
"slug": "mobile-legends-sekilli-nick", "file": "mobile-legends-sekilli-nick.html",
"title": "Mobile Legends Şekilli Nick — MLBB İsim Oluşturucu ve Öneriler",
"desc": "Mobile Legends (MLBB) için şekilli nick oluşturucu: zarif ve havalı stiller, hazır MLBB isimleri ve isim kartı kullanmadan önce bilmen gerekenler.",
"h1": "Mobile Legends <span class='hl'>Şekilli Nick</span>",
"lead": "MLBB'de nickin, kahramanın kadar önemlidir. Zarif el yazılarından karanlık gotik stillere kadar onlarca seçeneği dene; sayaç, oyunun isim sınırına göre seni uyarır.",
"badge": "İsim sınırı sayaçlı",
"tool": "generator",
"cfg": {"limit": 20, "sample": "AyŞövalyesi", "placeholder": "Mobile Legends nickini yaz...",
"label": "MLBB nickini yaz"},
"chips": ["AyŞövalyesi", "KaranlıkLord", "EfsaneAvcısı", "YıldızMuhafızı", "SisPerisi", "KızılKılıç"],
"intro": [
"<p>Mobile Legends: Bang Bang, isim konusunda oyunculara görece cömert davranır: Şekilli harfler ve pek çok sembol profilinde görünür. Bu yüzden MLBB nickleri, diğer oyunlara kıyasla daha süslü ve yaratıcı olabilir. Atasözü gibi: Lobi ne kadar kalabalık olursa, zarif bir el yazısı o kadar fark edilir.</p>",
"<p>Bu sayfadaki araç 20 karakter sınırını baz alır; ancak bazı özel karakterlerin oyunda iki birim sayılabildiğini unutma. İsmini kesinleştirmeden önce oyun içi önizlemede kontrol etmek her zaman iyi bir fikirdir.</p>",
],
"sections": [
("MLBB İçin Stil Tavsiyeleri",
"<ul>"
"<li><strong>Destansı görünüm:</strong> Kalın gotik + kraliyet çerçevesi, ana kahraman (main) profillerinde çok tutulur.</li>"
"<li><strong>Zarif görünüm:</strong> El yazısı + çiçek süslemesi; destek ve büyücü oyuncularının favorisidir.</li>"
"<li><strong>Karanlık görünüm:</strong> Çift çizgili + ay süslemesi; suikastçı profillerine yakışır.</li>"
"</ul>"
"<div data-nick-list='AyŞövalyesi|KızılKılıç|EfsaneYolcusu|SessizBüyücü|YıldızAvcısı|KaranlıkNöbetçi|GümüşKanat|SonEfsane' data-list-styles='boldscript,fraktur,bold' data-list-wraps='royal,moon,flower'></div>"),
],
"faqs": [
("MLBB'de isim kaç karakter olabilir?",
"Mobile Legends isimleri en fazla 20 karakter olabilir. Bazı çok baytlı semboller oyunda daha fazla yer kaplayabilir; araçtaki sayaç görsel karakter sayısını gösterir."),
("İsim değiştirme kartı gerekli mi?",
"İlk isim genelde ücretsiz belirlenir; sonraki değişiklikler İsim Değiştirme Kartı isteyebilir. Kart elmasla alınabildiği için nickini burada önceden kesinleştirmen tasarruf sağlar."),
("MLBB'de hangi semboller görünür?",
"Kalp, yıldız, taç ve ay gibi popüler semboller görünür. Nadir süsler için önce profil önizlemesinde dene."),
("Boşluklu isim yapabilir miyim?",
"MLBB isim alanında normal boşluk sınırlıdır; görünmez boşluk karakterleriyle boşluk etkisi verilebilir. Karakterler için <a href='bosluk-kopyala.html'>boşluk kopyala</a> sayfasına bak."),
("Aynı nicki arkadaşım da kullanabilir mi?",
"MLBB'de isimler benzersiz olmak zorunda değildir; yanında görünen ID numarası oyuncuları ayırır. Yine de özgün bir isim, akılda kalıcılığını artırır."),
],
},

# ============================================================ 14. DİĞER OYUNLAR (HUB)
{
"slug": "diger-oyunlar", "file": "diger-oyunlar.html",
"title": "Oyun Nickleri — LoL, CoD Mobile, Metin2, Knight Online, Agar.io Şekilli Nick",
"desc": "Diğer oyunlar için şekilli nickler: League of Legends, CoD Mobile, Metin2, Knight Online ve Agar.io isim kuralları, ipuçları ve tek üreteçte tüm stiller.",
"h1": "Diğer Oyunlar İçin <span class='hl'>Şekilli Nickler</span>",
"lead": "Oyunun hangisi olursa olsun, şekilli nick burada. Üreteç tüm oyunlarda çalışır; aşağıda her oyun için isim kuralları ve küçük ipuçları seni bekliyor.",
"tool": "generator",
"cfg": {"limit": 0, "sample": "EfsaneOyuncu", "placeholder": "Nickini yaz...",
"label": "Nickini yaz, tüm stilleri gör"},
"chips": ["EfsaneOyuncu", "VadiKralı", "LoncaReisi", "KralKatili"],
"intro": [
"<p>Her oyunun isim kuralları farklıdır; bazıları şekilli harflere bayılır, bazıları yalnızca sade harflere izin verir. Bu sayfada en çok sorulan beş oyunun isim özelliklerini tek çatı altında topladık. Üstteki üreteçle nickini hazırla, sonra oynadığın oyunun bölümündeki notlara göre son dokunuşu yap.</p>",
],
"sections": [
("League of Legends (LoL) Nickleri",
"<p>LoL, Riot ID sistemine geçtiği için isim kuralları Valorant'la benzer: Oyun adı 3-16 karakter, yanında bir etiket. Süslü sembollerin çoğu kabul edilmez; kalın ve modern stillerin harf karşılıkları da Riot tarafında sadeleştirilebilir. LoL için en güvenlisi, özgün ve kısa bir oyun adı + akılda kalıcı bir etikettir. Ayrıntılar için <a href='valorant-cs2-nickleri.html'>Valorant &amp; CS2 sayfasındaki</a> Riot ID bölümüne bak.</p>"),
("CoD Mobile Nickleri",
"<p>Call of Duty: Mobile isim alanı sınırlıdır ve değişiklik İsim Değiştirme Kartı (CP ile) gerektirebilir. Askerî temalı kısa nickler (ör. tek kelimelik, vurucu isimler) bu oyunda çok tutulur. Şekilli harfler ve temel semboller genelde görünür; yoğun süslemeden kaçın.</p>"),
("Metin2 Nickleri",
"<p>Metin2, Türkiye'de yıllardır oynanan bir efsane; lonca kültüründe isim her şeydir. Metin2 isimlerinde Türkçe harfler zaten desteklenir; şekilli harflerse sınırlı destek görür. Lonca adı ve karakter adında zarif el yazısı denemeden önce, karakter oluşturma ekranında önizlemeyi kontrol et. Kabul edilmezse aynı ismin sade halini yedek olarak hazır tut.</p>"),
("Knight Online Nickleri",
"<p>Knight Online'da da durum Metin2'ye benzer: İsimler genelde harf ve rakam ağırlıklıdır. Şekilli stillerin bir kısmı istemcide kutu görünebilir. Bu yüzden Knight için sade, güçlü ve Türkçe isimler (ör. tek kelime + sembolsüz) en güvenilir seçimdir; süsü klan tanıtım yazılarına sakla.</p>"),
("Agar.io Nickleri",
"<p>Agar.io isim konusunda en özgür oyunlardandır; şekilli harfler ve semboller hücre üstünde görünür ve kısa nickler dev hücrelerde bile okunur. Balon ve kare stiller Agar.io'da özellikle eğlenceli durur. Ayrıca oyunun özel resimli nick kodları dönem dönem değiştiği için, en kalıcı çözüm Unicode şekilli isimdir.</p>"
"<div data-nick-list='VadiKralı|LoncaReisi|HücreKralı|GörevAdamı|SavaşLordu|KaranlıkŞövalye' data-list-styles='bold,sansbold,boldscript' data-list-wraps='crown,none,star'></div>"),
],
"faqs": [
("Roblox için şekilli nick neden önerilmiyor?",
"Roblox, kullanıcı adlarında şekilli harflere izin vermez; kullanıcı adı yalnızca harf, rakam ve tek alt çizgi içerebilir. Şekilli yazıyı yalnızca görüntü adında (display name) ve biyografide kullanabilirsin. Öneriler için <a href='nick-listeleri.html'>nick listeleri</a> sayfasındaki İngilizce listeye bak."),
("Metin2 ve Knight Online'da şekilli harf neden bazen kutu görünüyor?",
"Bu oyunların eski istemcileri, yeni Unicode bloklarını tanımaz. Sade stiller ve temel semboller daha güvenlidir; yine de kesin sonuç için oyun içi önizlemeyi kontrol et."),
("CoD Mobile'da isim değiştirmek ücretli mi?",
"Genelde İsim Değiştirme Kartı gerekir ve kart CP (oyun parası) ile alınır. Nickini burada kesinleştirip karta tek seferde doğru ismi yazmak en ekonomik yoldur."),
("LoL'de etiket (tag) ne işe yarar?",
"Aynı oyun adını birden çok oyuncu kullanabilir; etiket seni diğerlerinden ayırır. Etiketini kısa ve akılda kalıcı seç (ör. TR1, ASLN)."),
("Agar.io'da ismim neden tam görünmüyor?",
"Çok uzun isimler küçük hücrelerde taşabilir. Kısa (en fazla 10-12 karakter) ve kalın stiller en iyi sonucu verir."),
],
},

]

PAGES += [

# ============================================================ 15. INSTAGRAM
{
 "slug": "instagram-sekilli-yazi", "file": "instagram-sekilli-yazi.html",
 "title": "Instagram Şekilli Yazı — Bio ve İsim İçin Süslü Yazı Stilleri",
 "desc": "Instagram şekilli yazı oluşturucu: biyografi (bio) ve görüntü adı için el yazısı, italik ve kalın stiller. 150 karakter bio sınırı notlarıyla, tek tıkla kopyala.",
 "h1": "Instagram <span class='hl'>Şekilli Yazı</span>",
 "lead": "Profilin, seni saniyeler içinde anlatan vitrinin. Biyografini ve görüntü adını şekilli yazılarla düzenle; sayaç, Instagram biyografi sınırı olan 150 karaktere göre çalışır.",
 "badge": "Bio sınırı: 150 karakter",
 "tool": "generator",
 "cfg": {"limit": 150, "sample": "Hayatı sev, gülümse", "placeholder": "Bio veya isim metnini yaz...",
         "label": "Bio satırını veya görüntü adını yaz"},
 "chips": ["Hayatı sev", "Gezgin ruh", "Kahve ve kitap", "İstanbul", "Fotoğraf tutkunu"],
 "intro": [
   "<p>Instagram biyografisi 150 karakterdir ve bu alan, profilini ziyaret eden kişinin gördüğü ilk şeydir. Şekilli yazılar burada iki işe yarar: Satırları birbirinden ayırır ve gözü önemli bilgiye (meslek, şehir, ilgi alanı) yönlendirir. El yazısı ve italik stiller biyografide zarif; kalın stil ise başlık satırında güçlü durur.</p>",
   "<p>Görüntü adı (kullanıcı adının üstündeki kalın satır) da şekilli harfleri destekler. Aramada çıkan bu satıra adını şekilli yazmak, aynı isimdeki profiller arasında seni ayırır. Kullanıcı adının kendisinde ise yalnızca harf, rakam, nokta ve alt çizgiye izin verilir; şekilli harf orada kullanılamaz.</p>",
 ],
 "sections": [
   ("Etkili Bir Instagram Biyografisi Nasıl Kurulur?",
    "<ul>"
    "<li><strong>1. satır — Kimlik:</strong> Adın ya da mesleğin. Kalın stille yaz.</li>"
    "<li><strong>2. satır — İlgi alanı:</strong> El yazısı stiliyle kişisel bir not.</li>"
    "<li><strong>3. satır — Vurgu:</strong> Minik üst yazı ya da sembolle ayrılmış kısa bir söz.</li>"
    "<li><strong>4. satır — Yönlendirme:</strong> 'DM açık', şehir bilgisi veya bağlantı çağrısı.</li>"
    "</ul>"
    "<p>Satır aralarına <a href='bosluk-kopyala.html'>görünmez boşluk</a> eklemek, biyografinin mobilde dağınık değil düzenli görünmesini sağlar. Sembolleri ise <a href='sekilli-semboller.html'>kütüphaneden</a> tek tıkla alabilirsin: ✦ ♡ ☾ gibi küçük işaretler satır başlarında çok zarif durur.</p>"),
 ],
 "faqs": [
   ("Instagram biyografisi kaç karakter?",
    "150 karakter. Bu sayfadaki sayaç tam bu sınıra göre çalışır; çok satırlı biyografi yazarken toplamı takip edebilirsin."),
   ("Kullanıcı adıma şekilli harf ekleyebilir miyim?",
    "Hayır. Kullanıcı adı yalnızca küçük harf, rakam, nokta ve alt çizgi kabul eder. Şekilli yazıyı görüntü adında ve biyografide kullan."),
   ("Şekilli biyografi aramada görünür mü?",
    "Görüntü adı ve biyografi metni Instagram aramasında taranır; ancak şekilli harfler düz harf gibi indekslenmeyebilir. Bulunabilirlik önemliyse adının düz halini de biyografide bir yerde geçir."),
   ("Bioya boş satır nasıl eklenir?",
    "Satır sonlarında görünmez boşluk karakteri kullanmak, Instagram'ın fazla boşlukları silmesini engeller. Karakterler <a href='bosluk-kopyala.html'>boşluk kopyala</a> sayfasında."),
   ("Hangi stil biyografide en iyi görünür?",
    "El yazısı ve italik en çok tercih edilenlerdir; kalın stil başlık satırında, minik üst yazı ise dipnot gibi kısa vurgu satırlarında güzel durur."),
 ],
},

# ============================================================ 16. WHATSAPP
{
 "slug": "whatsapp-sekilli-nick", "file": "whatsapp-sekilli-nick.html",
 "title": "WhatsApp Şekilli Nick — Profil İsmi ve Durum İçin Şekilli Yazı",
 "desc": "WhatsApp için şekilli isim yazma: profil adında 25 karakter sınırına uygun sayaçlı araç, durum mesajları için süslü yazı stilleri ve boş mesaj ipucu.",
 "h1": "WhatsApp <span class='hl'>Şekilli Nick</span>",
 "lead": "WhatsApp profil adın, rehberde kayıtlı olmayanların gördüğü kimliğindir. 25 karakterlik sınıra uygun, şık bir şekilli isim yap; durumuna da süslü bir söz ekle.",
 "badge": "Profil adı sınırı: 25 karakter",
 "tool": "generator",
 "cfg": {"limit": 25, "sample": "Yıldız", "placeholder": "WhatsApp profil adını yaz (en fazla 25 karakter)...",
         "label": "Profil adını yaz"},
 "chips": ["Yıldız", "Gece Kuşu", "Sessiz", "Meşgul", "Çevrimiçi"],
 "intro": [
   "<p>WhatsApp'ta iki farklı yazı alanın var: Profil adı (en fazla 25 karakter) ve 'hakkında'/durum satırı. İkisi de şekilli harfleri gösterir. Profil adında sade ve okunaklı bir stil seçmek önemlidir; çünkü bu ad, gruplarda ve bilinmeyen numaralarda senin tanıtımındır.</p>",
   "<p>Durum satırında ise özgürsün: El yazısı bir söz, minik harflerle bir motto ya da sembollerle süslenmiş bir cümle... Bu sayfadaki araç profil adı sınırına (25) göre ayarlıdır; durum için daha uzun metin yazarsan sayaç aşımı uyarısını görmezden gelebilirsin, durum alanı daha uzundur.</p>",
 ],
 "sections": [
   ("WhatsApp'ta Şekilli Yazının Başka Kullanımları",
    "<ul>"
    "<li><strong>Mesaj içi biçimlendirme:</strong> WhatsApp'ın kendi kalın (*yıldız* arasında) ve italik (_alt çizgi_ arasında) yazımı, mesajlarda çalışır; şekilli harfler ise profil ve durumda kalıcıdır.</li>"
    "<li><strong>Boş mesaj şakası:</strong> <a href='bosluk-kopyala.html'>Görünmez karakterle</a> arkadaşına boş mesaj balonu gönderebilirsin.</li>"
    "<li><strong>Grup adları:</strong> Grup yöneticisiysen grup adını şekilli harflerle yenilemek, gruplar listesinde ayırt edilmeni sağlar.</li>"
    "</ul>"),
 ],
 "faqs": [
   ("WhatsApp profil adı kaç karakter olabilir?",
    "25 karakter. Araç bu sınıra göre sayaç tutar; aşan kombinasyonları işaretler."),
   ("Şekilli isim karşı tarafta da görünür mü?",
    "Evet. Unicode karakterler herkesin telefonunda aynı görünür. Çok eski cihazlarda nadir stiller kutu olabilir; kalın ve modern stiller en güvenlisidir."),
   ("Durum (hakkında) yazısı için de kullanabilir miyim?",
    "Evet, aynı araçla durum cümleni de şekillendirebilirsin; durum alanının sınırı profil adından uzundur."),
   ("WhatsApp'ta boş mesaj nasıl gönderilir?",
    "Normal boşluk gönderilemez ama görünmez karakter gönderilebilir. <a href='bosluk-kopyala.html'>Boşluk kopyala</a> sayfasındaki karakteri kopyalayıp mesaj alanına yapıştırman yeterli."),
   ("İşletme hesabında şekilli isim uygun mu?",
    "Resmî iletişimde sade stiller (kalın, modern) profesyonel görünür. Aşırı süsleme ciddiyeti azaltabilir; işletme adında ölçülü ol."),
 ],
},

# ============================================================ 17. DISCORD
{
 "slug": "discord-sekilli-nick", "file": "discord-sekilli-nick.html",
 "title": "Discord Şekilli Nick — Sunucu Takma Adı ve Kullanıcı Adı Stilleri",
 "desc": "Discord şekilli nick oluşturucu: 32 karakter sunucu takma adı sınırına uygun sayaçlı araç, kullanıcı adı kuralları ve sunucularda öne çıkma ipuçları.",
 "h1": "Discord <span class='hl'>Şekilli Nick</span>",
 "lead": "Discord'da her sunucuda farklı bir takma adın olabilir. 32 karakterlik takma ad sınırına uygun şekilli nickler üret; sunucu listesinde adın bir bakışta tanınsın.",
 "badge": "Takma ad sınırı: 32 karakter",
 "tool": "generator",
 "cfg": {"limit": 32, "sample": "GeceMuhafızı", "placeholder": "Discord takma adını yaz (en fazla 32 karakter)...",
         "label": "Takma adını yaz"},
 "chips": ["GeceMuhafızı", "Moderatör", "OyunKralı", "BotAvcısı", "SesliKraliçe"],
 "intro": [
   "<p>Discord'da iki isim katmanı vardır: Her yerde geçerli kullanıcı adın ve sunucuya özel takma adın (nickname). Kullanıcı adları sade karakterlerle sınırlıyken, sunucu takma adları şekilli harflerin çoğunu kabul eder ve 32 karaktere kadar uzayabilir. Bu araç tam o sınıra göre çalışır.</p>",
   "<p>Kalabalık sunucularda takma adın; üye listesinde, sesli kanal göstergesinde ve mesajlarının başında görünür. Okunaklı bir kalın ya da daktilo stili, yöneticilerin ve arkadaşlarının seni hızlı bulmasını sağlar.</p>",
 ],
 "sections": [
   ("Sunucuya Göre Takma Ad Stratejisi",
    "<ul>"
    "<li><strong>Oyun sunucuları:</strong> Oyun nickinle aynı şekilli adı kullan; tutarlılık tanınmanı sağlar.</li>"
    "<li><strong>Topluluk sunucuları:</strong> Rolünü belli eden bir vurgu (ör. başta ♛ ya da ✦) yöneticilik görevlerinde işine yarar.</li>"
    "<li><strong>Çalışma/okul sunucuları:</strong> Sade stiller seç; adının düz halini parantezde tutmak ciddiyeti korur.</li>"
    "</ul>"
    "<p>Takma ad değiştirmek için sunucuda 'takma adı değiştir' iznin olmalı; bazı sunucular bunu kısıtlar. Kullanıcı adının kendisini şekillendirmek istersen Discord'un izin verdiği karakterlerle sınırlı kalacağını unutma.</p>"),
 ],
 "faqs": [
   ("Discord takma adı kaç karakter olabilir?",
    "Sunucu takma adları en fazla 32 karakterdir. Bu sayfadaki sayaç o sınıra göre çalışır."),
   ("Kullanıcı adıma şekilli harf koyabilir miyim?",
    "Discord kullanıcı adları (pomelo sistemiyle) büyük ölçüde sade harf, rakam ve sınırlı işaret kabul eder; şekilli harflerin çoğu reddedilir. Şekilli yazıyı takma ad alanında kullan."),
   ("Takma adım neden bazı sunucularda değişmiyor?",
    "Sunucu, üyelere takma ad değiştirme izni vermemiş olabilir. Bu durumda yöneticiye başvurman gerekir; izin olan sunucularda profilinden kendin düzenlersin."),
   ("Her sunucuda farklı takma adım olabilir mi?",
    "Evet. Takma ad sunucuya özeldir; oyun sunucusunda oyun nickin, arkadaş sunucusunda gerçek adın görünebilir."),
   ("Şekilli takma ad bildirimlerde sorun çıkarır mı?",
    "Hayır. Bahsetmeler (@etiket) kullanıcı adına bağlıdır; takma ad yalnızca görünümü değiştirir. Yalnızca çok nadir semboller bazı cihazlarda kutu görünebilir."),
 ],
},

# ============================================================ 18. TIKTOK
{
 "slug": "tiktok-sekilli-yazi", "file": "tiktok-sekilli-yazi.html",
 "title": "TikTok Şekilli Yazı — İsim ve Biyografi İçin Süslü Yazılar",
 "desc": "TikTok şekilli yazı aracı: görüntü adı ve biyografi için süslü yazı stilleri, kullanıcı adı kuralları ve profilde fark yaratma ipuçları.",
 "h1": "TikTok <span class='hl'>Şekilli Yazı</span>",
 "lead": "TikTok'ta profilin, videon kadar önemlidir. Görüntü adını ve biyografini şekilli yazılarla tasarla; kalabalık akışta bile adın akılda kalsın.",
 "tool": "generator",
 "cfg": {"limit": 0, "sample": "Dans Kraliçesi", "placeholder": "TikTok adını veya bio satırını yaz...",
         "label": "Görüntü adını ya da bio satırını yaz"},
 "chips": ["Dans Kraliçesi", "Komik Çocuk", "Gece Yayını", "Oyun Zamanı", "Mini Şef"],
 "intro": [
   "<p>TikTok'ta kullanıcı adı (@ ile başlayan) sade karakterlerle sınırlıdır; ama görüntü adı ve biyografi, şekilli harfleri destekler. Keşfet akışında videonun altında görünen görüntü adındır; adın orada ne kadar ayırt ediciyse, izleyicinin profilini ziyaret etme ihtimali o kadar artar.</p>",
   "<p>Bu araçla adını ve biyografi satırlarını onlarca stilde deneyebilirsin. Özellikle el yazısı ve kalın stiller, TikTok'un hızlı tüketim ortamında hem şık hem okunaklı sonuçlar verir.</p>",
 ],
 "sections": [
   ("TikTok Profilinde Şekilli Yazı İpuçları",
    "<ul>"
    "<li><strong>Kısa tut:</strong> Görüntü adı videonun altında tek satır görünür; 15-20 karakter sonrası kesilebilir.</li>"
    "<li><strong>İçeriğinle eşleştir:</strong> Oyun kanalıysan gotik/kalın, günlük vlog ise el yazısı tarzı içerik vaadini güçlendirir.</li>"
    "<li><strong>Biyografide sembol kullan:</strong> Satır başlarında ✦ ☾ ♡ gibi küçük işaretler, biyografiyi düzenli gösterir; sembolleri <a href='sekilli-semboller.html'>kütüphaneden</a> al.</li>"
    "<li><strong>Kullanıcı adını sade tut:</strong> Söylenmesi ve aranması kolay bir @ adı, şekilli görüntü adıyla en iyi ikilidir.</li>"
    "</ul>"),
 ],
 "faqs": [
   ("TikTok kullanıcı adıma şekilli harf ekleyebilir miyim?",
    "Hayır. Kullanıcı adı harf, rakam, nokta ve alt çizgiyle sınırlıdır. Şekilli yazıyı görüntü adı ve biyografi alanında kullan."),
   ("Görüntü adı kaç karakter olabilir?",
    "Görüntü adları kullanıcı adından uzundur; ancak mobil görünümde uzun adlar kesilir. Kısa ve vurucu bir ad, her cihazda tam görünür."),
   ("Şekilli ad arama sonuçlarını etkiler mi?",
    "Arama genelde kullanıcı adı ve düz metin üzerinden çalışır. Bulunabilirlik için kullanıcı adını sade ve akılda kalıcı seç; şekilli adı görsel imza olarak kullan."),
   ("Biyografime bağlantı ve satır ekleyebilir miyim?",
    "Biyografi çok satırlı olabilir; satırları şekilli yazı ve sembollerle ayırmak okunabilirliği artırır. Boş satırlar için <a href='bosluk-kopyala.html'>görünmez boşluk</a> karakterlerinden yararlan."),
   ("Canlı yayın ismimde de görünür mü?",
    "Evet, görüntü adın yayınlarda ve yorumlarda da aynı şekilli haliyle görünür."),
 ],
},

# ============================================================ 19. DİĞER SOSYAL MEDYA (HUB)
{
 "slug": "diger-sosyal-medya", "file": "diger-sosyal-medya.html",
 "title": "Facebook, X, Telegram, YouTube ve Twitch İçin Şekilli Yazılar",
 "desc": "Diğer sosyal medya platformları için şekilli yazı rehberi: Facebook, X (Twitter), Telegram, YouTube ve Twitch'te şekilli isim ve yazı kullanmanın kuralları ve araç.",
 "h1": "Diğer Platformlarda <span class='hl'>Şekilli Yazı</span>",
 "lead": "Her platformun isim kuralları farklı. Bu sayfadaki üreteç hepsinde çalışır; aşağıdaki bölümlerde Facebook, X, Telegram, YouTube ve Twitch için platforma özel notları bulursun.",
 "tool": "generator",
 "cfg": {"limit": 0, "sample": "Sosyal Kral", "placeholder": "İsmini veya metnini yaz...",
         "label": "İsmini ya da metnini yaz"},
 "chips": ["Sosyal Kral", "Yayıncı", "Kanalım"],
 "intro": [
   "<p>Bazı platformlar şekilli harfleri sever, bazıları isim politikası gereği kısıtlar. Aşağıdaki özet, hazırlığını doğru alana yapman için hazırlandı: Hangi platformda şekilli yazıyı nerede (isim, başlık, açıklama, sohbet) kullanabileceğini tek bakışta gör.</p>",
 ],
 "sections": [
   ("Facebook",
    "<p>Facebook, gerçek isim politikası uygular; profil isminde şekilli harfler kabul edilmeyebilir ya da sonradan inceleme isteyebilir. Buna karşılık <strong>sayfa adları, grup adları, gönderi metinleri ve yorumlar</strong> şekilli yazıyı rahatça gösterir. Topluluk yöneticileri için şekilli başlıklar, duyuru gönderilerinde harika iş görür.</p>"),
   ("X (Twitter)",
    "<p>X'te görünen ad (display name) şekilli harfleri destekler ve 50 karaktere kadar yazılabilir. Kullanıcı adı (@) sade karakterlerle sınırlıdır. Biyografi de şekilli yazıya açıktır; satır başı sembolleriyle düzenli bir bio kurabilirsin.</p>"),
   ("Telegram",
    "<p>Telegram isim ve biyografi alanlarında Unicode desteği geniştir; şekilli yazılar sorunsuz görünür. Kanal ve grup başlıklarında da kullanılabilir. Telegram'ın kendi biçimlendirmesi (kalın/italik) mesajlar içindir; şekilli harfler kalıcı alanlarda devrededir.</p>"),
   ("YouTube",
    "<p>Kanal adı şekilli harf içerebilir; ancak aramada bulunabilirlik için kanal adının düz okunuşunu da açıklamada geçirmek akıllıca olur. Video başlıklarında şekilli kelimeleri ölçülü kullan: Bir-iki vurgu kelimesi dikkat çeker, tamamı şekilli bir başlık okunabilirliği düşürür.</p>"),
   ("Twitch",
    "<p>Twitch görünen adı şekilli harflere izin verir; kullanıcı adı sade karakterlidir. Yayın başlıklarında ve panellerde (hakkımda bölümü) şekilli yazılar yaygındır. Sohbette de özel biçimlendirme olmadığı için önemli duyurularını şekilli panellerle öne çıkarabilirsin.</p>"),
 ],
 "faqs": [
   ("Facebook ismim neden kabul edilmedi?",
    "Facebook profil isimlerinde gerçek isim politikası uygular ve süslü karakterleri reddedebilir. Şekilli yazıyı sayfa, grup ve gönderilerde kullanman daha sorunsuzdur."),
   ("X'te görünen ad ile kullanıcı adı arasındaki fark ne?",
    "Kullanıcı adı (@...) benzersiz kimliğindir ve sade karakter ister. Görünen ad ise profilinde büyük yazılan addır; şekilli harfleri orada kullanabilirsin."),
   ("YouTube kanal adım şekilli olursa aramada çıkar mıyım?",
    "Arama, kanal adının düz metin eşleşmesine de bakar. Şekilli ad kullanıyorsan açıklama ve 'hakkında' bölümünde adının düz halini de yazmak bulunabilirliği korur."),
   ("Telegram'da kanal adımda sembol kullanabilir miyim?",
    "Evet, Telegram Unicode desteği geniştir. Yine de aşırı sembol, kanalın ciddiyetini azaltabilir; baş ve sonda birer işaret yeterlidir."),
   ("Twitch'te görünen adımı ne sıklıkla değiştirebilirim?",
    "Kullanıcı adı değişiklikleri 60 günde bir gibi aralıklarla sınırlı olabilir; görünen ad (büyük/küçük harf ve görüntü) değişiklikleri daha esnektir. Güncel koşulu hesabından kontrol et."),
 ],
},

# ============================================================ 20. HAVALI NİCKLER
{
 "slug": "havali-nickler", "file": "havali-nickler.html",
 "title": "Havalı Nickler — Hazır Şekilli Nick Önerileri (2026)",
 "desc": "Hazır havalı nickler: karanlık, efsanevi, kısa ve gösterişli kategorilerde özgün şekilli nick önerileri. Beğendiğine tıkla, kopyala, oyunda kullan.",
 "h1": "Hazır <span class='hl'>Havalı Nickler</span> 2026",
 "lead": "Sıfırdan düşünmek zorunda değilsin. İşte sana kategorilere ayrılmış, tamamı özgün ve kullanılmaya hazır şekilli nick önerileri. Tıkla, kopyala, oyuna yapıştır.",
 "tool": "lists",
 "cfg": {},
 "intro": [
   "<p>Bu sayfadaki listeler, bu site için özel olarak uydurulmuş özgün isimlerden oluşur; başka sitelerin listelerinden kopyalanmamıştır. Her isim, farklı bir yazı stili ve süslemeyle hazır sunulur. Hoşuna giden bir ismi aynen kullanabilir ya da <a href='index.html'>ana üreteçte</a> aynı ismi farklı stillerde yeniden üretebilirsin.</p>",
 ],
 "sections": [
   ("Karanlık ve Gizemli Nickler",
    "<div data-nick-list='GeceGölgesi|KaranlıkRuh|SisLord|MezarlıkBekçisi|KabusAvcısı|KaraBüyü|SoğukNefes|YarasaKral' data-list-styles='fraktur,boldfraktur,doublestruck' data-list-wraps='cross,moon,royal'></div>"),
   ("Efsanevi ve Güçlü Nickler",
    "<div data-nick-list='EjderhaYüreği|ŞimşekTanrısı|DemirYumruk|KralınGölgesi|FırtınaLordu|AslanYürek|Titansoyu|ÖlümsüzKral' data-list-styles='bold,sansbold,boldscript' data-list-wraps='crown,bolt,star'></div>"),
   ("Kısa ve Vurucu Nickler",
    "<div data-nick-list='Reis|Zehir|Atmaca|Pusu|Kobra|Şahin|Yargıç|Kabus' data-list-styles='negsquared,circled,sansbold,bold' data-list-wraps='none,crown,star'></div>"),
   ("Zarif ve Estetik Nickler",
    "<div data-nick-list='AyPerisi|YıldızTozu|GeceÇiçeği|İnciKız|MorSis|RüyaGezgini|KristalKalp|NazlıAy' data-list-styles='script,boldscript,italic' data-list-wraps='flower,heart,moon'></div>"),
 ],
 "faqs": [
   ("Bu nickler daha önce başkası tarafından kullanılmış olabilir mi?",
    "Listeler özgün olarak hazırlandı; ancak popüler kelimelerden türedikleri için benzerlerine rastlamak mümkündür. Oyunda kullanıcı adı doluysa sonuna sembol ya da kısa bir ek ekleyerek kendine özgü hale getirebilirsin."),
   ("Nicki kendi ismimle nasıl birleştiririm?",
    "Listedeki yapıyı örnek al: Örneğin 'Gece' + kendi ismin ya da ismin + 'Kral/Perisi' gibi. Sonra üreteçte kendi karışımını şekillendir."),
   ("Hangi liste oyun için daha uygun?",
    "Oyun lobbiesinde karanlık ve efsanevi listeler; sosyal medyada zarif liste; karakter sınırı kısa oyunlarda kısa liste öne çıkar."),
   ("Nicklerin yanına klan etiketi ekleyebilir miyim?",
    "Evet. <a href='klan-isimleri.html'>Klan isimleri</a> sayfasındaki etiket şablonlarıyla birleştir; toplam karakter sayısına dikkat etmeyi unutma."),
   ("Listeler güncelleniyor mu?",
    "Sayfadaki listeler 2026 için hazırlandı; yeni kategoriler eklendikçe bu sayfa üzerinden ulaşabilirsin."),
 ],
},

# ============================================================ 21. NİCK LİSTELERİ
{
 "slug": "nick-listeleri", "file": "nick-listeleri.html",
 "title": "Nick Listeleri — Türkçe, İngilizce, Kız, Erkek, Kısa ve Anlamlı Nickler",
 "desc": "Nick listeleri tek sayfada: Türkçe nickler, İngilizce nickler, kız ve erkek oyun nickleri, kısa havalı nickler ve anlamlı nickler. Tıkla, kopyala, kullan.",
 "h1": "<span class='hl'>Nick Listeleri</span>",
 "lead": "Kime, hangi dile, hangi tarza? Aradığın listeyi aşağıda bul: Türkçe, İngilizce, kız, erkek, kısa ve anlamlı nicklerin hepsi özgün olarak hazırlandı.",
 "tool": "lists",
 "cfg": {},
 "intro": [
   "<p>İyi bir nick, sahibini anlatır. Bu sayfada altı farklı liste var; her biri kendi zevkine göre seçilmiş isimlerden oluşur. Listelerdeki isimler şekilli halleriyle sunulur ve tek tıkla kopyalanır. Dilersen ismi <a href='index.html'>ana üretece</a> yapıştırıp onlarca farklı stilde yeniden üretebilirsin.</p>",
 ],
 "sections": [
   ("Türkçe Nickler",
    "<div data-nick-list='YalnızKurt|Karaşahin|Bozkurt|AnadoluAslanı|GeceNöbeti|Demirci|KuzeyYıldızı|SessizYolcu' data-list-styles='bold,sansbold' data-list-wraps='star,none,crown'></div>"),
   ("İngilizce Nickler",
    "<div data-nick-list='NightWolf|SilentStorm|IronGhost|DarkLegend|ShadowFox|IceBreaker|LoneRanger|StormRider' data-list-styles='sansbold,mono,bold' data-list-wraps='arrow,none,bolt'></div>"),
   ("Kız Oyun Nickleri",
    "<div data-nick-list='AyKızı|PembeKabus|YıldızPerisi|GeceKelebeği|ŞekerKraliçe|RüzgarKızı|İnciTanesi|MorBulut' data-list-styles='script,boldscript' data-list-wraps='flower,heart,spark'></div>"),
   ("Erkek Oyun Nickleri",
    "<div data-nick-list='DemirAdam|KurtSürü Lideri|GeceKomutanı|SavaşMakinesi|KralAvcısı|SertÇocuk|YıkımEkibi|SonSamuray' data-list-styles='bold,fraktur' data-list-wraps='crown,bolt,none'></div>"),
   ("Kısa Havalı Nickler",
    "<div data-nick-list='As|Zor|Tek|Vur|Kaos|Efsane|Usta|Rex' data-list-styles='negsquared,squared,circled' data-list-wraps='none,star'></div>"),
   ("Anlamlı Nickler",
    "<div data-nick-list='Sabır|UmutYolcusu|Cesaret|BilgeBaykuş|Sadakat|ÖzgürRuh|Merhamet|KaderAvcısı' data-list-styles='italic,boldscript,sansitalic' data-list-wraps='moon,flower,none'></div>"),
 ],
 "faqs": [
   ("Türkçe nick mi İngilizce nick mi daha havalı?",
    "Bu, oynadığın kitleye bağlı: Türkiye sunucularında Türkçe nick hem anlam hem akılda kalıcılık olarak öne çıkar; uluslararası sunucularda İngilizce nick daha evrenseldir. İkisini karıştıran (ör. Türkçe kelime + İngilizce ek) isimler de çok tutulur."),
   ("Kız nickleri neden daha zarif stillerde sunuluyor?",
    "Listelerdeki stil eşleşmeleri zevke göre seçildi; ama hiçbir kural yok: Beğendiğin herhangi bir ismi istediğin stilde kullanabilirsin. Üreteçte stili değiştirmen yeterli."),
   ("Anlamlı nickler için kelimeyi nereden bulabilirim?",
    "Seni anlatan bir duygu ya da erdemle başla: sabır, cesaret, umut, bilgelik... Sonra yanına bir imge ekle (yolcu, muhafız, avcı). Kendi anlamlı nickini kurmak, hazır almaktan daha kalıcıdır."),
   ("Kısa nicklerin avantajı nedir?",
    "Karakter sınırı olan oyunlara (Free Fire 12, PUBG 14) rahat sığarlar, kill ekranında hızlı okunurlar ve sözlü iletişimde söylemesi kolaydır."),
   ("Listedeki nick dolu çıkarsa ne yaparım?",
    "Sonuna ★, 彡 gibi kısa bir sembol ya da tek rakam eklemek genelde benzersizlik sağlar. Karakter sınırını aşmamaya dikkat et."),
 ],
},

# ============================================================ 22. KLAN İSİMLERİ
{
 "slug": "klan-isimleri", "file": "klan-isimleri.html",
 "title": "Klan İsimleri — Şekilli Klan Adları ve Klan Etiketi Oluşturucu",
 "desc": "Klan isimleri ve önerileri: güçlü, komik ve havalı klan adları, klan etiketi (tag) oluşturucu ile PUBG ve diğer oyunlar için şekilli klan isimleri.",
 "h1": "<span class='hl'>Klan İsimleri</span> ve Etiket Oluşturucu",
 "lead": "Klanın, adıyla anılır. Aşağıdaki mini araçla klan etiketini şekillendir; listelerden de klanına yakışan güçlü bir isim seç.",
 "tool": "clan",
 "cfg": {},
 "intro": [
   "<p>Klan etiketi (tag), üye nicklerinin önünde taşınan kısa imzadır; klan ismi ise ekibin kimliğidir. İyi bir klan adı kısa söylenir, yazması kolaydır ve rakibe gözdağı verir. Bu sayfada önce etiket aracını, sonra da farklı tarzlarda klan ismi listelerini bulacaksın.</p>",
 ],
 "sections": [
   ("Güçlü Klan İsimleri",
    "<div data-nick-list='KaranlıkLejyon|GeceMuhafızları|DemirYumruklar|Yıkılmazlar|FırtınaBirliği|Son Kale|KurtSürüsü|ŞimşekOrdusu' data-list-styles='bold,fraktur,sansbold' data-list-wraps='royal,crown,cross'></div>"),
   ("Eğlenceli Klan İsimleri",
    "<div data-nick-list='ÇayDemleyenler|PingMağdurları|SonKurşunKulübü|KampçılarBirliği|ŞanslıNooblar|GeceAtıştıranlar|LagDostları|KutudanÇıkanlar' data-list-styles='sansbold,bold' data-list-wraps='flower,star,none'></div>"),
   ("Klan İsmi Seçerken",
    "<ul>"
    "<li><strong>Söylenebilirlik:</strong> Sesli sohbette tek nefeste söylenebilen isimler turnuvalarda avantajdır.</li>"
    "<li><strong>Yazılabilirlik:</strong> Etiketin klavye ile kolay yazılması, üyelerin etiketini doğru taşımasını sağlar.</li>"
    "<li><strong>Esneklik:</strong> Tek bir oyuna kilitlenmeyen isimler, klanın başka oyunlara taşınmasını kolaylaştırır.</li>"
    "<li><strong>Benzersizlik:</strong> Seçtiğin ismi oyun içinde arat; aynı isimde büyük bir klan varsa küçük bir ek ile farklılaştır.</li>"
    "</ul>"),
 ],
 "faqs": [
   ("Klan etiketi kaç harf olmalı?",
    "Genelde 2-5 harf idealdir. PUBG gibi sınırlı isim alanlarında etiket + nick toplam 14 karakteri geçmemeli."),
   ("Etiket oluşturucu nasıl çalışır?",
    "Üstteki kutuya klan kısaltmanı yaz; şablonlar anında üretilir. Beğendiğin etikete tıklayıp kopyala ve nickinin önünde kullan."),
   ("Klan ismimi şekilli harflerle yazabilir miyim?",
    "Oyunun klan adı alanı Unicode destekliyorsa evet. Listelerdeki isimler şekilli sunulur; desteklemeyen oyunlarda düz halini kullan."),
   ("Aynı etiketi tüm üyeler nasıl taşır?",
    "Etiketi bir kez belirleyip üyelerin nicklerinin başına aynı biçimde eklemesi yeterli. Biçim birliği (aynı çerçeve, aynı büyük/küçük harf) profesyonel görüntü verir."),
   ("Klan adını sonra değiştirmek zor mu?",
    "Çoğu oyunda klan adı değişikliği kart ya da oyun parası gerektirir. Bu yüzden ismi burada dikkatle seçip ekibinle oylamak en sağlıklısıdır."),
 ],
},

# ============================================================ 23. REHBER
{
 "slug": "rehber", "file": "rehber.html",
 "title": "Blog — Şekilli Nick Rehberi ve İpuçları",
 "desc": "NickUstası Blog: şekilli nick nasıl yapılır, kutu (□) sorunu çözümleri, ban kuralları, hata vermeyen semboller, PUBG nick seçimi ve Instagram biyografi fikirleri.",
 "h1": "Şekilli Nick <span class='hl'>Blogu</span>",
 "lead": "Rehberler, sorun çözümleri ve fikir yazıları: şekilli nicki doğru yapmanın, kutu sorunundan kurtulmanın ve her platformda öne çıkmanın yolları.",
 "badge": "Blog",
 "tool": "",
 "cfg": {},
 "intro": [
 "<p>Burada araçların ötesine geçen soruların cevapları var: Şekilli nick tam olarak nasıl yapılır, nick neden bazı telefonlarda kutu kutu görünür, oyunlar şekilli isme nasıl bakar ve hangi semboller her cihazda sorunsuz görünür? Her yazı ilgili araca tek tıkla bağlanır; okurken hemen uygulayabilirsin.</p>"
 "<div class='card-grid'><a class='page-card blog-card' href='sekilli-nick-nasil-yapilir.html'><span class='bc-cat'>Rehber</span><span class='pc-title'>Şekilli Nick Nasıl Yapılır?</span><span class='pc-desc'>İsim seçiminden kopyalamaya, adım adım şekilli nick üretimi ve yeni başlayanların hataları.</span><span class='bc-meta'>4 dk okuma</span></a><a class='page-card blog-card' href='sekilli-nick-neden-kutu-gorunuyor.html'><span class='bc-cat'>Sorun Çözümü</span><span class='pc-title'>Nick Neden Kutu Görünüyor?</span><span class='pc-desc'>Kare (□) sorununun gerçek nedeni ve kesin çözüm yolları.</span><span class='bc-meta'>3 dk okuma</span></a><a class='page-card blog-card' href='sekilli-nick-ban-sebebi-mi.html'><span class='bc-cat'>Oyun Kuralları</span><span class='pc-title'>Şekilli Nick Ban Sebebi mi?</span><span class='pc-desc'>Oyunların isim kuralları biçime değil içeriğe bakar; yaptırım gören durumlar ve güvenli kullanım.</span><span class='bc-meta'>3 dk okuma</span></a><a class='page-card blog-card' href='hata-vermeyen-sekilli-semboller.html'><span class='bc-cat'>Semboller</span><span class='pc-title'>Hata Vermeyen Şekilli Semboller</span><span class='pc-desc'>Her cihazda ve oyunda görünen güvenli sembol grupları ve seçim kuralları.</span><span class='bc-meta'>4 dk okuma</span></a><a class='page-card blog-card' href='pubg-havali-nick-secme-rehberi.html'><span class='bc-cat'>PUBG Mobile</span><span class='pc-title'>PUBG İçin Havalı Nick Seçme Rehberi</span><span class='pc-desc'>14 karakter sınırını akıllıca kullan; isim değiştirme kartını boşa harcama.</span><span class='bc-meta'>5 dk okuma</span></a><a class='page-card blog-card' href='instagram-biyografi-sekilli-yazi-fikirleri.html'><span class='bc-cat'>Instagram</span><span class='pc-title'>Instagram Biyografisi İçin Şekilli Yazı Fikirleri</span><span class='pc-desc'>150 karakterlik biyografini satır satır planla, stille öne çık.</span><span class='bc-meta'>5 dk okuma</span></a></div>",
],
 "sections": [
 ("Yazılar Nasıl Sıralanıyor?",
 "<p>Yazılar konuya göre etiketlenir: <strong>Rehber</strong> yazıları adım adım anlatır, <strong>Sorun Çözümü</strong> yazıları kutu sorunu gibi can sıkıcı dertleri giderir; oyun ve platform yazıları ise tek bir alana derinlemesine odaklanır. Yeni başlıyorsan önerimiz net: önce <a href='sekilli-nick-nasil-yapilir.html'>Şekilli Nick Nasıl Yapılır?</a> yazısıyla başla, sonra ihtiyacına göre diğerlerine geç.</p>"),
],
 "faqs": [
   ("Şekilli nick yapmak için uygulama indirmek gerekir mi?",
    "Hayır. Bu sitedeki üreteç tarayıcıda çalışır; telefondan da bilgisayardan da aynı şekilde kullanılır."),
   ("Kutu görünen nick karşı tarafta da kutu mu?",
    "Şart değil. Kutu, bakan cihazın yazı tipine bağlıdır; güncel bir telefonda düzgün görünebilir. İki cihazda da kontrol etmek en doğrusu."),
   ("Oyun ismimi reddederse ne yapmalıyım?",
    "Önce süslemeleri kaldırıp yalnızca şekilli harflerle dene; yine olmazsa stili sadeleştir (kalın veya modern). Sorun genelde tek bir karakterdedir; sembolleri tek tek eleyerek bulabilirsin."),
   ("Şekilli nick ekran okuyucularda nasıl duyulur?",
    "Bazı ekran okuyucular şekilli karakterleri harf harf ya da anlamsız okuyabilir. Erişilebilirlik önemliyse (ör. resmî bir topluluk) sade isim tercih et."),
   ("Nickimin aynısını biri kopyalarsa ne olur?",
    "Kullanıcı adı benzersizliği platform tarafından korunur; görünen adın kopyalanması ise teknik olarak engellenemez. Özgün bir kelime + sana özel bir sembol kombinasyonu, taklidi zorlaştırır."),
 ],
},


# ============================================================ 24. BLOG — NASIL YAPILIR
{
"slug": "sekilli-nick-nasil-yapilir", "file": "sekilli-nick-nasil-yapilir.html",
"title": "Şekilli Nick Nasıl Yapılır? — Adım Adım Şekilli Nick Yapma Rehberi",
"desc": "Şekilli nick nasıl yapılır? Adım adım anlatım: isim seçimi, üreteç kullanımı, süsleme seçimi, karakter sınırı kontrolü ve kopyalama. Türkçe harf destekli şekilli nick rehberi.",
"h1": "Şekilli Nick <span class='hl'>Nasıl Yapılır?</span>",
"lead": "Bir isim fikrinden, lobide herkesin fark ettiği bir nicke: şekilli nick yapmanın tüm adımlarını püf noktalarıyla anlatıyoruz.",
"badge": "Blog · Başlangıç Rehberi",
"cfg": {},
"intro": [
"<p>Şekilli nick yapmak, göründüğünden çok daha kolay: Uygulama indirmek yok, üyelik yok, teknik bilgi yok. Tek ihtiyacın bir isim fikri ve birkaç dakika. Bu yazıda süreci sıfırdan sona kadar, her adımda nelere dikkat edeceğini de söyleyerek anlatıyoruz.</p>",
],
"sections": [
("Adım Adım Şekilli Nick Yapımı", "<p>Şekilli nick yapmak için yalnızca üç şeye ihtiyacın var: Bir isim fikri, bu sitedeki üreteç ve kopyala-yapıştır. İşte adım adım süreç:</p><ul><li><strong>1. İsmini belirle:</strong> Kendi adın, bir lakap ya da tamamen yeni bir kelime. Kısa isimler her alanda avantajlıdır.</li><li><strong>2. Üretece yaz:</strong> <a href='index.html'>Ana sayfadaki</a> kutuya ismini yaz; 100'den fazla stil anında üretilir.</li><li><strong>3. Süslemeyi seç:</strong> Süsleyici (yıldız, taç, çerçeve) ve ayraç menüleriyle tarzını kişiselleştir.</li><li><strong>4. Karakter sınırını kontrol et:</strong> Oyununun sınırı varsa ilgili sayfadaki sayaçlı aracı kullan (ör. <a href='pubg-sekilli-nick.html'>PUBG 14</a>, <a href='free-fire-sekilli-nick.html'>Free Fire 12</a>).</li><li><strong>5. Kopyala ve yapıştır:</strong> Karta tıkla; nick panona gider. Oyunun isim alanına yapıştır ve onayla.</li><li><strong>6. Önizlemede kontrol et:</strong> Değişikliği kalıcı yapmadan önce profil ve lobi görünümüne bak; kutu görünen karakter varsa stili değiştir.</li></ul>"),
("Yeni Başlayanların Yaptığı 5 Hata",
"<p>Adımlar basit; ama şu hatalar sonucu baştan bozar:</p>"
"<ul>"
"<li><strong>Çok fazla sembol:</strong> Nick okunmaz hâle gelir. Bir çerçeve ve bir stil çoğu zaman yeterlidir.</li>"
"<li><strong>Sınırı hesaba katmamak:</strong> Oyunun karakter sınırını aşan nick ya kesilir ya da reddedilir.</li>"
"<li><strong>Nadir stillerle başlamak:</strong> İlk denemede en yaygın stilleri seç; kutu riskini azaltırsın.</li>"
"<li><strong>Başkasının nickini kopyalamak:</strong> Özgün bir kelime her zaman daha akılda kalıcıdır ve taklit sorunu yaşamazsın.</li>"
"<li><strong>Önizlemeden onaylamak:</strong> Profili görmeden ismi kalıcı yapma; kutu görünen karakter varsa hemen değiştir.</li>"
"</ul>"),
("Şimdi Sıra Sende",
"<div class='info-box'><p>Anlatım bitti, uygulama başlasın: <a href='index.html'>Şekilli nick oluşturucuya</a> ismini yaz, 110'dan fazla stil arasından beğendiğini tek tıkla kopyala. Karakter sınırı olan bir oyunda oynuyorsan <a href='pubg-sekilli-nick.html'>PUBG aracı</a> gibi sayaçlı sayfaları kullan.</p></div>"),
],
"faqs": [
("Şekilli nick yapmak ne kadar sürer?",
"İsim fikrin hazırsa birkaç dakika. En çok zaman, 110'dan fazla stil arasından seçim yapmakta geçer; o da işin keyifli kısmıdır."),
("Telefonda da aynı adımlar geçerli mi?",
"Evet. Araç tarayıcıda çalışır; telefon, tablet ve bilgisayarda adımlar birebir aynıdır."),
("Yaptığım nicki sonra değiştirebilir miyim?",
"Bu sayfada metni yeniden yazıp yeni sonucu kopyalaman yeterli. Oyundaki değişim ise o oyunun kurallarına bağlıdır; bazı oyunlar isim değişimi için kart ister."),
],
},

# ============================================================ 25. BLOG — KUTU SORUNU
{
"slug": "sekilli-nick-neden-kutu-gorunuyor", "file": "sekilli-nick-neden-kutu-gorunuyor.html",
"title": "Şekilli Nick Neden Kutu (□) Görünüyor? — Nedeni ve Kesin Çözümleri",
"desc": "Nickin neden kutu kutu (□) görünüyor? Yazı tipi ve glif eksikliğinin açıklaması, en az risk taşıyan stiller ve kutu sorununu çözmenin yolları.",
"h1": "Nick Neden <span class='hl'>Kutu Görünüyor?</span>",
"lead": "Nickin senin telefonda düzgün, arkadaşınınkinde kutu kutu mu? Sorun nickinde değil, bakan cihazın yazı tipinde. İşte nedeni ve çözüm yolları.",
"badge": "Blog · Sorun Çözümü",
"cfg": {},
"intro": [
"<p>Kutu sorunu, şekilli nick kullanan herkesin en az bir kez yaşadığı derttir: Özenle seçtiğin nick, başka bir ekranda yan yana boş karelere dönüşür. İyi haber şu: Nickin bozuk değil ve sorun çözülebilir. Önce nedenini anlayalım.</p>",
],
"sections": [
("Kutu Sorununun Nedeni ve Çözümü", "<p>Kutu sorunu, karakterin kendisinden değil, onu göstermeye çalışan cihazın yazı tipinden kaynaklanır. Her karakterin ekranda çizilebilmesi için yazı tipinde o karakterin resmi (glif) bulunmalıdır. Telefonun ya da oyunun yazı tipi, seçtiğin karakteri tanımıyorsa yerine boş bir kutu (□), bazen de soru işareti gösterir.</p><p><strong>Çözüm yolları:</strong></p><ul><li>Daha yaygın stillere dön: Kalın, modern, balon ve el yazısı stilleri neredeyse her yazı tipinde bulunur.</li><li>Nadir sembolleri ele: Özellikle sonradan eklenen süs işaretleri eski cihazlarda eksik olabilir; <a href='sekilli-semboller.html'>sembol kütüphanesindeki</a> temel kategorilerle yetin.</li><li>Cihazını güncelle: Telefon güncellemeleri yazı tiplerini de genişletir.</li><li>Şunu bil: Kutu, senin cihazında görünüyor olabilir ama arkadaşının güncel telefonunda nickin gayet düzgün görünebilir. Karar vermeden önce ikinci bir cihazda kontrol et.</li></ul>"),
("Hangi Stiller En Az Kutu Riski Taşır?",
"<p>Stiller arasında görünürlük farkı büyüktür. Genel sıralama şöyle:</p>"
"<ul>"
"<li><strong>En güvenli:</strong> Kalın ve modern (sans) stiller. Neredeyse her yazı tipinde karşılığı vardır.</li>"
"<li><strong>Güvenli:</strong> Balon, kare ve daktilo stilleri. Yaygın cihazların tamamına yakını destekler.</li>"
"<li><strong>Orta risk:</strong> Gotik ve çift çizgili stiller. Güncel telefonlarda sorunsuz, eski cihazlarda yer yer eksik olabilir.</li>"
"<li><strong>Dikkat isteyen:</strong> Az kullanılan süs blokları ve çok yeni semboller. Bunları nickin ana gövdesinde değil, tek bir vurgu işareti olarak kullan.</li>"
"</ul>"
"<p>Şüphede kaldığında kural basit: Nicki önce kalın stilde kur, görünürlüğünden emin olduktan sonra süslemeyi ekle.</p>"),
("Hemen Dene",
"<div class='info-box'><p>Kutu riski en düşük stillerle başlamak için <a href='index.html'>ana üreteci</a> aç ve önce Kalın ile Modern sonuçlara bak. Sembol seçiminde de <a href='hata-vermeyen-sekilli-semboller.html'>hata vermeyen semboller</a> yazısındaki güvenli listeleri kullan.</p></div>"),
],
"faqs": [
("Kutu görünen nick karşı tarafta da kutu mu?",
"Şart değil. Kutu, bakan cihazın yazı tipine bağlıdır; güncel bir telefonda düzgün görünebilir. Karar vermeden önce ikinci bir cihazda kontrol etmek en doğrusudur."),
("Kutu sorununu çözmek için nicki baştan mı yapmalıyım?",
"Hayır. Aynı ismi daha yaygın bir stilde yeniden üretmen yeterli; metin aynı kalır, yalnızca harflerin stili sadeleşir."),
("Oyunun yazı tipini değiştirebilir miyim?",
"Çoğu oyunda hayır; yazı tipi oyuna gömülüdür. Değiştirebileceğin şey nickinin stilidir — bu yüzden çözüm her zaman sadeleşmekten geçer."),
],
},

# ============================================================ 26. BLOG — BAN SORUNU
{
"slug": "sekilli-nick-ban-sebebi-mi", "file": "sekilli-nick-ban-sebebi-mi.html",
"title": "Şekilli Nick Ban Sebebi mi? — Oyunlarda Güvenli İsim Kullanımı",
"desc": "Şekilli nick kullanmak ban sebebi midir? Oyunların isim kuralları, yaptırım gören durumlar ve güvenle şekilli nick kullanmanın yolları.",
"h1": "Şekilli Nick <span class='hl'>Ban Sebebi mi?</span>",
"lead": "Kısa cevap: hayır — ama istisnalarıyla. Oyunların isim kurallarının biçime değil içeriğe baktığını ve hangi durumlarda yaptırım geldiğini tek tek açıklıyoruz.",
"badge": "Blog · Oyun Kuralları",
"cfg": {},
"intro": [
"<p>Bu soru, şekilli nick yapmadan önce herkesin aklından geçer: 'Ya hesabım ceza alırsa?' Rahat bir nefes al: Şekilli harfler, oyunların teknik olarak desteklediği standart karakterlerdir. Yaptırımlar harflerin süsüne değil, ismin taşıdığı anlama uygulanır. Ayrıntılar aşağıda.</p>",
],
"sections": [
("Kurallar Biçime Değil, İçeriğe Bakar", '<p>Kısa cevap: Şekilli harflerin kendisi ban sebebi değildir. Oyunların isim kuralları biçime değil, içeriğe bakar. Şu durumlarda isim şekilli de olsa yaptırım görebilirsin:</p><ul><li>Küfür, hakaret veya uygunsuz içerik taşıyan isimler</li><li>Başka bir oyuncuyu, yayıncıyı ya da oyun görevlisini taklit eden isimler</li><li>Hile, satış veya reklam çağrışımı yapan isimler</li><li>Oyunun teknik olarak kabul etmediği karakterlerle sistemi zorlayan isimler (bu durumda genelde isim reddedilir, ban gelmez)</li></ul><p>Kurallara uygun, özgün bir isim seçtiğin sürece şekilli nickini gönül rahatlığıyla kullanabilirsin. Şikâyet durumunda oyunlar genelde önce isim sıfırlama ister; tekrarı halinde yaptırımlar ağırlaşır. Bu yüzden ilk seçimde dikkatli olmak her zaman en iyisidir.</p>'),
("Güvenli Bölgede Kalmak İçin Kontrol Listesi",
"<ul>"
"<li>İsminde küfür, hakaret veya müstehcen gönderme yok mu?</li>"
"<li>Başka bir oyuncuyu, yayıncıyı ya da oyun ekibini taklit etmiyor musun?</li>"
"<li>Hile, hesap satışı veya reklam çağrışımı taşımıyor mu?</li>"
"<li>Oyunun kabul etmediği tek bir karakter için ısrar etmiyor musun? (Reddedilen isim, genelde ban değil yalnızca kayıttır.)</li>"
"<li>Klan etiketin ve nickin, topluluk kurallarına uygun mu?</li>"
"</ul>"
"<p>Beş soruya da 'evet, temiz' diyorsan şekilli nickini gönül rahatlığıyla kullanabilirsin.</p>"),
("Nickini Güvenle Yap",
"<div class='info-box'><p>Kurallara uygun, özgün nickini şimdi üret: <a href='index.html'>Şekilli nick oluşturucu</a> tüm stilleri ücretsiz sunar. Sınırı olan oyunlar için <a href='pubg-sekilli-nick.html'>PUBG</a> ve <a href='free-fire-sekilli-nick.html'>Free Fire</a> sayfalarındaki sayaçlı araçlar işini kolaylaştırır.</p></div>"),
],
"faqs": [
("İsmim şikâyet edilirse ne olur?",
"Oyunlar genelde önce isim sıfırlama veya değiştirme zorunluluğu uygular. Tekrarı ve ağır içerik hâlinde yaptırımlar ağırlaşır; bu yüzden ilk seçimde dikkatli olmak en iyisidir."),
("Şekilli harfler hile sayılır mı?",
"Hayır. Şekilli harfler oyunun kendi isim alanına yazılan standart Unicode karakterlerdir; oyuna dışarıdan müdahale eden hiçbir şey yoktur."),
("Eski, düz nickime dönebilir miyim?",
"Elbette. İsim değiştirme adımları oyundan oyuna değişir; bazıları kart ister, bazıları belirli sürelerde ücretsiz hak tanır."),
],
},

# ============================================================ 27. BLOG — GÜVENLİ SEMBOLLER
{
"slug": "hata-vermeyen-sekilli-semboller", "file": "hata-vermeyen-sekilli-semboller.html",
"title": "Hata Vermeyen Şekilli Semboller — Her Oyunda Çalışan Güvenli Semboller",
"desc": "Hata vermeyen şekilli semboller hangileri? Her cihazda ve oyunda görünen güvenli sembol grupları, destek düzeyleri ve sembol seçim kuralları.",
"h1": "Hata Vermeyen <span class='hl'>Şekilli Semboller</span>",
"lead": "Sembol seçiminde tek kural: yaygın olan kazanır. Her oyunda ve cihazda çalışan güvenli sembol gruplarını ve uzak durman gereken riskli blokları derledik.",
"badge": "Blog · Semboller",
"cfg": {},
"intro": [
"<p>Bir sembolün 'hata vermemesi', teknik olarak şu anlama gelir: O karakter, karşındaki kişinin cihazındaki yazı tipinde de bulunur ve oyunun isim filtresi tarafından engellenmez. İki şartı da sağlayan semboller, on yıllardır her sistemde olanlardır. İşte o güvenli limanlar.</p>",
],
"sections": [
("Seçimin Altın Kuralları", "<p>'Hata vermeyen sembol' arayışının özü basittir: Ne kadar eski ve yaygın bir karakter seçersen, o kadar çok cihazda görünür. İşte seçim kuralları:</p><ul><li><strong>Temel geometrik ve kart sembolleri</strong> (★ ☆ ♠ ♣ ♥ ♦) 1990'lardan beri her yazı tipindedir.</li><li><strong>Satranç taşları</strong> (♔–♟) oyun kültürünün ortak dili olduğu için güvenli limandır.</li><li><strong>Basit oklar ve işaretler</strong> (→ ➢ •) yaygın destek görür.</li><li><strong>Dikkat isteyenler:</strong> Az bilinen dillerin harfleri, çok yeni emoji ve süs blokları eski cihazlarda kutu olabilir.</li></ul><p>Bu sitenin <a href='pubg-sekilli-nick.html'>PUBG sayfasındaki güvenli semboller</a> bölümü ve <a href='sekilli-semboller.html'>ana kütüphanenin</a> ilk kategorileri, güvenli seçimlerden derlenmiştir. Yine de hiçbir listenin %100 garanti veremeyeceğini unutma: Oyunun güncel sürümünde, kendi cihazında küçük bir deneme yapmak en kesin testtir.</p>"),
("Güvenli Sembol Grupları ve Destek Düzeyleri",
"<table class='limit-table'>"
"<tr><th>Grup</th><th>Örnekler</th><th>Destek Düzeyi</th></tr>"
"<tr><td>Kart sembolleri</td><td>★ ☆ ♠ ♣ ♥ ♦</td><td>Çok yüksek</td></tr>"
"<tr><td>Satranç taşları</td><td>♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛</td><td>Çok yüksek</td></tr>"
"<tr><td>Oklar ve işaretler</td><td>→ ➢ • ✚ ✖</td><td>Yüksek</td></tr>"
"<tr><td>Çerçeveler</td><td>『 』 〘 〙</td><td>Yüksek (oyunlarda yaygın)</td></tr>"
"<tr><td>Temel süsler</td><td>✿ ❀ ☾ ☀ ♪</td><td>Yüksek</td></tr>"
"</table>"
"<p>Tablodaki gruplar, <a href='sekilli-semboller.html'>sembol kütüphanemizin</a> ilk kategorilerinde tek tıkla kopyalanabilir. Yeni ve az bilinen bloklardan gelen semboller ise bu listede bilinçli olarak yok: Onlar güzel olabilir ama her ekranda görünmezler.</p>"),
("Sembollerini Seç",
"<div class='info-box'><p>Hazırsan <a href='sekilli-semboller.html'>şekilli semboller kütüphanesinden</a> güvenli sembollerini kopyala; PUBG için ayrıca hazırlanmış listeye <a href='pubg-sekilli-nick.html'>PUBG sayfasından</a> ulaş. Kutu sorununun nedenini merak ediyorsan <a href='sekilli-nick-neden-kutu-gorunuyor.html'>kutu sorunu yazısına</a> bak.</p></div>"),
],
"faqs": [
("Bir sembolün güvenli olduğunu nasıl test ederim?",
"En kesin test, sembolü oyunun isim alanında deneyip profil önizlemesine bakmak ve mümkünse ikinci bir cihazdan kontrol etmektir."),
("Emoji sembol olarak güvenli mi?",
"Renkli emojiler çoğu oyunun isim alanında ya reddedilir ya da kutu görünür. İsimlerde metin sembollerini, emojiyi ise biyografi ve mesaj alanlarında kullan."),
],
},

# ============================================================ 28. BLOG — PUBG NICK SEÇİMİ
{
"slug": "pubg-havali-nick-secme-rehberi", "file": "pubg-havali-nick-secme-rehberi.html",
"title": "PUBG Mobile İçin Havalı Nick Seçme Rehberi — Kurallar, Örnekler, İpuçları",
"desc": "PUBG Mobile için havalı nick nasıl seçilir? 14 karakter sınırını akıllıca kullanma, klan etiketi uyumu, güvenli semboller ve örnek nick tarzları. İsim kartını harcamadan önce oku.",
"h1": "PUBG Mobile İçin <span class='hl'>Havalı Nick</span> Seçme Rehberi",
"lead": "İsim değiştirme kartı değerli; onu harcamadan önce doğru nicki bul. PUBG'ye özel kurallar, sınırlar ve örneklerle havalı nick seçmenin tam rehberi.",
"badge": "Blog · PUBG Mobile",
"cfg": {},
"intro": [
"<p>PUBG Mobile'da nickin, senin sahadaki imzan: Lobide, kill mesajlarında ve klan listesinde herkes seni onunla tanır. Üstelik isim değişimi karta bağlı olduğu için 'sonra düzeltirim' deme lüksün pek yok. Bu rehber, kartı yakmadan önce doğru ismi bulman için yazıldı.</p>"
"<p>Rehberi iki parçalı düşün: Önce seçimin kurallarını öğreneceksin, sonra örnekler üzerinden kendi tarzını bulacaksın. En sonda da tek tıkla üreten araca geçeceksin.</p>",
],
"sections": [
("İyi Bir PUBG Nickinin 5 Özelliği",
"<ul>"
"<li><strong>Kısa ve net:</strong> 14 karakter sınırında her harf değerli. Uzun cümleler yerine tek güçlü kelime veya iki kelimelik vurucu bir birleşim seç.</li>"
"<li><strong>Okunabilir:</strong> Kill mesajında bir bakışta okunamayan nick, akılda da kalmaz. Süslemeyi gövdeye değil, başa ve sona sakla.</li>"
"<li><strong>Söylenebilir:</strong> Takımın sesli sohbette sana adınla seslenecek. Telaffuzu zor bir nick, pratikte dezavantajdır.</li>"
"<li><strong>Özgün:</strong> Ünlü oyuncuların nicklerinin kopyası hem taklit sayılır hem de arama ve arkadaş eklemede karışıklık çıkarır.</li>"
"<li><strong>Klanla uyumlu:</strong> Klan etiketiyle yan yana geldiğinde bütün görünmeli; etiketi nickin parçası gibi planla.</li>"
"</ul>"),
("14 Karakter Sınırını Akıllıca Kullanmak",
"<p>Sınır, boşluklar ve semboller dahil her karakteri sayar. Bu yüzden önce çekirdek kelimeni belirle, süslemeyi en sona bırak. Basit bir bütçe işe yarar: 10-11 karakter kelimeye, 2-3 karakter süslemeye. Örneğin iki işaretlik bir çerçeve, kelimeni daraltmadan nicki tamamlar.</p>"
"<p>Bir de görünmez boşluk hilesi var: Kelimeler arasına normal boşluk yerine <a href='bosluk-kopyala.html'>görünmez boşluk</a> koymak, ismin tek parça gibi görünmesini sağlar ve bazı filtreleri aşar. Kullanacaksan ölçülü kullan; aşırı görünmez karakter, ismin kopyalanmasını ve arkadaşlarının seni bulmasını zorlaştırır.</p>"
"<p>Sayacı elinde tutmak için <a href='pubg-sekilli-nick.html'>PUBG şekilli nick aracı</a> sınırı aşan sonuçları otomatik işaretler; kartı harcamadan önce final nickini orada dene.</p>"),
("Örnek Nick Tarzları",
"<p>Aşağıdaki çekirdek isimler, tarzları görmen için birkaç stilde üretildi. Kartlara tıklayarak kopyalayabilirsin; ama asıl önerimiz, bunları ilham alıp kendi kelimeni üretmen:</p>"
"<div data-nick-list='KeskinAvcı|GeceKurdu|SonKurşun|AslanYürek|KaraKaplan|SessizÖlüm' data-list-styles='bold,fraktur,sansbold' data-list-wraps='none,crown,star'></div>"
"<p>Tarz olarak üç ana yol var: <strong>Tek kelime gücü</strong> (kısa ve sert), <strong>ikili birleşim</strong> (sıfat + isim) ve <strong>klan ön ekli</strong> düzen. Hangisini seçersen seç, lobide küçük boyutta da okunup okunmadığını kontrol et.</p>"),
("Klan Etiketiyle Uyum",
"<p>Klan etiketi, nickin ayrılmaz parçasıdır. Etiket kalın stildeyse nicki daha sade bir stilde tutmak denge kurar; ikisi de yoğun olursa isim kalabalıklaşır. Etiket şablonları ve hazır klan adları için <a href='klan-isimleri.html'>klan isimleri sayfasına</a> bak; hazır nick listeleri için de <a href='havali-nickler.html'>havalı nickler</a> bölümünü karıştır.</p>"),
("Kartı Yakmadan Önce",
"<div class='info-box'><p>Final adayını belirlediysen iş bitmedi say: <a href='pubg-sekilli-nick.html'>PUBG aracında</a> nickini üret, karakter sayacından geçir, lobide görüneceği hâliyle son kez bak. Beğenmezsen kart hâlâ cebinde.</p></div>"),
],
"faqs": [
("PUBG nickinde Türkçe harf kullanabilir miyim?",
"Şekilli stiller Türkçe harflerin Unicode karşılıklarını kullanır ve bu sitedeki üreteç ğ, ü, ş, ı, ö, ç ve İ harflerini bozmadan üretir. Yine de kartı kullanmadan önce oyun içi önizlemede son hâlini kontrol et."),
("İsim değiştirme kartı olmadan nick değişir mi?",
"Hayır. PUBG Mobile'da isim değişimi kart gerektirir; kart, görevler, etkinlikler ve mağaza yoluyla edinilebilir. Bu yüzden seçim aşamasını aceleye getirme."),
("Aynı görünen adı iki kişi kullanabilir mi?",
"Görünen ad benzerliği teknik olarak mümkün olsa da her hesabın benzersiz bir kimliği (ID) vardır. Arkadaş eklerken karışıklığı önlemek için ID ile ekleme yapmak en sağlıklısıdır."),
],
},

# ============================================================ 29. BLOG — INSTAGRAM BİO
{
"slug": "instagram-biyografi-sekilli-yazi-fikirleri", "file": "instagram-biyografi-sekilli-yazi-fikirleri.html",
"title": "Instagram Biyografisi İçin Şekilli Yazı Fikirleri — Satır Satır Bio Rehberi",
"desc": "Instagram biyografin için şekilli yazı fikirleri: isim alanı ve bio için stil önerileri, 150 karakter sınırı planlaması ve hazır bio şablonları.",
"h1": "Instagram Biyografisi İçin <span class='hl'>Şekilli Yazı</span> Fikirleri",
"lead": "Biyografin, profilinin vitrini. 150 karakteri satır satır planlayıp şekilli yazıyla nasıl öne çıkaracağını, hazır fikirlerle gösteriyoruz.",
"badge": "Blog · Instagram",
"cfg": {},
"intro": [
"<p>Bir profile giren kişinin ilk baktığı yer biyografidir; kararını da çoğu zaman orada verir: Takip et ya da etme. Şekilli yazı, o birkaç satırda hem düzeni hem de karakteri aynı anda kurmanın en kolay yoludur. Bu yazıda biyografini bir vitrin gibi düzenlemeyi öğreneceksin.</p>"
"<p>Başlamadan önce en kritik ayrımı netleştirelim: Şekilli yazı, kullanıcı adında çalışmaz. Kullanıcı adı yalnızca düz harf, rakam, nokta ve alt çizgi kabul eder. Şekilli yazının alanı, görünen adın ve biyografi metnindir.</p>",
],
"sections": [
("Nerede Şekilli Yazı Çalışır, Nerede Çalışmaz?",
"<ul>"
"<li><strong>Kullanıcı adı (@...):</strong> Şekilli yazı çalışmaz; düz ve akılda kalıcı tut.</li>"
"<li><strong>Görünen ad (30 karakter):</strong> Şekilli yazı çalışır. Aramada da tarandığı için anahtar kelimeni (örn. mesleğin) düz yazıyla da geçirmen akıllıca olur.</li>"
"<li><strong>Biyografi (150 karakter):</strong> Şekilli yazının asıl sahnesi. Satır satır plan aşağıda.</li>"
"<li><strong>Öne çıkanlar ve gönderi açıklamaları:</strong> Başlıklarda şekilli vurgu kullanabilirsin; uzun metinde sade kal.</li>"
"</ul>"),
("Satır Satır Plan: 4 Satırlık Bio Formülü",
"<p>Mobilde düzenli görünen biyografiler genelde dört satırı geçmez. Kanıtlanmış formül:</p>"
"<ul>"
"<li><strong>1. satır — Kimsin:</strong> El yazısı stili zarif bir giriş yapar.</li>"
"<li><strong>2. satır — Ne yapıyorsun:</strong> Minik harf veya küçük büyük harf stili, satırı sakinleştirir.</li>"
"<li><strong>3. satır — Ayrıntın / kanıtın:</strong> Tek bir kalın vurgu; sayı veya unvan burada parlar.</li>"
"<li><strong>4. satır — Çağrı:</strong> İletişim veya yönlendirme; en sade stilde bırak ki tıklanabilir bilgi kaybolmasın.</li>"
"</ul>"
"<p>Satır başlarına <a href='sekilli-semboller.html'>sembol kütüphanesinden</a> tek bir küçük işaret koymak, listeyi okunaklı bir düzene sokar. Her satıra farklı işaret değil, aynı işareti tekrarlamak profesyonel görünür.</p>"),
("Hazır Bio Şablonları",
"<p>Aşağıdaki şablonları kendi bilgilerinle doldur, sonra <a href='instagram-sekilli-yazi.html'>Instagram şekilli yazı aracında</a> satırları stillendir:</p>"
"<div class='info-box'><p><strong>Kişisel profil:</strong><br>[İsmin — el yazısı]<br>[Bölümün · Şehrin — minik harf]<br>[Tek kelimelik motton — kalın]<br>[İletişim — sade]</p></div>"
"<div class='info-box'><p><strong>Küçük işletme:</strong><br>[İşletme adın — kalın]<br>[Ne sattığın / hizmetin — sade]<br>[Çalışma saatin · Şehrin — sade]<br>[Sipariş için DM — el yazısı]</p></div>"
"<div class='info-box'><p><strong>İçerik üretici:</strong><br>[İsmin — el yazısı]<br>[İçerik konun — minik harf]<br>[Yeni video günü — kalın]<br>[İş birliği e-postası — sade]</p></div>"),
("Okunabilirlik ve Kutu Riski",
"<p>Biyografi her telefonda açılır; yaşlı bir cihazda kutu görünen stil, özenini boşa çıkarır. Yoğun stilleri yalnızca ilk satırda kullan, geri kalanını yaygın stillerle kur. Kutu sorununun mantığını <a href='sekilli-nick-neden-kutu-gorunuyor.html'>kutu sorunu yazısında</a> ayrıntılı anlattık.</p>"),
("Biyografini Şimdi Kur",
"<div class='info-box'><p>Hazırsan <a href='instagram-sekilli-yazi.html'>Instagram şekilli yazı aracına</a> geç: Satırlarını yaz, stilleri seç, kopyala ve profiline yapıştır. Sembol lazım olursa <a href='sekilli-semboller.html'>kütüphane</a> tek tık uzağında.</p></div>"),
],
"faqs": [
("Şekilli yazı kullanıcı adımda neden olmuyor?",
"Çünkü kullanıcı adı, sistemin kimlik alanıdır ve yalnızca düz harf, rakam, nokta ve alt çizgiye izin verir. Şekilli yazı, görünen ad ve biyografi gibi serbest metin alanlarında çalışır."),
("Biyografide kaç satır kullanabilirim?",
"Enter ile istediğin kadar satır ayırabilirsin ama mobil görünümde dört satırın ötesi dağınık durur. 150 karakteri dört satıra bölmek en dengeli sonuç verir."),
("Şekilli biyografi aramada bulunmamı etkiler mi?",
"Arama; kullanıcı adını ve görünen adı tarar. Şekilli karakterler bazı aramalarda eşleşmeyebilir; bu yüzden mesleğin gibi anahtar kelimeleri görünen adında düz yazıyla da bulundurmak güvenli yoldur."),
],
},

# ============================================================ 30. HAKKIMIZDA
{
 "slug": "hakkimizda", "file": "hakkimizda.html",
 "title": "Hakkımızda — NickUstası",
 "desc": "NickUstası hakkında: Türkçe harfleri bozmayan, üyeliksiz ve tamamen tarayıcıda çalışan ücretsiz şekilli nick, şekilli yazı ve sembol araçları.",
 "h1": "Hakkımızda",
 "lead": "NickUstası; oyun ve sosyal medya için şekilli nick, şekilli yazı ve sembol araçlarını tek adreste toplayan, tamamı Türkçe ve ücretsiz bir araç sitesidir.",
 "badge": "NickUstası",
 "tool": "",
 "cfg": {},
 "intro": [
 "<p>NickUstası, bir ismi yazıp saniyeler içinde yüzlerce şekilli hâlini görme fikrinden doğdu. Sitede bir şekilli nick oluşturucu, yazı stilleri ve şekilli harf araçları, 401 sembolden oluşan tıklayıp kopyalamalı bir sembol kütüphanesi ile emoji ve kaomoji kütüphaneleri bulunur. PUBG Mobile, Free Fire, Brawl Stars, Instagram, Discord ve WhatsApp gibi her platform için, o alanın karakter sınırına uygun sayaçlı özel sayfalar da hazırdır.</p>",
 "<p>Sitedeki her araç tamamen senin tarayıcında çalışır. Yazdığın isim hiçbir sunucuya gönderilmez, hiçbir yere kaydedilmez; sayfayı kapattığında geride hiçbir şey kalmaz. Üyelik yoktur, indirme yoktur, ücret yoktur.</p>",
 ],
 "sections": [
 ("Ne Sunuyoruz?",
 "<ul>"
 "<li><strong>Şekilli nick oluşturucu:</strong> Tek isimden 110 farklı stil; süsleyici ve harf ayracıyla binlerce kombinasyon.</li>"
 "<li><strong>Yazı stilleri ve şekilli harfler:</strong> El yazısından gotike, stilleri harf harf inceleme ve kopyalama.</li>"
 "<li><strong>Sembol, emoji ve kaomoji kütüphaneleri:</strong> Kategorilere ayrılmış, tek tıkla kopyalanan geniş arşiv.</li>"
 "<li><strong>Boşluk kopyala aracı:</strong> Görünmez boşluk türleri ve toplu boşluk üretici.</li>"
 "<li><strong>Oyuna ve platforma özel sayfalar:</strong> Karakter sınırı sayaçları, güvenli sembol listeleri ve hazır nick önerileri.</li>"
 "<li><strong>Blog:</strong> Nasıl yapılır rehberleri, kutu (□) sorunu çözümleri ve platform ipuçları.</li>"
 "</ul>"),
 ("Türkçe Harf Sözümüz",
 "<p>Çoğu şekilli yazı aracı ğ, ü, ş, ı, ö, ç ve İ harflerini ya atar ya da bozuk gösterir. NickUstası tam tersine kuruldu: Türkçe harfler her stilde doğru karşılıklarıyla üretilir; karşılığı olmayan stilde harf sessizce silinmez, en yakın doğru biçim kullanılır. Bir Türk kullanıcının ismi, Türkçenin harfleriyle yazılabilmelidir.</p>"),
 ("Nasıl Çalışır?",
 "<p>Araçlar Unicode karakter dönüşümleriyle çalışır: Yazdığın metin, her stilin karakter tablosuna göre anında yeniden yazılır. Dönüşüm tarayıcında, sen yazarken gerçekleşir. Beğendiğin sonuca tıklaman yeterlidir; nick panona kopyalanır ve dilediğin oyuna ya da uygulamaya yapıştırabilirsin.</p>"),
 ],
 "faqs": [],
},

# ============================================================ 31. GİZLİLİK POLİTİKASI
{
 "slug": "gizlilik-politikasi", "file": "gizlilik-politikasi.html",
 "title": "Gizlilik Politikası — NickUstası",
 "desc": "NickUstası gizlilik politikası: araçlar tarayıcında çalışır; yazdığın isimler sunucuya gönderilmez ve saklanmaz. Hesap yok, kişisel veri toplama, satma ve paylaşma yok.",
 "h1": "Gizlilik <span class='hl'>Politikası</span>",
 "lead": "Bu sayfa, NickUstası'nı kullanırken hangi verilerin işlendiğini — daha doğrusu işlenmediğini — açık ve kısa biçimde anlatır.",
 "badge": "NickUstası",
 "tool": "",
 "cfg": {},
 "intro": [
 "<p>Son güncelleme: <strong>26 Ekim 2026</strong></p>",
 "<p>NickUstası'nın gizlilik anlayışı tek cümleyle özetlenebilir: Araçlar senin cihazında çalışır, verin senin cihazında kalır. Aşağıdaki maddeler bu ilkenin ayrıntılarıdır.</p>",
 ],
 "sections": [
 ("Veriler Tarayıcında Kalır",
 "<p>Şekilli nick üretimi, stil dönüşümleri ve kopyalama işlemlerinin tamamı tarayıcında, sayfanın içindeki kodla gerçekleşir. Oluşturucuya yazdığın isimler ve metinler sunucumuza gönderilmez, iletilmez ve saklanmaz. Sayfayı kapattığında yazdıkların da kapanır.</p>"),
 ("Hesap ve Üyelik Yoktur",
 "<p>Siteyi kullanmak için hesap açman gerekmez. Ad, soyad, e-posta adresi, telefon numarası veya parola gibi hiçbir kişisel bilgin istenmez ve toplanmaz.</p>"),
 ("Kişisel Veriler Satılmaz ve Paylaşılmaz",
 "<p>Toplamadığımız veriyi satmamız ya da paylaşmamız da söz konusu değildir. NickUstası, kişisel verileri üçüncü kişilerle pazarlama veya başka herhangi bir amaçla paylaşmaz.</p>"),
 ("Barındırma Kayıtları ve Çerezler",
 "<p>Her internet sitesinde olduğu gibi, sitenin barındırma (hosting) hizmeti güvenlik ve işletim amacıyla standart teknik erişim kayıtları tutabilir; bu kayıtlar ziyaret saati, tarayıcı türü ve IP adresi gibi teknik bilgiler içerebilir ve barındırma sağlayıcısının politikasına tabidir. Site, seni takip eden çerezler kullanmaz. İleride istatistik veya reklam çerezleri eklenmesi gerekirse bu politika önce güncellenir ve değişiklik bu sayfada duyurulur.</p>"),
 ("Dış Bağlantılar",
 "<p>Sayfalardaki bağlantılar oyunların ve platformların kendi sitelerine gidebilir. O sitelerin gizlilik uygulamaları bu politikanın kapsamı dışındadır; ilgili sitenin kendi gizlilik sayfasına bakman gerekir.</p>"),
 ("Politika Değişiklikleri",
 "<p>Bu politika güncellenirse yeni metin bu sayfada yayımlanır ve üstteki 'son güncelleme' tarihi değiştirilir. Önemli bir değişiklik, sayfada ayrıca belirtilir.</p>"),
 ],
 "faqs": [],
},

# ============================================================ 32. İLETİŞİM
{
 "slug": "iletisim", "file": "iletisim.html",
 "title": "İletişim — NickUstası",
 "desc": "NickUstası iletişim: öneri, hata bildirimi ve içerik düzeltme talepleri için iletişim bilgileri ve mesajında yer vermen gereken ayrıntılar.",
 "h1": "İletişim",
 "lead": "Bir önerin, hata bildirimin ya da düzeltme isteğin mi var? Doğru yerdesin; mesajını hazırlarken aşağıdaki ayrıntılara dikkat etmen, işimizi çok kolaylaştırır.",
 "badge": "NickUstası",
 "tool": "",
 "cfg": {},
 "intro": [
 "<p>NickUstası'nı daha iyi yapacak her görüş değerlidir: Çalışmayan bir stil, kutu görünen bir karakter, eksik bir sembol ya da yeni bir araç fikri... Hepsini duymak isteriz. İçerikte bir hata fark edersen düzeltme talebi de aynı yoldan iletilir.</p>",
 ],
 "sections": [
 ("Mesajında Neler Olmalı?",
 "<ul>"
 "<li><strong>Sayfanın adı veya bağlantısı:</strong> Sorunu hangi sayfada gördüğünü yaz (örn. PUBG Şekilli Nick sayfası).</li>"
 "<li><strong>Sorunun kısa açıklaması:</strong> Ne bekliyordun, ne oldu? İki üç cümle yeterlidir.</li>"
 "<li><strong>Cihaz ve tarayıcın:</strong> Telefon/bilgisayar modeli ile kullandığın tarayıcı (örn. Android — Chrome), sorunun kaynağını bulmayı hızlandırır.</li>"
 "<li><strong>Yazdığın metin:</strong> Sorun belli bir isimde çıkıyorsa, o metni de ekle; özellikle Türkçe harf içeren örnekler çok işe yarar.</li>"
 "</ul>"),
 ("İletişim Bilgileri",
 "<div class='info-box'><p><strong>İletişim bilgileri yakında buraya eklenecektir.</strong></p></div>"
 "<p>İletişim adresi yayımlandığında, öneri ve hata bildirimlerini yukarıdaki ayrıntıları ekleyerek gönderebilirsin. O zamana kadar sayfalardaki rehber yazıları ve sık sorulan sorular bölümleri, en sık karşılaşılan sorunların cevaplarını içerir.</p>"),
 ],
 "faqs": [],
},

]
