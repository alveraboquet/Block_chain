from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
import requests
import json
import re
from faker import Faker
fake = Faker()


excel_row = 22   #待注册的邮箱. 新的一批号,从第20往后开始
write_resent_to_excel_column = "D" #通过查看resent, 来判断是否发送激活链接
write_active_excel_column = "E" #激活信息
email_excel_column = "B" #邮箱
pw_excel_column = "C"  #密码

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'

browser_wait_times = 10
alchemyURL = f"https://auth.alchemyapi.io/signup?redirectUrl=https%3A%2F%2Fdashboard.alchemy.com%2Fsignup%2F%3Freferrer_origin%3DDIRECT"
alchemy_official_URL = f"https://www.alchemy.com"
#从脆球官网获取
cuiqiu_token = '88434c9de6ef45b0b8f360a190f60abd'
cuiqiu_mail_id = '608142'

while 1:
    for i in range(excel_row, 120):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_resent_to_excel_column)
        print("excel中, 是否激活的信息是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            #注册alchemy
            try:
                print(f" ========== {i} 号需要注册 alchemy ")
                email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
                email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, pw_excel_column)
                print("开始注册, 待注册邮箱, 密码是:", email_account, email_pw)

                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(221) #设置网页加载最多1分钟
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==========正式开始注册
                browser.get(alchemyURL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #=======================注册, 输入个人信息
                signup_alchemy_random_info(browser, wait, email_account, email_pw)

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
                        time_sleep(5, "**********暂时还没有找到resent链接, 尝试再次点击sign up")
                        try:#尝试再次点击login
                            confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//form/button[text()='Sign up']")))
                            time_sleep(2,"======准备再次点击登录")
                            browser.execute_script("arguments[0].click();", confirm_login)
                            print("===========已经再次点击sugn up")
                        except:
                            print("===尝试再次点击sign up,失败!!!")

                    if try_times == 8:
                        print("没有找到resent按钮,可能是有验证, 记录到excel")
                        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_resent_to_excel_column, "×")
                        check_resent_flag = False #不要再检查resent了
                        browser.quit()
                        a = random.randint(10, 15)
                        time_sleep(a, f"++++++++++随机等待时间{a}")
                
                 #判断需要去激活邮箱
                if active_email_flag:
                    try:
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
                            else: #去浏览器激活
                                print("#找到了激活链接,开始打开浏览器激活")
                                try_times +=1
                                #返回: 是否已经点击verify, build
                                dashboard_flag, alread_click_verify, alread_build = cuiqiu_browser_active_alchemy_link(activate_link)
                                
                                #如果已经点击了 dashboard_flag 为真, 记录Y
                                if dashboard_flag: 
                                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
                                    a = random.randint(2, 10)
                                    time_sleep(a, f"-------------注册成功!!==随机等待时间{a}")
                                    browser.quit()
                                    a = random.randint(1, 10)
                                    time_sleep(a, f"+++++++注册成功, 已经推出了浏览器,机等待时间{a}")

                            #读取标识位, 防止死循环
                            success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
                            print(f"---------第{try_times}次去点击激活链接")
                            if try_times == 5:
                                print("点击激活链接失败, 记录到excel")
                                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                                browser.quit()
                                a = random.randint(10, 15)
                                time_sleep(a, f"++++++++++@@@@@随机等待时间{a}")
                    except:
                        print("=======激活alchemy失败")
                        try:
                            browser.quit()
                        except:
                            print("可能已经推出浏览器了")
                        a = random.randint(10, 15)
                        time_sleep(a, f"####随机等待时间 {a} ####")   
            except:
                print("=======注册alchemy失败")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_resent_to_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(10, 15)
                time_sleep(a, f"@ @ @ @ @ 随机等待时间 {a} @ @ @ @")    

           
                

                

