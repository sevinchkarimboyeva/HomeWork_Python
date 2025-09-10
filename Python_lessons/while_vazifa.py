# 1-misol
ranglar = ["qizil", "sariq", "yashil"]
while True:
    rang = input("Svetofor qaysi rangda?:").lower()
    if rang in ranglar:
        print(f"Rahmat, to'g'ri keladi.")
        break
    print(f"Bu xato rang.")

# 2-misol
import random

def guess_game():
    opportunities = 10
    rand = random.randrange(1, 100)
    while opportunities > 0:
        num = int(input("son kiriting: "))
        if num == rand:
            print("Tabriklaymiz! to'g'ri javob")
            break
        elif num > rand:
            print("Biz o'ylagan son siz o'ylagan sondan kichik")
        elif num < rand:
            print("Biz o'ylagan son siz o'ylagan sondan katta")
        opportunities -= 1
    else:
        print("Imkonyatingiz tugadi!")
    return f"Bot taxmin qilgan son: {rand}"

print(guess_game())

# 3-misol
ismlar = []
n=1
while True:
    ism = input(f"{n}-Do'stingiz ismini kiriting:(Dasturni to'xtatish uchun 'stop' deb yozing): ")
    if ism.lower() !='stop':
        ismlar.append(ism)
        n=n+1
        continue
    else:
        break
ismlar.append(ism)

print(f"\nDo'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism)


# 4-misol
USD = 12600

while True:
    summa = input("Iltimos, so'm miqdorini kiriting (dasturni to'xtatish uchun 'exit' deb yozing): ")
    if summa.lower() == 'exit':
        print("Dastur to'xtatildi.")
        break
    elif summa.isdigit():
        som = int(summa)
        dollar = som / USD
        print(f"{som} so'm {dollar:.2f} USD)")
    else:
        print("Iltimos, son kiriting!")
























