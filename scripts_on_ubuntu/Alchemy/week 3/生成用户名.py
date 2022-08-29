from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *
import requests
import json
import re
from faker import Faker
fake = Faker()


browser_wait_times = 15
email_excel_column = "C" #邮箱
pw_excel_column = "D"  #密码
username_to_excel_column = "E" #用户名

excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 3/week 3.xlsx'
for i in range(127, 296):
    email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
    user_name = email_account.split("@")[0]
    print(f" =============== {i}个", user_name)
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, username_to_excel_column, user_name)

