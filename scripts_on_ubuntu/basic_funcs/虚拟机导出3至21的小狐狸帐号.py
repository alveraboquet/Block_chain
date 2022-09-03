#做sync上的所有项目,包括:
#1)ETH转USDC
#2)USDC转ETH
#3)提供流动性
#4)解除流动性

#为了跨文件夹导入包
import sys
from functions import *


#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
excel_path = 'C:/software/L2_to_L2/小狐狸账号.xlsx'

write_account_to_excel_column = "A"  #把成功或失败记录到excel的列
write_key_to_excel_column = "B"  #把成功或失败记录到excel的列

for id in range(3, 22): #不同的谷歌用户资料 id
    #准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
    wait, browser = my_chrome(id)
    login_metamask(browser, wait, metamask_pw, metamask_home)
    for i in range(49, 51):
        print(f"第{i}个号需要做任务")
        # time_sleep(3600, "waiting.........")
        fox_change_account(browser, wait, i)
        # #获取账户信息
        account_text, key_text = fox_account_key_detail(browser, wait)
        print("帐号, 私钥, 余额分别是: ", account_text, key_text)

        Do_Excel(excel_path, sheetname='SheetJS').plain_write( i +50 * ( int(id) - 3 ), write_account_to_excel_column, account_text)
        Do_Excel(excel_path, sheetname='SheetJS').plain_write( i +50 * ( int(id) - 3 ), write_key_to_excel_column, key_text)
        aa = random.randint(2, 3)
        time_sleep(aa, f"++++++++++随机等待时间{aa}")
    time_sleep(2)
    browser.quit()
    time_sleep(5) 