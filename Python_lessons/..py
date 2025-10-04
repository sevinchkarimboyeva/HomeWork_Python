
def baxola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()}ning baxosini kiriting:")
        baholar[ism]=baho
    return baholar

talabalar=['ali','vali','hasan','husan']
baholar=baxola(talabalar)
print(baholar)


def katta_harf(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar=['ali','vali','husan','hasan']
yangi_ismlar=katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

ismlar=['ali','vali','husan','hasan']
def baxola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning baxosini kiriting:")
        baholar[ism]=baho
    return baholar
baholar=baxola(talabalar)
print(baholar)
print(talabalar)


def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi
print(summa(5,4,5,6,1,8,9,8,65,5,5,65,63,6,5,8,))

def summa(*sonlar):
    return sum(sonlar)

print(summa(3,4,2,1))


def summa(x,y,*sonlar):
    return  x+y+sum(sonlar)
print(summa(3,5,6,6,6,5,4,))

def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1=avto_info("GM",'malibu',rang='qora',yil=2018,narxi=18000)
avto2=avto_info("Kia",'K5',rang='qora',yil=2018,narxi=35000)
print(avto1,avto2)













































