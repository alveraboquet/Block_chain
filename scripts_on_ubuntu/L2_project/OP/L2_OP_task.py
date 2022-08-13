import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

excel_path = '/home/parallels/ubuntu_op/Block_chain/scripts_on_ubuntu/L2_project/OP/eth1000_OP_操作后.xlsx'

write_success_to_excel_column = "H"  #把成功或失败记录到excel的列
read_from_excel_column = "H" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 20

while 1:
    for i in range(excel_start_row, 201):
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        if success_or_fail !="成功":
            try:
                print(f"第 {i} 个号需要做 op")
                ##============= 一, 准备浏览器、切换IP、清理缓存
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                ##============= 二, 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home)
                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

                # ============= 三, 小狐狸换号
                print(f"===============小狐狸开始换号{i} ==============")
                fox_change_account(browser, wait, i)  #换号，选列表里的


                # ============= 四, 从 Debank 上获取某个网络余额
                from_source = get_balance_from_debank(browser, wait, "Optimism")
                if from_source == "ETH":                  
                    stable_coin_list = ["USDC", "DAI"]
                    # stable_coin_list = ["USDT", "USDT"]
                    to_source = random.choice(stable_coin_list)
                    # return "不要接着做任务了, 因为想把所有代币换位ETH"
                else: #说明稳定币的余额更多
                    to_source = "ETH"

                # ============= 五, 开始做任务
                print(f"本次要从 {from_source} 转到 {to_source}")                
                if i in range(2,40):
                    a = random.randint(1,2)
                    if a == 1:
                        save_record = OP_zipswap(browser, wait, from_source, to_source)
                    else:
                        save_record = OP_sushiswap(browser, wait, from_source, to_source)
                elif i in range(40,80):
                    a = random.randint(1,2)
                    if a == 1:
                        save_record = OP_uniswap(browser, wait, from_source, to_source)
                    else:
                        save_record = OP_matcha(browser, wait, from_source, to_source)
                elif i in range(80,120):
                    a = random.randint(1,2)
                    if a == 1:
                        save_record = OP_sushiswap(browser, wait, from_source, to_source)
                    else:
                        save_record = OP_clipper(browser, wait, from_source, to_source)
                elif i in range(120,160):
                    a = random.randint(1,2)
                    if a == 1:
                        save_record = OP_uniswap(browser, wait, from_source, to_source)
                    else:
                        save_record = OP_zipswap(browser, wait, from_source, to_source)
                elif i in range(160,201):
                    a = random.randint(1,2)
                    if a == 1:
                        save_record = OP_sushiswap(browser, wait, from_source, to_source)
                    else:
                        save_record = OP_clipper(browser, wait, from_source, to_source)


                print("记录是：",save_record)

                if "成功" in save_record:
                    Do_Excel(excel_path, sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "成功")
                else:
                    Do_Excel(excel_path, sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "×")

                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            except:
                print("出错了,将会记录到excel中")
                Do_Excel(excel_path, sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "×")
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()


