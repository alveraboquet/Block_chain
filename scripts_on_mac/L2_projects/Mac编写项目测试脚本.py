#pycharm通过git同步代码：窗口右上角粉色小箭头➡️
from functions import *

excel_path = '/Users/spencer/PycharmProjects/Block_chain/eth1000_操作后.xlsx'
write_success_to_excel_column = "D"  #把成功或失败记录到excel的列
read_from_excel_column = "D" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 30
browser_wait_times = 10

for i in range(excel_start_row, 201):
    # one_sign =str(Do_Excel(excel_path).read(i, read_from_excel_column))
    # if "1" in one_sign:
    fail_sign = Do_Excel(excel_path).read(i, read_from_excel_column)

    if fail_sign != "成功":
        print(f"第 {i} 个号需要做zk")
        ##=========== 准备浏览器、切换IP、清理缓存
        wait, browser = my_mac_chrome(time_out = browser_wait_times)

        # open_clash_dashboard(browser, wait, url_dashboard)
        # random_select_clash_ip(browser, wait)
        # delete_cookie(browser)

        ##=========== 登陆小狐狸，
        login_metamask(browser, wait, metamask_pw, metamask_home, "Optimism")

        # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

        # 小狐狸换号
        print(f"===============小狐狸开始换号{i} ==============")
        fox_change_account(browser, wait, i)  #换号，选列表里的


        ##=========== 开始做任务
        save_record = galaxy_claim_op_hop_NFT(browser, wait)
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

