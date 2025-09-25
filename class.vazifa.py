class User:

    def __init__(self,ism,foydalanuvchi_ismi,email,tel_raqam):
        self.foydalanuvchi = foydalanuvchi_ismi
        self.ism=ism
        self.email=email
        self.tel=tel_raqam

    def get_info(self):
        return (f"Foydalanuvchi:{self.foydalanuvchi} \nIsmi:{self.ism} \nEmaili:{self.email}"
                f" \nFoydalanuvchining telefon raqami:{self.tel}")

foydalanuvchi1=User("Dilrabo Baltayeva","Dilrabo1234","dilrabo1234@gmail.com",999877609)
foydalanuvchi2=User("Maftuna Jasurbekova","Jasurbekova05","maftun01@gmail.com",872314253)
foydalanuvchi3=User("O'razmetova Nodira","Nodush07","Nadush4@gmail.com",887491502)
print(foydalanuvchi1.get_info())

print(foydalanuvchi3.ism)
print(foydalanuvchi2.tel)
print(foydalanuvchi1.email)

class Avto:
    def __init__(self,model,rang,karobka,narx,chiqarilgan_yil):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narx=narx
        self.sana=chiqarilgan_yil
        self.kilometr=0

    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_karobka(self):
        return self.karobka
    def get_narx(self):
        return self.narx
    def get_sana(self):
        return self.sana

    def update_km(self):
        return self.kilometr

    def get_info(self):
     return (f"Avtomobil {self.model},uning rangi {self.rang} karobka {self.karobka} va uning narxi {self.narx}$ u"
             f" {self.sana}-yilda ishlab chiqarilgan.")

avtomobil=Avto("Jentra",'qora',"avtomat",35000,2022)
print(avtomobil.get_narx())
print(avtomobil.get_sana())

print(avtomobil.get_info())

avtomobil.kilometr=2
print(avtomobil.kilometr)


class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
        self.nomi=salon_nomi
        self.manzil=manzili
        self.sotuvda=sotuvdagi_avtomobillar
        self.avtomobilla=0
        self.avtomobillar=[]

    def add_avto1(self,avto):
        self.avtomobillar.append(avto)
        self.avtomobilla +=1
    def get_a(self):
        return (avto.get_info() for avto in self.avtomobillar)

    def get_info(self):
        return (f"{self.nomi} nomli avtosalonda {self.sotuvda} ta avtomobil sotiladi. Manzili:{self.manzil}")

# mashina=Avtosalon("URGANCH")
avtomobil1=Avtosalon("BYD Urganch","Fayozov ko'chasi,10",200)
avtomobil2 = Avtosalon("Chery Urganch", "Sanoatchilar ko'chasi,25", 120)
#
# mashina.add_avto1(avtomobil1)
# mashina.add_avto1(avtomobil2)

print(avtomobil1.get_info())

print(dir(str))
print(dir(Avto))
print(dir(avtomobil))














