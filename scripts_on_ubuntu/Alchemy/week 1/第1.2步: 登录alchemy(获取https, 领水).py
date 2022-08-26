from faker import Faker
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

create_app = 1 #是否要创建app
excel_row = 18
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
email_to_login =  Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "C")
pw = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "D")
fox_address = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "A")

print("待激活邮箱是:", email_to_login)

##=========== 准备浏览器
browser_wait_times = 15
print("登录alchemy")
wait, browser = my_linux_chrome(time_out=browser_wait_times)
alchemy_login_url = f"https://auth.alchemyapi.io/?redirectUrl=https%3A%2F%2Fdashboard.alchemyapi.io%2Fsignup%2F"

#=======清理下缓存
delete_cookie(browser)

#=============正式开始
browser.get(alchemy_login_url)
time_sleep(5, "等待 alchemy 加载,可能会卡在这里")
switch_tab_by_handle(browser, 1, 0)  # 切换到

# ======================================== 登录alchemy
login_flag = True
try_times = 0
while login_flag:
    browser.refresh()
    time_sleep(10, "网页刷新.准备循环登录")
    try:#如果能找到输入邮箱
        email_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='gavin@hooli.com']")))
        login_flag = True
        print("需要登录alchemy")
    except:
        print("可能已经登录了, 不需要重新登录了")
        login_flag = False
    if login_flag:
        try:
            try_times +=1
            email_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='gavin@hooli.com']")))
            time_sleep(2,"准备输入邮箱")
            email_button.send_keys(email_to_login)

            pw_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='••••••••']")))
            time_sleep(2,"准备输入密码")
            pw_button.send_keys(pw)

            confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
            time_sleep(2,"准备点击登录")
            # browser.execute_script("arguments[0].click();", confirm_login)
            ActionChains(browser).click(confirm_login).perform()  # 用模拟鼠标点

            time_sleep(20,"已经点击登录, 等待网页加载")
        except:
            print("登录失败")
    print(f"第{try_times}次登录alchemy")   
    if try_times == 5:
        browser.quit()

# #==================填写描述
try:
    fill_in_alchemy_project_des(browser, wait)
except:
    print("可能是不需要填写alchemy项目描述")

# ===================创建app
if create_app == 1:
    try:
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Create')]]")))
        time_sleep(2,"准备创建")
        browser.execute_script("arguments[0].click();", create_button)

        name_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='name']")))
        time_sleep(2,"准备输入name")
        name_button.send_keys(fake.last_name())

        desc_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='description']")))
        time_sleep(2,"准备输入desc")
        desc_button.send_keys(fake.first_name())

        #下拉列表
        try:
            down_list_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='select-input-container css-1tyu61v']//div[@class='css-1hkumgc']/span")))
            time_sleep(2,"准备点击下拉")
            # browser.execute_script("arguments[0].click();", down_list_button)
            ActionChains(browser).click(down_list_button).perform()  # 必须用模拟鼠标点
        except:
            print("下拉没找到哦啊")

        # #选择rinkeby
        rinkeby_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-1hkumgc']/span[text()[contains(.,'Rinkeby')]]")))
        time_sleep(2,"准备选择 rinkeby")
        browser.execute_script("arguments[0].click();", rinkeby_button)
        # ActionChains(browser).click(rinkeby_button).perform()  # 模拟鼠标点

        #确定创建
        confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
        time_sleep(2,"准备点击创建")
        browser.execute_script("arguments[0].click();", confirm_login)
    except:
        print("可能是已经超过数量了,那就不要创建了")
else:
    print("不要再创建app了")

#==========================   获取https
# viw_key_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//tbody[@class='table-body']/tr[3]/td[8]/span")))
# time_sleep(2,"准备点击view key")
# browser.execute_script("arguments[0].click();", viw_key_button)

browser.refresh()
time_sleep(20,"等待更新")
code_https_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//code/span[2]")))
print("寻找到的https是: ", code_https_button.text)
https_result = code_https_button.text[1:-1]
Do_Excel(excel_path, sheetname='Sheet1').plain_write(excel_row, "G", https_result)


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