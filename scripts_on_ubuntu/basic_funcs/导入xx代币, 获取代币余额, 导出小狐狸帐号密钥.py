import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *

#LINK币在rinkeby上的地址
token_address = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"
token_name = "LINK"
accurancy = "18"
browser_wait_time = 15

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
wait, browser = my_linux_chrome(time_out = browser_wait_time)
login_metamask(browser, wait, metamask_pw, metamask_home)

for i in range(2, 249):
    # get_fox_network_token_balance(browser, wait)
    fox_change_account(browser, wait, i)

    fox_import_token(browser, wait, token_address, token_name, accurancy)

    token_1_balance, token_2_balance = fox_get_rinkeby_balance(browser, wait)

    account_text, key_text = fox_account_key_detail(browser, wait)
    print("帐号, 私钥, 余额分别是: ", account_text, key_text, token_1_balance, token_2_balance)
    time_sleep(3,"waiting")

# get_fox_network_token_balance(browser, wait)
# def fox_get_token_balance(browser, wait)
# //div[@class='tabs__content']/div[2]//div[@class='list-item__heading']
time_sleep(3600, "waiting...")