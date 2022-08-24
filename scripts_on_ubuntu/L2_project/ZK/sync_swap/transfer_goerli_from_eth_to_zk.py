#把ETH上的goerli转到zk上。小狐狸切换到goerli


#为了跨文件夹导入包
# import os,inspect
# current_dir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# os.chdir(current_dir)
# import sys
# sys.path.append('../../../')
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *


#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
url_dashboard = 'https://clash.razord.top/#/proxies'
zksync_goerli_bridge = 'https://portal.zksync.io/bridge'
zhsync_home = "https://wallet.zksync.io/"
excel_path = "/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/L2_project/ZK/sync_swap/sync_swap_50-之后变为200号.xlsx"

excel_start = 2
browser_wait_times = 30
wait, browser = my_linux_chrome(time_out=browser_wait_times)

#打開clash
open_clash_dashboard(browser, wait, url_dashboard)

#切換ip
ip_switcher(browser, wait, url_google)

#登錄小狐狸
login_metamask(browser, wait, metamask_pw, metamask_home)

#切換到i小狐狸,準備換號
switch_tab_by_handle(browser, 1, 0)
fox_change_account(browser, wait, excel_start)

#新建标签页,准备转goerli
new_tab(browser, zksync_goerli_bridge)
switch_tab_by_handle(browser, 2, 0)
# #选择小狐狸
# goerli_login_metamask(browser, wait)

#准备转账
transfer_goerli_from_eth_to_zk(browser, wait)

#切換到小狐狸,准备确认
switch_tab_by_handle(browser, 1, 1)
fox_statue = fox_confirm_goerli_transfer(browser, wait)
if "失败" in fox_statue:
    print(f"第{excel_start}个号失败")
    Do_Excel(excel_path, sheetname="Sheet1").plain_write(excel_start, "B", "×")
elif "成功" in fox_statue:
    Do_Excel(excel_path, sheetname="Sheet1").plain_write(excel_start, "B", "成功")

#随机休息
aa = random.randint(20, 50)
time_sleep(aa, f"++++++++++随机等待时间{aa}")

for i in range(excel_start+1,201):
    print(f"准备换号:{i}")
    # success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, "B")
    # if success_or_fail != '成功':
    try:
        #第一步: 切换到ip页面,换ip
        switch_tab_by_handle(browser, 0, 0)
        random_select_clash_ip(browser, wait)
        time_sleep(5)

        #第二步: 切换到小狐狸页面,换帐号
        switch_tab_by_handle(browser, 1, 0)
        fox_change_account(browser, wait, i)
        time_sleep(5)

        #第三步: 切换到交易界面,进行作业
        switch_tab_by_handle(browser, 2, 0)

        #准备转账
        transfer_goerli_from_eth_to_zk(browser, wait)
        time_sleep(5)

        #第四步: 切换到小狐狸页面,进行确认
        switch_tab_by_handle(browser, 1, 1)
        fox_statue = fox_confirm_goerli_transfer(browser, wait)
        if "失败" in fox_statue:
            print(f"第{i}个号失败")
            Do_Excel(excel_path, sheetname="Sheet1").plain_write(i, "B", "×")
        elif "成功" in fox_statue:
            Do_Excel(excel_path, sheetname="Sheet1").plain_write(i, "B", "成功")

        #随机休息
        aa = random.randint(30, 60)
        time_sleep(aa, f"++++++++++==随机等待时间{aa}")
    except:
        continue

