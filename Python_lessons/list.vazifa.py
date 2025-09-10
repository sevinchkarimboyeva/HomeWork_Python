# clear()-ro'yhatdagi barcha elementlarni o'chirib, uni bo'sh qiladi.
fruits=["apple","banana","cherry"]
fruits.clear()
print(fruits)
family=["father","mother","sister","brother"]
family.clear()
print(family)
hafta_kunlari=['Dushanba','Seshanba','chorshanba']
hafta_kunlari.clear()
print(hafta_kunlari)

# copy()-listdagi elementlardan nusxa oladi.
sweets=["biscuit",'cookies','four']
sweet=sweets.copy()
print(sweet)
clothes=['shirt','shoes','shorts','skirt']
clothes1=clothes.copy()
print(clothes1)
mevalar=['olma', 'anor','nok',"o'rik",'uzum']
mevalar1=mevalar.copy()
print(mevalar)

# extend()-bir ro'yhatni ikkinchisiga qo'shib bir list paydo qiladi.
mevala_r=['anjir','shaftoli']
yangi_mevalar=['kivi','ananas','banan']
mevala_r.extend(yangi_mevalar)
print(mevala_r)
sabzavotlar=['kartoshka','piyoz']
sabzavot=['sabzi']
sabzavotlar.extend(sabzavot)
print(sabzavotlar)
hayvonlar=["bo'ri","sher","yo'lbars"]
uy_hayvonlari=['it','mushuk']
hayvonlar.extend(uy_hayvonlari)
print(hayvonlar)

# index()-shu listga yozilgan elementni indeksini topadi.
sweets=["biscuit",'cookies','four']
sweet=sweets.index("biscuit")
print(sweet)
clothes=['shirt','shoes','shorts','shirt']
clothes1=clothes.index('shoes')
print(clothes1)
sonlar=[12,34,21,67,89,37]
son=sonlar.index(37)
print(son)

# pop()-ro'yhatdagi elementni olib tashlash uchun ishlatiladi.
mevalar=['olma', 'anor','nok',"o'rik",'uzum']
mevalar1=mevalar.pop()
print(mevalar)
number=[11,23,554,56778,88990,12345,890765]
num=number.pop(2)
print(number)
bozorlik=['yog','un','piyoz','banan',"go'sht"]
mahsulot=bozorlik.pop(3)
print(bozorlik)

# reverse()-Listdagi elementlarning tartibini teskariga o'zgartiradi.
sOnlar=[1,2,3,4,5]
sOnlar.reverse()
print(sOnlar)
cars=['Lasetti', 'Nexia 3', 'Cobalt']
cars.reverse()
print(cars)
ichimliklar=['cola','fanta','choy','cofee','suv']
ichimliklar.reverse()
print(ichimliklar)

# sort()-Ro'yhatdagi elementlarni tartib bo'yicha saralaydi.
sOnlar=[1,2,3,4,5]
sOnlar.sort()
print(sOnlar)
cars=['Lasetti', 'Nexia 3', 'Cobalt']
cars.sort()
print(cars)
ichimliklar=['cola','fanta','choy','cofee','suv']
ichimliklar.sort()
print(ichimliklar)

















