from faker import Faker

fake = Faker()

a = fake.last_name()
b = fake.first_name()
c = fake.md5()
print("姓:", a)
print("名:", b)
print("绝对不重名:", c)