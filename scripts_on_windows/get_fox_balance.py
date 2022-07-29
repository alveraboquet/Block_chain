#L1转到L2之后，查询L2各个链上的余额
from functions import *

#开始遍历所有Account
for i in range(2,52):
    ##调用浏览器
    wait, browser = my_chrome()
    ##=========== 预备步骤：切换IP。先打开
    open_clash_dashboard(browser, wait, url_dashboard)
    # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
    ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页

    ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
    delete_cookie(browser)

    ##=========== 登陆小狐狸，
    login_metamask(browser, wait, metamask_pw, metamask_home)
    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
    time_sleep(3)
    # 小狐狸换号
    fox_change_account(browser, wait, i)
    time_sleep(3, f"=======换号成功  {i}==============")

    ##===========先切换到小狐狸
    switch_tab_by_handle(browser, 1, 0)
    # 要查询zk余额前，账户要先切换到主网
    fox_change_network(browser, wait, "Ethereum")
    time_sleep(3)

    #===========切换到zk，去查询余额
    new_tab(browser, ZK_balance_url)
    switch_tab_by_handle(browser, 2, 0)
    wait_zk_tab(browser,wait)

    # =====连接小狐狸
    zk_connect_wallet(browser, wait)

    # ===获取余额，返回的是字符串
    zksync_ETH = get_zk_eth_balance(wait) #返回的类似"0.054992745993"
    print("zk上的余额情况",zksync_ETH)

    #======切换到小狐狸，查询其它网络的余额
    switch_tab_by_handle(browser, 1, 0)
    all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)
    Ethereum_ETH = return_fox_net_token_balance("Ethereum", "ETH", all_networks, all_token_and_balance)
    Optimism_ETH = return_fox_net_token_balance("Optimism", "ETH", all_networks, all_token_and_balance)
    Arbitrum_ETH = return_fox_net_token_balance("Arbitrum", "ETH", all_networks, all_token_and_balance)

    print("小狐狸上的余额情况",all_networks, all_token_and_balance)

    #====转为字符串，保存到 excel
    all_info = f"'Arbitrum':{float(Arbitrum_ETH)}, 'Optimism':{float(Optimism_ETH)}, 'zksync':{float(zksync_ETH)}"
    dict_type_string = "{" + all_info + "}"

    Do_Excel('eth1000_操作后.xlsx').write(i+49, 5, f"Ethereum: {Ethereum_ETH}")
    Do_Excel('eth1000_操作后.xlsx').write(i+49, 6, dict_type_string)

    ##=========== 这里要设置随机等待时间
    a = random.randint(20, 50)
    time_sleep(a, "++++++++++随机等待时间")
    browser.quit()

