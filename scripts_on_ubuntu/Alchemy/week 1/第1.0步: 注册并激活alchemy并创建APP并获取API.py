from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
import requests
import json
import re
from faker import Faker
fake = Faker()


email_excel_column = "C" #邮箱
pw_excel_column = "D"  #密码
write_active_excel_column = "E" #帐号激活成功信息
https_link_excel_column = "G" # https 放在这一列
api_info_excel_column = "H" #api 放在这里

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/week 1.xlsx'
browser_wait_times = 15
alchemyURL = f"https://auth.alchemyapi.io/signup?redirectUrl=https%3A%2F%2Fdashboard.alchemy.com%2Fsignup%2F%3Freferrer_origin%3DDIRECT"
alchemy_official_URL = f"https://www.alchemy.com"

#从提取邮件用
email_from = "hello@alchemy.com"
email_subject = "Verify your email"



excel_row = 101   #待注册的邮箱. 新的一批号,从第20往后开始
while 1:
    for i in range(excel_row, 120):
        #=======================如果没有resent, 说明没有发送激活链接,
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_active_excel_column)
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

                #==========正式开始注册alchemy
                browser.get(alchemyURL)
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                #================注册, 输入个人信息
                active_email_flag = signup_alchemy_random_info(browser, wait, email_account, email_pw)

                #================判断需要去邮箱提取链接
                if active_email_flag:
                    email_id = cuiqiu_find_alchemy_activate_email_id(email_account, email_from, email_subject)
                    activate_link = cuiqiu_extract_alchemy_link_from_email_id(email_id)
                
                #===========需要去浏览器激活链接
                if activate_link:
                    dashboard_flag= cuiqiu_browser_active_alchemy_link(browser, wait, activate_link)
                    
                #========如果进入了主页 dashboard, 则记录Y, 开始主线任务
                if dashboard_flag: 
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "Y")
    
                    # 1)删除demo app, Rinkeby是要保留的
                    alchemy_delete_app(browser, wait, "RinkebyGoerli")

                    # 2)创建app
                    app_name = alchemy_create_rinkeby_app(browser, wait)
                    
                    # 3)获取https
                    
                    https_info, api_info = get_alchemy_app_info(browser, wait, app_name)
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, https_link_excel_column, https_info)
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, api_info_excel_column, api_info)
                    a = random.randint(50, 100)
                    time_sleep(a, f"++++++++++随机等待时间{a}, 之后关闭浏览器")
                    browser.quit()
                    a = random.randint(50, 200)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                
            except:
                print("=======注册alchemy失败")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_active_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(10, 15)
                time_sleep(a, f"============ 随机等待时间 {a} ==========")    

           
                

                

