import os

dizin = input("Yeniden adlandirilacak dosyalarin bulunduğu dizin yolunu belirtin: ")

if dizin == "":
    dizin = "/home/halil/Belgeler/Yeniden_Adlandir"

dosya_klasor_adlari = os.listdir(dizin)
dosya_adlari = []

for isim in dosya_klasor_adlari:
    if isim.count(".") > 0:         # sadece dosya isimlerini almak için olusturalan kosul, klasor isimlerini alma
        dosya_adlari.append(isim)

Yeni_Dosya_Adi = input("Dosyalara Verilecek Yeni Adı Belirtin: ")

sayac_1 = 1
yeni_dosya_adi_listesi = []

for dosya_adi in dosya_adlari:
    uzanti_indeksi = dosya_adi.rfind(".")   # dosya uzantisinin indis değerini tespit ettim.
    uzanti = dosya_adi[uzanti_indeksi:]     # dosya uzantisini aldım
    yeni_dosya_adi_listesi.append(Yeni_Dosya_Adi + str(sayac_1) + uzanti)
    sayac_1 += 1

sayac_2 = 0
for ad in dosya_adlari:
    os.rename(dizin+"/"+ad, dizin+"/"+yeni_dosya_adi_listesi[sayac_2])
    sayac_2 += 1

print("Dosyalar Yeniden İsimlendirildi. Dosyaların isimleri;")
for isim in yeni_dosya_adi_listesi:
    print(isim)
