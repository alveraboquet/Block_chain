#L1转到L2之后，查询L2各个链上的余额。从 orb 去获取，加快速度，不用切换 IP
from functions import *
##=========== 调用浏览器
wait, browser = my_chrome()

##=========== 登陆小狐狸，
login_metamask(browser, wait, metamask_pw, metamask_home)

# ========== 打开 orb
new_tab(browser, orbiter_url)
time_sleep(8, "正在打开 orb，在此之前请确保小狐狸切换到了对应网络")

for i in range(96, 201):
    #=========== 切换到小狐狸
    switch_tab_by_handle(browser, 0, 0)
    #== 1）小狐狸换号
    fox_change_account(browser, wait, i)
    time_sleep(3, f"=======换号成功  {i}==============")

    # == 2）小狐狸换网络
    fox_change_network(browser, wait, "Ethereum")
    time.sleep(3)

    # =========== 切换到 orb
    switch_tab_by_handle(browser, 1, 1)

    # 1） 判断要不要连接钱包
    if orb_whether_connect_wallet(wait):
        print("orb 要连接钱包")
        orb_connect_wallet(browser, wait)
        # switch_tab_by_handle(browser, 0, 1)  # 切换到第小狐狸，刷新
        # fox_confirm_connect_account(browser, wait)  # 小狐狸连接所有账户
        # time.sleep(3)
        # switch_tab_by_handle(browser, 1, 0)  # 切换到：lifi

    # 获取 L2 实时金额，比如zk的余额从 orb 上找
    # Optimism、Arbitrum、zkSync、 Ethereum ，返回的是浮点数
    Ethereum_ETH = get_L2_balance_from_orb(browser, wait, "Ethereum")
    print(f"这个号在orb上的实时 Ethereum 金额是：{Ethereum_ETH}")
    time.sleep(3)

    zksync_ETH = get_L2_balance_from_orb(browser, wait, "zkSync")
    print(f"这个号在orb上的实时 zkSync 金额是：{zksync_ETH}")
    time.sleep(3)

    Optimism_ETH = get_L2_balance_from_orb(browser, wait, "Optimism")
    print(f"这个号在orb上的实时 Optimism 金额是：{Optimism_ETH}")
    time.sleep(3)

    Arbitrum_ETH = get_L2_balance_from_orb(browser, wait, "Arbitrum")
    print(f"这个号在orb上的实时 Arbitrum 金额是：{Arbitrum_ETH}")
    time.sleep(3)

    #====转为字符串，保存到 excel
    all_info = f"'Arbitrum':{Arbitrum_ETH}, 'Optimism':{Optimism_ETH}, 'zksync':{zksync_ETH}"
    dict_type_string = "{" + all_info + "}"

    Do_Excel('eth1000_操作后.xlsx').write(i, 5, f"Ethereum: {Ethereum_ETH}")
    Do_Excel('eth1000_操作后.xlsx').write(i, 6, dict_type_string)

    ##=========== 这里要设置随机等待时间
    a = random.randint(5, 10)
    time_sleep(a, "++++++++++随机等待时间")
    browser.quit()

