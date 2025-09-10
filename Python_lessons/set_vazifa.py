# add()-To'plamga element qo'shish uchun ishlatiladi.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

cars={"bmw",'mercedes benz','volvo','tesla','audi'}
cars.add('mers')
print(cars)

brendlar={'Zara','Dior','Gucci'}
brendlar.add('Iphone')
brendlar.add('Samsung')
print(brendlar)

# clear()-To'plamni tozalaydi.
fruits= {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

cars={"bmw",'mercedes benz','volvo','tesla','audi'}
cars.clear()
print(cars)

brendlar={'Zara','Dior','Gucci'}
brendlar.clear()
print(brendlar)

# copy()-Setdan nusxa oladi.
sonlar={1,2,3,4,5}
sonlar.copy()
print(sonlar)

oyinchoqlar={"qo'g'irchoq",'mashina','quyon','ayiq'}
oyinchoqlar.copy()
print(oyinchoqlar)

phone={'samsung','iphone','infinix'}
phone.copy()
print(phone)

# difference()-birinchi to'plamda bor ammo ikkinchisida yo'q elementni qaytaradi.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

A={1,2,3,4,5}
B={3,4,5,6,7}
c=A.difference(B)
print(c)

harflar={'a','b','c','d'}
unlilar={'a','o','e','u','i'}
h=harflar.difference(unlilar)
print(h)

# difference_update()-bevosita setni o'zgartiradi, yangi set qaytarmaydi.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

A={1,2,3,4,5}
B={3,4,5,6,7}
A.difference_update(B)
print(A)

harflar={'a','b','c','d'}
unlilar={'a','o','e','u','i'}
harflar.difference_update(unlilar)
print(harflar)

# discard()-Set ichiga berilgan elementni o'chiradi agar u element bo'lmasa hech nma chiqarmaydi.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

oyinchoqlar={"qo'g'irchoq",'mashina','quyon','ayiq'}
oyinchoqlar.discard("quyon")
print(oyinchoqlar)

phone={'samsung','iphone','infinix'}
phone.discard('Xonor')
print(phone)

# intersection()-To'plamdagi kesishma vazifasini bajaradi.(ikkisida ham bor elementni qaytaradi)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
a = x.intersection(y,z)
print(a)

harflar={'a','b','c','d'}
unlilar={'a','o','e','u','i'}
q=harflar.intersection(unlilar)
print(q)

 #issubset- ikkinchisining ichida bormi shuni tekshiradi.
#  True → agar hammasi ichida bo‘lsa.
a = {"Musiqa", "Sayr qilish"}
b = {"Musiqa", "Sayr qilish", "Rasm chizish"}
print(a.issubset(b))

a = {"O‘qituvchi", "Shifokor"}
b = {"O‘qituvchi", "Shifokor", "Muhandis"}
print(a.issubset(b))

a = {"Drama", "Komediya"}
b = {"Drama", "Fantastika"}
print(a.issubset(b))


 # remove()- Belgilangan elementni o‘chiradi.Agar element mavjud bo‘lmasa — xato chiqaradi.
a = {"Musiqa", "Sayr qilish", "Rasm chizish"}
a.remove("Sayr qilish")
print(a)

a = {"Drama", "Komediya"}
a.remove("Komediya")
print(a)

# pop()-To'plamdan tasodifiy elementni o‘chiradi va qaytaradi.
a = {"Tabiat", "Sayr qilish", "Rasm chizish"}
print(a.pop())
print(a)

a = {"O‘qituvchi", "Shifokor", "Quruvchi"}
print(a.pop())
print(a)

a = {"Drama", "Komediya", "She’riyat"}
print(a.pop())
print(a)

# issuperset()-Bir set boshqasini ichiga oladimi tekshiradi. True → agar ikkinchi set elementlari birinchida mavjud bo‘lsa.
a = {"Musiqa", "Sayr qilish", "Rasm chizish"}
b = {"Musiqa", "Sayr qilish"}
print(a.issuperset(b))

a = {"O‘qituvchi", "Shifokor", "Muhandis"}
b = {"O‘qituvchi", "Shifokor"}
print(a.issuperset(b))


 # update()-Birinchi setni o‘zgartirib, ikkinchi set elementlarini qo‘shib yuboradi.
a = {"Rasm chizish", "Sport zal"}
b = {"Sayr qilish", "Musiqa"}
a.update(b)
print(a)

a = {"Tarjimon", "Shifokor"}
b = {"Muhandis", "Arxitektor"}
a.update(b)
print(a)

a = {"Drama", "Fantastika"}
b = {"She’riyat", "Roman"}
a.update(b)
print(a)






















