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

email_excel_column = "C" #邮箱
pw_excel_column = "D"  #密码
write_active_excel_column = "E" #激活信息


excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 2/week 2.xlsx'
browser_wait_times = 15
replit_signup_URL = "https://replit.com/signup"

#提取邮箱用
email_from = "verify@replit.com"
email_subject = "Replit: Verify Your Email"

# email_id = cuiqiu_find_replit_activate_email_id("sierrabootman@gmail.com", email_from, email_subject)
# activate_link = cuiqiu_extract_replit_link_from_email_id(email_id)
# time_sleep(3600, "邮件测试")

excel_row = 181   #待注册的邮箱
while 1:
    for i in range(excel_row, 308):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
        print("excel中, 是否激活的信息是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            #注册alchemy
            try:
                print(f" ================================ {i} 号需要注册 replit=================================")
                email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
                email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, pw_excel_column)
                print("开始注册, 待注册邮箱, 密码是:", email_account, email_pw)

                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(121) #设置网页加载最多1分钟
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==========正式开始注册
                browser.get(replit_signup_URL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #=======================注册, 输入个人信息
                active_email_flag = signup_replit_random_info(browser, wait, email_account, email_pw)
                
                 #=========判断需要去提取, 激活邮箱
                if active_email_flag:
                    print("======准备提取激活链接")
                    email_id = cuiqiu_find_replit_activate_email_id(email_account, email_from, email_subject)
                    activate_link = cuiqiu_extract_replit_link_from_email_id(email_id)
                    
                #========== 去浏览器激活链接
                if activate_link:
                    dashboard_flag = cuiqiu_browser_active_replit_link(wait, browser, activate_link, email_account, email_pw)
                    
                #============如果已经点击了 dashboard_flag 为真, 记录Y
                if dashboard_flag: 
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
                    a = random.randint(600, 1000)
                    time_sleep(a, f"-------------注册成功!!==随机等待时间{a}")
                    a = random.randint(300, 600)
                    time_sleep(a, f"+++++++注册成功, 等待时间{a}")
                    browser.quit()

            except:
                print("=======注册失败")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(10, 15)
                time_sleep(a, f"@ @ @ @ @ 随机等待时间 {a} @ @ @ @")