dictionaries={
    'Boolean': "Mantiqiy qiymat",
    'Float': "0'nlik son",
    'For': 'Biror amalni qayta-qayta bajarish tsikli',
    ' If':"Shartlarni tekshirish operatori",
    'Integer':"Butun son",
    'capitalize':"Gapdagi birinchi harf katta bo'ladi",
    'copy':"lug'atdan nusxa oladi",
    'upper':"Barcha harflari katta harflarga aylantiradi",
}
print(dictionaries.items())

for kalit,qiymat in sorted(dictionaries.items()):
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat} \n")


davlatlar={
    'Aqsh':"Vashington",
    'Italiya':"Rim",
    'Malayziya':"Kuala-Lumpur",
    "O'zbekiston":"Toshkent",
    "Qirg'iziston":"Bishkek",
    "Qozog'iston":"Nursulton",
    'Rossiya':"Moskva",
    'Singapur':"Singapur",
    'Tojikiston':"Dushanbe ",
}
for davlat in sorted(davlatlar.keys()):
    print(f"Davlatlar:{davlat}")
for poytaxt in davlatlar.values():
    print(f"Davlatlarning poytaxtlari:{poytaxt}")


sorov = input("Qaysi davlatning poytaxtini bilishni istaysiz? : ").strip().upper()
poytaxt =davlatlar.get(sorov)
if poytaxt:
     print(f"{sorov} ning poytaxti {poytaxt} shahri.")
else:
    print("Kechirasiz, bizda bu haqda ma'lumot yo'q.")


kinolar = {
    'Sarvinoz' : ['Oila uchun', '365 kun', 'Sen yetim emassan'],
    'Dilrabo' : ['Suyunchi', 'Samodagi bolalar', 'Charxpalak'],
    'Xanimjon' : ['Qora niyat', 'Yerning oxirgi kuni', 'Opa-singillar'],
    'Shahruza' : ['Sotqin', 'Tilim qursin','Onam bilmasin'],
    'Shukuroy' : ['Fotima-Zuhra', 'Tundan-tonggacha', 'Oshiqlar']
}
for ism, kino in kinolar.items():
    print(f"\n{ism}ning Sevimli kinolari : ")
    for cenema in kino:
        print( cenema.upper())

davlatlar = {
    'Uzbekiston' : {
        'poytaxt' : 'Toshkent',
        'hududi' : '448 978 kv.km',
        'axolisi' : 38_000_000,
        'pul birligi' : "so'm"
},
    'Rassiya' : {
        'poytaxt' : 'Moskva',
        'hududi' : '17 098 246 kv.km',
        'axolisi' : 144_000_000,
        'pul birligi' : "rubl"
},
    'AQSH' : {
        'poytaxt' : 'Vashington',
        'hududi' : '9 631 418 kv.km',
        'axolisi' : 327_000_000,
        'pul birligi' : "dollar"
},
    'Malayziya' : {
        'poytaxt' : 'Kuala-Lumpur',
        'hududi' : '326 750 kv.km',
        'axolisi' : 25_000_000,
        'pul birligi' : "rinngit"
}
}

for kalit, qiymat in davlatlar.items():
    print(f"\n {kalit}ning poytaxti {davlatlar[kalit]['poytaxt']}\n"
          f" hududi {qiymat['hududi']}\n"
          f" axolisi {qiymat['axolisi']}\n"
          f" pul birligi {qiymat['pul birligi']}")




# clear()-Lug'atdagi barcha kalit-qiymat juftliklarini o'chiradi.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

talaba= {
  "ism": "Sevinch",
  "familiya":'Karimboyeva',
  "year": 2006
}
talaba.clear()
print(talaba)
kiyim = {
  "brand": "Zara",
  "fasoni": "uzun",
}
kiyim.clear()
print(kiyim)

# copy()-Lug'atdan nusxa olish uchun ishlatiladi.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a=car.copy()
print(a)

talaba= {
  "ism": "Sevinch",
  "familiya":'Karimboyeva',
  "year": 2006
}
b=talaba.copy()
print(b)
kiyim = {
  "brand": "Zara",
  "fasoni": "uzun",
}
c=kiyim.copy()
print(c)

# fromkeys()-U berilgan kalitlar ro'yhati asosida yangi lug'at yaratadi.
a=('rabbit','dog','bear')
b=1
c=dict.fromkeys(a,b)
print(c)

a=('Sarvinoz','Shahruza','Shukurjon')
b=0
c=dict.fromkeys(a,b)
print(c)

a=(1,2,3)
b='talaba'
c=dict.fromkeys(a,b)
print(c)

# pop()-Lug'atdagi biror bir elementni jufti bn sug'irib oladi.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

talaba= {
  "ism": "Sevinch",
  "familiya":'Karimboyeva',
  "year": 2006
}
talaba.pop('familiya')
print(talaba)

kiyim = {
  "brand": "Zara",
  "fasoni": "uzun",
}
kiyim.pop("fasoni")
print(kiyim)

# popitem()-U lug'atdagi oxirgi qo'shilgan elementni olib tashlaydi uni juftlik sifatida qaytaradi.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

talaba= {
  "ism": "Sevinch",
  "familiya":'Karimboyeva',
  "year": 2006
}
talaba.popitem()
print(talaba)

kiyim = {
  "brand": "Zara",
  "fasoni": "uzun",
}
kiyim.popitem()
print(kiyim)

# setdefaults()-Bu kalitni tekshiradi va kk bo'lsa qo'shib qo'yadi.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

talabalar = {
    "Ali": {"yosh": 20},
    "Vali": {"yosh": 19},
    "Hasan": {"yosh": 21}
}
x = car.setdefault("Ali", 20)
print(x)

talaba = {"ism": "Guli", "yosh": 20}
print(talaba.setdefault("kurs", 1))
print(talaba)

# update()-yangilash yoki lug'atga yangi qiymat qo'shish uchun ishlatiladi
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

oquvchi= {
  "ism": "Lobar",
  "familiya":'Karimboyeva',
  "year": 2009
}
oquvchi.update({"o'zlashtirishi":"Yaxshi"})
print(oquvchi)

koylak = {
  "brand": "Zara",
  "fasoni": "uzun",
}
koylak.update({"Sifati":"Ajoyib"})
print(koylak)


































