from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
import requests
import json
import re
from faker import Faker
fake = Faker()


email_excel_column = "A" #邮箱
pw_excel_column = "B"  #密码
active_excel_column = "C" #帐号激活成功信息
# https_link_excel_column = "F" # https 放在这一列
# api_info_excel_column = "G" #api 放在这里

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/邮箱注册激活类项目/consensys纪念以太坊升级NFT/consensys注册信息.xlsx'
browser_wait_times = 15
official_URL = "https://consensys.net/merge/"

#从提取邮件用
email_from = "info@consensys.net"
email_subject = "Regenesis Open Edition NFT"

#测试邮件接受
# email_id = cuiqiu_find_consensys_activate_email_id("mpass7289@gmail.com", email_from, email_subject)
# email_id = cuiqiu_find_alchemy_activate_email_id("curtissaunder@gmail.com", email_from, email_subject)
# activate_link = cuiqiu_extract_alchemy_link_from_email_id(email_id)
# time_sleep(3600, "测试邮寄")

excel_row = 11   #待注册的邮箱. 新的一批号,从第20往后开始
while 1:
    for i in range(excel_row, 308):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, active_excel_column)
        print("excel中, 是否激活的信息是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            #注册alchemy
            try:
                print(f" ============================= {i} 号需要注册  ==========================")
                email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
                # email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, pw_excel_column)
                print("开始注册, 待注册邮箱, 密码是:", email_account)

                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(221) #设置网页加载最多1分钟
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==========正式开始注册
                browser.get(official_URL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #================注册, 输入个人信息
                active_email_flag = signup_consensys_random_info(browser, wait, email_account)

                #================判断需要去邮箱提取链接
                if active_email_flag:
                    email_id = cuiqiu_find_consensys_activate_email_id(email_account, email_from, email_subject)                
                #===========需要去浏览器激活链接
                if email_id:
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, active_excel_column, "Y")
                    a = random.randint(100, 200)
                    time_sleep(a, f"++++++++++随机等待时间{a}, 之后关闭浏览器")
                    browser.quit()
                    a = random.randint(100, 200)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                else: #失败, 关闭浏览器
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, active_excel_column, "x")
                    try:
                        browser.quit()
                    except:
                        print("可能已经推出浏览器了")
                    a = random.randint(100, 200)
                    time_sleep(a, f"============ 随机等待时间 {a} ==========") 
                
            except:
                print("=======注册失败")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, active_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(100, 200)
                time_sleep(a, f"============ 随机等待时间 {a} ==========") 