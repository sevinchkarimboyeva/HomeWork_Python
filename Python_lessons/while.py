print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol="Istalgan son kiriting"
savol+="(dasturni to'xtatish uchun 'exit' deb yozing )"
while True:
    qiymat=input(savol)
    if qiymat =='exit':
        break
    else:
        print(float(qiymat)**2)


sonlar=list(range(1,1000))
for son in sonlar:
    if son ==10:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")

ismlar=[]
print("Yaqin do'stingiz ro'yxatini tuzamiz.")
n=1
while True:
    savol=input(f"{n}-do'stingizni ismini kiriting:")
    ismlar.append(savol)
    javob=input("Yana ism qo'shasizmi?(ha/yo'q)")
    if javob =='ha':
        n=n+1
        continue
    else:
        break

print(ismlar)

print("Do'stlaringiz yoshini saqlaymiz.")
dostlar={}
ishora=True
while ishora:
    ism=input("Do'stingiz ismini kiriting:")
    yosh=input(f"{ism.title()}ning yoshini kiriting:")
    dostlar[ism]=int(yosh)
    javob=input("Yana ma'lumot qo'shaszmi? (ha/yo'q)")
    if javob=="no":
        ishora=False

for ism,yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

cars=['lasetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)

talabalar=['Sevinch','Sarvish','Shahruza']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning baxosini kiriting:")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba]=baho

print(baholangan_talabalar)























