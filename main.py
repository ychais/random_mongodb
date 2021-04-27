
from faker import Faker
fake = Faker()
from 
skills = ['Java', 'JavaScript', 'Python', 'SQL', 'C', 'C++', 'C#', 'Ruby', 'Docker', 'Grafana', 'Vue.js', 'Git', 'Angular', 'Erlang', 'Matlab', 'AutoCAD', 'PHP', 'Swift']


for i in range(50):
    print(fake.name())

for i in range(50):
    print(fake.phone_number())

for i in range(50):
    print(fake.numerify(text = '%#'))

for i in range(50):   
    a = fake.sentence(ext_word_list=skills)
    print(a)
