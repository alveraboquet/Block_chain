from faker import Faker
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

excel_row = 23
browser_wait_times = 15
read_active_excel_column = "E" #帐号是否激活了
https_link_excel_column = "F" # https 放在这一列
email_account_excel_column = "B" #帐号
email_pw_excel_column = "C"  #密码
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
alchemy_login_url = f"https://auth.alchemyapi.io/?redirectUrl=https%3A%2F%2Fdashboard.alchemyapi.io%2Fsignup%2F"
create_app = 1 #是否要创建app

# 小狐狸地址
# fox_address = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "A")

#如果已经激活,则开始创建项目
while 1:
    for i in range(excel_row, 120):
        #=======================先查看这个号有没有激活过
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, read_active_excel_column)
        print("excel中, 是否已激活帐号的数据是:", str(success_or_fail))

        if "Y" in str(success_or_fail): #表明这个号已经激活了,但还需要再判断有没有https 链接
            success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, https_link_excel_column)
            print("excel中, https数据是:", str(success_or_fail))
            if True: #测试用
            # if "https://eth-rinkeby.alchemyapi.io/v2/" not in str(success_or_fail):
                print(f"===== {i} 号需要登录 alchemy 获取https")
                email_to_login =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_account_excel_column)
                email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, email_pw_excel_column)
                print("待登录邮箱, 密码是:", email_to_login, email_pw)

                ##=========== 准备浏览器, 清理下缓存
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.set_page_load_timeout(60)
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                #==================正式开始
                browser.get(alchemy_login_url)
                time_sleep(5, "等待 alchemy 加载,可能会卡在这里")
                switch_tab_by_handle(browser, 1, 0)  # 切换到

                # =============== 登录alchemy
                login_flag = True
                try_times = 0
                while login_flag:
                    try:
                        try_times +=1
                        alchemy_login(browser, wait, email_to_login, email_pw)
                        time_sleep(30,"已经点击登录, 等待网页加载")
                    except:
                        print("登录失败")
                    
                    browser.refresh()
                    time_sleep(10, "网页刷新, 检查下是否已经登录进去了")
                    try:#如果能找到Alchemy的首页,说明已经进入了
                        print("尝试查看是不是已经进入 Alchemy 了")
                        Dashboard_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()[contains(.,'Dashboard')]]")))
                        login_flag = False
                        print("=======已经登录了 Alchemy")
                    except:
                        print("======需要重新登录=====")
                    print(f"第{try_times}次登录alchemy")   
                    if try_times == 5:
                        browser.quit()

                # #==================填写描述
                try:
                    fill_in_alchemy_project_des(browser, wait)
                except:
                    print("====可能是不需要填写alchemy项目描述")

                
                #======删除demo app, Rinkeby是要保留的
                alchemy_delete_app(browser, wait, "0Rinkeby")

                # ===================创建app
                if create_app == 1:
                    app_name = alchemy_create_rinkeby_app(browser, wait)
                else:
                    print("不要再创建app了")

                #==========================   获取https
                
                https_info, api_info = get_alchemy_app_info(browser, wait, app_name)
                # QyuVLX4O0LJJraiREQeUSI86TcK2S7PS
                # https://eth-rinkeby.alchemyapi.io/v2/QyuVLX4O0LJJraiREQeUSI86TcK2S7PS
                time_sleep(3600, "春")
                time_sleep(3600, "春")

                code_https_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//code/span[2]")))
                https_result = code_https_button.text[1:-1]
                print("===寻找到的https是: ", code_https_button.text)
                print("===提取后: ", https_result)
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(excel_row, https_link_excel_column, https_result)
                time_sleep(3600, "春")

#=================================== 领水
app_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//tbody[@class='table-body']/tr[3]/td[1]/a")))
time_sleep(2,"准备点击进入app, 打算去领水")
browser.execute_script("arguments[0].click();", app_button)


get_test_ETH = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()[contains(.,'Get Test ETH')]]")))
time_sleep(2,"准备点击进入水龙头")
browser.execute_script("arguments[0].click();", get_test_ETH)

switch_tab_by_handle(browser, 2, 0)  # 切换到

#============查看是不是要登录
login_flag = True
try_times = 0
while login_flag:
    #去检查需不需要登录
    browser.refresh()
    time_sleep(10, "领水网页刷新")
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()[contains(.,'Please signup or login')]]")))
        print("需要登录login")
        login_flag = True
    except:
        print("可能是已经登录了")
        login_flag = False
    #需要的话去登录
    if login_flag:
        try:
            try_times +=1
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Alchemy Login')]]")))
            time_sleep(2,"准备登录")
            browser.execute_script("arguments[0].click();", login_button)
            time_sleep(20,"已经点击登录alchemy")

        except:
            browser.refresh()
            time_sleep(15, "登录失败, 重新登录")
    print(f"第{try_times}次领水尝试登录")        
    if try_times == 5:
        browser.quit()


#=========循环领取
faucet_flag = True
try_times = 0
while faucet_flag:
    browser.refresh()
    time_sleep(10, "进入领水, 等待刷新")
    #去检查需不需要领. 如果是空,说明需要领取
    try:
        blank_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='alchemy-faucet-table-data col']")))
        print("领取列表是空的,需要领水")
    except:
        print("可能是已经领到了")
        faucet_flag = False
    #需要的话去领
    if faucet_flag:
        try:
            try_times +=1
            address_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='address']")))
            time_sleep(2,"准备输入小狐狸帐号")
            address_button.send_keys(fox_address)

            confirm_send = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']//span")))
            time_sleep(2,"准备点击send")
            # browser.execute_script("arguments[0].click();", confirm_login)
            ActionChains(browser).click(confirm_send).perform()  # 用模拟鼠标点

            time_sleep(30,"已经点击send")
        except:
            browser.refresh()
            time_sleep(15, "领取失败, 重新领")
    print(f"第{try_times}次领水~~~")   
    if try_times == 5:
        browser.quit()

print("介绍")