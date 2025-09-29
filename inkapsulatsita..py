class Kitob:
    __kitoblar_soni=0
    def __init__(self,nomi,muallif,sahifa,narx):
        self.__nomi=nomi
        self.__muallif=muallif
        self.__sahifa=sahifa
        self.__narxi=narx

        Kitob.__kitoblar_soni +=1

    def get_nomi(self):
        return self.__nomi
    def get_muallif(self):
        return self.__muallif
    def get_sahifa(self):
        return self.__sahifa

    def get_muallif(self):
        return self.__muallif

    def set_sahifa(self,yangi_sahifa):
        if yangi_sahifa >0:
            self.__sahifa=yangi_sahifa
        else:
            print(f"Kechirasiz,kitobning sahifasi manfiy bo'lmaydi!")

    @classmethod
    def kitoblar_soni(cls):
        return cls.__kitoblar_soni

class Kutubxona:
    __kutubxonalar_soni=0

    def __init__(self,nomi):
        self.__nomi=nomi
        self.__kitoblar=[]
        Kutubxona.__kutubxonalar_soni +=1

    def get_nomi(self):
        return self.__nomi

    def set_nomi(self,yangi_nom):
        self.__nomi=yangi_nom


    def kitob_qosh(self,kitob):
        self.__kitoblar.append(kitob)
        print(f"{kitob.get_nomi()} kutubxonaga qo'shildi.")
    def kitoblar_royxati(self):
        if not self.__kitoblar:
            print("Kechirasz,Kutubxonada hali kitoblar yo'q")

        else:
            print(f"{self.__nomi} kutubxonadagi kitoblar:")

        for kitob in self.__kitoblar:
            print(f"{kitob.get_nomi()} {kitob.get_muallif()}")

    @classmethod
    def kutubxonalar_soni(cls):
        return cls.__kutubxonalar_soni

k1 = Kutubxona("Yoshlar kutubxona")
k2 = Kutubxona("Axborot resurslari")


kitob1 = Kitob("Ikki eshik orasi", "O'tkir Hoshimov", 717,30000)
kitob2 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 350,45000)
kitob3=Kitob("Yashamoq","Yoy Xya",300,75000)
kitob4=Kitob("Duo taqdirni o'zgartiradi","Adham Amin Nemutlu",273,90000)
kitob5=Kitob("Avf et Allohim","Qadir Akel",452,150000)

k1.kitob_qosh(kitob1)
k1.kitob_qosh(kitob2)
k2.kitob_qosh(kitob4)
k2.kitob_qosh(kitob3)
k1.kitob_qosh(kitob5)

k1.kitoblar_royxati()
k2.kitoblar_royxati()

print("Kitoblar soni:", Kitob.kitoblar_soni())
print("Kutubxonalar soni:", Kutubxona.kutubxonalar_soni())







