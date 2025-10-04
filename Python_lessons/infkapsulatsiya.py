from uuid import uuid4

class Avto:
    __num_avto=0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto +=1


    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    # def get_km(self):
    #     return self.__km
    #
    # def get_id(self):
    #     return self.__id
    #
    # def add_km(self,km):
    #     if km >=0:
    #         self.__km +=km
    #     else:
    #         print("Mashina km kamaytirib bo'lmaydi")
avto1=Avto("GM","Malibu","qora",2020,40000,100000)
avto2=Avto("GM","Malibu","qora",2020,40000,100000)
avto3=Avto("GM","Malibu","qora",2020,40000,100000)

print(Avto.get_num_avto())

# avto1.add_km(211100)
# print(avto1.get_km())


