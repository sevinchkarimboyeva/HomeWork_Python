import json
data = {
    "Model" : "Malibu",
    "Rang" : "Qora",
    "Yil":2020,
    "Narh":40000
}
data_json=json.dumps(data)
print(data_json)

talaba= {
    "ism":"Hasan",
    "familiya":"Husanov",
    "tyil":2000
}
talaba_json=json.dumps(talaba)
print(f"Talabaning ismi:{talaba['ism']}")
print(f"Talabaning familiyasi:{talaba['familiya']}")

with open('data.json','w') as d:
    json.dump(data,d)

with open('talaba.json','w') as t:
    json.dump(talaba,t)



with open('talabalar.json','r') as t_j:
    talaba=json.load(t_j)

talabalar_list=talaba["student"]
for student in talabalar_list:
    id=student['id']
    name=student['name']
    lastname=student['lastname']
    year=student['year']
    faculty=student['faculty']

    print(f"Id:{id},\nIsm-Familiyasi:{name} {lastname},\nYili:{year} \nFakulteti:{faculty}")







