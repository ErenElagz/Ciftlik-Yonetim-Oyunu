import random
from prettytable import PrettyTable as pt

# Sınıflar
class Ciftlik():
    def __init__(self, isim, para, toplamDeger):
        self.isim = isim
        self.para = para
        self.toplamDeger = toplamDeger

    def CiftlikDegeri(self):
        for i in hayvanListesi, bitkiListesi, urunListesi:
            for j in i:
                ciftlik.toplamDeger += (j.adet * j.fiyat)
        return round(ciftlik.toplamDeger,2)

class Hayvan(Ciftlik):
    def __init__(self, isim, adet, urun, uretimKatsayisi, fiyat):
        self.isim = isim
        self.adet = adet
        self.uretimKatsayisi = uretimKatsayisi
        self.fiyat = fiyat
        self.oncekiFiyat = 0
        self.urun = urun
        self.haftalikUretim = 0

    def Alim(self):
        if ciftlik.para > 0:
            print(">", self.isim, "Pazarı")
            print("--------------------------------------------")
            print("> Güncel Fiyatları            :", self.fiyat)
            print("> Toplam Adet                 :", self.adet)
            print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
            print("> Toplam Paranız              :", ciftlik.para, "₺")
            print("> En Fazla Alınabilecek Sayı  :", round((ciftlik.para/self.fiyat), 0))
            alimadeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik.para = ciftlik.para - (self.fiyat * alimadeti)
            self.adet = self.adet + alimadeti
        else:
            print("\n> Paranız Yetersiz!\n")

    def Satim(self):
        print(">", self.isim, "Pazarı")
        print("--------------------------------------------")
        print("> Güncel Fiyatları            :", self.fiyat)
        print("> Toplam Adet                 :", self.adet)
        print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
        print("> Toplam Paranız              :", ciftlik.para, "₺")
        print("> En Fazla Satılabilecek Sayı :", self.adet)
        satimadeti = int(input("Kaç Tane Satmak İstersiniz? "))
        if satimadeti <= self.adet:
            ciftlik.para = ciftlik.para + (self.fiyat * satimadeti)
            self.adet = self.adet - satimadeti
        else:
            print("\n> Hata, O kadar Hayvanınız Yok.")

class Bitki(Ciftlik):
    def __init__(self, isim, adet, urun, uretimKatsayisi, fiyat):
        self.isim = isim
        self.adet = adet
        self.uretimKatsayisi = uretimKatsayisi
        self.fiyat = fiyat
        self.oncekiFiyat = 0
        self.urun = urun
        self.haftalikUretim = 0

    def Alim(self):
        if ciftlik.para > 0:
            print(">", self.isim, "Pazarı")
            print("--------------------------------------------")
            print("> Güncel Fiyatları            :", self.fiyat)
            print("> Toplam Adet                 :", self.adet)
            print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
            print("> Toplam Paranız              :", ciftlik.para, "₺")
            print("> En Fazla Alınabilecek Sayı  :", round((ciftlik.para/self.fiyat), 0))
            alimadeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik.para = ciftlik.para - (self.fiyat * alimadeti)
            self.adet = self.adet + alimadeti
        else:
            print("\n> Paranız Yetersiz!\n")

    def Satim(self):
        print(">", self.isim, "Pazarı")
        print("--------------------------------------------")
        print("> Güncel Fiyatları            :", self.fiyat)
        print("> Toplam Adet                 :", self.adet)
        print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
        print("> Toplam Paranız              :", ciftlik.para, "₺")
        print("> En Fazla Satılabilecek Sayı :", self.adet)
        satimadeti = int(input("Kaç Tane Satmak İstersiniz? "))
        if satimadeti <= self.adet:
            ciftlik.para = ciftlik.para + (self.fiyat * satimadeti)
            self.adet = self.adet - satimadeti
        else:
            print("\n> Hata, O kadar Bitkiniz Yok.")

class Urun(Ciftlik):
    def __init__(self, isim, adet, fiyat):
        self.isim = isim
        self.adet = adet
        self.fiyat = fiyat
        self.oncekiFiyat = 0

    def Alim(self):
        if ciftlik.para > 0:
            print(">", self.isim, "Pazarı")
            print("--------------------------------------------")
            print("> Güncel Fiyatları            :", self.fiyat)
            print("> Toplam Adet                 :", self.adet)
            print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
            print("> Toplam Paranız              :", ciftlik.para, "₺")
            print("> En Fazla Alınabilecek Sayı  :", round((ciftlik.para/self.fiyat), 0))
            alimadeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik.para = ciftlik.para - (self.fiyat * alimadeti)
            self.adet = self.adet + alimadeti
        else:
            print("\n> Paranız Yetersiz!\n")

    def Satim(self):
        print(">", self.isim, "Pazarı")
        print("--------------------------------------------")
        print("> Güncel Fiyatları            :", self.fiyat)
        print("> Toplam Adet                 :", self.adet)
        print("> Geçen Haftaki Fiyat         :", self.oncekiFiyat, "₺")
        print("> Toplam Paranız              :", ciftlik.para, "₺")
        print("> En Fazla Satılabilecek Sayı :", self.adet)
        satimadeti = int(input("Kaç Tane Satmak İstersiniz? "))
        if satimadeti <= self.adet:
            ciftlik.para = ciftlik.para + (self.fiyat * satimadeti)
            self.adet = self.adet - satimadeti
        else:
            print("\n> Hata, O kadar Ürününüz Yok.")

# Değişkenler
hafta = 1

# Nesneler
ciftlik = Ciftlik("Ciftlik", 5000, 0)
#
inek = Hayvan("İnek", 3, "Süt", 2, 750)
koyun = Hayvan("Koyun", 5, "Yün", 1, 250)
tavuk = Hayvan("Tavuk", 7, "Yumurta", 5, 50)
hayvanListesi = [inek, koyun, tavuk]
#
pamuk = Bitki("Pamuk", 3, "Kumaş", 1, 200)
bugday = Bitki("Buğday", 5, "Un", 5, 500)
aycicegi = Bitki("Ayçiçeği", 7, "Yağ", 3, 100)
bitkiListesi = [pamuk, bugday, aycicegi]
#
süt = Urun("Süt", 0, 7)
yün = Urun("Yün", 0, 30)
yumurta = Urun("Yumurta", 0, 2)
kumas = Urun("Kumaş", 0, 80)
un = Urun("Un", 0, 35)
yag = Urun("Yağ", 0, 60)
saman = Urun("Saman", 200, 50)
gubre = Urun("Gübre", 300, 60)
urunListesi = [süt, yün, yumurta, kumas, un, yag, saman, gubre]

# Fonksiyonlar
def Fiyatlandirma():
    for i in hayvanListesi:
        i.oncekiFiyat = i.fiyat
        i.fiyat = round(i.fiyat * (random.uniform(0.9, 1.1)), 2)

    for i in bitkiListesi:
        i.oncekiFiyat = i.fiyat
        i.fiyat = round(i.fiyat * (random.uniform(0.85, 1.15)), 2)

    for i in urunListesi:
        i.oncekiFiyat = i.fiyat
        i.fiyat = round(i.fiyat * (random.uniform(0.75, 1.25)), 2)

def Uretim():
    süt.adet = süt.adet + (inek.adet * inek.uretimKatsayisi)
    yün.adet = yün.adet + (koyun.adet * koyun.uretimKatsayisi)
    yumurta.adet = yumurta.adet + (tavuk.adet * tavuk.uretimKatsayisi)
    kumas.adet = kumas.adet + (pamuk.adet * pamuk.uretimKatsayisi)
    un.adet = un.adet + (bugday.adet * bugday.uretimKatsayisi)
    yag.adet = yag.adet + (aycicegi.adet * aycicegi.uretimKatsayisi)

    inek.haftalikUretim = inek.adet * inek.uretimKatsayisi
    koyun.haftalikUretim = koyun.adet * koyun.uretimKatsayisi
    tavuk.haftalikUretim = tavuk.adet * tavuk.uretimKatsayisi
    pamuk.haftalikUretim = pamuk.adet * pamuk.uretimKatsayisi
    bugday.haftalikUretim = bugday.adet * bugday.uretimKatsayisi
    aycicegi.haftalikUretim = aycicegi.adet * aycicegi.uretimKatsayisi

def SamanTuketimi():
    if saman.adet > 0:
        saman.adet -= (inek.adet * 3)+(koyun.adet * 2)+(tavuk.adet * 1)
        print("\nKaç Haftalık Samanınız Kaldı?", int(saman.adet/((inek.adet * 3)+(koyun.adet * 2)+(tavuk.adet * 1))), "Hafta")
        print("Saman Tüketimi:", ((inek.adet * 3) +(koyun.adet * 2)+(tavuk.adet * 1)))

    else:
        print("Yeterli Kaynak Yok. Eğer Saman Almazsanız Hayvanlarınız Ölmeye Başlayacak.")
        print("Telef Olan İnek  Sayısı:", 2)
        print("Telef Olan Koyun Sayısı:", 3)
        print("Telef Olan Tavuk Sayısı:", 5)
        inek.adet  -= 2
        koyun.adet -= 3
        tavuk.adet -= 5
    
        if inek.adet <= 0:
            inek.adet = 0
            print("Hiç İneğiniz Kalmadı!")

        if koyun.adet <= 0:
            koyun.adet = 0
            print("Hiç Koyununuz Kalmadı!")

        if tavuk.adet <= 0:
            tavuk.adet = 0
            print("Hiç Tavuğunuz Kalmadı!")

def GubreTuketimi():
    if gubre.adet > 0:
        gubre.adet -= (pamuk.adet * 2)+(bugday.adet * 2)+(aycicegi.adet * 3)
        print("\nKaç Haftalık Gübre Kaldı?", str(int(gubre.adet/((pamuk.adet * 2)+(bugday.adet * 2)+(aycicegi.adet * 3)))), "Hafta")
        print("Gübre Tüketimi:", ((pamuk.adet * 2) +(bugday.adet * 2)+(aycicegi.adet * 3)))

    else:
        print("Yeterli Kaynak Yok. Eğer Saman Almazsanız Hayvanlarınız Ölmeye Başlayacak.")
        print("Solan Pamuk  Sayısı   :", 2)
        print("Solan Buğday Sayısı   :", 2)
        print("Solan Ayçiçeği Sayısı :", 3)
        pamuk.adet  -= 2
        bugday.adet -= 2
        aycicegi.adet -= 3
    
        if pamuk.adet <= 0:
            pamuk.adet = 0
            print("Hiç Pamuk Kalmadı!")

        if bugday.adet <= 0:
            bugday.adet = 0
            print("Hiç Buğday Kalmadı!")

        if aycicegi.adet <= 0:
            aycicegi.adet = 0
            print("Hiç Ayçiçeği Kalmadı!")

def PazaryeriAlim(liste):
    alimIndex = 1
    print("\n-----------------------------------------------")
    for i in liste:
        print(alimIndex, i.isim)
        print("Güncel Adet:", i.adet)
        print("-----------------------------------------------")
        alimIndex += 1
    alimInput = int(input("Ürün Numarası Giriniz: "))
    
    if alimInput == 0:
        print("\n> Geçerli Bir Değer Giriniz!\n")
    
    else:
        try:
            liste[alimInput-1].Alim()

        except:
            print("\n> Geçerli Bir Değer Giriniz!\n")

def PazaryeriSatim(liste):
    satimIndex = 1
    print("\n-----------------------------------------------")
    for i in liste:
        print(satimIndex, i.isim)
        print("Güncel Adet:", i.adet)
        print("-----------------------------------------------")
        satimIndex += 1
    satimInput = int(input("Ürün Numarası Giriniz: "))

    if satimInput == 0:
        print("\n> Geçerli Bir Değer Giriniz!\n")

    else:
        try:
            liste[satimInput-1].Satim() 

        except:
            print("\n> Geçerli Bir Değer Giriniz!\n")

# Ana Döngü
while True:
    print("\n----------------------------------------")
    print("          Çiftlik Yönetim Oyunu           ")
    print("----------------------------------------")
    print("> 1: Çiftlik")
    print("> 2: Bir Sonraki Hafta >", hafta, ". hafta")
    print("> 3: Fiyatlar")
    print("> 4: Pazaryeri")
    print("> 5: İstatistlikler")
    print("> 6: Hakkında")
    print("> 0: Çıkış")
    print("----------------------------------------")
    anasayfaSayfa = int(input("Sayfa Numarası Giriniz: "))

    # Çıkış
    if anasayfaSayfa == 0:
        print("Oyundan Çıkış Yapıldı.")
        break

    # Çiftlik
    elif anasayfaSayfa == 1:
        while True:
            print("\n----------------------------------------")
            print("               Çiftliğim                ")
            print("----------------------------------------")
            print("> 1: Ahır")
            print("> 2: Tarla")
            print("> 3: Envanter")
            print("> 0: Çıkış")
            ciftlikSayfa = int(input("Sayfa Numarası Giriniz: "))

            # Çıkış
            if ciftlikSayfa == 0:
                break

            # Ahır
            elif ciftlikSayfa == 1:
                tb = pt()
                tb.field_names = ["Ad", "Adet", "Fiyat", "Önceki Fiyat", "Toplam değer", "Ürün", "Haftalık Üretim"]
                for i in hayvanListesi:
                    tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat,round((i.adet*i.fiyat),2), i.urun, i.haftalikUretim])
                print(tb)

            # Tarla
            elif ciftlikSayfa == 2:
                tb = pt()
                tb.field_names = ["Ad", "Adet", "Fiyat", "Önceki Fiyat", "Toplam değer", "Ürün", "Haftalık Üretim"]
                for i in bitkiListesi:
                    tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat,round((i.adet*i.fiyat),2) ,i.urun, i.haftalikUretim])
                print(tb)

            # Envanter
            elif ciftlikSayfa == 3:
                tb = pt()
                tb.field_names = ["Ad", "Adet", "Fiyat", "Önceki Fiyat","Toplam değer"]
                for i in urunListesi:
                    tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat,round((i.adet*i.fiyat),2)])
                print(tb)

            # Hata
            else:
                print("\n> Geçerli Bir Değer Giriniz!\n")

    # Bir sonraki hafta
    elif anasayfaSayfa == 2:
        hafta += 1
        Fiyatlandirma()
        Uretim()
        SamanTuketimi()
        GubreTuketimi()

    # Fiyatlar
    elif anasayfaSayfa == 3:
        print("\n----------------------------------------")
        print("          Bu Haftaki Fiyatlar           ")
        print("----------------------------------------")
        tb = pt()
        tb.field_names = ["Ad", "Adet", "Fiyat", "Önceki Fiyat"]
        for i in hayvanListesi:
            tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat])
        tb.add_row(["--------", "--------", "--------", "--------"])
        for i in bitkiListesi:
            tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat])
        tb.add_row(["--------", "--------", "--------", "--------"])
        for i in urunListesi:
            tb.add_row([i.isim, i.adet, i.fiyat, i.oncekiFiyat])
        print(tb)

    # Pazaryeri
    elif anasayfaSayfa == 4:
        print("\n----------------------------------------")
        print("                Pazar Yeri              ")
        print("----------------------------------------\n")
        print("Hayvan")
        print("> 1: Alım")
        print("> 2: Satım")
        print("------------------------\n")
        print("Bitki")
        print("> 3: Alım")
        print("> 4: Satım")
        print("------------------------\n")
        print("Ürün")
        print("> 5: Alım")
        print("> 6: Satım")
        print("------------------------\n")
        print("> 0: Çıkış")
        print("------------------------")
        pazaryeriSayfa = int(input("Sayfa Numarası Giriniz: "))

        # Çıkış
        if pazaryeriSayfa == 0:
            print("Anasayfaya Dönüldü.")

        # Hayvan Alım
        elif pazaryeriSayfa == 1:
            PazaryeriAlim(hayvanListesi)

        # Hayvan Satım
        elif pazaryeriSayfa == 2:
            PazaryeriSatim(hayvanListesi)

        # Bitki Alım
        elif pazaryeriSayfa == 3:
            PazaryeriAlim(bitkiListesi)

        # Bitki Satım
        elif pazaryeriSayfa == 4:
            PazaryeriSatim(bitkiListesi)

        # Ürün Alım
        elif pazaryeriSayfa == 5:
            PazaryeriAlim(urunListesi)

        # Ürün Satım
        elif pazaryeriSayfa == 6:
            PazaryeriSatim(urunListesi)

        # Hata
        else:
            print("\n> Geçerli Bir Değer Giriniz!\n")

    # İstatistikler
    elif anasayfaSayfa == 5:
        print("\n----------------------------------------")
        print("          Çiftlik İstatistikleri          ")
        print("----------------------------------------")
        ciftlik.toplamDeger = 0
        print("> Toplam Çiftlik Değeri :", ciftlik.CiftlikDegeri())
        print("> Güncel Paranız        :", ciftlik.para)

    # Hakkında
    elif anasayfaSayfa == 6:
        print("\n------------------------")
        print("Yapımcılar: Eren Elagöz\n")
        print("Çiftlik oyunu ,bir ahır birde tarlanızın olduğu küçük bir çiftlikte başlar.\nVe oyuna birkaç hayvan birkaç tarla ve 5000₺ ile başlarsınız.")
        print("Amacınız her hafta üretim yapıp ve elde ettiginiz ürünleri pazar yerinde sattığınız ve elde ettiğiniz parayla yatırım yaptığınız bir oyun")
        print("Fakat Herşey bu kadar basit değil! Her hafta fiyatlar değişiyor bazen fiyatlar çakılıyor bazende uçabiliyor")
        print("Peki ya şimdi sıra sende... elindekileri satacak mısın? bekleyecek misin? \n")

    # Hata
    else:
        print("\n> Geçerli Bir Değer Giriniz!\n")
