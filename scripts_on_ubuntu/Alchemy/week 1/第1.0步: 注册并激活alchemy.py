from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
import requests
import json
import re
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
#从脆球官网获取
cuiqiu_token = '88434c9de6ef45b0b8f360a190f60abd'
cuiqiu_mail_id = '608142'

excel_row = 23   #待注册的邮箱. 新的一批号,从第20往后开始
write_resent_to_excel_column = "D" #通过查看resent, 来判断是否发送激活链接
write_active_excel_column = "E"
email_excel_column = "B"
pw_excel_column = "C"

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'

browser_wait_times = 10
alchemyURL = f"https://auth.alchemyapi.io/signup?redirectUrl=https%3A%2F%2Fdashboard.alchemy.com%2Fsignup%2F%3Freferrer_origin%3DDIRECT"
alchemy_official_URL = f"https://www.alchemy.com"

while 1:
    for i in range(excel_row, 120):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_resent_to_excel_column)
        print("excel数据是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            print(f" {i} 号需要注册 alchemy ")
            email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
            email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, pw_excel_column)
            print("开始注册, 待注册邮箱, 密码是:", email_account, email_pw)

            ##=========== 准备浏览器
            wait, browser = my_linux_chrome(time_out=browser_wait_times)
            open_clash_dashboard(browser, wait, url_dashboard)
            random_select_clash_ip(browser, wait)
            delete_cookie(browser)

            #==========正式开始注册
            browser.get(alchemyURL)
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
            email_button.send_keys(email_account)

            pw_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='••••••••']")))
            time_sleep(2,"准备输入密码")
            pw_button.send_keys(email_pw)

            confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//form/button[text()='Sign up']")))
            time_sleep(2,"准备点击登录")
            browser.execute_script("arguments[0].click();", confirm_login)
            time_sleep(10,"纯倒计时,等待查看resent按钮")

            #=========循环查看是不是有resent按钮
            check_resent_flag = True
            active_email_flag = False #初始定义不要去邮箱检查激活链接
            try_times = 0
            while check_resent_flag:
                try:
                    try_times +=1  
                    resent_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Resend email']")))
                    print("找到了resent按钮, 待激活")
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_resent_to_excel_column, "Y")
                    check_resent_flag = False #不用再检查resent了
                    active_email_flag = True #需要去激活邮件
                    browser.quit()
                    a = random.randint(10, 15)
                    time_sleep(a, f"++++++++++已经找到了resent, 随机等待时间{a}")
                except:
                    time_sleep(5, "暂时还没有找到resent链接, 等待一下")

                if try_times == 5:
                    print("没有找到resent按钮,可能是有验证, 记录到excel")
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_resent_to_excel_column, "×")
                    check_resent_flag = False #不要再检查resent了
                    browser.quit()
                    a = random.randint(10, 15)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
            
            #判断需要去激活邮箱
            if active_email_flag:
                #提取激活链接
                activate_link = cuiqiu_find_alchemy_activate_email(email_account)
                
                #查看是否已经激活成功
                try_times = 0
                success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
                print("excel数据是:", str(success_or_fail))
                
                while "Y" not in str(success_or_fail):    
                    print("#需要激活链接")
                    if activate_link == "not receive active email":
                        print("没有找到激活链接, 可能是网站没有发送")
                        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                    else:
                        print("#找到了激活链接,开始打开浏览器激活")
                        try_times +=1
                        #返回: 是否已经点击verify, build
                        alread_click_verify, alread_build = cuiqiu_browser_active_alchemy_link(activate_link)
                        
                        #如果已经点击了verify为真, 记录Y
                        if alread_click_verify: 
                            Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
                            
                    #读取标识位, 防止死循环
                    success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
                    print(f"第{try_times}次去点击激活链接")
                    if try_times == 5:
                        print("点击激活链接失败, 记录到excel")
                        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                        browser.quit()
                        a = random.randint(10, 15)
                        time_sleep(a, f"++++++++++随机等待时间{a}")
                # else:
                #     print("邮箱激活成功")
                #     active_email_flag = False
                #     time_sleep(5, "休息一下")

                

