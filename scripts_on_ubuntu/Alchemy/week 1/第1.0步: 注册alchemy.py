from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

lastname = fake.last_name()
firstname = fake.first_name()
pw = fake.password()
company = fake.company()
md5 = fake.md5()
sentence = fake.sentence()

# print("姓:", lastname)
# print("名:", firstname)
# print("密码:", pw)
# print("company:", company)
# print("md5:", md5)
# print("sentence:", sentence)


excel_row = 20   #待注册的邮箱. 新的一批号,从第20个开始
write_to_excel_column = "D"
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
email =  Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "C")
print("待注册邮箱是:", email)

alchemyURL = f"https://auth.alchemyapi.io/signup?redirectUrl=https%3A%2F%2Fdashboard.alchemy.com%2Fsignup%2F%3Freferrer_origin%3DDIRECT"
alchemy_official_URL = f"https://www.alchemy.com"

while 1:
    for i in range(excel_row,201):
        #=======================如果没有ipfs_json 的话, 开始任务吧
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_to_excel_column)
        print("excel数据是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            print(f" {i} 号没有ipfs, 需要做创建ipfs")

##=========== 准备浏览器
print("开始注册")
browser_wait_times = 10
wait, browser = my_linux_chrome(time_out=browser_wait_times)

#=======清理下缓存
delete_cookie(browser)

#==========正式开始注册
time_sleep(2)
browser.get(alchemyURL)
# browser.get(alchemyURL)
switch_tab_by_handle(browser, 1, 0)  # 切换到

#===============================================注册, 输入个人信息
first_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Gavin']")))
time_sleep(2,"准备输入姓")
first_name.send_keys(fake.last_name())
time.sleep(2)

second_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Belson']")))
time_sleep(2,"准备输入名")
second_name.send_keys(fake.first_name())

email_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='gavin@hooli.com']")))
time_sleep(2,"准备输入邮箱")
email_button.send_keys(email)

pw_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='••••••••']")))
time_sleep(2,"准备输入密码")
pw = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "D")
pw_button.send_keys(pw)

#=========循环确认
faucet_flag = True
try_times = 0
while faucet_flag:
    # browser.refresh()
    # time_sleep(10, "进入领水, 等待刷新")
    #去检查需不需要领. 如果是空,说明需要领取
    try:  
        confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Sign up']")))
        print("要确认")
        faucet_flag = True
    except:
        print("已经确认了")
        faucet_flag = False
    #需要的话去领
    if faucet_flag:   
        try_times += 1
        confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//form/button[text()='Sign up']")))
        time_sleep(2,"准备点击登录")
        browser.execute_script("arguments[0].click();", confirm_login)
        time_sleep(15,"纯倒计时,等待确认")
    print(f"第{try_times}次确认~~~")   
    if try_times == 5:
        browser.quit()

