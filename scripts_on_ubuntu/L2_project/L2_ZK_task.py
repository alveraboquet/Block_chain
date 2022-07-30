import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

#============ZK上的项目
ZK_url = "https://wallet.zksync.io/transaction/deposit"  # 官方桥，L1转L2
zk_zigzag_url = "https://info.zigzag.exchange/"
zk_tevaera_url = "https://tevaera.com/"

#做 ZK 上的 zigzag，快进快出  buy_or_sell，由金额自动判断，当 USDC在前面是，去 Buy；当 ETH在前时，自动去 Sell
def ZK_zigzag_in_out(browser, wait):
    time_sleep(5, "准备打开 zigzag ")
    new_tab(browser, zk_zigzag_url)
    time_sleep(20, "正在打开 zigzag ")
    switch_tab_by_handle(browser, 2, 0)  # 切换到被撸网站

    zk_zigzag_start_tradding(browser, wait) #点击 start tradding
    ##++++++ 新账号需要激活 zigzag 账号。同样是小狐狸签名即可
    if zk_whether_connect_wallet(wait) == "CONNECT WALLET":
        print("zk 确实要连接钱包")
        try:
            zk_zigzag_connect_metamask(browser, wait)  # 在跳出的页面里，选择小狐狸
            time_sleep(3)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            fox_confirm_sign(browser, wait)  # 第一次是确认连接小狐狸签名
            time_sleep(10, "小狐狸第一次签名完毕")

            browser.refresh() #有可能要第二次签名，第二次是付费签名，
            time_sleep(10, "刷新完毕，有可能要第2次签名")
            fox_confirm_sign(browser, wait)
            time_sleep(5, "尝试第2次签名完毕")

            switch_tab_by_handle(browser, 2, 0)  # 【签名】成功后，再切换到zigzag
            time_sleep(3, "已经切换到 zigzag")
        except:
            print("不需要激活账号，因为小狐狸尝试第二次签名失败了")
            switch_tab_by_handle(browser, 2, 0)  # 【签名】成功后，再切换到zigzag
            time_sleep(3, "已经切换到 zigzag")

    ## =============== 判断是否连接小狐狸
    if zk_whether_connect_wallet(wait) == "CONNECT WALLET":
        print("确实要连接钱包")
        try:
            zk_zigzag_connect_metamask(browser, wait)  # 在跳出的页面里，选择小狐狸
            time_sleep(5)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            fox_confirm_sign(browser, wait)
            time_sleep(5)
            switch_tab_by_handle(browser, 2, 0)  # 【签名】成功后，再切换到zigzag
            time_sleep(3)
            # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
            # fox_confirm_connect_account(browser, wait) #小狐狸确认连接所有账号
        except:
            print("zigzag，小狐狸确认连接账号失败，是否影响？")
            switch_tab_by_handle(browser, 2, 0)  # 【签名】成功后，再切换到zigzag

    #选择 ETH 的兑换标的，可选 DAI、USDT、USDC
    select_token = "DAI"
    ZK_zigzag_choose_token(browser, wait, select_token)

    ## ============== 获取Zigzag上有多少ETH，返回余额（字符串），之后传参给 zk_zigzag_prepare_swap()
    balance_and_token = get_ZK_zigzag_balance(browser, wait)
    print("获得的余额是：", balance_and_token)
    matches = re.search('[\d.]+', balance_and_token)  # 正则提取类似 “0.001 ETH”
    zigzag_balance = matches.group()

    ##  自动判断 Sell或 Buy，
    if select_token in balance_and_token:
        buy_or_sell = "Buy"
    elif "ETH" in balance_and_token:
        buy_or_sell = "Sell"

    detail = zk_zigzag_prepare_swap(browser, wait, zigzag_balance, buy_or_sell)

    # 小狐狸去确认交易
    if "成功" in detail:  #如果 zk_zigzag_prepare_swap 成功，则小狐狸去确认
        print("小狐狸去【签名】")
        switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：
        fox_info = fox_confirm_sign(browser, wait) #可能会出现签名
        # success_or_fail = fox_confirm_swap(browser, wait)  # 小狐狸确认交易
        print(f"本次zigzag 交易额是{detail}")
        switch_tab_by_handle(browser, 2, 0)  # 切换到zigzag
    print(detail)
    time_sleep(30, "准备关闭当前页面")
    browser.close()  # 关闭当前的zigzag 网页，方便反向操作
    switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

    if "成功" in fox_info:
        return "ZK zigzag 任务完成；" + detail + fox_info
    elif "失败" in fox_info:
        return fox_info


excel_path= '/home/parallels/ubuntu_zk/Block_chain/eth1000_操作后.xlsx'
#excel中, 标志列(用于记录任务成功或失败)
# B列 = goerli转到zk上,
# C列 = ETH转USDC, D列 = USDC转ETH
# E列 = 提供流动性, F列 = 解除流动性

write_success_to_excel_column = "D"  #把成功或失败记录到excel的列
write_major_token_to_excel_column = "F"  #记录主要代币是什么

read_from_excel_column = "D" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 30

while 1:
    for i in range(10, 201):
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        current_major_token = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        print(f"现在的运行状态是：{success_or_fail}, 主要代币是：{current_major_token}")
        if success_or_fail != "成功":
            if current_major_token !="ETH":
                print(f"第{i} 个号需要做 zk ")
                try:
                        ##=========== 准备浏览器
                    wait, browser = my_linux_chrome()

                    ##=========== 预备步骤：切换IP。先打开
                    open_clash_dashboard(browser, wait, url_dashboard)
                    # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                    # ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页
                    random_select_clash_ip(browser, wait)


                    ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
                    delete_cookie(browser)

                    ##=========== 登陆小狐狸，
                    login_metamask(browser, wait, metamask_pw, metamask_home, "Ethereum")
                    switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
                    # 小狐狸换号
                    print(f"==============开始换号{i} ==============")
                    fox_change_account(browser, wait, i)  #换号，选列表里的
                    
                    time_sleep(3600, "waiting")
                    ##=========== 开始做任务
                    #正向操作，记录保存信息到excel
                    save_record = ZK_zigzag_in_out(browser, wait)
                    if "ZK zigzag" in save_record:
                        Do_Excel(excel_path).write(i, "V", save_record)  #
                        time_sleep(30, f"{save_record}，日志写入excel成功，30 秒后反向操作")
                    else:
                        Do_Excel(excel_path).write(i, "V", save_record)  # 
                        time_sleep(30, f"{save_record}，日志写入excel成功，30 秒后反向操作")

                    #===========反向操作, 保存信息到excel
                    save_record = ZK_zigzag_in_out(browser, wait)
                    if "ZK zigzag" in save_record:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        Do_Excel(excel_path).write(i, "P", "√")
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(excel_path).write(i, "V", save_record)  
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    
                    # 
                    Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
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
