# L2 做 OP 的任务
# 主要是swap，自动判断从金额高的token转到低token
from Basic_files.functions import *

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
    swap_times = "0" #用于记录是否需要再交互一次

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
        swap_times = "1" #因为是从ETH换出去
        print("matcha，由于最大代币是ETH，所以 swap_times = ", swap_times)
        from_token = "Ethereum"
        to_token = "USD Coin"
        # return 0  # 暂时不换

    elif "USDC" in max_token:
        print("matcha，由于最大代币是USDC，所以只要兑换一次")
        from_token = "USD Coin"
        to_token = "Ethereum"

    elif "DAI" in max_token:
        print("matcha，由于最大代币是DAI，所以只要兑换一次")
        from_token = "Dai"
        to_token = "Ethereum"

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
            return "OP matcha 任务完成；" + fox_info + detail, swap_times
        else:
            return " matcha 还是换钱失败", swap_times
    elif "失败" in fox_info:
        return fox_info, swap_times

#做 OP上的 zipswap
def OP_zipswap():
    # =====小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Optimism")
    # time.sleep(5)
    swap_times = "0"  # 用于记录是否需要再交互一次
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
        swap_times = "0"
        from_token = "USDC"
        to_token = "ETH"
        L2_max_value = L2_USDC_value
    else:
        L2_max_value = L2_ETH_value #从ETH换过去
        swap_times = "1"
        print("matcha，由于最大代币是ETH，所以 swap_times = ", swap_times)
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
        return "OP zipswap 任务完成；" + fox_info + detail, swap_times
    elif "失败" in fox_info:
        return fox_info, swap_times

#做 OP上的 clipper
def OP_clipper():
    #========== 小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)
    # fox_change_network(browser, wait, "Optimism")
    # time_sleep(5)
    swap_times = "0"
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
        swap_times = "0"
        from_token = "USDC"
        to_token = "ETH"
        L2_value = L2_USDC_value
    else:
        L2_value = L2_ETH_value #从ETH换出去
        swap_times = "1"
        print("matcha，由于最大代币是ETH，所以 swap_times = ", swap_times)
        # return 0 #暂时不换

    detail = clipper_prepare_transfer(browser, wait, L2_value, from_token, to_token)
    time_sleep(3)

    #=======小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    info = fox_confirm_OP(browser, wait)
    time_sleep(5)
    switch_tab_by_handle(browser, 2, 0)  # 切换到
    if "成功" in info:
        return " OP clipper 任务完成；" + info + detail, swap_times
    elif "失败" in info:
        return info, swap_times


#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5
# 得从第二个号开始才有钱
excel_path= "/Users/spencer/PycharmProjects/Blockchain项目/eth1000_操作后.xlsx"

for i in range(109, 201):
        # one_sign = str(Do_Excel(excel_path).read(i, "I"))
        # if "1" in one_sign:
        fail_sign = Do_Excel(excel_path).read(i, "G")
        if fail_sign != "·成功":
            print(f"=====================第 {i} 个号需要做 OP ==================")
            try:
                ##=========== 准备浏览器
                wait, browser = my_mac_chrome()
                time_sleep(5,"开始干活")
                ##=========== 预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页

                ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
                delete_cookie(browser)

                ##=========== 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home, "Optimism")
                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
                # 小狐狸换号
                print(f"=======开始换号{i}   ==============")
                fox_change_account(browser, wait, i)  # 换号，选列表里的
                time_sleep(2)
                ##=========== 开始做任务

                a = random.randint(1, 3)
                if a == 1:
                    print("做OP_matcha()")  # from_token，可选"Ethereum"， "USD Coin"， "sUSD"
                    save_record, swap_times = OP_matcha()
                    #记录 excel 信息
                    if "OP matcha" in save_record:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        Do_Excel(excel_path).write(i, "T", "√")
                        Do_Excel(excel_path).plain_write(i, "G", "·成功")
                        Do_Excel(excel_path).plain_write(i, "K", swap_times) #用于记录是否要第2次换钱
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        time_sleep(2, f"{save_record}，日志写入excel成功")

                elif a == 2:
                    print("做OP_zipswap()")
                     #from，to可选"ETH"， "USDC"，"USDT"
                    save_record, swap_times = OP_zipswap()  #测试通过
                    # =====记录信息到 excel 中
                    if "OP zipswap" in save_record:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        Do_Excel(excel_path).write(i, "R", "√")
                        Do_Excel(excel_path).plain_write(i, "G", "·成功")
                        Do_Excel(excel_path).plain_write(i, "K", swap_times)  # 用于记录是否要第2次换钱
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        time_sleep(2, f"{save_record}，日志写入excel成功")

                elif a == 3:
                    print("做OP_clipper()")
                    #from，to可选"ETH"， "USDC"，"USDT"
                    save_record, swap_times = OP_clipper() # 测试通过
                    # save_record = OP_clipper("USDC", "ETH") # 测试通过
                    # =====记录信息到 excel 中
                    if "OP clipper" in save_record:
                        Do_Excel(excel_path).write(i, "V", save_record)
                        Do_Excel(excel_path).write(i, "S", "√")
                        Do_Excel(excel_path).plain_write(i, "G", "·成功")
                        Do_Excel(excel_path).plain_write(i, "K", swap_times)  # 用于记录是否要第2次换钱
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
                Do_Excel(excel_path).plain_write(i, "G", "×")
                time_sleep(5, "出错了")
                browser.quit()
                continue

