#功能：把L1的钱，转到L2
import time

from functions import *
test_url = "https://www.baidu.com/"

L1_ETH_save_min = 0.01  #想要在L1保留的最小值

#主网——》lifi——》ARB
def mainnet_lifi_ARB(browser, wait, L1_ETH_value):
    print("通过lifi，转到OP。第一步是：小狐狸切换到主网")
    switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
    fox_change_network(browser, wait, "Ethereum")

    #======打开lifi
    new_tab(browser, lifi_url)
    switch_tab_by_handle(browser, 2, 0)  # 切换到第lifi
    if lifi_whether_connect_wallet(browser, wait) == "Connect Your Wallet":
        lifi_connect_wallet(browser, wait)
        # switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
        # fox_confirm_connect_network(browser, wait)
        time.sleep(3)
        # switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi

    # lifi准备换币。返回本次的交易值
    input_balance = L1_lifi_L2_prepare_transfer_coin(browser, wait, L1_ETH_value, L1_ETH_save_min, "Ethereum", "Arbitrum One")

    #lifi确认换币
    lifi_swap(browser, wait)
    time_sleep(10, "lifi 确认换币")

    #===== 小狐狸查询gas fee，高的话拒绝交易，否则直接交易，返回成功或失败信息
    switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
    success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)

    if "成功" in success_or_fail:
        #回到lifi，
        switch_tab_by_handle(browser, 2, 0)  # 切换到lifi
        wait_lifi_complete(wait)
        time.sleep(2)
        success = "成功"
        detail = f"【ARB】通过lifi，转到ARB：{input_balance}ETH，{success_or_fail}"
        # switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return success, detail
    else: #交易失败
        fail = "fail"
        detail = f"【失败ARB】通过lifi，转到ARB：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return fail, detail

#主网——》lifi——》OP
def mainnet_lifi_OP(browser, wait, L1_ETH_value):
    print("通过lifi，转到OP。第一步是：小狐狸切换到主网")
    switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
    fox_change_network(browser, wait, "Ethereum")

    #打开lifi
    new_tab(browser, lifi_url)
    switch_tab_by_handle(browser, 2, 0)  # 切换到第lifi

    if lifi_whether_connect_wallet(browser, wait) == "Connect Your Wallet":
        lifi_connect_wallet(browser, wait)
        # switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
        # fox_confirm_connect_network(browser, wait)
        time.sleep(3)
        # switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi

    # lifi准备换币。返回本次的交易值
    input_balance = L1_lifi_L2_prepare_transfer_coin(browser, wait, L1_ETH_value, L1_ETH_save_min, "Ethereum", "Optimistic Ethereum")

    # lifi确认换币
    lifi_swap(browser, wait)
    time_sleep(10, "lifi确认换币")

    # 小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
    success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)  # 小狐狸确认交易

    # 回到lifi，关闭它
    if "成功" in success_or_fail:
        switch_tab_by_handle(browser, 2, 0)  # 切换到第小狐狸，刷新
        wait_lifi_complete(wait)
        time.sleep(2)
        success = "成功"
        detail = f"【OP】通过lifi，转到OP：{input_balance}ETH，{success_or_fail}"
        # switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return success, detail
    else:
        fail = "fail"
        detail = f"【失败OP】通过lifi，转到OP：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return fail, detail

#主网——》ARB官方桥——》ARB
def mainnet_ARB_official_ARB(browser, wait, L1_ETH_value):
    print("通过ARB官方桥，转到ARB。第一步是：小狐狸切换到主网")
    switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
    fox_change_network(browser, wait, "Ethereum")
    new_tab(browser, ARB_url)
    switch_tab_by_handle(browser, 2, 0)  # 切换到第ARB
    time_sleep(10, "切换到第ARB")

    #=========连接钱包
    ARB_connect_wallet(browser, wait)
    time_sleep(15,"ARB连接钱包")
    ARB_bridge_I_agree(browser, wait)
    time_sleep(10, "ARB 点击I agree")

    # ===========ARB输入转账金额，并提交订单
    input_balance = ARB_prepare_transfer(browser, wait, L1_ETH_value, L1_ETH_save_min )
    time_sleep(10, "ARB 准备订单")

    # =========小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：被撸网站
    success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)  # 小狐狸确认交易

    if "成功" in success_or_fail:
        # 切换到ARB，并关闭
        switch_tab_by_handle(browser, 2, 0)  # 切换到第
        time_sleep(32, "等待ARB交易成功")
        # wait_OP_complete(wait)#等待关闭 很慢
        # browser.close()
        success = "成功"
        detail = f"【ARB】通过ARB官方桥，转到ARB：{input_balance}ETH，{success_or_fail}"
        # switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return success, detail
    else:
        fail = "fail"
        detail = f"【失败ARB】通过ARB官方桥，转到ARB：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return fail, detail

#主网——》OP官方桥——》OP
def mainnet_OP_official_OP(browser, wait,L1_ETH_value):
    print("通过OP官方桥，转到OP。第一步是：小狐狸切换到OP")
    switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
    fox_change_network(browser, wait, "Ethereum")
    new_tab(browser, OP_url)
    switch_tab_by_handle(browser, 2, 0)  # 切换到OP
    time_sleep(8, "切换到第 OP")

    # ARB输入转账金额，并提交订单
    input_balance = OP_prepare_transfer(browser, wait, L1_ETH_value, L1_ETH_save_min)
    time_sleep(8, "OP准备订单完毕")
    # 小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：被撸网站
    success_or_fail= fox_get_gas_fee_and_confirm_swap(browser, wait)  # 小狐狸确认交易
    time.sleep(3)

    # 切换到OP，并关闭
    switch_tab_by_handle(browser, 2, 0)  # 切换到第
    wait_OP_transfer_ok(wait)

    switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
    # return detail
    if "成功" in success_or_fail:
        # 切换到OP，并关闭
        switch_tab_by_handle(browser, 2, 0)  # 切换到第
        # wait_OP_transfer_ok(wait) #太慢了
        time_sleep(30,"等待OP交易完成")
        success = "成功"
        detail = f"【OP】通过OP官方桥，转到OP：{input_balance}ETH，{success_or_fail}"
        # switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return success, detail
    else:
        fail = "fail"
        detail = f"【失败OP】通过OP官方桥，转到OP：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return fail, detail

#主网——》zk官方桥——》ZK
def mainnet_ZK_official_ZK(browser, wait,L1_ETH_value):
    print("通过ZK官方桥，转到ZK。第一步是：小狐狸切换到主网")
    fox_change_network(browser, wait, "Ethereum")
    new_tab(browser, ZK_url)
    time_sleep(10,"准备打开zk")
    switch_tab_by_handle(browser, 2, 0)  # 切换到第

    #判断是否连接小狐狸
    zk_connect_wallet(browser, wait)
    time_sleep(5, "等待连接小狐狸")
    #返回转账值
    input_balance = zk_prepare_transfer(browser, wait, L1_ETH_value, L1_ETH_save_min)
    time_sleep(15, "ZK准备订单完毕")

    # 小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：
    success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)  # 小狐狸确认交易

    if "成功" in success_or_fail:
        # 回到 zk，关闭它
        switch_tab_by_handle(browser, 2, 0)  # 切换
        # wait_zk_complete(wait)  # 等待关闭，太慢了
        time.sleep(30)
        success = "成功"
        detail = f"【ZK】通过ZK官方桥，转到ZK：{input_balance}ETH，{success_or_fail}"
        # switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return success, detail
    else:
        fail = "fail"
        detail = f"【失败ZK】通过ZK官方桥，转到ZK：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return fail, detail


# taks_list=[mainnet_lifi_ARB, mainnet_lifi_OP, mainnet_ARB_official_ARB, mainnet_OP_official_OP, mainnet_ZK_official_ZK]

#===不用 lifi
taks_list=[ mainnet_ARB_official_ARB, mainnet_OP_official_OP, mainnet_ZK_official_ZK]

#读取excel表中的资金分布情况


# 得从第二个号开始才有钱
while True:
    for i in range(96, 201):  #110
        if "成功" != Do_Excel('eth1000_操作后.xlsx').read(i, 2): #这里需要换成行与列
            try:
                print(f"第{i}个状态：", Do_Excel('eth1000_操作后.xlsx').read(i, 2))
                time.sleep(1)
                ##======== 准备浏览器
                wait, browser = my_chrome()

                ##======== 预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                ip_switcher(browser, wait, url_google)  #这里会新建一个标签页
                #从上面新建的标签页里，打开下面的链接
                delete_cookie(browser)

                ##======= 准备工作：登陆小狐狸
                login_metamask(browser, wait, metamask_pw, metamask_home)
                switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
                print(f"=======开始换号 {i}==============")
                fox_change_account(browser, wait, i)
                time.sleep(2)

                #====== 获取主网的初始值，将来传入到 L1转L2的函数
                L1_ETH_value = float(get_fox_Ethereum_ETH_balance(browser))
                print("主网初始：", L1_ETH_value)
                initial_amount = f"主网初始：{L1_ETH_value}"

                # =====记录初始值到excel
                Do_Excel('eth1000_操作后.xlsx').write(i, 3, initial_amount)

                ##====== 随机抽任务
                random.shuffle(taks_list)
                # index = random.randint(0, 4) #把lifi加入了列表
                index = random.randint(0, 2)
                situation, save_record = taks_list[index](browser, wait, L1_ETH_value)

                # situation, save_record = mainnet_lifi_ARB(browser, wait, L1_ETH_value)                # 测试通过
                # situation, save_record = mainnet_ARB_official_ARB(browser, wait, L1_ETH_value)        # 测试通过
                # situation, save_record =mainnet_lifi_OP(browser, wait, L1_ETH_value)                  # 测试通过
                # situation, save_record =mainnet_OP_official_OP(browser, wait, L1_ETH_value)          # 测试通过
                # situation, save_record = mainnet_ZK_official_ZK(browser, wait, L1_ETH_value)          # 测试通过

                # =====记录转账值到excel
                Do_Excel('back_up_excel/eth1000_操作后.xlsx').write(i, 2, situation)
                Do_Excel('back_up_excel/eth1000_操作后.xlsx').write(i, 4, save_record)

                # 这里要设置随机等待时间
                a = random.randint(30, 300)
                time_sleep(a, "++++++++++随机等待时间")
                browser.quit()
            except:
                print(f"第{i}个号出错了，继续")
                browser.quit()
                time.sleep(2)
                continue

#获取网络、代币、余额
# get_fox_network_token_balance(browser, wait)

#切换账户
