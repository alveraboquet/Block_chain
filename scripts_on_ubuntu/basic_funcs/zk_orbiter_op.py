# 功能：把zk的钱，转移到op, 各分一半
# ARB 的钱转到其他生态
import time
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
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
    if from_source == "zkSync":  # 如果源是 Optimism，则用 Optimism
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
        from_source_value, to_source_value = get_L2_balance_from_orb(browser, wait, from_source, to_destination)
        print(f"{from_source}的实时金额是: {from_source_value}, {to_destination}的实时金额是: {to_source_value}")
        
        ########## lifi准备换币。返回本次的交易值
        transfer_detail = L2_orb_L2_prepare_transfer_coin(browser, wait, from_source_value, to_source_value)
        # print(transfer_detail)
        # 切换到第小狐狸，刷新，签名。
        switch_tab_by_handle(browser, 1, 1)
        for i in range(1,3):#必须要签名2次
            fox_info = fox_confirm_sign(browser, wait)
            time_sleep(15, f"第{i}次签名结束")

        ######## 确认交易
        # fox_info = fox_confirm_L2_swap(browser, wait)  #这个网络不用签名3次
        switch_tab_by_handle(browser, 2, 0)
        orb_fail = ""
        try:  # 如果Completed，说明转账success
            confirm_and_send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[4]/div/div[1]')))
            if confirm_and_send.text == "Completed":
                print("小狐狸点击确认后，orb转过去了")
                orb_fail = "orb 成功"
                return orb_fail
        except:
            orb_fail = "orb失败"
            print("orb失败")
            return orb_fail

        # if "成功" in fox_info:
        #     if "失败" not in orb_fail:
        #         all_info = f"【成功】通过orb，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_info}"
        #         return all_info
        #     print("小狐狸点击确认后，orb失败，还是没有转过去")
        #     return "小狐狸点击确认后，orb失败，还是没有转过去"
        # else:
        #     print(fox_info)
        #     return fox_info  # 失败了，orb
    else:
        print("L2_orb_L2(), 源输入错误")


#=== ARB 可以转到哪
def zk_orb_OP(write_success_to_excel_column):
    info = L2_orb_L2(browser, wait, "zkSync", "Optimism")  # 测试通过
    print(info)  # 记录该info
    if "失败" in info:
        Do_Excel(excel_path).write(i, "W", info)
        Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")
    else:
        # Do_Excel(excel_path).write(i, "M", "1")
        Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
        Do_Excel(excel_path).write(i, "W", info)

def zk_orb_ARB(write_success_to_excel_column):
    info = L2_orb_L2(browser, wait, "zkSync", "Arbitrum")  # 测试通过
    print(info)  # 记录该info
    if "失败" in info:
        Do_Excel(excel_path).write(i, "W", info)
        Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")

    else: #如果成功的话就做标记
        Do_Excel(excel_path).write(i, "L", "1")
        Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "成功")
        Do_Excel(excel_path).write(i, "W", info)


excel_path= '/home/parallels/ubuntu_zk/Block_chain/eth1000_操作后.xlsx'
write_success_to_excel_column = "L"  #把成功或失败记录到excel的列
read_from_excel_column = "L" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 2
browser_wait_times = 30


for i in range(excel_start_row, 201):
        #============ 首先确定要转的源是哪个，比如 from 源是 ZK
        success_or_fail = Do_Excel(excel_path,sheetname='SheetJS').read(i, read_from_excel_column)
        print(f"现在的运行状态是：{success_or_fail}")
        if success_or_fail != "成功": # ZK 转钱
            try:
                print(f"==========第{i} 个号需要从 ZK 转到 OP =========")
                ##=============准备浏览器
                wait, browser = my_linux_chrome()

                ##=========== 预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                random_select_clash_ip(browser, wait)
                # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                # ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页


                # 清缓存, 登錄小狐狸,并换号
                delete_cookie(browser)
                login_metamask(browser, wait, metamask_pw, metamask_home)
                fox_change_account(browser, wait, i)
        

                #==== 开始任务
                a = random.randint(2, 2)
                time_sleep(2, f"准备执行任务{a}")
                if a == 1:
                    zk_orb_ARB(write_success_to_excel_column)
                    # ARB_lifi_OP()
                elif a == 2:
                    zk_orb_OP(write_success_to_excel_column)

                #==== 操作结束，关闭浏览器
                a = random.randint(5, 10)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(5, 10)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            except:
                print(f"====={i}出错了=========")
                Do_Excel(excel_path).plain_write(i, write_success_to_excel_column, "×")
                a = random.randint(10, 20)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                try:
                    browser.quit()
                except:
                    print("尝试关闭浏览器，但浏览器可能之前已关闭")
                a = random.randint(10, 20)
                time_sleep(a, f"++++++++++随机等待时间{a}")
