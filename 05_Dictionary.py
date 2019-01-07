import sys
i=0
rehber= { "rüya"   : {"05301231212" : "İzmir"},
          "gamzeB" : {"05302342343" : "Mersin"},
          "gamzeP" : {"05308766787" :"Manisa"},
          "tuğçe"  : {"05308796786" : "İzmir"},
          "jülide" : {"05308975629" : "İzmir"}}

# def kontrol(girdi):
#     tuslar = { 1 : kisi_ekle(),
#                2 : kisi_bulma() }
#     try :

        
    

while i==0:
    girdi = input(" Yeni kişi eklemek için 1\n Telefon numarasına ulaşmak için 2\n Çıkmak için 3\n \t\t\t e basın    ")

    if girdi == "1" :
        isimYeni = input("Lütfen rehbere eklenecek kişinin adını girin : ")
        isim= isimYeni.lower()
        numara = input("Numarayı girin : ")
        rehber = {isim: numara}
        print("Başarıyla rehbere eklendi.")
        
    elif girdi == "2" :
        isimAra = input("Lütfen aranacak kişinin adını girin : ")
        isim=isimAra.lower()
        ad = rehber[isim]
        print ("Aradığınız numara : " + ad)
        
    elif girdi == "3" :
        #sys.exit()
        break
    else :
        print("Hatalı seçim. Tekrar deneyin.\n ")


