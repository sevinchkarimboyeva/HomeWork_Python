mevalar=['olma', 'anjir','shaftoli',"o'rik"]
narxlar=[12000,18000,10900,22000]
sonlar=['bir','ikki',3,4,5]
ismlar=[]
print(mevalar)
print(narxlar)
print(sonlar)
print(ismlar)

print(mevalar[0].title())
print(mevalar[2].upper())
print(narxlar[3]+narxlar[2])
print(sonlar[4])
print(ismlar)

narxlar[0]=13000
narxlar[2]=11000
narxlar[3]=narxlar[3]+2000
print(narxlar)

mevalar=['olma', 'anjir','shaftoli',"o'rik"]
mevalar.append("tarvuz")
print(mevalar)

cars=[]
cars.append("Lasetti")
cars.append("Nexia 3")
cars.append("Cobalt")
print(cars)

cars=['Lasetti', 'Nexia 3', 'Cobalt']
cars.insert(0,"Malibu")
print(cars)
cars.insert(2,"Damas")
print(cars)

mevalar=['olma', 'anjir','shaftoli',"o'rik"]
del mevalar[1]
print(mevalar)
mevalar.remove("shaftoli")
print(mevalar)

hayvonlar=['it','mushuk','sigir','qoy','quyon','mushuk']
hayvonlar.remove("mushuk")
print(hayvonlar)

bozorlik=['yog','un','piyoz','banan',"go'sht"]
mahsulot=bozorlik.pop(3)
print("Men" + mahsulot + "sotib oldim")
print("Olinmagan mahsulotlar:" , bozorlik)























