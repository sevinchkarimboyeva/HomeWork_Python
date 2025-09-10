# 1-misol
pochtalar=['user1@gmail.com','user2yahoo.com','user2@outlook.com']
for pochta in pochtalar:
    if "@" in pochta:
       print(f"To'gri email: {pochta}")
    else:
        print(f"Noto'g'ri email: {pochta}")


# 2-misol
parollar=["password123",'Qwerty','admin','StrongPass1!']
for parol in parollar:
    if len(parol)>8:
        print(f"{parol}  Juda qisqa")
    elif  parol.isalpha():
        print(f"{parol}  Kuchsiz parol.")
    else:
        print(f"{parol}   Kuchli parol")

# 3-misol
haroratlar=[20,22,19,24,25,23,21]
ortacha=sum(haroratlar)/len(haroratlar)
print(f"O'rtacha harorat: {ortacha}")

for kun in range(len(haroratlar)):
    if haroratlar[kun]>22:
        print(f"{kun+1}-kun: {haroratlar[kun]}  Iliq kun")
    else:
        print(f"{kun + 1}-kun: {haroratlar[kun]}  Salqin kun")

# 4-misol
taomlar=['osh',"shashlik",'manti',"lag'mon"]
taom=input("Assalomu aleykum mijoz, nima buyurtma berasiz?")
for a in taomlar:
    if a==taom:
        print("Buyurtmangiz qabul qilindi")
        break
    else:
        print("Kechirasiz,bunday taom yo'q")
# 5-misol
yoshlar=[16,21,17,30,25]
for yosh in yoshlar:
    if yosh <18:
        print(f"{yosh}-Yosh chegarasiga yetmagan")
    else:
        print(f"{yosh}-Xush kelibsiz!")

# 6-misol
xabarlar=['Yangi xabar','Bateriya past',"Yangilanish mavjud"]
for xabar in xabarlar:
    if xabar==xabarlar[1]:
        print("Telefoningizni quvvatlang")

# 7-misol
fayllar = [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar=[]
rasmlar=[]
for fayl in fayllar:
    if "jpg" in fayl:
        rasmlar.append(fayl)
    elif "mp3" in fayl:
        musiqalar.append(fayl)
print(f"Rasmlar:{rasmlar}")
print(f"Musiqalar:{musiqalar}")




























