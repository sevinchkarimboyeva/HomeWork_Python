from math import sqrt

def daraja(n):
    return lambda x: x**n
kvadrat=daraja(2)
kub=daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)


import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))

product=lambda x,y : x**y
print(product(3,2))

sonlar=list(range(11))

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return  x*x
print(list(map(daraja2,sonlar)))

kvadratlar=list(map(lambda x:x*x,sonlar))
print(kvadratlar)

a=[4,5,6]
b=[7,8,9]
a_plus_b=list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismla=['Dilrabo','Dilnoza','Dilshoda','Dilora']
print(list(map(lambda matn:matn.upper(),ismla)))

import random as r
sonlar=r.sample(range(100),10)
# def juftmi(x):
#     """x juft bo'lsa,True, aks holda False qaytaruvchi funksiya"""
#     return x%2==0

juft_sonlar=list(filter(lambda son:son%2==0,sonlar))
print(sonlar)
print(juft_sonlar)


mevalar=['olma','anor','anjir','shaftoli',"O'rik",'tarvuz','qovun','banan']
mevalar_b=list(filter(lambda meva:meva.startswith('a'),mevalar))
print(mevalar_b)

mevalar2=list(filter(lambda meva:len(meva)<=4,mevalar))
print(mevalar2)






















