class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil


    def get_info(self):
            """Shaxs haqida ma'lumot"""
            info=f"{self.ism} {self.familiya} {self.passport} {self.tyil}-yilda tug'ilgan"
            return info

    def get_age(self,yil):
            """Shaxsning yoshini qaytaruvchi metod"""
            return yil-self.tyil

class Talaba(Shaxs):
    """Talaba classi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil=manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_info(self):
            """Shaxs haqida ma'lumot"""
            info=f"{self.ism} {self.familiya} {self.get_bosqich()} {self.idraqam}"
            return info

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

class Manzil:

    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat


    def get_manzil(self):
        manzil=f"{self.viloyat}-viloyati,{self.tuman} tumani, {self.kocha} ko'chasi {self.uy}-uy"
        return  manzil

talaba_manzil=Manzil(12,"Olmazor","Bogbon","Samarqand")
talaba=Talaba("Sevinch","Karimboyeva","AD2730483",2006,98663622,talaba_manzil)
print(talaba.get_info())
print(talaba.get_age(2025))
print(f"ID:{talaba.get_id()} \nBosqichi:{talaba.get_bosqich()}")
print(talaba.manzil.get_manzil())
