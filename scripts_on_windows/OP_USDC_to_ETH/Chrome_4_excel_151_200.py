# L2 做 ARB 的任务
from L2.functions import *

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
def OP_matcha(from_token, to_token):
    # ==========将小狐狸的网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Optimism")
    # time_sleep(5, "开始OP_matcha任务")
    new_tab(browser, matcha_url)
    time_sleep(20, "等待抹茶加载")
    switch_tab_by_handle(browser, 2, 0)  # 切换到抹茶

    time_sleep(5, "准备判断小狐狸是否连接钱包")
    # 如果没有连接小狐狸钱包，则先去连接钱包
    if matcha_fox_icon_exit(browser, wait) != 1: # 返回值是1，说明有小狐狸图标，说明已经连接了小狐狸
        print("Match没有连接小狐狸，先去连接")
        matcha_connect_wallet(browser, wait)  # 先连接钱包
        # switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，去连接账号
        # fox_confirm_connect_account(browser, wait)  #
        # time.sleep(4)
        # switch_tab_by_handle(browser, 2, 1)  # 切换到第3个标签页：matcha

    time_sleep(5, "先把抹茶上的网络切为 OP")
    if matcha_whether_change_net(browser, wait) != "Optimism":
        matcha_change_net(browser, wait)

    time_sleep(5, "通过抹茶，实时获取OP上的余额有多少")
    L2_ETH_balance = get_OP_ETH_by_matcha_and_prepare_from_to_token(browser, wait, from_token, to_token)

    time_sleep(5, "正式换钱")
    detail = matcha_input_coin_amount(browser, wait, L2_ETH_balance, from_token, to_token)  #准备换钱
    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，
    fox_info = fox_confirm_OP(browser, wait)  # 小狐狸确认交易
    time.sleep(5)
    switch_tab_by_handle(browser, 2, 0)  # 切换到
    if "成功" in fox_info:
        return "OP matcha 任务完成；" + fox_info + detail
    elif "失败" in fox_info:
        return fox_info
    # # 转账后，20秒后，查询OP上的USDC是否到账
    # time.sleep(20)
    # switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
    # all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
    # OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
    #
    # while OP_USDC_balance_after == OP_USDC_balance_before:
    #     print("OP上的 USDC 还没到账，20秒轮询一次")
    #     time.sleep(20)  # 20秒去轮询一次
    #     switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
    #     all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
    #     OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
    #
    # print(f"OP上的 USDC 到账了，金额是 {OP_USDC_balance_after}")
    # switch_tab_by_handle(browser, 2, 0)  # 切换到：matcha
    # time.sleep(5)

#做 OP上的 zipswap
def OP_zipswap(from_token, to_token):
    # =====小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Optimism")
    # time.sleep(5)
    print("开始OP_zipswap任务")
    new_tab(browser, op_zipswap_url)
    time_sleep(30, "等待zipswap加载")
    switch_tab_by_handle(browser, 2, 0)  # 切换到zipswap

    #======连接钱包
    if zipswap_whether_connect_wallet(browser, wait) == "Connect Wallet":
        print("需要连接钱包")
        zipswap_connect_wallet(browser, wait)
        # time.sleep(5)
        # switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
        # fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
        # switch_tab_by_handle(browser, 2, 0)  # 切换到第1个标签页：被撸网站

    #=========实时获取 OP上的ETH金额，返回浮点型数据
    L2_ETH_value = get_OP_ETH_and_select_from_to_token_by_zipswap(browser, wait, from_token, to_token)

    #======选择代币、输入金额、确认交易
    detail = zipswap_prepare_transfer(browser, wait, L2_ETH_value, from_token, to_token)
    time.sleep(8)
    #========小狐狸确认
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    fox_info = fox_confirm_OP(browser, wait)
    switch_tab_by_handle(browser, 2, 0)
    if "成功" in fox_info:
        return "OP zipswap 任务完成；" + fox_info + detail
    elif "失败" in fox_info:
        return fox_info

#做 OP上的 clipper
def OP_clipper(from_token, to_token):
    #========== 小狐狸网络切换成OP
    # switch_tab_by_handle(browser, 1, 0)
    # fox_change_network(browser, wait, "Optimism")
    # time_sleep(5)
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
    L2_ETH_value = get_OP_ETH_and_select_from_to_token_by_clipper(browser,wait, from_token, to_token)


    detail = clipper_prepare_transfer(browser, wait, L2_ETH_value, from_token, to_token)
    time_sleep(3)

    #=======小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    info = fox_confirm_OP(browser, wait)
    time_sleep(5)
    switch_tab_by_handle(browser, 2, 0)  # 切换到
    if "成功" in info:
        return "OP clipper 任务完成；" + info + detail
    elif "失败" in info:
        return info


#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5
# 得从第二个号开始才有钱
while True:
    for i in range(38, 52):
      if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i+149, "E")) == "1":   # OP 所在列
          if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i+149, "G")) != "换ETH":
            print(f"=====================第{i}, {i+149}个 OP 号需要 USDC 转 ETH  ==================")
            try:
                ##=========== 准备浏览器
                which_chrome = 4
                wait, browser = my_chrome(which_chrome)

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
                print(f"=======开始换号{i}  ==============")
                fox_change_account(browser, wait, i)  # 换号，选列表里的

                #======== 正式开始做任务
                a = random.randint(1,3)#2-4
                if a == 1:
                    print("做OP_zipswap()")
                    #from，to可选"ETH"， "USDC"，"USDT"
                    # save_record = OP_zipswap("ETH", "USDC")  #测试通过
                    save_record = OP_zipswap("USDC", "ETH")  # 测试通过
                    # save_record = OP_zipswap("USDC", "ETH")  # 测试通过
                    # =====记录信息到 excel 中
                    if "OP zipswap" in save_record:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i+149, "G", "换ETH")
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        time_sleep(2, f"{save_record}，日志写入excel成功")

                elif a == 2:
                    print("做OP_clipper()")
                    #from，to可选"ETH"， "USDC"，"USDT"
                    # save_record = OP_clipper("ETH", "USDC") # 测试通过
                    save_record = OP_clipper("USDC", "ETH")  # 测试通过
                    # save_record = OP_clipper("USDC", "ETH") # 测试通过
                    # =====记录信息到 excel 中
                    if "OP clipper" in save_record:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i+149, "G", "换ETH")
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                elif a == 3:
                    print("做OP_matcha()")
                    # from_token，可选"Ethereum"， "USD Coin"，"sUSD"
                    # save_record = OP_matcha("Ethereum", "USD Coin")
                    save_record = OP_matcha("USD Coin", "Ethereum")
                    if "OP matcha" in save_record:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i+149, "G", "换ETH")
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                    else:
                        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "V", save_record)
                        time_sleep(2, f"{save_record}，日志写入excel成功")
                ##=========== 这里要设置随机等待时间
                a = random.randint(1, 3)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(1, 3)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            except:
                print("出错了")
                Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i+149, "G", "出错了")
                a = random.randint(5, 20)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(5, 20)
                time_sleep(a, f"++++++++++随机等待时间{a}")
