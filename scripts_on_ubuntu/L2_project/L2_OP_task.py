# L2 做 OP 的任务: swap-----> matcha, clipper, zipswap
# 主要是swap，自动判断从金额高的token转到低token
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

#####################一些url
lifi_url = "https://transferto.xyz/swap"
ARB_url = "https://bridge.arbitrum.io/"
ZK_url = "https://wallet.zksync.io/transaction/deposit"
OP_url = "https://app.optimism.io/bridge"
test_url = "https://www.baidu.com/"

#============OP上的项目
op_pika_url = "https://app.pikaprotocol.com/trade/ETH-USD"
op_showme_url = "https://optimismair.showme.fan/"
op_zipswap_url = "https://zipswap.fi/#/swap"
op_clipper_url = "https://clipper.exchange/app/swap"
matcha_url = "https://matcha.xyz/login"


#==================================下面是 OP 的任务
# from_token，可选"Ethereum"， "USD Coin"，"sUSD"
def OP_matcha():
    # ==========将小狐狸的网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Optimism")
    # time_sleep(5, "开始OP_matcha任务")
    major_token = "" #记录经过swap后的主要代币是什么

    new_tab(browser, matcha_url)
    time_sleep(10, "等待抹茶加载")
    switch_tab_by_handle(browser, 2, 0)  # 切换到抹茶

    time_sleep(3, "准备判断小狐狸是否连接钱包")
    # 如果没有连接小狐狸钱包，则先去连接钱包
    if matcha_fox_icon_exit(browser, wait) != 1: # 返回值是1，说明有小狐狸图标，说明已经连接了小狐狸
        print("Match没有连接小狐狸，先去连接")
        matcha_connect_wallet(browser, wait)  # 先连接钱包
        # switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，去连接账号
        # fox_confirm_connect_account(browser, wait)  #
        # time.sleep(4)
        # switch_tab_by_handle(browser, 2, 1)  # 切换到第3个标签页：matcha

    time_sleep(2, "提醒：请记得先把抹茶上的网络切为 OP")
    if matcha_whether_change_net(browser, wait) != "Optimism":
        matcha_change_net(browser, wait)

    time_sleep(2, "通过抹茶，实时获取OP上的最大余额有多少，并确定from token")
    max_token, L2_balance = get_OP_token_balance_by_matcha(browser, wait)

    if "ETH" in max_token:
        print("matcha，从ETH换出去")
        from_token = "Ethereum"
        to_token = "USD Coin"
        major_token = "USDC" #因为是从ETH换出去

        # return 0  # 暂时不换

    elif "USDC" in max_token:
        print("matcha，由于最大代币是USDC，所以只要兑换一次")
        from_token = "USD Coin"
        to_token = "Ethereum"
        major_token = "ETH" #因为是从USDC换出去

    elif "DAI" in max_token:
        print("matcha，由于最大代币是DAI，所以只要兑换一次")
        from_token = "Dai"
        to_token = "Ethereum"
        major_token = "ETH" #因为是从USDC换出去

    time_sleep(2, f"正式换钱，从 {from_token} 换到 {to_token}")
    detail = matcha_input_coin_amount(browser, wait, L2_balance, from_token, to_token)  #准备换钱

    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，
    fox_info = fox_confirm_OP(browser, wait)  # 小狐狸确认交易
    time_sleep(8)
    switch_tab_by_handle(browser, 2, 0)  # 切换到matcha

    # 转账后，20秒后，查询OP上的USDC、DAI是否到账
    time_sleep(20,"准备查询是否 matcha Success？")
    transfer_status = matcha_whether_transfer_success(browser, wait)

    if "成功" in fox_info:
        if transfer_status == "Success!":
            print("matcha 确实换钱 Success！")
            return "OP matcha 任务完成；" + fox_info + detail, major_token
        else:
            return " matcha 还是换钱失败", major_token
    elif "失败" in fox_info:
        return fox_info, major_token

#做 OP上的 zipswap
def OP_zipswap():
    # =====小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Optimism")
    # time.sleep(5)
    major_token = "" #记录经过swap后的主要代币是什么
    print("开始OP_zipswap任务")
    new_tab(browser, op_zipswap_url)
    time_sleep(15, "等待zipswap加载")
    switch_tab_by_handle(browser, 2, 0)  # 切换到zipswap

    #======连接钱包
    if zipswap_whether_connect_wallet(browser, wait) == "Connect Wallet":
        print("需要连接钱包")
        zipswap_connect_wallet(browser, wait)
        time.sleep(5)
        switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
        fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
        switch_tab_by_handle(browser, 2, 0)  # 切换到第1个标签页：被撸网站

    #=========实时获取 OP上的ETH金额，返回浮点型数据
    # L2_ETH_value = get_OP_ETH_by_zipswap(wait)
    from_token = "ETH"
    to_token = "USDC"
    L2_ETH_value, L2_USDC_value = get_OP_ETH_and_select_from_to_token_by_zipswap(browser, wait, from_token, to_token)
    if L2_ETH_value < 0.01:
        from_token = "USDC"
        to_token = "ETH"
        L2_max_value = L2_USDC_value
        major_token = "ETH" #因为是从USDC换出去
    else:
        L2_max_value = L2_ETH_value #从ETH换过去
        major_token = "USDC" #因为是从USDC换出去
        print("matcha，从ETH换出去")
        # return 0  # 暂时不换

    #======选择代币、输入金额、确认交易， #from，to可选"ETH"， "USDC"，"USDT"
    detail = zipswap_prepare_transfer(browser, wait, L2_max_value, from_token, to_token)
    time_sleep(8)

    #========小狐狸确认
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    fox_info = fox_confirm_OP(browser, wait)

    #关闭zipswap
    switch_tab_by_handle(browser, 2, 0)  # 切换到第0个标签页：小狐狸
    time_sleep(5)

    if "成功" in fox_info:
        return "OP zipswap 任务完成；" + fox_info + detail, major_token
    elif "失败" in fox_info:
        return fox_info, major_token

#做 OP上的 clipper
def OP_clipper():
    #========== 小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)
    # fox_change_network(browser, wait, "Optimism")
    # time_sleep(5)
    major_token = "" #记录经过swap后的主要代币是什么
    print("开始OP_clipper任务")
    new_tab(browser, op_clipper_url)
    time_sleep(15, "等待 clipper 加载")
    switch_tab_by_handle(browser, 2, 0)
    time_sleep(3)

    #连接钱包
    if clipper_whether_connect_wallet(browser, wait) == "Connect your wallet":
        print("需要连接钱包")
        clipper_connect_wallet(browser, wait)
        time_sleep(5)
        # switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
        # fox_confirm_showme_zipswap(browser, wait)
        # switch_tab_by_handle(browser, 2, 0)  # 切换到第1个标签页：被撸网站
        # time_sleep(5)
    #============选择代币、输入金额、确认交易，返回浮点数
    # L2_ETH_value = get_OP_ETH_by_clipper(wait)
    from_token = "ETH"
    to_token = "USDC"
    L2_ETH_value, L2_USDC_value = get_OP_ETH_and_select_from_to_token_by_clipper(browser, wait, from_token, to_token)

    # from，to可选"ETH"， "USDC"，"USDT"
    if L2_ETH_value < 0.01:
        from_token = "USDC"
        to_token = "ETH"
        L2_value = L2_USDC_value
        major_token = "ETH" #因为是从USDC换出去
    else:
        L2_value = L2_ETH_value #从ETH换出去
        major_token = "USDC" #因为是从USDC换出去
        print("matcha，从ETH换出去")
        # return 0 #暂时不换

    detail = clipper_prepare_transfer(browser, wait, L2_value, from_token, to_token)
    time_sleep(3)

    #=======小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    info = fox_confirm_OP(browser, wait)
    time_sleep(5)
    switch_tab_by_handle(browser, 2, 0)  # 切换到
    if "成功" in info:
        return " OP clipper 任务完成；" + info + detail, major_token
    elif "失败" in info:
        return info, major_token


excel_path= '/home/parallels/ubuntu_op/Block_chain/eth1000_操作后.xlsx'
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
                        save_record, major_token = OP_matcha()
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
                        save_record, major_token = OP_zipswap()  #测试通过
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
                        save_record, major_token = OP_clipper() # 测试通过
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
                    a = random.randint(2, 10)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                    browser.quit()
                    a = random.randint(2, 10)
                    time_sleep(a, f"++++++++++随机等待时间{a}")
                except:
                    print(f"----第{i}出错了")
                    Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")
                    time_sleep(5, "出错了")
                    browser.quit()
                    continue

