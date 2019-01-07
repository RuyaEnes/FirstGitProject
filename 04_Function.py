import sys

def sistem_bilgisi():

    print("Sistemdeki Python'un :\n")
    print("Ana Sürüm Numarası             : " , sys.version_info.major)
    print("Alt Sürüm Numarası             : " , sys.version_info.minor)
    print("Minik Sürüm Numarası           : " , sys.version_info.micro)
    print("Kullanılan işletim sistemi adı :" , sys.platform)
    

print(sistem_bilgisi())


#######Doğum Tarihi ile İşlem yapan Fonksiyon
import datetime
import time
import locale

def dogum_hesap(dogum):
    now=datetime.datetime.today()
    dogumTarihi= datetime.datetime.strptime(dogum, "%d.%m.%Y")##try ekle###############
    dGünü=str(dogumTarihi.day)
    dAyı=str(dogumTarihi.month)
    dYılı=str(dogumTarihi.year)
    seneye=str(now.year+1)
    yas=now.year-dogumTarihi.year
    print("\nYaşınız : " + str(yas))


    if now.month < dogumTarihi.month :
        buYılDGStr=(dGünü+"."+dAyı+"."+str(now.year))
        buYılDGDate=datetime.datetime.strptime(buYılDGStr, "%d.%m.%Y")
        print("Doğum gününe kalan süre "+str(buYılDGDate-now))
    elif now.month > dogumTarihi.month:
        sonrakiDGStr=(dGünü+"."+dAyı+"."+seneye)
        sonrakiDGDate=datetime.datetime.strptime(sonrakiDGStr, "%d.%m.%Y")
        print("Doğum günününe kalan süre "+str(sonrakiDGDate-now))
    else :
        if now.day < dogumTarihi.day:
            print("Doğum gününe kalan süre "+str(dogumTarihi.day-now.day))
        elif now.day > dogumTarihi.day:
            print("Doğum gününe kalan süre "+str(365-(now.day-dogumTarihi.day)))
        else:
            print("Doğum günün kutlu olsun!!!\n")

print("\n### Örnek Format 12.12.1986 ###\n")
dogum=input("Doğum tarihinizi gün ay yıl şeklinde örnek formattaki gibi giriniz :  ")
print(dogum_hesap(dogum))





'''#####Kullanıcı istediği kadar sayı girecek onlarla min max işlemleri yapıcaz


giris = input("Lütfen sayılarınızı aralarında birer boşluk bırakarak girin\n veya çıkmak için bir harfe basın : ")
degerDizisi = giris.split(" ")


def islemler(deger):
    degerler=list()
    sinir=0
    a=len(deger)
    while sinir != a :
        try:
            degerler + int(deger[sinir])
            sinir+=1
        except ValueError:
            print("Programdan çıkılıyor...")
            sys.exit()

    print("Dizinin en küçük elemanı : " , min(degerler))
    print("Dizinin en büyük elemanı : " , max(degerler))


islemler(degerDizisi)'''