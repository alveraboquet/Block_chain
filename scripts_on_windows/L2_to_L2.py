# 功能：把L2的钱，分散到其他到L2
# 思路，
# 1）读取excel里，3个生态的余额，找到最大的那一个，返回生态名字 "zksync", "Arbitrum", "Optimism"
# 2）注意记录到 excel 里的不同表单中
# 把最多钱的生态设置为from，

from functions import *

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
    if from_source == "zkSync":  # 如果源是 zksync，则用主网
        print(f"源是{from_source}，请确保小狐狸切换到了相关网络")
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        fox_change_network(browser, wait, "Ethereum")
        time_sleep(5, "小狐狸已经切换对应了网络")

        #========== 打开 orb
        new_tab(browser, orbiter_url)
        time_sleep(5, "正在打开 orb，在此之前请确保小狐狸切换到了对应网络")
        switch_tab_by_handle(browser, 2, 0)  # 切换到 orb

        #============ 判断要不要连接钱包
        if orb_whether_connect_wallet(wait):
            print("orb 要连接钱包")
            orb_connect_wallet(browser, wait)
            # switch_tab_by_handle(browser, 0, 1)  # 切换到第小狐狸，刷新
            # fox_confirm_connect_account(browser, wait)  # 小狐狸连接所有账户
            # time.sleep(3)
            # switch_tab_by_handle(browser, 1, 0)  # 切换到：lifi

        # 获取 L2 实时金额，比如zk的余额从 orb 上找
        # Optimism、Arbitrum、zkSync，返回的是浮点数
        L2_ETH_value = get_L2_balance_from_orb(browser, wait, "zkSync")
        print(f"这个号在orb上的实时 zkSync 金额是：{L2_ETH_value}")
        # # ==== 保证源里面有钱，否则记录出错，关闭浏览器
        # if L2_ETH_value <= 0.01:
        #     print(f"第{i}个号出错了，没有钱")
        #     balance_string = Do_Excel('eth1000_OP_操作后.xlsx', "Sheet_from_ZK").write(i, 10,
        #                                                                          f"第{i}个号出错了，只有{L2_ETH_value}ETH")
        #     browser.quit()


        #============ lifi准备换币。返回本次的交易值
        transfer_detail = L2_orb_L2_prepare_transfer_coin(browser, wait, L2_ETH_value, from_source,
                                                          to_destination)
        # print(transfer_detail)
        #============ 切换到第小狐狸，刷新，签名。or 必须两次签名才能成功
        switch_tab_by_handle(browser, 1, 1)
        for i in range(1, 4):  # orb 至少两次签名以上
            print(f"第{i}次签名")
            fox_info = fox_confirm_sign(browser, wait)
            time.sleep(8)
        switch_tab_by_handle(browser, 2, 0)
        all_info = f"【成功】通过orb，资金从{from_source}转到{to_destination} " + transfer_detail + fox_info
        return all_info

    elif from_source == "Optimism":  # 如果源是 Optimism，则用 Optimism
        print(f"源是{from_source}，请确保小狐狸切换到了相关网络")
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        fox_change_network(browser, wait, "Optimism")
        time_sleep(5, "小狐狸已经切换对应了网络")
        # 打开 orb
        new_tab(browser, orbiter_url)
        time_sleep(5, "正在打开 orb，在此之前请确保小狐狸切换到了对应网络")
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
        fox_success_or_fail = fox_confirm_L2_swap(browser, wait)  #这个网络不用签名3次
        switch_tab_by_handle(browser, 2, 0)
        all_info = f"【成功】通过orb，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_success_or_fail}"
        return all_info

    elif from_source == "Arbitrum":  # 如果源是 Arbitrum，则用Arbitrum
        print(f"源是{from_source}，请确保小狐狸切换到了相关网络")
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸
        fox_change_network(browser, wait, "Arbitrum One")
        time_sleep(5, "小狐狸已经切换对应了网络")


        # 打开 orb
        new_tab(browser, orbiter_url)
        time_sleep(5, "正在打开 orb，在此之前请确保小狐狸切换到了对应网络")
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
        L2_ETH_value = get_L2_balance_from_orb(browser, wait, "Arbitrum")
        print(f"这个号在orb上的实时 Arbitrum 金额是：{L2_ETH_value}")

        ########## lifi准备换币。返回本次的交易值
        transfer_detail = L2_orb_L2_prepare_transfer_coin(browser, wait, L2_ETH_value, from_source,
                                                          to_destination)
        # print(transfer_detail)
        # 切换到第小狐狸，刷新，签名。or 必须两次签名才能成功
        switch_tab_by_handle(browser, 1, 1)
        fox_success_or_fail = fox_confirm_L2_swap(browser, wait)  #确认一次即可
        switch_tab_by_handle(browser, 2, 0)
        all_info = f"【成功】通过orb，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_success_or_fail}"
        return all_info

    else:
        print("L2_orb_L2(), 源输入错误")


while True:
    for i in range(96, 100):
        time_sleep(3, f"在找号{i}")
        #============ 首先确定要转的源是哪个，比如 from 源是 ZK
        if Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").read(i, 9) == "1": #注意是字符串的 “1”
            # 且 Zk 之前没有转过，才进行操作
            if Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").read(i, 10) != "成功":
                print(f"第{i}个号需要从 ZK 转到其它 L2")
                ##=============准备浏览器
                wait, browser = my_chrome()

                ##=============预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页

                ##=============删除缓存
                # 从上面新建的标签页里，打开下面的链接
                delete_cookie(browser)

                ##========= 准备工作：登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home)
                time.sleep(2)
                switch_tab_by_handle(browser, 1, 1)  # 切换到第小狐狸

                ##====== 小狐狸换号
                print(f"=======开始换号 {i}==============")
                fox_change_account(browser, wait, i)
                time.sleep(2)

                ##===== 找到 L2 源的金额，法一：从excel上找 ；法二：找实时金额，比如zk的余额从 orb 上找
                # balance_string = Do_Excel('eth1000_OP_操作后.xlsx', "Sheet_from_ZK").read(i, 6)
                # balance_dict = dict_type_string_to_dict(balance_string)
                # L2_ETH_value = balance_dict['zksync'] # 得到该生态上的值，是 float 类型


                #只有 from 源上真正有钱时，才开始转
                a = random.randint(1, 2)
                if a == 1:
                    info = L2_orb_L2(browser, wait, "zkSync", "Optimism")  # 测试通过
                    print(info)  # 记录该info
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 10, "成功")
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 11, "Optimism")
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 12, info)
                elif a == 2:
                    info = L2_orb_L2(browser, wait, "zkSync", "Arbitrum")  # 测试通过
                    print(info)  # 记录该info
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 10, "成功")
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 11, "Arbitrum")
                    Do_Excel('eth1000_操作后.xlsx', "Sheet_from_ZK").write(i, 12, info)

                # 操作结束，关闭浏览器
                a = random.randint(20, 300)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(20, 500)
                time_sleep(a, f"++++++++++随机等待时间{a}")

