from faker import Faker
from random_word import RandomWords

import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
from functions import *


fake = Faker()

a = fake.last_name()
b = fake.first_name()
c = fake.md5()
print("姓:", a)
print("名:", b)
print("绝对不重名:", c)


r = RandomWords()
result = r.get_random_word()
print("随机单词是:", result)


#随机密码
for i in range(13,150):
    excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
    pw = fake.password()
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, "D", pw)

