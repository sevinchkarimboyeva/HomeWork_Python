car_0={'model':"ferrari",'rang':'qizil'}
print(car_0)
print(car_0["model"])
print(car_0["rang"])

talaba_0={'ism':"murod olimov",'yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tug'ilgan,\
 {talaba_0['yosh']} yoshda")

talaba_1={}
talaba_1['ism']="Shahruza Atanazarova"
talaba_1['yosh']=20
print(talaba_1)

talaba_1['kurs']=4

del talaba_1['kurs']
print(f"Talaba {talaba_1['ism'].title()}")
print(talaba_1)

telefonlar={
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}

print(telefonlar)
phone=telefonlar['ali']
phone1=telefonlar.get('eldor',"Bunday ism mavjud emas")

print(f"Alining telefoni:{phone}")
print(f"Orifning telefoni:{phone1}")

