fiyat = {
    "espresso": [20, 23, 27],
    "americano": [25, 27, 30],
    "latte": [30, 32, 35]
}


class otomat():
    
    
    def __init__(self, otomat_durum="kapalı", kahve_listesi=["espresso", "americano", "latte"], miktar="küçük",
                 seker=0):
        self.otomat_durum = otomat_durum
        self.kahve_listesi = kahve_listesi
        self.miktar = miktar
        self.fiyat = fiyat

    def otomat_ac(self):
        if (self.otomat_durum == "kapalı"):
            print("Otomat açılıyor....")
            self.otomat_durum = "açık"
        else:
            print("Otomat kapanıyor...")
            self.otomat_durum = "kapalı"
            print("otomat açık")

    def otomat_kapat(self):
        if self.otomat_durum == "kapalı":
            print("Önce otomatı açınız.")
        else:
            if (self.otomat_durum == "kapalı"):
                print("Otomat zaten kapalı....")
            else:
                print("Otomat kapanıyor...")
                self.otomat_durum = "kapalı"

    def kahve_ekle(self):
        if self.otomat_durum == "kapalı":
            print("Önce otomatı açınız.")
        else:
            for item in list(fiyat.keys()):
                print(f"{item.upper()} : {fiyat[item]} TL")
            veri = input("eklemek istediğiniz kahvenin adını girin: ")
            yeni_fiyat = int(input("kahvenin küçük boy fiyatını girin: "))
            yeni_fiyat2 = int(input("kahvenin orta boy fiyatını girin: "))
            yeni_fiyat3 = int(input("kahvenin büyük boy fiyatını girin: "))
            fiyat[veri] = [yeni_fiyat, yeni_fiyat2, yeni_fiyat3]

    def kahve_fiyati(self):
        if self.otomat_durum == "kapalı":
            print("Önce otomatı açınız.")
        else:
            for item in list(fiyat.keys()):
                print(f"{item.upper()} : {fiyat[item]} TL")
            kahve = input("istediğiniz kahvenin adını giriniz: ")
            for item in list(fiyat.keys()):
                if item.lower() == kahve:
                    
                    boyut = input("istediğiniz boyu seçin...(küçük/orta/büyük): ")
                    seker_miktari = int(input("kaç küp şeker istersiniz(max 5): "))
                    self.seker = seker_miktari
                    if boyut == "küçük":
                                print("ödemeniz gereken fiyat:", fiyat.get(kahve)[0])
                    if boyut == "orta":
                                print("ödemeniz gereken fiyat:", fiyat.get(kahve)[1])
                    if boyut == "büyük":
                                print("ödemeniz gereken fiyat:", fiyat.get(kahve)[2])
                    
                    cevap= input("Kahveniz hazır...\nYanında Kurabiye İster Misiniz ? (Evet/Hayır): ")
                    print("\nKurabiye: 20TL")
                    if cevap=="evet":
                        while(True):
                            kacTane= int(input("Kaç adet istersiniz: "))
                            if kacTane>0:
                                if boyut == "küçük":
                                    print("ödemeniz gereken toplam fiyat:", fiyat.get(kahve)[0]+20*kacTane)
                                    break
                                if boyut == "orta":
                                    print("ödemeniz gereken toplam fiyat:", fiyat.get(kahve)[1]+20*kacTane)
                                    break
                                if boyut == "büyük":
                                    print("ödemeniz gereken toplam fiyat:", fiyat.get(kahve)[2]+20*kacTane)
                                    break
                            else:
                                print("1 adet ve üstü seçiniz")
                    elif cevap=="hayır":
                        print("Afiyet Olsun...")

    def fiyat_guncelleme(self):
        if self.otomat_durum == "kapalı":
            print("Önce otomatı açınız.")
        else:
            güncel_kahve = input("fiyatını güncellemek istediğiniz kahveyi girin: ")
            güncel_fiyat = int(input("Ne kadar fiyat eklenecek ? : "))
            fiyat.get(güncel_kahve)[0] += güncel_fiyat
            fiyat.get(güncel_kahve)[1] += güncel_fiyat
            fiyat.get(güncel_kahve)[2] += güncel_fiyat

    def menu(self):
        if self.otomat_durum == "kapalı":
            print("Önce otomatı açınız.")
        else:
            for item in list(fiyat.keys()):
                print(f"{item.upper()} : {fiyat[item]} TL")


otomat = otomat()

print("""
Kahve Otomatı
1. Otomatı aç
2. Otomatı kapat
3. Menüyü yazdır
4. Kahve ekle
5. Kahvenizi seçin
6. Fiyat güncelle
Çıkmak için 'q' ya basın.""")



while True:
    islem = input("işlemi seçiniz:")
    if (islem == "q"):
        print("Afiyet olsun!!!")
        break
    elif (islem == "1"):
        otomat.otomat_ac()
    elif (islem == "2"):
        otomat.otomat_kapat()
    elif (islem == "3"):
        otomat.menu()
    elif (islem == "4"):
        otomat.kahve_ekle()
    elif (islem == "5"):
        otomat.kahve_fiyati()
    elif (islem == "6"):
        otomat.fiyat_guncelleme()
    else:
        pass
    

