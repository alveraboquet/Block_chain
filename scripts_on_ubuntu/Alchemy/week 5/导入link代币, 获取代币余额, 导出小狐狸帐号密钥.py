import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *

#LINK币在rinkeby上的地址
token_address = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
token_name = "LINK"
accurancy = "18"
browser_wait_time = 15

write_account_to_excel_column = "A"  #把成功或失败记录到excel的列
write_key_to_excel_column = "B"  #把成功或失败记录到excel的列
write_eth_to_excel_column = "C"   
write_link_to_excel_column = "D"  # 

excel_path = "/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 5/week 5检查link代币.xlsx"

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
wait, browser = my_linux_chrome(time_out = browser_wait_time)
login_metamask(browser, wait, metamask_pw, metamask_home)

for i in range(215, 249):
    #切换帐号
    fox_change_account(browser, wait, i)
    # time_sleep(3600)
    #导入代币
    fox_import_token(browser, wait, token_address, token_name, accurancy)
    time_sleep(20)
    
    #获取余额
    browser.refresh()
    time_sleep(60)

    token_1_balance, token_2_balance = fox_get_rinkeby_balance(browser, wait)
    time_sleep(10)

    # #获取账户信息
    account_text, key_text = fox_account_key_detail(browser, wait)
    print("帐号, 私钥, 余额分别是: ", account_text, key_text, token_1_balance, token_2_balance)

    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_account_to_excel_column, account_text)
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_key_to_excel_column, key_text)
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_eth_to_excel_column, token_1_balance)
    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_link_to_excel_column, token_2_balance)
    time_sleep(5,"waiting")


# get_fox_network_token_balance(browser, wait)
# def fox_get_token_balance(browser, wait)
# //div[@class='tabs__content']/div[2]//div[@class='list-item__heading']
# time_sleep(3600, "waiting...")