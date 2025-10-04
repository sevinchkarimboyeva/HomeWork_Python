#
# class Shaxs:
#     def __init__(self,ism,familiya,yil,tel_raqam):
#         self.ism=ism
#         self.familiya=familiya
#         self.yil=yil
#         self.raqam=tel_raqam
#
#     def get_info(self,):
#         return f"Ismi:{self.ism},Familiyasi:{self.familiya},{self.yil}-yilda tug'ilgan.Tel raqami:{self.raqam}"
#
# class Talaba(Shaxs):
#     def __init__(self,ism,familiya,yil,tel_raqam,idraqam):
#         super().__init__(self,ism,familiya,yil,tel_raqam)
#         self.idraqam=idraqam
#         self.fanlar=[]
#
#     def fanga_yozil(self):
#         pass
#
#
#
#
# class Professor(Shaxs):
#     """Shaxs klassidan vorislik oladi."""
#
#     def __init__(self, ism, familiya, passport, yil,fan, daraja):
#         super().__init__(self,ism, familiya, passport)
#         self.daraja = daraja
#         self.fan= fan
#
#     def dars_ber(self, fan_nomi):
#         return f"Professor {self.familiya} {self.ism} {fan_nomi.nomi} fanidan dars beryapti."
#
#     def get_info(self):
#         return f"Professor: {self.ism} {self.familiya}. Daraja: {self.daraja} da,{self.fan}-dan dars beryapti."
#
#
# class Foydalanuvchi(Shaxs):
#     """Shaxs classidan vorislik oladi"""
#
#     def init(self, ism, familiya, passport, yil,foydalanuchi_nomi,parol):
#         super().__init__(ism, familiya, passport, yil,parol)
#         self.f_nomi=foydalanuchi_nomi
#         self.parol=parol
#
#
#     def id_raqam(self):
#         return f"Foydalanuvchi {self.f_nomi} tizimga kirdi."
#
#     def get_info(self):
#         return f"Foydalanuvchi: {self.ism} {self.familiya}. Username: {self.f_nomi}. Paroli:{self.parol}"
#
#
# class Admin(Foydalanuvchi):
#     """Foydalanuvchi classidan vorislik oladi"""
#
#     def __init__(self, ism, familiya, passport, yil,foydalanuvchi_nomi,daraja):
#         super().init(ism, familiya, passport, yil,foydalanuvchi_nomi,daraja)
#         self.daraja = daraja
#
# v
#     def get_info(self):
#         return f"Admin: {self.ism} {self.familiya}. Username: {self.f_nomi}. Daraja: {self.daraja}"
#
#
# professorr = Professor("Sarvinoz", "Karimova", "AD7654321", 2000, "Matematika", "Dotsent")
# print(professorr.get_info())
#
# admin1 = Admin("Xanimjon", "Berdiboyeva", "AD9988776", 2007, "xanusha_07", "12345678")
# print(admin1.get_info())
#
#
