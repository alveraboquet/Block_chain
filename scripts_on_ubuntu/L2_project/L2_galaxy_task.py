import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *


excel_path= '/home/parallels/ubuntu_op/Block_chain/scripts_on_ubuntu/L2_project/ARB_NFT.xlsx'
             
write_success_to_excel_column = "B"  #把成功或失败记录到excel的列
read_from_excel_column = "B" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 30
browser_wait_times = 10

while 1:
    for i in range(excel_start_row, 201):
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, read_from_excel_column)
        print(f"现在的运行状态是：{success_or_fail}")
        if success_or_fail != "成功":
            print(f"第{i} 个号需要做 galaxy ")
            try:
                ##=========== 准备浏览器、切换IP、清理缓存
                wait, browser = my_linux_chrome(time_out = browser_wait_times)

                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                delete_cookie(browser)

                ##=========== 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home)

                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

                # 小狐狸换号
                print(f"===============小狐狸开始换号{i} ==============")
                fox_change_account(browser, wait, i)  #换号，选列表里的


                ##=========== 开始做任务
                save_record = galaxy_claim_op_hop_NFT(browser, wait)
                print("记录是：",save_record)

                if "成功" in save_record:
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "成功")
                else:
                    Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "×")

                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                    #
            except:
                ##=========== 使用指定工作表，保存信息到excel
                print(f"----第{i}出错了，是excel没关闭吗？")
                Do_Excel(excel_path,sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "×")
                time_sleep(10, "出错了")
                browser.quit()
                continue
