from sssssss import qiymat

myset={1,'apple',True,'banana',0,'cherry','apple',False}
print(myset)
print(len(myset))
print(tuple(myset))

c=set(('apple','banana','cherry','banana'))
print(c)

son=1
while son<=5:
    print(son, end=" ")
    son=son+1

# while True:
#     print("Salom ")
#

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol="Istalgan son kiriting"
savol+="(dasturni to'xtatish uchun 'exit' deb yozing )"
qiymat=''
while qiymat!='exit':
    qiymat=input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol="Istalgan son kiriting"
savol+="(dasturni to'xtatish uchun 'exit' deb yozing )"
qiymat=True
while qiymat:
    qiymat=input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)