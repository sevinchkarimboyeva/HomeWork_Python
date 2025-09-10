from python import fruits

# cars=['bmw','mercedas benz','volvo','general motors','tesla','audi']
# cars.sort()
# print(cars)
# print(sorted(cars,reverse=True))
#
# ages=[12,23,456,755,876,87,54]
# ages.sort()
# print(ages)
# print(sorted(ages,reverse=True))
#
# fruits=['apple','banana','pear','lemon']
# fruits.reverse()
# print(fruits)
#
# ism="Ali"
# print(len(ism))
#
# sonlar=list(range(0,11))
# print(sonlar)
#
# sonlar2=list(range(100))
# print(sonlar2)

toq_sonlar=list(range(1,100,2))
print(f"Toq sonlar:{toq_sonlar}")
narhlar=[12000,45110,14781,255893,1472]
arzon=min(narhlar)
qimmat=max(narhlar)
jami=sum(narhlar)
print(f"Eng arzon narx:{arzon},\n Eng qimmati:{qimmat}, \n Jami:{jami}")

cars=["bmw",'mercedes benz','volvo','general motors','tesla','audi']
my_cars=cars[0:3]
print(my_cars)
print(cars[ :4])
print(cars[2: ])

sonlar=[1,2,3,4,5]
sonlar2=sonlar[:]
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yhati:" ,sonlar)
print("Bu sonlar2 ro'yhati:" ,sonlar2)

tomonlar=(20,30,55)
print(tomonlar)

toys=('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
toys=list(toys)
toys.append("rabbit")
toys.remove("bus")
toys[1]='mcqueen'

toys=tuple(toys)
print(toys)








