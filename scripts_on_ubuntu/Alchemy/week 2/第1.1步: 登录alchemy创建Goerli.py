from faker import Faker
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

browser_wait_times = 15

email_account_excel_column = "C" #帐号
email_pw_excel_column = "D"  #密码
read_active_excel_column = "E" #帐号是否激活了
https_link_excel_column = "F" # https 放在这一列
api_info_excel_column = "G" #api 放在这里

excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 2/week 2.xlsx'
alchemy_login_url = f"https://auth.alchemyapi.io/?redirectUrl=https%3A%2F%2Fdashboard.alchemyapi.io%2Fsignup%2F"
create_app = 1 #是否要创建app
get_https = 1
# 小狐狸地址
# fox_address = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "A")

<<<<<<< HEAD
excel_row = 10
=======
<<<<<<< HEAD
excel_row = 61
=======
excel_row = 10
>>>>>>> 9aefd239b07b029a301c4cd6c28e98732a8daf31
>>>>>>> 9d66b6175a8b5e43eda2c504f9dd4133fa231c94
while 1:
    for i in range(excel_row, 120):
        #=======================先查看这个号有没有激活过
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, read_active_excel_column)
        print(f"excel中, {i} 号是否已激活帐号的数据是:", str(success_or_fail))

        if "Y" in str(success_or_fail): #表明这个号已经激活了,但还需要再判断有没有https 链接
            success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, https_link_excel_column)
            print(f"excel中, {i} 号 https 数据是:", str(success_or_fail))
            # if True: #测试用
            # https://eth-goerli.g.alchemy.com/v2/r1nIPHamIGYPFbV41VNm6121dH5XpqDN
            if "https://eth-goerli.g.alchemy.com/v2" not in str(success_or_fail):
                try:
                    print(f"============================ {i} 号需要登录 alchemy 获取 Goerli https =========================")
                    email_to_login =  Do_Excel(excel_path,sheetname='Sheet1').read(i, email_account_excel_column)
                    email_pw = Do_Excel(excel_path,sheetname='Sheet1').read(i, email_pw_excel_column)
                    print("待登录邮箱, 密码是:", email_to_login, email_pw)

                    ##=========== 准备浏览器, 清理下缓存
                    wait, browser = my_linux_chrome(time_out=browser_wait_times)
                    browser.set_page_load_timeout(221) #设置网页加载最多1分钟
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
                        try_times +=1
                        alchemy_login(browser, wait, email_to_login, email_pw)
                        time_sleep(60,"已经点击登录, 等待网页加载")
                        # #==================可能要填写描述
                        try:
                            fill_in_alchemy_project_des(browser, wait)
                        except:
                            print("====可能是不需要填写alchemy项目描述")

                        try:#如果能找到Alchemy的首页,说明已经进入了
                            print("尝试查看是不是已经进入 Alchemy 了")
                            Dashboard_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()[contains(.,'Dashboard')]]")))
                            login_flag = False
                            print("=======已经登录了 Alchemy")
                        except:
                            print("========登录失败, 重新登录")                        
                            browser.refresh()
<<<<<<< HEAD
                            time_sleep(30, "已经网页刷新, 检查下是否已经登录进去了")
=======
                            time_sleep(30, "已经网页刷新, 再次尝试登录")
>>>>>>> 9d66b6175a8b5e43eda2c504f9dd4133fa231c94
                            print(f"第{try_times}次登录alchemy")   
                        if try_times == 3:
                            browser.quit()
                            login_flag = False
                            create_app = 0
                            get_https = 0

                    # ===================删除demo app, Rinkeby, Goerli是要保留的, 创建app
                    if create_app == 1:
<<<<<<< HEAD
                        alchemy_delete_app(browser, wait, "Rinkeby Goerli")
=======
                        alchemy_delete_app(browser, wait, "Rinkeby Goerli Polygon Mumbai Mainnet")
>>>>>>> 9d66b6175a8b5e43eda2c504f9dd4133fa231c94
                        app_name = alchemy_create_goerli_app(browser, wait)
                    
                    if get_https == 1:
                        #==========================   获取https
                        https_info, api_info = get_alchemy_app_info(browser, wait, app_name)
                        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, https_link_excel_column, https_info)
                        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, api_info_excel_column, api_info)
                        a = random.randint(15, 29)
                        time_sleep(a, f"++++++++++随机等待时间{a}, 之后关闭浏览器")
                        browser.quit()
                        a = random.randint(10, 15)
                        time_sleep(a, f"++++++++++随机等待时间{a}")

                except:
                    try:
                        browser.quit()
                    except:
                        print("可能已经推出浏览器了")
                    a = random.randint(100, 150)
                    time_sleep(a, f"@ @ @ @ @ 超时出错了, 随机等待时间{a} @ @ @ @")

