# with open("pi.txt") as fayl:
#     pi=fayl.read()
# print(pi)
# print(type(pi))

# fayl=open("pi.txt")
# pi=fayl.read()
# print(pi)
# print(type(pi))
# fayl.close()
#
# pi=pi.rstrip()
# pi=pi.replace('\n', '')
# pi=float(pi)
# print(pi)

# faylnomi='stst.txt'
# with open(faylnomi,'w') as fayl:
#     fayl.write("Sevinch Karimboyeva")
#
#

faylnomi='new_text'
ism="Nodira O'razboyeva "
tyil=2007
with open(faylnomi,'w') as fayl:
    fayl.write(ism)
    fayl.write(str(tyil))


import pickle

talaba1={'ism':'olim','familiya':'husinov','tyil':2006,'kurs':1}
talaba2={'ism':'hasan','familiya':'husanov','tyil':2003,'kurs':2}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('info','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)

print(talaba2)
print(talaba1)



























