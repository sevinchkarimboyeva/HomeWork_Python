# 1-misol
havo=int(input("Ob-havo harorati qanday?"))
if havo<0:
    print(f"{havo}-Savuq")
elif 0<havo<20:
    print(f"{havo}-Salqin")
else:
    print(f"{havo}-Issiq")

# 2-misol
a=float(input("Assalomu aleykum mijoz, Xarid summangizni kiriting?\n"))
if a<50000 :
    print(f"Kechirasiz sizga chegirma yo'q")
elif 50000<a<100000:
    print(f"Tabriklaymiz, sizga {(a*5)/100} so'm chegirma bor.")
else:
    print(f"Tabriklaymiz, sizga {(a * 10) / 100} so'm chegirma bor.")

# 3-misol
login=input("Loginingizni kiriting:")
parol=input("Parol kiriting:")
if login=="admin" and parol=="12345":
    print(f"Xush kelibsiz,admin!")
else:
    print("Login yoki parol xato")

# 4-misol
yosh=int(input("Foydalanuvchi yoshingizni kiriting:"))
if yosh<13:
    print(f"Kechirasiz,sizga ushbu film tavsiya etilmaydi!")
elif 13<yosh<17:
    print(f"Siz filmni ota-onangiz bilan ko'rishingiz mumkin.")
else:
    print(f"Siz filmni tamosha qilishingiz mumkin.")

# 5-misol
print("Menyudan taom tanlang:")
print("1 - Osh","2 - Mastava","3 - Shashlik")
tanlov = input("Tanlovingizni kiriting (1-3): ")

if tanlov == "1":
    print("Siz 'Osh' tanladingiz.")
    print("Narxi: 25 000 so'm")
    print("Tayyorlanish vaqti: 20 daqiqa")
elif tanlov == "2":
    print("Siz 'Mastava' tanladingiz.")
    print("Narxi: 18 000 so'm")
    print("Tayyorlanish vaqti: 15 daqiqa")
elif tanlov == "3":
    print("Siz 'Shashlik' tanladingiz.")
    print("Narxi: 30 000 so'm")
    print("Tayyorlanish vaqti: 25 daqiqa")
else:
    print("Bunday tanlov mavjud emas!")
#
# 6-misol
email=input("Email manzilingizni kiriting:")
if email.find("@")==-1 and email.find(".")==-1:
    print("Noto'g'ri email manzil kiritdingiz!")
else:
    print(f"Email qabul qilindi.")

# 7-misol
ball=int(input("Olgan ballingizni kiriting:"))
if 86<ball<100:
    print(f"Siz 5 baho oldingiz.")
elif 70<ball<85:
    print(f"Siz 4 baho oldingiz.")
elif 55<ball<69:
    print(f"Siz 3 baho oldingiz.")
else:
    print(f"Baxoyingiz 2")

# 8-misol
summa=float(input("Kartangizdagi summani kiriting:"))
summa1=float(input("Yechib olmoqchi bo'lgan summani kiriting:"))
if summa<summa1:
    print(f"Hisobingizda yetarli mablag' mavjud emas.")
elif summa1<5000:
    print(f"Minimal yechish summasi 5000 so'm")
else:
    print(f"Pul muvaffaqiyatli yechildi.")

# 9-misol
kun=input("Haftaning qaysi kuni?(Dushanba,Seshanba.........Yakshanba)")
if kun.title()=="Shanba" or kun.title()=="Yakshanba":
    print(f"Bugun dam olish kuni.")
else:
    print("Bugun ish kuni!")

# 10-misol
mb=int(input("Oyiga qancha internet tarifidan foydalanasiz?"))
if mb<1000:
    print(f"Sizga 'Mini' tarifi mos keladi.")
elif 1000<mb<5000:
    print(f"Sizga 'Standard'tarifi mos keladi")
else:
    print(f"Sizga 'Unlimited tarifi mos keladi")


