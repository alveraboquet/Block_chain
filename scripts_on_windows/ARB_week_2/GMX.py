# 功能：把L2的钱，分散到其他到L2
# ARB 的钱转到其他生态
#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

from L2.functions import *

while True:
    for i in range(2, 201):
        print(f"=======在找号{i}")
        #============ 首先确定要转的源是哪个，比如 from 源是 ZK
        # if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').read(i, "I")) == "1" or str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').read(i, "I")) == "·1":  # OP 转钱
        # if Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').read(i, "K") != "成功":
            # try:
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
        login_metamask(browser, wait, metamask_pw, metamask_home, "Arbitrum One")

        # login_metamask(browser, wait, metamask_pw, metamask_home, "Ethereum")
        time.sleep(2)
        switch_tab_by_handle(browser, 1, 0)  # 切换到第小狐狸

        ##====== 小狐狸换号、网络
        time_sleep(2, f"========开始换号{i}==========")
        fox_change_account(browser, wait, i)
        # time_sleep(2, "开始换网络，第一次换过之后，就不要换网络了")
        # fox_change_network(browser, wait, "Arbitrum One")

        #=========================== 开始任务
        new_tab(browser, gmx_trade_url)  # 到 lifi去，这是第2个标签
        time_sleep(5, "正在打开网页，在此之前请确保小狐狸切换到了对应网络")
        switch_tab_by_handle(browser, 2, 0)  # 切换到被撸网站
        # =====连接钱包
        gmx_whether_connect_wallet(browser, wait)
        # =====尝试输入邀请
        text = gmx_whether_input_referal(browser, wait)
        if "yes" in text:
            gmx_input_referal(browser, wait)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            fox_confirm_gmx_referal(browser, wait)
            switch_tab_by_handle(browser, 2, 0)  # 切换被

        # =====判断是否要允许杠杆
        gmx_prepare_input(browser, wait)
        text = gmx_whether_allow_leverage_or_formal_long(browser, wait)
        if "Leverage" in text:
            #允许使用杠杆
            print(text, "需要允许杠杆")
            gmx_allow_leverage_long_trade(browser, wait)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
            print(success_or_fail)
            switch_tab_by_handle(browser, 2, 0)  # 切换到 gmx

        # =========开始正式交易
        # 任务1：合约
        a = random.randint(1,2)
        if a == 1:
            print("准备做多")
            gmx_formal_long_trade(browser, wait)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
            print(success_or_fail)
            switch_tab_by_handle(browser, 2, 0)  # 切换到 gmx
            time_sleep(30, "准备取消long")
            #取消long
        elif a == 2:
            print("准备做空")
            gmx_formal_short_trade(browser, wait)
            switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
            success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
            print(success_or_fail)
            switch_tab_by_handle(browser, 2, 0)  # 切换到 gmx
            time_sleep(30, "准备取消short")
            # 取消short
        else:
            print("没有这个任务")

        # 任务2：换币
        gmx_prepare_ETH_swap_token(browser, wait, "USDC")

        # 任务3：流动性
        gmx_buy_or_sell_GLP(browser, wait, "buy")

        switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
        success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
        print(success_or_fail)
        switch_tab_by_handle(browser, 2, 0)  # 切换到 gmx

        # ========================== 操作结束，关闭浏览器
        a = random.randint(6, 8)
        time_sleep(a, f"++++++++++随机等待时间{a}")
        browser.quit()
        a = random.randint(6, 8)
        time_sleep(a, f"++++++++++随机等待时间{a}")
            # except:
            #     print(f"{i}出错了")
            #     Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').plain_write(i, "K", "×")
            #     a = random.randint(6, 8)
            #     time_sleep(a, f"++++++++++随机等待时间{a}")
            #     try:
            #         browser.quit()
            #         print("出错了")
            #     except:
            #         print("尝试关闭浏览器，但浏览器可能之前已关闭")
            #     a = random.randint(6, 8)
            #     time_sleep(a, f"++++++++++随机等待时间{a}")
