#1 ile 20 arasında sayı griliecek gilrine sayı bunların dışındaysa oyunu kaybettiniz bitti yazan oyun
#3 bulma hakkı bılursa 'tebrikler,kazanıdınız yazaacak'
#bilgisayar.ogretmen@gmail.com
tahmin_edilecek_cevap = 15
tahmin_sayisi = 3
while tahmin_sayisi == 0:
    verilen_cevap = int(input("cevabinizi girin?"))
    if verilen_cevap != tahmin_edilecek_cevap:
        print("yanlış kalan hakkınız:",tahmin_sayisi)
        tahmin_sayisi = tahmin_sayisi-1
    elif verilen_cevap == tahmin_edilecek_cevap:
        print("cevabınız doğru tebrikler")
        break
    else:  
        print("hakkınız bitti yeniden deneyin")
