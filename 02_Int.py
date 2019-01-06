#Hesap makinesi

print("Hesap Makinesi...")
a=0
b=0
sayac=0


while a == 0:           #İlk sayıyı aldığımız yer
    try:
        sayi=int(input("İlk sayıyı girin: "))
        a=1
    except ValueError:
        print("Sayı girmediniz.")
        continue






while sayac == 0:           #Yapılacak işlem içeriği

    while b == 0:           #İkinci sayıyı aldığımız yer
        try:
            ikinciSayi=int(input("Diğer sayıyı girin: "))
            b=1
        except ValueError:
            print("Sayı girmediniz.")
            continue

    #İşlem seçimi
    islem= input('''Yapmak istediğiniz işlemi seçin:\n
    Programdan çıkmak için 0\n
    Toplama işlemi için 1\n
    Çıkarma işlemi için 2\n
    Çarpma işlemi için 3\n
    Bölme işlemi için 4 e basın     ''')
    b=0

    if islem =="1":
        sayi=sayi+ikinciSayi
    elif islem =="2":
        sayi=sayi-ikinciSayi
    elif islem=="3":
        sayi=sayi*ikinciSayi
    elif islem=="4":
        if ikinciSayi!=0:
            sayi=sayi/ikinciSayi
        else :
            print("\nLütfen 0 dışında bir sayı girin. ") #ikinciSayi=int(input("Lütfen 0 dışında bir sayı girin: "))
            continue
    elif islem=="0":
        print("Programdan çıkılıyor...")
        sayac=1
        break
    else:
        print("Hatalı Giriş.")
        continue

    print(sayi)
        











