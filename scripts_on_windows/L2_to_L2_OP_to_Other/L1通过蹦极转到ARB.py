# 功能：把L2的钱，分散到其他到L2
# ARB 的钱转到其他生态
#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

from L2.functions import *

# L2——》lifi——》L2，可以实现：
# 1）"Arbitrum One"——>"Optimism"
# 2）"Optimism"——>"Arbitrum One"
# from, to 是想要转到的链，比如 "Optimistic Ethereum"、"Arbitrum One"、"Ethereum"
def L2_lifi_L2(browser, wait, L2_ETH_value, From, to):  # "Optimism"、"Arbitrum One"、
    print("L2与L2之间通过 lifi 分布资金。要注意小狐狸切换到 From_source")
    if From == "Optimistic Ethereum":  # 如果源是 zksync，则用主网
        print(f"源是{From}，请确保小狐狸切换到了相关网络")
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        fox_change_network(browser, wait, "Optimism")
        time_sleep(5, "即将去 lifi ")
        # 打开 lifi
        new_tab(browser, lifi_url)  # 到 lifi去，这是第2个标签
        time_sleep(5, "正在打开 lifi，在此之前请确保小狐狸切换到了对应网络")
        switch_tab_by_handle(browser, 2, 0)  # 切换到第3个标签页：lifi
        # 预转账，这样才能判断是否要切换网络。返回本次预存金额。

        # from to 是想要转到的链，比如 "Optimistic Ethereum"、"Arbitrum One"、"Ethereum"
        input_value = L2_lifi_L2_prepare_transfer_coin(browser, wait, L2_ETH_value, From, to)

        # 判断 lifi 要不要连接小狐狸，是的话先连接小狐狸
        if lifi_whether_connect_wallet(browser, wait) == "Connect Your Wallet":
            lifi_connect_wallet(browser, wait)  #有可能点一下就行
            # switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
            # fox_confirm_connect_account(browser, wait)  # 小狐狸连接所有账户
            # time_sleep(3)
            # switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi

        # 判断 lifi是否要切换网络，是的话先切换网络
        # if lifi_switch_net_or_swap(browser, wait) != "Swap":  # 先切换网络，然后Swap交易
        #     lifi_switch_net(browser, wait)
        #     switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，因为上一步已经点击了“切换网络”
        #     fox_confirm_connect_network(browser, wait)  # 小狐狸确认切换网络
        #     time_sleep(5)
        #     switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi
        # fox_confirm_L2_swap(browser, wait)

        lifi_swap(browser, wait)
        switch_tab_by_handle(browser, 1, 1)  #切到小狐狸
        time.sleep(2)
        info = fox_confirm_L2_swap(browser, wait)
        switch_tab_by_handle(browser, 2, 0)  # 再切换lifi
        return info

    elif From == 'Arbitrum One':
        print(f"源是{From}，请确保小狐狸切换到了相关网络")
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        fox_change_network(browser, wait, "Arbitrum One")
        time_sleep(5, "即将去 lifi ")
        # 打开 lifi
        new_tab(browser, lifi_url)  # 到 lifi去，这是第2个标签
        time_sleep(5, "正在打开 lifi，在此之前请确保小狐狸切换到了对应网络")
        switch_tab_by_handle(browser, 2, 0)  # 切换到第3个标签页：lifi
        # 预转账，这样才能判断是否要切换网络。返回本次预存金额。

        # from to 是想要转到的链，比如 "Optimistic Ethereum"、"Arbitrum One"、"Ethereum"
        input_value = L2_lifi_L2_prepare_transfer_coin(browser, wait, L2_ETH_value, From, to)

        # 判断 lifi 要不要连接小狐狸，是的话先连接小狐狸
        if lifi_whether_connect_wallet(browser, wait) == "Connect Your Wallet":
            lifi_connect_wallet(browser, wait)  #有可能点一下就行
            # switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸，刷新
            # fox_confirm_connect_account(browser, wait)  # 小狐狸连接所有账户
            # time_sleep(3)
            # switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi

        # 判断 lifi是否要切换网络，是的话先切换网络
        # if lifi_switch_net_or_swap(browser, wait) != "Swap":  # 先切换网络，然后Swap交易
        #     lifi_switch_net(browser, wait)
        #     switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸，因为上一步已经点击了“切换网络”
        #     fox_confirm_connect_network(browser, wait)  # 小狐狸确认切换网络
        #     time_sleep(5)
        #     switch_tab_by_handle(browser, 2, 0)  # 切换到：lifi
        lifi_swap(browser, wait)
        switch_tab_by_handle(browser, 1, 1)
        time.sleep(2)
        info = fox_confirm_L2_swap(browser, wait)
        switch_tab_by_handle(browser, 2, 0)#再切换lifi
        return info
    else:
        print("L2_lifi_L2(), 源错误")


# orb L2与L2互转
# 可选 "zkSync" "Arbitrum" "Optimism"
# L2——》orbiter——》L2，可以实现：
# 1）"zkSync"——>"Optimism"    "zkSync"——>"Arbitrum"
# 3）"Arbitrum"——>"Optimism"   "Arbitrum"——>"zkSync"
# 5）"Optimism"——>"Arbitrum"    "Optimism"——>"zkSync"
def L2_orb_L2(browser, wait, from_source, to_destination):
    print("通过 orb，L2 转到 L2。重要第一步是：小狐狸切换网络")
    if from_source == "Optimism":  # 如果源是 Optimism，则用 Optimism
        # print(f"源是{from_source}，请确保小狐狸切换到了相关网络")
        # switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        # fox_change_network(browser, wait, "Optimism")
        # time_sleep(5, "小狐狸已经切换对应了网络")
        # 打开 orb
        new_tab(browser, orbiter_url)
        time_sleep(10, "正在打开 orb，在此之前请确保小狐狸切换到了对应网络")
        switch_tab_by_handle(browser, 2, 0)  # 切换到 orb

        ########### 判断要不要连接钱包
        if orb_whether_connect_wallet(wait):
            print("orb 要连接钱包")
            orb_connect_wallet(browser, wait)
            # switch_tab_by_handle(browser, 0, 1)  # 切换到第小狐狸，刷新
            # fox_confirm_connect_account(browser, wait)  # 小狐狸连接所有账户
            # time.sleep(3)
            # switch_tab_by_handle(browser, 1, 0)  # 切换到：lifi

        # 获取 L2 实时金额，比如zk的余额从 orb 上找
        # Optimism、Arbitrum、zkSync，返回的是浮点数
        L2_ETH_value = get_L2_balance_from_orb(browser, wait, "Optimism")
        print(f"这个号在 orb 上的实时 Optimism 金额是：{L2_ETH_value}")

        ########## lifi准备换币。返回本次的交易值
        transfer_detail = L2_orb_L2_prepare_transfer_coin(browser, wait, L2_ETH_value, from_source,
                                                          to_destination)
        # print(transfer_detail)
        # 切换到第小狐狸，刷新，签名。or 必须两次签名才能成功
        switch_tab_by_handle(browser, 1, 1)
        fox_info = fox_confirm_L2_swap(browser, wait)  #这个网络不用签名3次
        switch_tab_by_handle(browser, 2, 0)
        orb_fail = ""
        try:  # 如果orb 上这个按钮还在，说明转账失败
            confirm_and_send = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='CONFIRM AND SEND']")))
            if confirm_and_send:
                orb_fail = f"小狐狸点击确认后，orb失败，还是没有转过去"
                return orb_fail
        except:
            print("小狐狸点击确认后，orb转过去了")

        if "成功" in fox_info:
            if "orb失败" not in orb_fail:
                all_info = f"【成功】通过orb，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_info}"
                return all_info
            print("小狐狸点击确认后，orb失败，还是没有转过去")
            return "小狐狸点击确认后，orb失败，还是没有转过去"
        else:
            print(fox_info)
            return fox_info  # 失败了，orb
    else:
        print("L2_orb_L2(), 源输入错误")


#从bungee上转到L2
#1)"Optimism"——>"Arbitrum"

def L2_bungee_L2(browser, wait, from_source, to_destination):
    # ========== 打开 bungee
    new_tab(browser, bungee_url)  # 到 lifi去，这是第2个标签
    time_sleep(5, "正在打开 bungee ，在此之前请确保小狐狸切换到了对应网络")
    switch_tab_by_handle(browser, 2, 0)  # 切换到 bungee
    # ======= 可能有个提示，点击确定
    bungee_Agree_and_continue(browser, wait)
    # ======= 判断要不要连接钱包
    bungee_whether_connect_wallet(browser, wait)
    # ======== 选择源账户，目标账户
    transfer_detail = bungee_prepare_transfer_coin(browser, wait, from_source, to_destination)

    #小狐狸确认签名
    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
    fox_info = fox_confirm_L2_swap(browser, wait)  # 这个网络不用签名3次

    switch_tab_by_handle(browser, 2, 0)
    bungee_fail = ""
    try:  # 如果 bungee 上这个按钮还在，说明转账失败
        bridge_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/main/div/div[3]/div/div[3]/div[2]/button')))
        if bridge_button:
            bungee_fail = f"小狐狸点击确认后，bungee 失败，还是没有转过去"
            return bungee_fail
    except:
        print("小狐狸点击确认后，bungee 转过去了")

    if "成功" in fox_info:
        if "orb失败" not in bungee_fail:
            all_info = f"【成功】通过 bungee，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_info}"
            return all_info
        print("小狐狸点击确认后，bungee 失败，还是没有转过去")
        return "小狐狸点击确认后，bungee 失败，还是没有转过去"
    else:
        print(fox_info)
        return fox_info  # 失败了，orb

#=== ARB 可以转到哪
def OP_orb_zk():
    info = L2_orb_L2(browser, wait, "Optimism", "zkSync")  # 测试通过
    print(info)  # 记录该info
    if "失败" in info:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "G", "×")
    else:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "J", "1")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "G", "·成功")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)

def OP_orb_ARB():
    info = L2_orb_L2(browser, wait, "Optimism", "Arbitrum")  # 测试通过
    print(info)  # 记录该info
    if "失败" in info:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "G", "×")

    else: #如果成功的话就做标记
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "H", "1")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "G", "·成功")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)

def OP_bungee_ARB():
    info = L2_bungee_L2(browser, wait, "Ethereum", "Arbitrum")
    if "失败" in info:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "K", "×")

    else: #如果成功的话就做标记
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "L", "1")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "K", "·成功")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)

#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

for i in range(2, 201):
    print(f"=======在找号{i}")
    #============ 首先确定要转的源是哪个，比如 from 源是 ZK
    # if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i, "I")) == "1" or str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i, "I")) == "·1":  # OP 转钱
    #     if Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i, "K") != "成功":
    try:
        print(f"==========第{i}个号需要从 OP 转到其它 L2=========")
        ##=============准备浏览器
        which_chrome = 5
        wait, browser = my_chrome(which_chrome)

        ##=============预备步骤：切换IP。先打开
        open_clash_dashboard(browser, wait, url_dashboard)
        switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
        ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页

        ##=============删除缓存
        # 从上面新建的标签页里，打开下面的链接
        delete_cookie(browser)

        ##========= 准备工作：登陆小狐狸，
        # login_metamask(browser, wait, metamask_pw, metamask_home, "Optimism")
        login_metamask(browser, wait, metamask_pw, metamask_home, "Ethereum")
        time.sleep(2)
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸

        ##====== 小狐狸换号、网络
        time_sleep(2, f"========开始换号{i}==========")
        fox_change_account(browser, wait, i)
        # time_sleep(2, "开始换网络，第一次换过之后，就不要换网络了")
        # fox_change_network(browser, wait, "Arbitrum One")

        #==== 开始任务
        a = random.randint(3, 3)
        time_sleep(2, f"准备执行任务{a}")
        if a == 1:
            OP_orb_ARB()
            # ARB_lifi_OP()
        elif a == 2:
            OP_orb_zk()

        elif a == 3:
            OP_bungee_ARB()

        # ==== 操作结束，关闭浏览器
        a = random.randint(60, 80)
        time_sleep(a, f"++++++++++随机等待时间{a}")
        browser.quit()
        a = random.randint(60, 80)
        time_sleep(a, f"++++++++++随机等待时间{a}")
    except:
        print(f"{i}出错了")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "K", "×")
        a = random.randint(60, 80)
        time_sleep(a, f"++++++++++随机等待时间{a}")
        try:
            browser.quit()
            print("出错了")
        except:
            print("尝试关闭浏览器，但浏览器可能之前已关闭")
        a = random.randint(10, 20)
        time_sleep(a, f"++++++++++随机等待时间{a}")
