from faker import Faker
from pymongo import MongoClient

fake = Faker()
client = MongoClient('localhost', 27017)
db = client.mt

skills = ['Java', 'JavaScript', 'Python', 'SQL', 'C', 'C++', 'C#', 'Ruby', 'Docker', 'Grafana', 'Vue.js', 'Git', 'Angular', 'Erlang', 'Matlab', 'AutoCAD', 'PHP', 'Swift']

for i in range(50):
    id = fake.numerify(text = '###')
    username = fake.name()
    age = fake.random_int(min = 20, max = 60)
    phone_number = fake.phone_number()
    user_skills = fake.random_choices(elements = skills, length = 1)
    iban = fake.iban()
    swift = fake.swift()
    salary = fake.pyint()


    db.salaries.insert_one({
        "id": id,
        "name": username,
        "phone_number": phone_number,
        "iban": iban,
        "swift": swift,
        "salary": salary,
    })

    db.employees.insert_one({
        "id": id,
        "name": username,
        "age": age,
        "phone_number": phone_number,
        "user_skills": user_skills
    })

for i in range(120):
    id = fake.numerify(text = '###')
    username = fake.name()
    age = fake.random_int(min = 20, max = 60)
    phone_number = fake.phone_number()
    job = fake.job()
    address = fake.address()
    iban = fake.iban()
    swift = fake.swift()
    email = fake.ascii_email()
    db.clients.insert_one({
        "id": id,
        "name": username,
        "age": age,
        "phone_number": phone_number,
        "job": job,
        "address": address,
        "iban": iban,
        "swift": swift,
        "email": email  
    })

