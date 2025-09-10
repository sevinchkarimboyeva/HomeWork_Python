# mehmonlar=['Sarvinoz','Dilrabo','Munisa','Nargiza']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni yangi yilga taklif qilamiz.")
#     print(f"Hurmat bilan,Atabekovlar oilasi")
#
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng.")
#
#
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#
# print(sonlar)
# print(sonlar_kvadrati)
#
# dostlar=[]
# print("5 yaqin do'stingizni kiriting:")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:"))
# print(dostlar)

avtolar=['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'volvo':
        print(avto.upper())
    else:
        print(avto.title())

ism=input("Ismingizni kiriting:")
if ism.lower()!='ali':
    print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
else:
    print("Salom,ALi")



javob=float(input("12*6 nechiga teng? >>>"))
if javob!=72:
    print("Javob xato")
else:
    print("Javob to'g'ri")



login=input("Yangi login tanlang:")
if len(login)<=5:
    print("Login 5 harfdan ko'proq bo'lishi shart!")
else:
    print("Login qabul qilindi.")



yosh=int(input("Yoshingizni kiriting:"))
if yosh>65:
    print("Siz COVID-19 risk guruhida ekansiz.")


x,y=25,50
print("x>y") if x>y else print("x<y")
























