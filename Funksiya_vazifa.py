# 1-misol
def user_data(first_name,last_name,age):
    print(f"Ism:{first_name}")
    print(f"Familiya:{last_name}")
    print(f"Yosh:{age}")
user_data('Sevinch','Karimboyeva',19)

# 2-misol
def find_max(a,b,c):
    katta=max(a,b,c)
    katta_son=[]
    if a==katta:
        katta_son.append("A")
    elif b==katta:
        katta_son.append("B")
    else:
        katta_son.append("C")
    print(f"Eng katta son-{katta_son}")
find_max(5,3,1)

# 4-misol
def list_sum(myList):
    yigindi=sum(myList)
    print(f"Listning elementlar yig'indisi={yigindi}")
list_sum((16,4,8,2,2))

# 5-misol
def daraja(a,b):
    d=a**b
    print(f"{a}ning {b}-darajasi {d}")
daraja(5,3)

# 6-misol
def daraja4(a,b,c,d):
    r=a**b
    s=c**d
    print(f"{a} ning {b}-darajasi {r} va {c} ning {d}-darajasi {s}")
daraja4(3,4,5,9)
daraja4(12,4,2,11)

# 7-misol

# def digit_count_and_sum(word):
#     raqamlar_soni=0
#     raqamlar_yigindisi=0
# for i in word:
#     if i.isdigit():
#         raqamlar_s
#         sum+=int(i)


# 8-misol
def add_right(m,n):
    """'m' sonining o'ng tomoniga 'n'sonini qo'shib qo'yadi."""
    yangi_son=int(str(m)+str(n))
    print(f"Yangi son:{yangi_son}")
add_right(13,45)

# 9-misol
def add_left(a,b):
    """'a' sonining chap tomoniga 'b' sonini qo'shadi."""
    son=int(str(a)+str(b))
    print(f"Yangi son:{son}")
add_right(34,21)

# 10-misol

def work_with_list(a):
    """Ro'yxatdagi har bir elementni eng kichik elementga ko'paytiradi."""
    if not a:
        print("Ro'yxat bo'sh.")
        return
    min_num = min(a)
    new_list = [x * min_num for x in a]
    print(f"O'zgartirilgan ro'yxat: {new_list}")
my_list = [5, 2, 8, 3]
work_with_list(my_list)

# 11-misol
def big_sales(sales):
    if not sales:
        return

    max_sales_month = max(sales, key=sales.get)
    return max_sales_month

satuvlar = {
    "yanvar": 12000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000,
}
most_sales_month = big_sales(satuvlar)
if most_sales_month:
    print(f"Eng ko'p sotuv bo'lgan oy: {most_sales_month}")

# 12-misol
def min_max(numbers,min_num,max_num):
    kichik_son=min(numbers)
    katta_son=max(numbers)
    if kichik_son==min_num:
        print(f"Ro'yhatdagi {min_num} kichik son!")
    else:
        print(f"Ro'yhatdagi {min_num} katta son")

    if katta_son==max_num:
        print(f"Ro'yhatdagi {max_num} katta son!")
    else:
        print(f"Ro'yhatdagi {max_num} kichik son")

numbers=[7,7,47,5,9]
min_max(numbers,11,7)

# 13-misol
def expensiveProduct(products):
    """Mahsulotlar ro'yxatidan eng qimmatining nomini topadi va print qiladi."""
    if not products:
        print("Mahsulotlar ro'yxati bo'sh.")
        return

    qimmat = products[0]
    for product in products:
        if product["price"] > qimmat["price"]:
            most_expensive = product

    print(f"Eng qimmat telefon: {qimmat['name']}")
products= [
  {
    "name": "Iphone X",
    "price": 600 },
  {
    "name": "Iphone 12",
    "price": 1500 },
  {
    "name": "Samsung Note 9",
    "price": 800 },
  {
    "name": "Samsung S10",
    "price": 1100 },
]
expensiveProduct(products)

