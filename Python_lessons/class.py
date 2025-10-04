class Talaba:
    """Talaba nomli class yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1

    def get_name(self):
        return self.ism
#
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def tanishtir(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}.{self.tyil} yilda tug'ilganman"
#
#
#
#     def get_ege(self,yil):
#         return yil-self.tyil
#
#
# talaba1=Talaba("Alijon","Valiyev",2000)
# talaba2=Talaba("OLim","OLIMOV",2002)
# talaba3=Talaba("Alijon","Valiyev",2000)
# talaba4=Talaba("Alijon","Valiyev",2000)
#
#
# print(talaba1.ism,talaba1.familiya,talaba1.tyil)
# talaba2.tanishtir()
# print(talaba4.get_name())
# print(talaba1.get_lastname())
# print(talaba3.get_ege(2025))


    def get_info(self):
     return f"{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi"

    def set_bosqich(self,bosqich):
        self.bosqich=bosqich

    def update_bosqich(self):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich +=1


talaba1=Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())

talaba1.bosqich=2
print(talaba1.bosqich)

