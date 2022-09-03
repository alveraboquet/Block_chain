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
        fox_account_key_detail(browser, wait)

        aa = random.randint(2, 3)
        time_sleep(aa, f"++++++++++随机等待时间{aa}")

  