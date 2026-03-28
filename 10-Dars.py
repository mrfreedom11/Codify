#10 - Dars Konspekt
#Faktorialni hisoblash:
# son = int(input("Son kiriting: "))
# natija = 1
# for i in range(1, son + 1):
#     natija *= i
# print(f"{son} sonining faktoriali: {natija}")
# #Tub sonlarni topish:
# import math
# son = int(input("Son kiriting: "))
# if son < 2:
#     print(f"{son} tub ham, murakkab ham emas")
# else:
#     chegara = int(math.sqrt(son))
#     tub = True
#     for i in range(2, chegara + 1):
#         if son % i == 0:
#             tub = False
#             break
#     if tub:
#         print(f"{son} tub son")
#     else:
#         print(f"{son} tub emas")
#10-Dars Takrorlash va For sikli
#1.Elektron Pochta Manzillarini Tekshirish:
pochtalar = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]
kiritilgan_email = input("Emailingizni kiriting: ")

if kiritilgan_email in pochtalar:
    print("Xush kelibsiz!")
else:
    print("Bunday email ro'yxatda yo'q")
#2. Parol Kuchini Tekshirish:
belgilar = "1234567890!@#$%^&*()_+-=<>,.?/'\""
parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
for parol in parollar:
    if len(parol) < 8:
        print("Juda qisqa")
    else:
        bormi = False
        for b in belgilar:
            if b in parol:
                bormi = True
                break
        
        if bormi:
            print(f"{parol}: Kuchli parol")
        else:
            print(f"{parol}: Kuchsiz parol")
#3.Ob-havo Ma'lumotlarini Tahlil Qilish:
royhat = [20, 22 , 19 , 24 ,  25 , 23 , 21]
ortacha = sum(royhat) / len(royhat)
for i in royhat:
    if i > 22:
        print('Iliq kun')
    else:
        print('Salqin kun')
#4.Restoran Buyurtmalari:
taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
buyurtma = input("Buyurtma kiriting: ")
mavjud = False
for taom in taomlar:
    if taom == buyurtma:
        print("Buyurtmangiz qabul qilindi")
        mavjud = True
        break
if not mavjud:
    print("Kechirasiz, bunday taom yo'q")
#5.Anketa Tahlili:
for yosh in royhat:
    if yosh < 18:
        print('Yosh chegarasi yetmagan')
    else: # 18 va undan kattalar uchun
        print('Xush kelibsiz')
#6.Mobil Ilova Bildirishnomalari:
xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
for xabar in xabarlar:
    if xabar == xabarlar[1]:
        print("Telefoningizni quvvatlang")
#7.Fayllarni guruhlash:
fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []
for fayl in fayllar:
    if fayl.endswith(".jpg"):
        rasmlar.append(fayl)
    elif fayl.endswith(".mp3"):
        musiqalar.append(fayl)
print("Rasmlar ro'yxati:", rasmlar)
print("Musiqalar ro'yxati:", musiqalar)