def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib unga salom berivchi funksiya"""

    print(f"Assalomu aleykum,hurmatli {ism.title()}!")

salom_ber("Soliha")
print(salom_ber.__doc__)

def uchburchak_yuzi(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)+p*(p-b)+p*(p-c))**1/2
    print("S=",s)
uchburchak_yuzi(5,4,3)
uchburchak_yuzi(1,2,3)

def toliq_ism(ism,familiya):
    """Foydalanuvchi ism va familiya jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuchi ismi:{ism.title()}\n"
          f"Foydalanuvchi familiyasi:{familiya.title()}")

toliq_ism("ali","valiyev")

def yosh_hisobla(tugilgan_yil,joriy_yil=2025):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(2006)

def toliq_ism_yasa(ism,familiya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism=(f"{ism} {familiya}")
    return toliq_ism
a=toliq_ism_yasa("ali","valiyev")
print(a)

