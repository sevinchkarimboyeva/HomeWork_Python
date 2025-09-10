from itertools import product

from list import mahsulot

talaba_0={
    'ism':'Sevinch',
    'familiya':'Karimboyeva',
    'yosh':19,
    'fakultet':'kompyuter injenering',
    'kurs':2
   }

print(talaba_0.items())

for kalit,qiymat in talaba_0.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat} \n")
mahsulotlar={
'olma':10000,
'anor':20000,
'uzum':40000,
'anjir':25000,
'shaftoli':30000
}

print(mahsulotlar.keys())
print("Dokondagi mahsulotlar:")
for mahsulot in mahsulotlar:
      print(mahsulot.title())

bozorlik=['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


products=sorted(mahsulotlar)
print(products)
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

print(mahsulotlar.values())

print("Mahsulot narxlari:")
for mahsulot in mahsulotlar:
    print(mahsulot)


telefonlar={
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro ',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
}
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar:
    print(tel)

car0={
    'model':'lacetti',
    'rang':'oq',
    'yil':2018,
    'narx':13000,
    'km':50000,
    'korobka':'avtomat'

}
car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narx': 9000,
    'km': 89000,
    'korobka': 'mehanika'

}
car2 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narx': 13000,
    'km': 50000,
    'korobka': 'mexanika'

}

cars=[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}")


dasturchilar={
    'ali':['python','C++'],
    'vali':['html','css','js'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
for ism,tillar in dasturchilar.items():
     print(f"\n {ism.title()} quyidagi dasturlsh tillarini biladi:")
     for til in tillar:
         print(til.upper())














