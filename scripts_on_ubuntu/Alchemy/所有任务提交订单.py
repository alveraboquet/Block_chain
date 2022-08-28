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
write_active_excel_column = "E" #激活信息
fox_address_excel_column = "H"
projec_link_excel_column = "H"
contract_address__excel_column = "G"
submit_success_excel_column = "H"

excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 2/week 2.xlsx'
browser_wait_times = 15
submit_URL = "https://replit.com/signup"


excel_row = 2   #待注册的邮箱
while 1:
    for i in range(excel_row, 120):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, submit_success_excel_column)
        print("excel中, 是否激活的信息是:", str(success_or_fail))

        if "Y" not in str(success_or_fail):
            try:
                print(f" ================================ {i} 号需要提交信息=================================")
                email_account =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_excel_column)
                contract_address =  Do_Excel(excel_path,sheetname='Sheet1').read(i, contract_address__excel_column)
                fox_address =  Do_Excel(excel_path,sheetname='Sheet1').read(i, fox_address_excel_column)
                projec_link =  Do_Excel(excel_path,sheetname='Sheet1').read(i, projec_link_excel_column)

                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(221) #设置网页加载最多1分钟
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==========正式开始提交订单
                browser.get(submit_URL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #===========
                def submit_alchemy_info_to_google_form(browser, wait):
                
                
                
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
                a = random.randint(100, 300)
                time_sleep(a, f"-------------注册成功!!==随机等待时间{a}")
                a = random.randint(100, 300)
                time_sleep(a, f"+++++++注册成功, 等待时间{a}")
                browser.quit()

            except:
                print("=======提交失败")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, submit_success_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(10, 15)
                time_sleep(a, f"@ @ @ @ @ 随机等待时间 {a} @ @ @ @")    

           
                

                

