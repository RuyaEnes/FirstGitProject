import time
import datetime
import locale

'''for i in range(1):
#     time.sleep(1)
#     print(i)
#############################################################################'''
print("\n### Örnek Format 12.12.1986 ###\n")
dogum=input("Doğum tarihinizi gün ay yıl şeklinde örnek formattaki gibi giriniz :  ")
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







