import random
"""Har safar bir xil tasodifiy sonni oladi."""
random.seed(10)
print(random.random())

random.seed(12)
for a in range(4):
    print(random.randint(1,20))

import random
"""Tasodifiy sonni saqlab turib kn yana o'sha nuqtada davom ettirishi mumkin. """
x = random.getstate()
print(x)

#  Tasodifiy sonlar ketma-ketligini qayta tiklash uchun ishlatiladi.
print(random.random())
state = random.getstate()
random.setstate(state)

#getrandbits()-tasodifiy bitli son qaytaradi.
print(random.getrandbits(8))
print(random.getrandbits(16))

# randrange()-Range ichidan tasodifiy butun son tanlaydi
print(random.randrange(1, 9))

print(random.randrange(30,50))

 # choices()-Ro'yhatdan istalgan tasodifiy element tanlaydi vat takroriy bo'lishi ham mumkin.
mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist))

son=[1,2,3,4,5,6,7,8,9,10]
print(random.choices(son))

# shuffle()-Ro'yxat ichidagi elementlarning tartibini o'zgartiradi yani aralashtiradi.
# Bu metod faqat listlarda ishlaydi yoki listga aylantirib kn qo'llasa bo'ladi
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

toys=['dog','rabbit','car','boat']
random.shuffle(toys)
print(toys)

# sample()-listdan takrorlanmas tarzda k ta tasodifiy elementni tanlaydi.
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))

toys=['dog','rabbit','car','boat']
print(random.sample(toys,k=3))

# uniform()-Berilgan oraliqdagi tasodifiy float sonni qaytaradi.
print(random.uniform(20, 60))

print(random.uniform(12,24))

# triangular()-uchburchak taqsimotga asoslangan tasodifiy float son qaytaradi.
print(random.triangular(20, 60, 30))

print(random.triangular(34,25,7))

#betavariate()-Extimollik nazariyasi va statikada ishlatiladi.
son=random.betavariate(7,9)
print(son)

num=random.betavariate(23,43)
print(son)

# expovariate()-qandaydir hodisa qachon sodir bo'ladi-shu vaqtni tasodifiy tarzda belgilaydi.

a=random.expovariate(2.3)
print(a)

b=random.expovariate(4.5)
print(b)

# gauss()
a=random.gauss(100.3)
print(a)

b=random.gauss(34.5)
print(b)

# normalvariate()-Oddiy taqsimotga asoslangan tasodifiy float sonini qaytaradi.
print(random.normalvariate(0,1))

print(random.normalvariate(10,20))

# vonmisesvariate()- taqsimotiga asoslangan tasodifiy float sonini qaytaradi
# yo'nalish statistikasida foydalaniladi

print(random.vonmisesvariate(2,30))

print(random.vonmisesvariate(56,99))

# Paretovariate()- taqsimotiga asoslangan tasodifiy float sonini qaytaradi.
# ehtimol nazariyalarida qo'llaniladi

print(random.paretovariate(100))

print(random.paretovariate(-10))

# weibullvariate()- taqsimotiga asoslangan tasodifiy float sonini qaytaradi.
# statistikada ishlatiladi
print(random.weibullvariate(1,100))

print(random.weibullvariate(7,90))

























