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
#=========== 交易所
matcha_url = "https://matcha.xyz/login"

#============ZK上的项目
zk_zigzag_url = "https://info.zigzag.exchange/"
zk_tevaera_url = "https://tevaera.com/"
######################


# L1_ETH_value = 0.05     #L1上的ETH有多少钱
L1_ETH_save_min = 0.01  #想要在L1保留的最小值

####切换IP相关
url_dashboard = "http://127.0.0.1:9090/ui/#/proxies"
url_google = "https://www.google.com"
#######小狐狸相关
metamask_pw = "12345678" #小狐狸的密码
metamask_home = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"

#=========构建浏览器
# 获取驱动的路径
driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
TIME_OUT = 40  # 设置显示等待的超时时间，尽量设置的长一点，考虑到网络可能缓慢
option = ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
option.add_experimental_option('excludeSwitches', ['enable-outomation'])  # 防止被网站识别
option.add_experimental_option('useAutomationExtension', False)
#添加谷歌用户路径
# user_data_path = f'--user-data-dir=D:\\auto_video_projects\\xigua_video\\adidas\\{user_num}'
user_data_path = f'--user-data-dir=D:\\auto_video_projects\\xigua_video\\adidas\\1'
print("谷歌用户路径是：", user_data_path)
option.add_argument(user_data_path)  # 用指定的用户进行测试


#做 ZK 上的 zigzag，快进快出
def ZK_zigzag_in_out(browser, wait, buy_or_sell):
    print("做 ZK 上的 zigzag。第一步是：小狐狸切换到主网")
    fox_change_network(browser, wait, "Ethereum")
    new_tab(browser, zk_zigzag_url)
    time.sleep(10)
    switch_tab_by_handle(browser, 2, 0)  # 切换到被撸网站

    try: #判断是否连接小狐狸
        zk_zigzag_whether_connect_wallet(browser, wait)
        zk_zigzag_connect_metamask(browser, wait)  # 在跳出的页面里，选择小狐狸
        switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
        fox_confirm_sign(browser, wait)
        switch_tab_by_handle(browser, 2, 0)  # 【签名】成功后，再切换到zigzag
        time.sleep(5)
        # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
        # fox_confirm_connect_account(browser, wait) #小狐狸确认连接所有账号
    except:
        print("zigzag，小狐狸确认连接所有账号失败")

    #获取Zigzag上有多少ETH，返回余额（字符串）
    zigzag_balance = get_ZK_zigzag_balance(browser, wait)
    print("zigzag上的ETH/USDC余额是：", zigzag_balance)

    # 选择 Sell或 Buy，卖 ETH，换其它币
    #返回转账值。如果输入交易量成功，则小狐狸去确认
    input_balance = zk_zigzag_prepare_swap(browser, wait, zigzag_balance, buy_or_sell)
    if input_balance:  # 小狐狸确认交易
        print("小狐狸去【签名】")
        switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：
        fox_confirm_sign(browser, wait) #可能会出现签名
        # success_or_fail = fox_confirm_swap(browser, wait)  # 小狐狸确认交易
        print(f"本次zigzag 交易额是{input_balance}")
        switch_tab_by_handle(browser, 2, 0)  # 切换到zigzag
    print(input_balance)
    return input_balance

#做 ZK 上的 tevaera
def ZK_tevaera(browser, wait,L1_ETH_value):
    print("通过ZK官方桥，转到ZK。第一步是：小狐狸切换到主网")
    fox_change_network(browser, wait, "Ethereum")
    new_tab(browser, ZK_url)
    time.sleep(10)
    switch_tab_by_handle(browser, 2, 0)  # 切换到第

    #判断是否连接小狐狸
    zk_connect_wallet(browser, wait)
    time.sleep(5)
    #返回转账值
    input_balance = zk_prepare_transfer(browser, wait, L1_ETH_value, L1_ETH_save_min)
    time.sleep(15)

    # 小狐狸确认交易
    switch_tab_by_handle(browser, 1, 1)  # 切换到第1个标签页：
    success_or_fail = fox_confirm_swap(browser, wait)  # 小狐狸确认交易

    if "成功" in success_or_fail:
        # 回到 zk，关闭它
        switch_tab_by_handle(browser, 2, 0)  # 切换
        wait_zk_complete(wait)  # 等待关闭
        time.sleep(3)
        detail = f"【成功】通过ZK官方桥，转到ZK：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return detail
    else:
        detail = f"【失败】通过ZK官方桥，转到ZK：{input_balance}ETH，{success_or_fail}"
        switch_tab_by_handle(browser, 1, 0)  # 再切回小狐狸
        return detail

# 得从第二个号开始才有钱
for i in range(2,3):
    ##准备浏览器
    browser = webdriver.Chrome(driver_path, options=option)
    # browser.minimize_window()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                            )  # 反爬
    wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类

    ######预备步骤：切换IP。先打开
    open_clash_dashboard(browser, wait, url_dashboard)
    switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
    ip_switcher(browser, wait, url_google)  #这里会新建一个标签页

    #######清理缓存（从上面新建的标签页里，打开下面的链接）
    delete_cookie(browser)

    ####### 登陆小狐狸，
    login_metamask(browser, wait, metamask_pw, metamask_home)
    switch_tab_by_handle(browser, 1, 1)  # 切换到第lifi
    #小狐狸换号
    print(f"=======开始换号 {i}==============")
    fox_change_account(browser, wait, 11)
    # time.sleep(2)

    ####### 使用指定工作表
    my_excel = openpyxl.load_workbook('eth1000_OP_操作后.xlsx')  # 有路径应带上路径
    sheet = my_excel.active  # 当前激活的工作表

    ######读取哪个生态上的初始资金比较多。写一个生态资金对比函数

    ######随机抽任务
    # taks_list = [ZK_zigzag_in_out, ZK_tevaera]
    # random.shuffle(taks_list)
    # index = random.randint(0, 5)
    save_record = ZK_zigzag_in_out(browser, wait, "Sell")
    # save_record = taks_list[index](browser, wait, L1_ETH_value)
    # save_record = mainnet_lifi_ARB(browser, wait, L1_ETH_value) #保存交易值
    # save_record =mainnet_lifi_OP(browser, wait, L1_ETH_value)
    # save_record = mainnet_ARB_official_ARB(browser, wait, L1_ETH_value)
    # save_record =mainnet_OP_official_OP(browser, wait, L1_ETH_value)
    # save_record = mainnet_ZK_official_ZK(browser, wait, L1_ETH_value)

    sheet.cell(row=i, column=14, value= save_record)
    my_excel.save('eth1000_OP_操作后.xlsx')

    # 这里要设置随机等待时间
    a = random.randint(2, 5)
    print("++++++++++随机等待时间",a)
    time.sleep(a)
    browser.quit()


#到抹茶上换币
# def matcha_change_coin(browser, wait, destination_coin):
#     if OP_USDC_balance_before < 1: #如果USDC < 1$，则去抹茶换USDC，（前提是先看看OP链上有没有足够的ETH）
#         print("OP上的 USDC 金额小于 1，准备去抹茶换 USDC")
#
#         new_tab(browser, matcha_url)
#         switch_tab_by_handle(browser, 1, 0)  # 切换到抹茶
#         # 如果没有连接小狐狸钱包，则先去连接钱包
#         if matcha_fox_icon_exit(browser, wait) != 1:
#             print("Match没有连接小狐狸，先去连接")
#             matcha_connect_wallet(browser, wait)  # 先连接钱包
#             switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，去连接账号
#             fox_confirm_connect_account(browser, wait)  #
#             time.sleep(4)
#             switch_tab_by_handle(browser, 1, 1)  # 切换到第3个标签页：matcha
#         # 判断抹茶要不要换网络
#         if matcha_whether_change_net(browser, wait) != "Optimism":
#             matcha_change_net(browser, wait)
#         # 正式换钱
#         # try:
#         matcha_prepare_change_coin(browser, wait, 2, 20)  #准备换钱
#         time.sleep(5)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，切换网络
#         fox_confirm_connect_network(browser, wait)
#         time.sleep(3)
#         switch_tab_by_handle(browser, 1, 0)  # 切换到：matcha
#         matcha_formal_change_coin(browser, wait)  # 下单
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，切换网络
#         fox_confirm_swap(browser, wait)  # 小狐狸确认交易
#         time.sleep(5)
#
#         # 转账后，20秒后，查询OP上的USDC是否到账
#         time.sleep(20)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#         all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
#         OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
#
#         while OP_USDC_balance_after == OP_USDC_balance_before:
#             print("OP上的 USDC 还没到账，20秒轮询一次")
#             time.sleep(20)  # 20秒去轮询一次
#             switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#             all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
#             OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
#
#         print(f"OP上的 USDC 到账了，金额是 {OP_USDC_balance_after}")
#         switch_tab_by_handle(browser, 1, 0)  # 切换到：matcha
#         time.sleep(5)
#         browser.close()# 关闭当前标签页，因为句柄在当前页，所以可以直接关闭


##==================================下面是 OP 的任务
# #做 OP上的 pika
# def OP_pika(all_networks, all_token_and_balance):
#     # 小狐狸网络切换成OP
#     switch_tab_by_handle(browser, 0, 0)  # 切换到：pika
#     fox_change_network(browser, wait, "Optimism")
#     time.sleep(5)
#     print("开始OP_pika任务")
#     #一、先要有看OP上的 USDC、ETH 有多少
#     #如果USDC不够，去抹茶换USDC，前提是L2上要有ETH（先查L2上的ETH够不够，不够的话去lifi把的L1转到L2
#     if OP_USDC_balance_before < 1: #如果USDC < 1$，则去抹茶换USDC，（前提是先看看OP链上有没有足够的ETH）
#         print("OP上的 USDC 金额小于 1，准备去抹茶换 USDC")
#
#         new_tab(browser, matcha_url)
#         switch_tab_by_handle(browser, 1, 0)  # 切换到抹茶
#         # 如果没有连接小狐狸钱包，则先去连接钱包
#         if matcha_fox_icon_exit(browser, wait) != 1:
#             print("Match没有连接小狐狸，先去连接")
#             matcha_connect_wallet(browser, wait)  # 先连接钱包
#             switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，去连接账号
#             fox_confirm_connect_account(browser, wait)  #
#             time.sleep(4)
#             switch_tab_by_handle(browser, 1, 1)  # 切换到第3个标签页：matcha
#         # 判断抹茶要不要换网络
#         if matcha_whether_change_net(browser, wait) != "Optimism":
#             matcha_change_net(browser, wait)
#         # 正式换钱
#         # try:
#         matcha_prepare_change_coin(browser, wait, 2, 20)  #准备换钱
#         time.sleep(5)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，切换网络
#         fox_confirm_connect_network(browser, wait)
#         time.sleep(3)
#         switch_tab_by_handle(browser, 1, 0)  # 切换到：matcha
#         matcha_formal_change_coin(browser, wait)  # 下单
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸，切换网络
#         fox_confirm_swap(browser, wait)  # 小狐狸确认交易
#         time.sleep(5)
#
#         # 转账后，20秒后，查询OP上的USDC是否到账
#         time.sleep(20)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#         all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
#         OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
#
#         while OP_USDC_balance_after == OP_USDC_balance_before:
#             print("OP上的 USDC 还没到账，20秒轮询一次")
#             time.sleep(20)  # 20秒去轮询一次
#             switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#             all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)  # 获取该账户下的所有网络、代币及余额
#             OP_USDC_balance_after = float(return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance))  # 记下当前OP上USDC的金额
#
#         print(f"OP上的 USDC 到账了，金额是 {OP_USDC_balance_after}")
#         switch_tab_by_handle(browser, 1, 0)  # 切换到：matcha
#         time.sleep(5)
#         browser.close()# 关闭当前标签页，因为句柄在当前页，所以可以直接关闭
#
#     #二、正式打开pika，开始任务
#     print(f"OP上的 USDC 大于1，具体是 {OP_USDC_balance_before}，正式pika任务")
#     new_tab(browser, op_pika_url)
#     time.sleep(5)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到：pika
#
#     #1 判断是否要连接钱包
#     if pika_whether_connect_wallet(browser, wait) == "Connect Wallet":
#         print("需要连接钱包")
#         pika_connect_wallet(browser, wait)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#         fox_confirm_connect_network(browser, wait) #小狐狸【批准】、【切换网络】
#         # fox_confirm_connect_account(browser, wait) #什么时候出现这一步呢？
#         switch_tab_by_handle(browser, 1, 0)  # 切换到第1个标签页：被撸网站
#     else:
#         print("不用连接钱包，准备下一步操作")
#     #pika输入交易金额并提交
#     pika_input_margin(browser, wait, OP_USDC_balance_before)
#     if pika_try_approve_or_submit(browser, wait):  #如果有返回值是1，说明要approve
#         time.sleep(2)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#         fox_confirm_swap(browser, wait)
#         time.sleep(5)
#         switch_tab_by_handle(browser, 1, 0)  # 切换到pika
#     #没有approve，直接sumbit
#     pika_confirm(browser, wait)
#     time.sleep(4)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#     fox_confirm_swap(browser, wait)
#     time.sleep(random.randint(20,40)) #随机休眠10~30秒
#     switch_tab_by_handle(browser, 1, 0)  # 切换到pika
#
#     #下面取消pika交易
#     pika_close_transaction(browser, wait)
#     time.sleep(8)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#     fox_confirm_swap(browser, wait)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到pika
#     time.sleep(8)
#     browser.close()
#
# #做 OP上的 showme
# def OP_showme():
#     # 小狐狸网络切换成OP
#     switch_tab_by_handle(browser, 0, 0)  # 切换到：pika
#     fox_change_network(browser, wait, "Optimism")
#     print("开始OP_showme任务")
#     new_tab(browser, op_showme_url)
#     time.sleep(8)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到：pika
#     #判断是否连接钱包
#     if showme_whether_connect_wallet(browser, wait) == "Connect Wallet":
#         print("需要连接钱包")
#         showme_connect_wallet(browser, wait)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#         fox_confirm_connect_account(browser, wait) #什么时候出现这一步呢？
#         time.sleep(5)
#         fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
#         switch_tab_by_handle(browser, 1, 0)  # 切换到第1个标签页：被撸网站
#     else:
#         print("不用连接钱包，准备下一步操作")
#
#     #领取NFT
#     show_claim_NFT(browser, wait)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#     fox_confirm_swap(browser, wait)
#     time.sleep(5)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到pika
#     time.sleep(5)
#     browser.close()
#
# #做 OP上的 zipswap
# def OP_zipswap(keywords, L2_ETH_value, L2_ETH_save_min, L2_ETH_save_max):
#     # 小狐狸网络切换成OP
#     switch_tab_by_handle(browser, 0, 0)  # 切换到：pika
#     fox_change_network(browser, wait, "Optimism")
#     time.sleep(5)
#     print("开始OP_zipswap任务")
#     new_tab(browser, op_zipswap_url)
#     time.sleep(8)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到：pika
#
#     #连接钱包
#     if zipswap_whether_connect_wallet(browser, wait) == "Connect Wallet":
#         print("需要连接钱包")
#         zipswap_connect_wallet(browser, wait)
#         time.sleep(5)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#         fox_confirm_connect_account(browser, wait) #什么时候出现这一步呢？
#         time.sleep(5)
#         fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
#         switch_tab_by_handle(browser, 1, 0)  # 切换到第1个标签页：被撸网站
#     #选择代币、输入金额、确认交易
#     zipswap_prepare_transfer(browser, wait, keywords, L2_ETH_value, L2_ETH_save_min, L2_ETH_save_max)
#     time.sleep(5)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#     fox_confirm_swap(browser, wait)
#     print("卡在这里")
#     time.sleep(600)
#
# #做 OP上的 clipper
# def OP_clipper(L2_ETH_value, L2_ETH_save_min, L2_ETH_save_max):
#     # 小狐狸网络切换成OP
#     switch_tab_by_handle(browser, 0, 0)  # 切换到：clipper
#     fox_change_network(browser, wait, "Optimism")
#     time.sleep(5)
#     print("开始OP_clipper任务")
#     new_tab(browser, op_clipper_url)
#     time.sleep(8)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到：clipper
#
#     #连接钱包
#     if clipper_whether_connect_wallet(browser, wait) == "Connect your wallet":
#         print("需要连接钱包")
#         clipper_connect_wallet(browser, wait)
#         time.sleep(5)
#         switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#         fox_confirm_connect_account(browser, wait) #什么时候出现这一步呢？
#         time.sleep(5)
#         fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
#         switch_tab_by_handle(browser, 1, 0)  # 切换到第1个标签页：被撸网站
#     #选择代币、输入金额、确认交易
#     clipper_prepare_transfer(browser, wait, L2_ETH_value, L2_ETH_save_min, L2_ETH_save_max)
#     time.sleep(3)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到第0个标签页：小狐狸
#     fox_confirm_swap(browser, wait)
#     time.sleep(5)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到第0个标签页：小狐狸
