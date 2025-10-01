import pickle

# with open('data/pi_million_digits.txt','r') as file:
#     txt=file.read().strip()
# pi=txt[2:]
# print(pi)
#
# tugilgan_kunim="24072006"
# if tugilgan_kunim in txt:
#     print(f"{tugilgan_kunim} \nHa,pi soni ichida uchraydi!")
# else:
#     print(f"{tugilgan_kunim} \nYo'q,pi soni ichida uchramaydi!")
#
# pi_son=float(txt)
kitob1={'nomi':'kecha kunduz','muallif':'Cholpon','narxi':45000}
kitob2={'nomi':'Duo taqdirni ozgartiradi','muallif':'Adham Amin','narxi':75000}
kitob3={'nomi':'Avf et Allohim','muallif':'Qadel Akel','narxi':100000}

with open('kitob','wb') as f:
    pickle.dump(kitob1,f)
    pickle.dump(kitob2,f)
    pickle.dump(kitob3,f)
print(kitob1)
print(kitob2)
print(kitob3)


