import os

dizin = os.getcwd()
dosya_adlari = os.listdir(dizin)

Yeni_Dosya_Adi = input("Dosyalara Verilecek Yeni Adı Belirtin: ")

sayac_1 = 1
yeni_dosya_adi_listesi = []

for dosya_adi in dosya_adlari:
    if (dosya_adi.count(".") >=1 ):     # sadece dosyaları seçmek için bu kontrolü yazdım, Klasörleri adlandırmayacağım.
        uzanti_indeksi = dosya_adi.rfind(".")   # dosya uzantisinin indis değerini tespit ettim.
        uzanti = dosya_adi[uzanti_indeksi:]     # dosya uzantisini aldım
        yeni_dosya_adi_listesi.append(Yeni_Dosya_Adi + str(sayac_1) + uzanti)
        sayac_1 += 1

sayac_2 = 0
for ad in dosya_adlari:
    os.rename(ad, yeni_dosya_adi_listesi[sayac_2])
    sayac_2 += 1
