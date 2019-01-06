
sehirler=('''Adana Adıyaman Afyonkarahisar Ağrı Aksaray Amasya Ankara Antalya Ardahan Artvin Aydın Balıkesir Bartın Batman Bayburt Bilecik Bingöl Bitlis Bolu Burdur Bursa Çanakkale Çankırı Çorum Denizli Diyarbakır Düzce Edirne Elazığ Erzincan Erzurum Eskişehir Gaziantep Giresun Gümüşhane Hakkâri Hatay Iğdır Isparta İstanbul İzmir Kahramanmaraş Karabük Karaman Kars Kastamonu Kayseri Kırıkkale Kırklareli Kırşehir Kilis Kocaeli Konya Kütahya Malatya Manisa Mardin Mersin Muğla Muş Nevşehir Niğde Ordu Osmaniye Rize Sakarya Samsun Siirt Sinop Sivas Şanlıurfa Şırnak Tekirdağ Tokat Trabzon Tunceli Uşak Van Yalova Yozgat Zonguldak''')
sehirlerLower=sehirler.lower()
sehirlerDizi= sehirlerLower.split(" ")
basHarfler=""  #Şehirlerin başladığı harfler
a=0
ilkHarf=""
sehirSayisi=len(sehirlerDizi) #81 şehir var 


### Şehirlerin hangi harflerle başladığını belirleme ###
while a < sehirSayisi:
    sehir = sehirlerDizi[a]
    #sehir.startwith("a")
    ilkHarf=sehir[0]
    try:
        basHarfler.index(ilkHarf)
    except ValueError:
        basHarfler += ilkHarf
        continue
    a += 1
a=0

isim=input("\nBir İsim Yazın: ") #Kullanıcıdan (sadece string) isim alıyoruz 
while isim.isalpha() == False:
    isim=input("Lütfen Bir İsim Yazın: ")

isimLower=isim.lower()  ### Girilen isimin harflerim büyütüldü


### Girilen isimin harfleri ile başlayan şehirler
for i in isimLower[0:] : 
    j=""
    while a<sehirSayisi:
        #isim.startwith("a")
        sehir=sehirlerDizi[a]
        ilkHarf=sehir[0]
        if ilkHarf==i :
            j+=sehir+"  "
        a+=1

    if j=="" :
        print("\n"+i + "  "+"Harfiyle Başlayan Bir Şehir Bulunmamaktadır ! ")
        
    else :
        print("\n"+i +"  "+ "Harfiyle Başlayan Şehirler:  " + j,sep=" ")
    a=0

print("\n")
    
#isim.startwith("a")
# for j in len(isim):
#     harf=isim[j]