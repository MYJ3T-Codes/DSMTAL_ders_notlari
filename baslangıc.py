'''
değişkenler ve kuralları

Değişken İsimlendirme Kuralları:

1-Değişken isimleri harf veya alt çizgi (_) ile başlamalıdır.
2-Harf, sayı ve alt çizgi kullanılabilir, ancak sayı ile başlayamaz.
3-Büyük-küçük harf duyarlılığı vardır. degisken, Degisken ve DEGİSKEN farklı değişken isimleridir.
4-Python Anahtar Kelimeleri Kullanılamaz:
5-Değişken ismi olarak Python dilindeki anahtar kelimeler (if, else, for, while, gibi) kullanılamaz.
6-Değişken isimlerinde boşluk kullanılamaz. Eğer birden fazla kelime içeren bir değişken ismi kullanmak istiyorsanız
  alt çizgi (_) veya "camelCase" gibi teknikleri tercih edebilirsiniz. Örneğin: isim_soyisim, ogrenciAdi, kullaniciAdi.

Değişken isimleri, kullanım amacını yansıtmalıdır. Kodunuzun anlaşılabilir ve bakımı kolay olması için açıklayıcı isimler tercih edin.
'''
#Örnekler
# Geçerli değişken isimleri
yas = 25
ad_soyad = "Ahmet Yılmaz"
musteri_listesi = ["Ali", "Ayşe", "Can"] #burda listeleme yöntemi ile doğru bir örnek verdim

# Geçersiz değişken isimleri
3yas = 30  # Sayı ile başlayan değişken ismi aynı şekilde sayı ile başlamaz
müsteri_listesi = ["Zeynep", "Deniz"]  # Türkçe karakter kullanımı
for = 10  # Anahtar kelime kullanımı for bi döngü ismidir bu yüzden kod hata verir
'''
değişken türleri
1-Integer(int):tam sayi değişkenler için kullaniriz örn:yaş
2-String(str): bunu ise harfleri kullanacağimiz değişkenlerde kullaniriz örn:ismail
3-float:ondalikli sayilar için kullanilir örn:30.50 tarzinda
4-boolen:"True" veya "False" için kullanilir sadece doğru yanliş için kullanilir
daha bir kaç tane değişken türü var ama burada söylemicem daha görmediğimiz için
'''
'''
değişkenleri birleştirme
'''
#integer
sayi1 = 2
sayi2 = 3
toplam = sayi1+sayi2
print(toplam)#sonuç:5
#string
ilk_cümle = "hello"
ikinci_cümle = "world"
birlesim = ilk_cümle+ikinci_cümle
print(birlesim)#sonuç:hello world
#float
float_sayi1 = 3.50
float_sayi2 = 4.50
float_toplam = float_sayi1+float_sayi2
print(float_toplam)#sonuç:8 float bir python kelimesi olmasına rağmen ekleme yapıp tek bırakmadığım için çalışır
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#burada True değeri döeneceği için "b is greater than a" yazar ama False olsaydı tam tersi
#hatalı birleştirmeler
isim = "ismail"
yasim = int(15)
print(isim + yasim)#hata alırız çünkü string ile integer toplanmaz fakat araya "," koyarsak düzelir
#matematik işlemleri 
'''
1-Toplama (+): İki sayiyi toplar.
2-Çikarma (-): Bir sayiyi diğerinden çikarir.
3-Çarpma (*): İki sayiyi çarpar.
4-Bölme (/): Bir sayiyi diğerine böler. Bölme işlemi her zaman ondalik bir sonuç verir.
5-Tam Bölme (//): Bölme işleminin tam kismini alir, ondalik kismi atar.
6-Mod (%): Bölme işleminin kalanini verir.
7-Üs Alma ():** Bir sayinin üssünü alir.
bunlari örneklendirmicem bi zahmet anlarsiniz
'''
# Karşılaştırma Operatörleri
'''
1-"==" bu eşittir için kullanilir örn: if isim == "ismail"
2-"!=" eşit değildir bu ise tam tersi işe yarar
3-"<" bu ise bi sayının diğerinden küçük olduğunu gösterir
4-">" bu ise bi sayının diğerinden büyük olduğunu gösterir
5-"<="bu ise bi sayını diğerinden küçük veya eşit olduğunu ifade eder
6-">="bu ise bi sayını diğerinden büyük veya eşit olduğunu ifade eder
'''