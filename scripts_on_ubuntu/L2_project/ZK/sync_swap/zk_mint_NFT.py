import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
excel_path= '/home/parallels/ubuntu_zk/Block_chain/eth1000_操作后.xlsx'

write_success_to_excel_column = "E"  #把成功或失败记录到excel的列
read_from_excel_column = "E" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 15

while 1:  #到时要把对应的txt行数删掉
    for i in range(2, 101):
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        if success_or_fail != "成功":
            print(f"第{i} 个号需要mint NFT ")
            try:
                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out = browser_wait_times)

                ##=========== 预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)

                ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
                delete_cookie(browser)

                ##============ 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home)
                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

                #=======小狐狸换号
                print(f"==============开始换号{i} ==============")
                fox_change_account(browser, wait, i)  # 换号，选列表里的

                ##=========== 开始做任务
                CID_text = DO_TXT(r"../json_CID.txt", i).read_x_line()
                print("这次用的CID_text是", CID_text)
                save_record = zksync_mint_NFT(browser, wait, CID_text)

                print("记录是：", save_record)
                if "成功" in save_record:
                    Do_Excel(excel_path,sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "成功")
                else:
                    Do_Excel(excel_path, sheetname='SheetJS').plain_write(i, write_success_to_excel_column, "×")
                ##=========== 这里要设置随机等待时间
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            #
            except:
                ##=========== 使用指定工作表，保存信息到excel
                print(f"----第{i}出错了，是excel没关闭吗？")
                Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")
                time_sleep(6, "出错了")
                browser.quit()
                continue

