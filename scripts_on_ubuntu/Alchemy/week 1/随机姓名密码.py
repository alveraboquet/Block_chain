from faker import Faker
from random_word import RandomWords

import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
from functions import *


fake = Faker()

# a = fake.last_name()
# b = fake.first_name()
# c = fake.md5()
# print("姓:", a)
# print("名:", b)
# print("绝对不重名:", c)


# r = RandomWords()
# result = r.get_random_word()
# print("随机单词是:", result)


#随机密码
for i in range(150,309):
    excel_path = 'scripts_on_ubuntu/Alchemy/week 1/week 1.xlsx'
    pw = fake.password()
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, "D", pw)


# from faker import Faker
# fake = Faker()

# lastname = fake.last_name()
# firstname = fake.first_name()
# pw = fake.password()
# company = fake.company()
# md5 = fake.md5()
# sentence = fake.sentence()

# print("姓:", lastname)
# print("名:", firstname)
# print("密码:", pw)
# print("company:", company)
# print("md5:", md5)
# print("sentence:", sentence)