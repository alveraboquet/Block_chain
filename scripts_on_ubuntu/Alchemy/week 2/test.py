from random_word import RandomWords
from faker import Faker
fake = Faker()
mail = "linkguopengooooo@gmail.com"
name = mail.split("@")[0]
while len(name) > 15:
    name = name[:15]


print(name, len(name))