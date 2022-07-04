import os

# Fonksiyonlar
def sirali():
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

    print("Dosyalar Yeniden İsimlendirildi. Dosyaların Yeni İsimleri;")
    for isim in yeni_dosya_adi_listesi:
        print(isim)

def onEk():
    pass

def sonEk():
    pass

def buyukHarf():
    pass

def kucukHarf():
    pass

def karakterSil():
    pass

def kelimeDegistir():
    pass

def kelimeSil():
    pass

#Menü
menu = {"1": sirali, "2": onEk, "3": sonEk, "4": buyukHarf, "5": kucukHarf, "6": karakterSil, "7": kelimeDegistir, "8": kelimeSil}
print("***** MENÜ *****\n1: Sıralı Artır (Ör. resim1.png, resim2.png, ...)\n2: Ön Ek Ekle\n3: Son Ek Ekle\n4: Büyük Harfe Çevir\n5: Küçük Harfe Çevir\n6: Karakter Sil (Ör. boşluk, -)\n7: Kelime Değiştir\n8: Kelime Sil")

# Dosyayı çalıştır, Menüyü görüntüle, seçime göre işlem/fonksiyon çalıştır
while True:
    try:
        # Menü Seçeneklerinden birini Seçin
        islem = input("Menü seçeneklerinden birini belirtin: ")

        #Dizin Secimi
        dizin = input("Çalışma dizininin konumunu belirtin: ")  # Yeniden adlandırılmasını istediğiniz dosyaların bulunduğu klasöün bulunduğu dizin/yol

        # Varsayılan dizin yolu (Kod esnasinda zamandan kazanmak için)
        if dizin == "":
            dizin = "/home/halil/Belgeler/Yeniden_Adlandir"

        # İlgili dizindeki tüm Dosya ve Klasör isimleri
        dosya_klasor_adlari = os.listdir(dizin)

        # Yalnız Dosya adlarının barındırılacağı liste
        dosya_adlari = []

        # Yalnız Dosya isimlerini seç ve "dosya_adlari" listesine ekle
        for isim in dosya_klasor_adlari:
            if isim.count(".") > 0:         # sadece dosya isimlerini almak için olusturalan kosul, klasor isimlerini alma
                dosya_adlari.append(isim)

        menu[islem]()

    except KeyError:
        print("Geçersiz Seçim") 
        break
