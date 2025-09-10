# capitalize()- gapdagi birinchi harf katta bo'ladi.

meva="men bozordan olma va banan sotib oldim."
meva_1=meva.capitalize()
print(meva_1)
time="bugun dars bo'lmaydi."
time_1=time.capitalize()
print(time_1)
uy="Uyda kimdur bormi?"
uy_2=uy.capitalize()
print(uy_2)


# casefold()-barcha harfni kichik harflarga aylantiradi.

parents="Biz Oilada 3 ta Qizmiz."
parents_1=parents.casefold()
print(parents_1)
bekend="DARSIMIZ HAR JUFT KUNLARI BO'LADI"
bekend1=bekend.casefold()
print(bekend1)
oila="oilada 8 kishimiz"
oila2=oila.casefold()
print(oila2)


# center()-bosh joylar bilan markazlashadi.

meva3="Banana"
m_eva=meva3.center(10)
print(m_eva)
sabzavot="kartoshka,sabzi"
sabzavot1=sabzavot.center(30)
print(sabzavot1)
ichimlik="cola"
ichk=ichimlik.center(2)
print(ichk)


# count() -countga yozilgan so'z matnda necha marta takrorlaganini ko'rsatadi.

txt=" Sabina bozordan 3 ta qavun olgan shundan 1 ta qavuni mazzali chiqqan."
txt1=txt.count("qavun")
print(txt1)
kitob="Menga kitoblar yoqadi"
kitb=kitob.count("kitob")
print(kitb)
s="Javohir bugun ingliz tilidan 37/30 oldi"
s1=s.count("baxo")
print(s1)


# encode()-matnni bayt ko'rinishiga o'tkazish uchun ishlatiladi.

name="My name is Sevinch"
na_me=name.encode()
print(na_me)
surname="My surname is Karimboyeva"
sur=surname.encode()
print(na_me)
yosh=" I am old 19 years"
yoshs=yosh.encode()
print(yoshs)


# enswith()-tinish belgilarni to'gri yoki noto'g'ri qo'yilganinini ko'rsatadi.

a="Hello,How are you"
a1=a.endswith(",")
print(a1)
b="Javohir kech qoldi."
b1=b.endswith(".")
print(b1)
c="Lobar yalqov bo'lib o'tiribdi😒"
c1=c.endswith(".")
print(c1)


# expandtabs()- matn ichidagi /t bosh joylarga almashtirish uchun ishlatiladi.

txt = "H\ti"
print(txt.expandtabs(3))
txt = "S\ta\tl\to\tm"
print(txt.expandtabs())
txt = "S\te\tv\ti\tn\tc\th"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(4))


# find()-FINDGA YOZILGAN SO'ZNI O'LCHAMINI AYTADI

mmm="Darsda kimlar yo'q"
m1=mmm.find("kimlar")
print(m1)
fruits="Dukonda olma qolmabdi."
fruits1=fruits.find("olma")
print(fruits1)
boys="Bolalar uyga kirmadi"
boy=boys.find("bolalar")
print(boy)


# format()-O'zgaruvchining matnga qo'yish,formatlash uchun ishlatiladi.

kiyim="Bu kiyim {price:.2f} dollars!"
print(kiyim.format(price=30))
kiyim="Buni {price:.2f} dollarga olib bermayman!"
print(kiyim.format(price=92))
phone="Bu phone {price:.2f} dollars!"
print(phone.format(price=1000))


# format_map()-formatga o'xshaydi lekin lug'at bilan ishlaydi.

txt = "Name: {name} ; Age: {age}"
print(txt.format_map({'name': 'Sevinch', 'age': 19}))
txt = "T-shirt: {color} ; Price: {how much?}"
print(txt.format_map({'color':'White' , 'how much?': '10 dollars'}))
txt = "Country: {for} , City: {do}".format_map({'for':'Uzbekistan','do':'Hazorasp'})
print(txt)


# INDEX()-matn ichidan birinchi uchragan indeksni topadi.

x="Hello world"
x1=x.index("Hello")
print(x1)
s="shahrizoda qaydasan"
s1=s.index("shahrizoda")
print(s1)
ISM="soliha,lobar"
isM=ISM.index("soliha")
print(isM)


# isalnum()-true yoki false qaytaradi.

txt = "Python3"
print(txt.isalnum())
txt = "Hello World"
print(txt.isalnum())
txt = "123456"
print(txt.isalnum())


# isalpha()-matn ichida faqat harflar bo'lsa true aks holda false qaytaradi.

txt = "HelloWorld"
print(txt.isalpha())
txt = "Python3"
print(txt.isalpha())
txt = "OpenAI"
print(txt.isalpha())


# isascii()-faqat inglizcha belgilarni tekshiradi.

txt = "tea"
print(txt.isascii())
txt = "123456"
print(txt.isascii())
txt = "Dunyo123"
print(txt.isascii())
number = "56789"


# isdecimal()-faqat (0-9) yoki shu kabi decimal raqamlarni tekshiradi.

print(number.isdecimal())
number = "12.34"
print(number.isdecimal())
number = "987654"
print(number.isdecimal())


# isdigit()-decimal raqamlar va boshqa raqamga o'xshash belgilar masalan kvadrat ildiz kabi.

txt = "12345"
print(txt.isdigit())
txt = "1234a"
print(txt.isdigit())
txt = "987654"
print(txt.isdigit())


# isidentifier()-Python identifikatori sifatida yaroqliligini tekshiradi.

txt = "my_var"
print(txt.isidentifier())
txt = "2cool"
print(txt.isidentifier())
txt = "_private"
print(txt.isidentifier())


# islower()-matndagi hardlarning barchasi kichik bo'lsa True.

txt = "python programming"
print(txt.islower())
txt = "12345!"
print(txt.islower())
txt = "hello world 123"
print(txt.islower())


# isnumeric()-barcha turdagi raqamlar bilan ishlaydi.

txt = "123456"
print(txt.isnumeric())
txt = "12.34"
print(txt.isnumeric())
txt = "2025"
print(txt.isnumeric())


# join()-u elementlarni bitta satrga birlashtirish uchun ishlatiladi.
myList = ["Apple", "Banana", "Pear"]
x = ", ".join(myList)
print(x)
myTuple = ("Dilrabo","Sarvinoz","Shahzoda")
x = " and ".join(myTuple)
print(x)
words = ("Today", "the", "weather", "is", "good")
x = " ".join(words)
print(x)


# ljust()-satrlarni chapga tekislab,o'ng tomonini boshqa belgi bilan to'ldirish uchun ishlatiladi.

animal = "rabbit"
x = animal.ljust(10)
print(animal, "is very friendly.")
animal = "cat"
animal = animal.ljust(8)
print(animal, "is a lovely pet.")
cars = "car"
c = txt.ljust(8)
print(x, "is fast.")


# lower()-barcha harflarni kichik harfga o'zgartiradi.
txt = "HELLO"
print(txt.lower())
txt = "Hello"
print(txt.lower())
txt = "hello"
print(txt.lower())


# lstrip()-chap tarafdan bosh joylarni olib tashlaydi.

salom= "\n\nHello"
x = txt.lstrip()
print("Greeting:", x)
mushuk = "    cat   "
x = txt.lstrip()
print("Animal:", x)
matn = "\n\nHello"
x = txt.lstrip()
print("Greeting:", x)


# maketrans()-satrlarni almashtirish uchun ishlatiladi translate bn birga kelad.

write= "Apple and Banana"
table = str.maketrans("AB", "XY")
print(txt.translate(table))
cats = "Cat and Rabbit"
m11 = str.maketrans("CR", "AB")
print(txt.translate(m11))
mevA = " Uzum va Anjir"
mytab = str.maketrans("UB", "SH")
print(txt.translate(mytab))


# partition()-satrni uch qismga bo'lib beradi.

tx = "I could eat bananas all day"
y= tx.partition("bananas")
print(y)
hafta = "Bugun haftaning yakshanba kuni"
y= tx.partition("yakshanba")
print(y)
havo= "Bugun havo anch issiq"
y= havo.partition("issiq")
print(y)


# replace()-satr ichidagi belgilar yoki so'zlarni boshqasiga almashtirib beradi.

kongil = "Dilrabo hamisha kulib yuridi"
x = txt.replace("kulib", "hafa")
print(x)
best = "U mening eng yaxshi do'stim."
x = best.replace("yaxshi", "yomon")
print(x)
xx = "Shahruza menga yoqmidi"
x = xx.replace("yoqmidi", "yoqadi😍")
print(x)


# rfind()-agar matn topilmasa -1 qaytaradi.

txt = "Hello world!"
print(txt.rfind("world"))
txt = "Hello world!"
print(txt.rfind("q"))
txt = "Hello ,how are you"
print(txt.rfind("0",5,20))


# rindex()-agar matn topilmasa  ValueError qaytaradi.

txt = "Hello world!"
print(txt.rindex("world"))
txt = "Hello world!"
print(txt.rindex("o",4,20))
txt = "Hello how are you have a good day!"
print(txt.rfind("q"))


# rjust()-o'ngga tekislab chapdagi boshliqni boshqa qiymat bilan to'ldiradi.

a = "20"
print(a.rjust(5,"1"))
b = "Soliha"
print(b.rjust(20,"!"))
ss = "Job"
print(ss.rjust(20))


# rpartition()-o'ngdan birinchi uchragan ajratuvini oladi.

num = "apple-banana-cherry"
print(num.rpartition("-"))
num2 = "I go to work, I'm working"
print(num2.rpartition("work"))
num3 = "Hello wold!"
print(num3.rpartition("o"))


#split()-satrni bo'laklarga achratib list qilib qaytaradi.

txt = "apple,banana,pear"
x = txt.split(',')
print(x)
nums = "one|two|three|four"
x = nums.split('|')
print(x)
s0n = '1,2,3,4,5,6,7,8,9,10'
x = s0n.split(',')
print(x)


# splitlines()-satrni qatorlar boyicha ajratadi va list qilib chiqaradi.

txt = "Line 1\nLine 2\nLine 3"
lines = txt.splitlines()
print(lines)
manzara = "Tabiat qo'ynida o'tirish mazza"
Manzara = manzara.splitlines()
print(Manzara)
fasl= "Kuz kelyapti......."
lines = txt.splitlines()
print(fasl)


# isprintable()-Satr ichidagi barcha belgilar ekranga chiqarilishi mn bo'lsa true qiymat qaytaradi.

txt = "Lobar ish qilyapti"
print(txt.isprintable())
txt = "Sevinch ismining ma'nosi quvonch"
print(txt.isprintable())
txt = "Hello \tI'm 19"
print(txt.isprintable())


# isspace()-Faqat bo'shliqdan iboratligini tekshiradi.

txt = "   "
print(txt.isspace())
txt = "  !  "
print(txt.isspace())
txt = "  \t  \n"
print(txt.isspace())


# title()-Har bir so'zni bosh harf bilan yozadi.

b= "salom python"
print(b.title())
b = "Yaxshi kun"
print(b.title())
b = "hammasi uchun raxmat"
print(b.title())


# istitle()-Har bir sozning birinchi harfi katta qolgani kichik bo'lsa true.

txt = "Hello Python"
print(txt.istitle())
txt = "hello python"
print(txt.istitle())
txt = "HELLO PYTHON"
print(txt.istitle())


# isupper()-Matndagi harflarning barchasi katta bo'lsa True.

txt = "Hello Python"
print(txt.isupper())
txt = "hello python456"
print(txt.isupper())
txt = "HELLO PYTHON"
print(txt.isupper())


# translate()-Belgilarni almashtirish yoki o'chirish uchun ishlatiladi.

mydict = {97: 111}
txt = "apple"
print(txt.translate(mydict))
mydict = {32: 45}
nature= "Tabiat"
print(txt.translate(mydict))
mydict = {11:231}
rasm= "Manzara rasmi"
print(txt.translate(mydict))


# upper()-barcha harflari katta harflarga aylantiradi.

aralash= "123abcDEF"
x =aralash.upper()
print(x)
dastur = "python eng oson dasturlash tili"
x = dastur.upper()
print(x)
s = "Alhamdulillah❤️"
x = s.upper()
print(x)


# zfill()-Satrni belgilangan uzunlikgacha chap tomondan nol bilan to'ldiradi.

a = "1000"
print(a.zfill(5))
y = "yaxshiiii"
print(y.zfill(10))
yaxshi = "hammasi yaxshi"
print(yaxshi.zfill(5))





















