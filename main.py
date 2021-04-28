from faker import Faker
from pymongo import MongoClient

fake = Faker()
client = MongoClient('localhost', 27017)
db = client.mt

skills = ['Java', 'JavaScript', 'Python', 'SQL', 'C', 'C++', 'C#', 'Ruby', 'Docker', 'Grafana', 'Vue.js', 'Git', 'Angular', 'Erlang', 'Matlab', 'AutoCAD', 'PHP', 'Swift']

for i in range(50):
    username = fake.name()
    age = fake.numerify(text = '%#')
    phone_number = fake.phone_number()
    user_skills = fake.random_choices(elements=skills, length = 1)
    db.employees.insert_one({
        "name": username,
        "age": age,
        "phone_number": phone_number,
        "user_skills": user_skills
    })
