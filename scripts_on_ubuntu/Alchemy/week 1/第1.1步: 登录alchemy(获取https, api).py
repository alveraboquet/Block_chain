from faker import Faker
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

excel_row = 41
browser_wait_times = 15

email_account_excel_column = "C" #帐号
email_pw_excel_column = "D"  #密码
read_active_excel_column = "F" #帐号是否激活了
https_link_excel_column = "G" # https 放在这一列
api_info_excel_column = "H" #api 放在这里

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
        print(f"excel中, {i} 号是否已激活帐号的数据是:", str(success_or_fail))

        if "Y" in str(success_or_fail): #表明这个号已经激活了,但还需要再判断有没有https 链接
            success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, https_link_excel_column)
            print(f"excel中, {i} 号 https 数据是:", str(success_or_fail))
            # if True: #测试用
            if "https://eth-rinkeby.alchemyapi.io/v2/" not in str(success_or_fail):
                try:
                    print(f"===== {i} 号需要登录 alchemy 获取https")
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
                        try:
                            try_times +=1
                            alchemy_login(browser, wait, email_to_login, email_pw)
                            time_sleep(30,"已经点击登录, 等待网页加载")
                        except:
                            print("登录失败")
                        
                        browser.refresh()
                        time_sleep(10, "已经网页刷新, 检查下是否已经登录进去了")
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
                    alchemy_delete_app(browser, wait, "RinkebyGoerli")

                    # ===================创建app
                    if create_app == 1:
                        app_name = alchemy_create_rinkeby_app(browser, wait)
                    else:
                        print("不要再创建app了")

                    #==========================   获取https
                    
                    https_info, api_info = get_alchemy_app_info(browser, wait, app_name)
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, https_link_excel_column, https_info)
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, api_info_excel_column, api_info)
                    a = random.randint(15, 19)
                    time_sleep(a, f"++++++++++随机等待时间{a}, 之后关闭浏览器")
                    browser.quit()
                    a = random.randint(10, 15)
                    time_sleep(a, f"++++++++++随机等待时间{a}")

                except:
                    try:
                        browser.quit()
                    except:
                        print("可能已经推出浏览器了")
                    a = random.randint(10, 15)
                    time_sleep(a, f"@ @ @ @ @ 超时出错了, 随机等待时间{a} @ @ @ @")

