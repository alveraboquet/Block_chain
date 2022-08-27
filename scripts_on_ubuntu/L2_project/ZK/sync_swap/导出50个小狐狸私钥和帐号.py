#做sync上的所有项目,包括:
#1)ETH转USDC
#2)USDC转ETH
#3)提供流动性
#4)解除流动性

#为了跨文件夹导入包
import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *


#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
url_dashboard = 'http://clash.razord.top/#/proxies'
sync_swap_trade = "https://syncswap.xyz/swap" #用于做swap任务
sync_swap_pool = "https://syncswap.xyz/pool/add"#用于流动性任务
excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/L2_project/ZK/sync_swap/week 2.xlsx'



write_account_to_excel_column = "A"  #把成功或失败记录到excel的列
write_key_to_excel_column = "B"  #把成功或失败记录到excel的列

excel_start_row = 2
browser_wait_times = 15
wait, browser = my_linux_chrome(time_out = browser_wait_times)

login_metamask(browser, wait, metamask_pw, metamask_home)
while True:
    for i in range(excel_start_row, 52):
        print(f"第{i}个号需要做任务")

        fox_change_account(browser, wait, i)

        ##=========== 点击账户详情
        icon_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='账户选项']")))
        time_sleep(1, "先点击三个点")
        browser.execute_script("arguments[0].click();", icon_button)

        account_detail_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='账户详情']")))
        time_sleep(1, "再点击账户详情")
        browser.execute_script("arguments[0].click();", account_detail_button)

        ##=========== 点击提取account
        account_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='qr-code__address-container']/div[1]")))
        account_text = account_text_button.text
        print(account_text)
        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i+22, write_account_to_excel_column, account_text)
        ##=========== 点击导出私钥匙
        key_detail_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='导出私钥']")))
        time_sleep(1, "点击导出私钥匙")
        browser.execute_script("arguments[0].click();", key_detail_button)
        

        #输入密码
        send_detail_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
        time_sleep(1, "输入密码")
        send_detail_button.send_keys("12345678")

        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='确认']")))
        time_sleep(1, "点击导出私钥匙")
        browser.execute_script("arguments[0].click();", confirm_button)
        try:
            #获取text
            key_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='export-private-key-modal__private-key-display']")))
            key_text = key_text_button.text
            print(key_text)
        except:
            time_sleep(36, "出错")
        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i+22, write_key_to_excel_column, key_text)

        ##=========== 点击完成
        key_detail_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='完成']")))
        time_sleep(1, "点击完成")
        browser.execute_script("arguments[0].click();", key_detail_button)
        

        aa = random.randint(2, 3)
        time_sleep(aa, f"++++++++++随机等待时间{aa}")

  