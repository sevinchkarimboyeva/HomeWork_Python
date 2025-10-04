# import modul
# import modul as m

# from modul import avto_info as ai,info_print as ip


avto1=avto_info("GM","Malubu","qora","Mehanika",2016,4000000)
info_print(avto1)

import math
from math import pi
x=400
print(math.sqrt(x))
print(pi)
print(pow(2,4))

print(math.log2(8))
print(math.log10(100))

import  random as r
son=r.randint(0,100)
print(son)

ismlar=['olim','anvar','hasan','husan']
ism=r.choice(ismlar)
print(ism)
print(r.choice(ism))

x=list(range(0,51,5))
print(x)
print(r.choice(x))
x=list(range(11))
print(x)

# shuffle()-Ro'yxat ichidagi elementlarning tartibini o'zgartiradi yani aralashtiradi.
# Bu metod faqat listlarda ishlaydi yoki listga aylantirib kn qo'llasa bo'ladi
import random
mylist = ["apple", "banana", "cherry"]
print(random.shuffle(mylist))

toys=['dog','rabbit','car','boat']
print(random.shuffle(toys))

# sample()-
import random

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))





















