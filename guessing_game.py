import random
def tahmin_oyunu():
    while True :
        rastgele_sayı= random.randint(1,100)
        hak= 7
        print("/n Lütfen 1 ile 100 arası bir sayı tahmin ediniz. Toplam 7 hakkınız var")
        while hak> 0 :
            tahmin= input(f"Kalan hakkınız {hak} - Tahmininizi giriniz:")
            if tahmin.isdigit():
                tahmin= int(tahmin)

                if tahmin== rastgele_sayı :
                    print("Tebrikler doğru tahmin ettiniz!")

                elif tahmin<rastgele_sayı :
                    print("Lütfen daha büyük bir sayı giriniz")

                else :
                    print("Lütfen daha küçük bir sayı giriniz")
                hak -= 1       
            else:
                print("Lütfen sadece sayı giriniz")
    
    
        if tahmin != rastgele_sayı :

            print(f"Bilemediniz doğru sayı {rastgele_sayı}idi ")

            tekrar= input("Tekrar oynamak ister misiniz? (Evet/Hayır)").strip().lower()

        if tekrar != "Evet" :
           print("Oyunu oynadığınız için tesekkürler")
           break



tahmin_oyunu()




        
     