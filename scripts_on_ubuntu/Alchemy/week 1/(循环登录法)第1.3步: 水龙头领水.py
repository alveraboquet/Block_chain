from faker import Faker
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
from faker import Faker
fake = Faker()

excel_row = 14
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
email_to_login =  Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "C")
pw = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "D")
fox_address = Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "A")

print("待激活邮箱是:", email_to_login)

##=========== 准备浏览器
browser_wait_times = 10
print("登录alchemy")
wait, browser = my_linux_chrome(time_out=browser_wait_times)
faucet_url = "https://rinkebyfaucet.com/"

#=======清理下缓存
delete_cookie(browser)

#=============正式开始
browser.get(faucet_url)
time_sleep(5, "等待水龙头网站加载")
switch_tab_by_handle(browser, 1, 0)  # 切换到


# ======================================== 登录alchemy
login_flag = True
try_times = 1
while login_flag:
    #去检查需不需要登录
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Alchemy Login')]]")))
    except:
        print("可能是已经登录了")
        login_flag = False
    #需要的话去登录
    if login_flag:
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Alchemy Login')]]")))
            time_sleep(2,"准备登录")
            browser.execute_script("arguments[0].click();", login_button)
            time_sleep(30,"已经点击登录")

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

            time_sleep(40,"已经点击登录")
            break
        except:
            # browser.refresh()
            browser.get(faucet_url)
            time_sleep(15, "登录失败, 重新登录")
            try_times +=1
    if try_times == 10:
        browser.quit()


#======================================= 准备领水
faucet_flag = True
try_times = 1
while faucet_flag:
    #去检查需不需要登录
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='']")))
    except:
        print("可能是已经登录了")
        faucet_flag = False
time_sleep(3600)


# ===================创建app
if create_app == 1:
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
else:
    print("不要再创建app了")

#=======================获取https
# viw_key_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//tbody[@class='table-body']/tr[3]/td[8]/span")))
# time_sleep(2,"准备点击view key")
# browser.execute_script("arguments[0].click();", viw_key_button)

time_sleep(20,"等待更新")
code_https_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//code/span[2]")))
print("寻找到的https是: ", code_https_button.text)
https_result = code_https_button.text[1:-1]
Do_Excel(excel_path, sheetname='Sheet1').plain_write(excel_row, "G", https_result)


#真实:https://eth-rinkeby.alchemyapi.io/v2/IhQ2gl-ANUQmfTqn51z6K7VJWhs9Nczt

time_sleep(3660,"纯倒计时")

# https://eth-rinkeby.alchemyapi.io/v2/6qcLDO7APBwB_9eEXF0-QCCNRJqTaR-_
# https://eth-rinkeby.alchemyapi.io/v2/6qcLDO7APBwB_9eEXF0-QCCNRJqTaR-_