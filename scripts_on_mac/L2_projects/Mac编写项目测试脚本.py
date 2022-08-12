#pycharm通过git同步代码：窗口右上角粉色小箭头➡️
from functions import *

excel_path = '/Users/spencer/PycharmProjects/Block_chain/eth1000_操作后.xlsx'
write_success_to_excel_column = "F"  #把成功或失败记录到excel的列
read_from_excel_column = "F" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 10
while 1:
    for i in range(excel_start_row, 101):
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        if success_or_fail !="成功":
            try:
                print(f"第 {i} 个号需要做zk")
                ##=========== 准备浏览器、切换IP、清理缓存
                wait, browser = my_mac_chrome(time_out = browser_wait_times)
                # wait, browser = my_linux_chrome(time_out=browser_wait_times)
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                ##=========== 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home)
                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

                # =============小狐狸换号
                print(f"===============小狐狸开始换号{i} ==============")
                fox_change_account(browser, wait, i)  #换号，选列表里的


                ##=========== 开始做任务
                CID_text = DO_TXT(r"json_CID.txt", i).read_x_line()
                print("这次用的CID_text是",CID_text)
                save_record = zksync_mint_NFT(browser, wait, CID_text)

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
                Do_Excel(excel_path, sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "×")
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()


