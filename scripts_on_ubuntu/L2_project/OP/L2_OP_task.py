# L2 做 OP 的任务: swap-----> matcha, clipper, zipswap
# 主要是swap，自动判断从金额高的token转到低token
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *



excel_path = '/home/parallels/ubuntu_op/Block_chain/scripts_on_ubuntu/L2_project/OP/eth1000_OP_操作后.xlsx'
#excel中, 标志列(用于记录任务成功或失败)
# B列 = goerli转到zk上,
# C列 = ETH转USDC, D列 = USDC转ETH
# E列 = 提供流动性, F列 = 解除流动性

write_success_to_excel_column = "H"  #把成功或失败记录到excel的列
write_major_token_to_excel_column = "J"  #记录主要代币是什么

read_from_excel_column = "H" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 30


while 1:
    for i in range(excel_start_row, 201):
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        current_major_token = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        print(f"现在的运行状态是：{success_or_fail}, 主要代币是：{current_major_token}")
        if success_or_fail != "成功":
            if current_major_token !="ETH":
                print(f"===================== 第 {i} 个号需要做 OP ==================")
                try:
                    ##=========== 准备浏览器
                    wait, browser = my_linux_chrome()

                    ##=========== 预备步骤：切换IP。先打开
                    open_clash_dashboard(browser, wait, url_dashboard)
                    random_select_clash_ip(browser, wait)
                    # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                    # ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页


                    #清缓存, 登錄小狐狸,并换号
                    delete_cookie(browser)
                    login_metamask(browser, wait, metamask_pw, metamask_home)
                    fox_change_account(browser, wait, i)
                    ##=========== 开始做任务

                    a = random.randint(1, 3)
                    if a == 1:
                        print("做OP_matcha()")  # from_token，可选"Ethereum"， "USD Coin"， "sUSD"
                        save_record, major_token = OP_matcha(browser, wait)
                        #记录 excel 信息
                        if "OP matcha" in save_record:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            Do_Excel(excel_path).write(i, "T", "√")
                            Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
                            Do_Excel(excel_path).plain_write(i, write_major_token_to_excel_column, major_token) #用于记录是否要第2次换钱
                            time_sleep(2, f"{save_record}，日志写入excel成功")
                        else:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            time_sleep(2, f"{save_record}，日志写入excel成功")

                    elif a == 2:
                        print("做OP_zipswap()")
                            #from，to可选"ETH"， "USDC"，"USDT"
                        save_record, major_token = OP_zipswap(browser, wait)  #测试通过
                        # =====记录信息到 excel 中
                        if "OP zipswap" in save_record:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            Do_Excel(excel_path).write(i, "R", "√")
                            Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
                            Do_Excel(excel_path).plain_write(i, write_major_token_to_excel_column, major_token)  # 用于记录是否要第2次换钱
                            time_sleep(2, f"{save_record}，日志写入excel成功")
                        else:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            time_sleep(2, f"{save_record}，日志写入excel成功")

                    elif a == 3:
                        print("做OP_clipper()")
                        #from，to可选"ETH"， "USDC"，"USDT"
                        save_record, major_token = OP_clipper(browser, wait) # 测试通过
                        # save_record = OP_clipper("USDC", "ETH") # 测试通过
                        # =====记录信息到 excel 中
                        if "OP clipper" in save_record:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            Do_Excel(excel_path).write(i, "S", "√")
                            Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
                            Do_Excel(excel_path).plain_write(i, write_major_token_to_excel_column, major_token)  # 用于记录是否要第2次换钱
                            time_sleep(2, f"{save_record}，日志写入excel成功")
                        else:
                            Do_Excel(excel_path).write(i, "V", save_record)
                            time_sleep(2, f"{save_record}，日志写入excel成功")


                    ##=========== 这里要设置随机等待时间
                    a = random.randint(10, 15)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                    browser.quit()
                    a = random.randint(5, 10)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                except:
                    print(f"----第{i}出错了")
                    Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")
                    time_sleep(10, "出错了")
                    browser.quit()
                    continue

