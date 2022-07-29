#做sync上的所有项目,包括:
#1)ETH转USDC
#2)USDC转ETH
#3)提供流动性
#4)解除流动性

#为了跨文件夹导入包
import os,inspect
current_dir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(current_dir)
import sys
sys.path.append('../')

from basic.functions import *

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
url_dashboard = 'http://clash.razord.top/#/proxies'
sync_swap_trade = "https://syncswap.xyz/swap" #用于做swap任务
sync_swap_pool = "https://syncswap.xyz/pool/add"#用于流动性任务
excel_path = "/home/parallels/Documents/block_chain/sync_swap_50.xlsx"


#excel中, 标志列(用于记录任务成功或失败)
# B列 = goerli转到zk上,
# C列 = ETH转USDC, D列 = USDC转ETH
# E列 = 提供流动性, F列 = 解除流动性

write_to_excel_column = "E"  #把成功或失败记录到excel的列
read_from_excel_column = "E" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 23
browser_wait_times = 30

while True:
    for i in range(excel_start_row, 52):
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, read_from_excel_column)
        if success_or_fail != "成功":
            try:
                print(f"第{i}个号需要做任务")
                wait, browser = my_linux_chrome(time_out = browser_wait_times)
                #===========做一些准备工作
                #打開clash 切換ip
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                # ip_switcher(browser, wait, url_google)
                
                #清缓存, 登錄小狐狸,并换号
                delete_cookie(browser)
                login_metamask(browser, wait, metamask_pw, metamask_home)
                fox_change_account(browser, wait, i)

                #=============开始任务, i 用于记录第几个号, excel_which_column用于记录成功或失败
                #任务1:ETH转USDC. 任务成功会记录到excel中
                # ETH_swap_USDC(browser, wait, i, write_to_excel_column)
                
                # #任务2:USDC转ETH.模式0:随机转金额;模式1:全部转
                # USDC_swap_ETH(browser, wait, i, write_to_excel_column, 0)
                

                # #任务3:提供流动性
                syncswap_provide_LP(browser, wait, i, write_to_excel_column)

                # #任务4:解除流动性.模式0:移除随机比例的流动性;模式1:移除所有流动性
                # syncswap_remove_LP(browser, wait, i, write_to_excel_column, 0)

                ##=========== 这里要设置随机等待时间
                aa = random.randint(45, 80)
                time_sleep(aa, f"++++++++++随机等待时间{aa}")
                #循环安全关闭网页,最后关闭浏览器
                for j in range(2, -1, -1):
                    print(f"循环关闭网页{j}")
                    switch_tab_by_handle(browser, j, 0)
                    browser.close()
                    time.sleep(2)

                # browser.quit()
                aa = random.randint(2, 10)
                time_sleep(aa, f"++++++++++随机等待时间{aa}")

            except:
                Do_Excel(excel_path,sheetname='Sheet1').plain_write(i, write_to_excel_column, "×")
                time_sleep(5, f"----啊啊!第{i}个号出错了, 已经记录")
                try:
                    #循环安全关闭网页,最后关闭浏览器
                    for k in range(2, -1, -1):
                        print(f"循环关闭网页{k}")
                        switch_tab_by_handle(browser, k, 0)
                        browser.close()
                        time.sleep(2)
                except:
                    print("可能网页数量没那么多")
                # browser.quit()
                #随机休息
                aa = random.randint(10, 30)
                time_sleep(aa, f"++++++++++随机等待时间{aa}")
                continue
                





#     #新建标签页,准备转goerli
#     new_tab(browser, zksync_goerli_bridge)
#     switch_tab_by_handle(browser, 2, 0)
# # #选择小狐狸
# # goerli_login_metamask(browser, wait)

# #准备转账
# transfer_goerli_from_eth_to_zk(browser, wait)

# #切換到小狐狸,准备确认
# switch_tab_by_handle(browser, 1, 1)
# fox_statue = fox_confirm_goerli_transfer(browser, wait)
# if "失败" in fox_statue:
#     print(f"第{excel_start}个号失败")
#     Do_Excel(excel_path, sheetname="Sheet1").plain_write(excel_start, "B", "×")
# elif "成功" in fox_statue:
#     Do_Excel(excel_path, sheetname="Sheet1").plain_write(excel_start, "B", "成功")

# #随机休息
# aa = random.randint(20, 50)
# time_sleep(aa, f"++++++++++随机等待时间{aa}")

# for i in range(excel_start+1,52):
#     print(f"准备换号:{i}")
#     success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, "B")
#     if success_or_fail != '成功':
#         #第一步: 切换到ip页面,换ip
#         switch_tab_by_handle(browser, 0, 0)
#         random_select_clash_ip(browser, wait)
#         time_sleep(5)

#         #第二步: 切换到小狐狸页面,换帐号
#         switch_tab_by_handle(browser, 1, 0)
#         fox_change_account(browser, wait, i)
#         time_sleep(5)

#         #第三步: 切换到交易界面,进行作业
#         switch_tab_by_handle(browser, 2, 0)

#         #准备转账
#         transfer_goerli_from_eth_to_zk(browser, wait)
#         time_sleep(5)

#         #第四步: 切换到小狐狸页面,进行确认
#         switch_tab_by_handle(browser, 1, 1)
#         fox_statue = fox_confirm_goerli_transfer(browser, wait)
#         if "失败" in fox_statue:
#             print(f"第{i}个号失败")
#             Do_Excel(excel_path, sheetname="Sheet1").plain_write(i, "B", "×")
#         elif "成功" in fox_statue:
#             Do_Excel(excel_path, sheetname="Sheet1").plain_write(i, "B", "成功")

#         #随机休息
#         aa = random.randint(30, 60)
#         time_sleep(aa, f"++++++++++随机等待时间{aa}")

