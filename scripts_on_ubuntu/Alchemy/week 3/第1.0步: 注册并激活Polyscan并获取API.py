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
write_active_excel_column = "F" #激活信息
write_api_excel_column = "G" #激活信息
polygon_api_excel_column = "H" #激活信息
excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 3/week 3.xlsx'


#验证邮件用
from_email = "noreply@polygonscan.com"
email_subject = "Please confirm your email"
active_email_start_with = "https://polygonscan.com/confirmemail"

#注册url
polygonscan_signup_URL = "https://polygonscan.com/register"
#从提取邮件用
email_from = "noreply@polygonscan.com"
email_subject = "Please confirm your email [polygonscan.com]"

# #测试邮件接收
# email_id = cuiqiu_find_polyscan_activate_email_id("lambertslandon40@gmail.com", email_from, email_subject)
# activate_link = cuiqiu_extract_polyscan_link_from_email_id(email_id)
# time_sleep(3600, "测试邮件")

excel_row = 267
while 1:
    for i in range(excel_row, 295):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
        print("excel中, 是否激活的信息是:", str(success_or_fail))
        if "Y" not in str(success_or_fail): #只有已经注册且激活的帐号才去做
            #注册alchemy
            try:
                print(f" ================================ {i} 号需要注册 =================================")
                email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
                email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, pw_excel_column)
                signup_name = Do_Excel(excel_path,sheetname='Sheet1').read(i, username_to_excel_column)
                print("开始注册, 待注册邮箱, 用户名, 密码,是:", email_account, signup_name, email_pw)

                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(221) #设置网页加载最多1分钟
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==========正式开始注册
                browser.get(polygonscan_signup_URL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #================开始注册, 
                already_in_flag = signup_polygonscan_random_info(browser, wait, email_account, email_pw, signup_name)
                
                #================若注册成功, 则去提取邮箱
                if already_in_flag:
                    print("======准备提取激活链接")
                    email_id = cuiqiu_find_polyscan_activate_email_id(email_account, email_from, email_subject)
                    activate_link = cuiqiu_extract_polyscan_link_from_email_id(email_id)
                    
                #================邮件提取成功, 则去激活邮箱
                if activate_link != "not receive active email":
                    print("===开始激活邮件")
                    #返回: 是否已经点击verify, build
                    dashboard_flag = cuiqiu_browser_active_polygonscan_link(wait, browser, activate_link)

                #=================激活邮箱成功, 需要去登录,
                if dashboard_flag: 
                    print("====开始正式登录")
                    already_home_flag = login_polygonscan(wait, browser, email_pw, signup_name)
                    #记录, Y
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
                
                if already_home_flag:
                    print("=======开始记录API info")
                    API_info = pologanscan_get_API(wait, browser)
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_api_excel_column, API_info)

                    #=========终于结束任务, 可以关闭浏览器了
                    a = random.randint(200, 400)
                    time_sleep(a, f"-------------终于结束任务, 可以关闭浏览器了!!==随机等待时间{a}")
                    browser.quit()
                    a = random.randint(200, 400)
                    time_sleep(a, f"+++++++注册成功, 等待时间{a}")
                                
            except:
                print("=======注册失败了")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(100, 150)
                time_sleep(a, f"@ @ @ @ @ 随机等待时间 {a} @ @ @ @")    