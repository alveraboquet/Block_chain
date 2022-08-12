# 功能：把L2的钱，分散到其他到L2
# ARB 的钱转到其他生态
#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

from L2.functions import *


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
    transfer_detail = bungee_prepare_transfer_coin(browser, wait, from_source, to_destination, 0.2, 0.3)

    #小狐狸确认签名
    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
    fox_info = fox_confirm_bungee_swap(browser, wait)  # 这个网络不用签名3次

    if "成功" in fox_info:
        all_info = f"【成功】通过 bungee，资金从{from_source}转到{to_destination} " + transfer_detail + f" {fox_info}"
        return all_info
        print("小狐狸点击确认后，bungee 失败，还是没有转过去")
        return "小狐狸点击确认后，bungee 失败，还是没有转过去"
    else:
        print(fox_info)
        return fox_info  # 失败了，orb

#基础函数
def L1_or_L2_hop_L2(browser, wait, from_source, to_destination):
    # ========== 打开 bungee

    new_tab(browser, hop_url)  # 到 lifi去，这是第2个标签
    time_sleep(5, "正在打开 hop ，在此之前请确保小狐狸切换到了对应网络")
    switch_tab_by_handle(browser, 2, 0)  # 切换到 bungee

    hop_whether_connect_wallet(browser, wait)
    hop_prepare_transfer_coin(browser, wait, from_source, to_destination, 0.2, 0.3)
    switch_tab_by_handle(browser, 1, 1)  # 切换到小狐狸
    success_or_fail = fox_confirm_hop_swap(browser, wait)
    print(success_or_fail)
    return success_or_fail  # 失败了，orb


# 打包基础函数
def L1_bungee_ARB():
    info = L2_bungee_L2(browser, wait, "Ethereum", "Arbitrum")
    if "失败" in info:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "B", "×")

    else: #如果成功的话就做标记
        # Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').write(i, "L", "1")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "B", "成功")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)

def L1_hop_ARB():
    info = L1_or_L2_hop_L2(browser, wait, "Mainnet", "Arbitrum")
    if "失败" in info:
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "B", "×")

    else: #如果成功的话就做标记
        # Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').write(i, "L", "1")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "B", "成功")
        Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i, "W", info)

#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

while True:
    for i in range(7, 201):
        print(f"=======在找号{i}")
        #============ 首先确定要转的源是哪个，比如 from 源是 ZK
        # if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').read(i, "I")) == "1" or str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_OP_操作后.xlsx').read(i, "I")) == "·1":  # OP 转钱
        if Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i, "B") != "成功":
            try:
                print(f"==========第{i}个号需要从 L1 转到 ARB =========")
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
                a = random.randint(1, 2)
                time_sleep(2, f"准备执行任务{a}")
                if a == 1:
                    L1_hop_ARB()
                elif a == 2:
                    L1_bungee_ARB()


                # ==== 操作结束，关闭浏览器
                a = random.randint(4, 8)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(5, 8)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            except:
                print(f"{i}出错了")
                Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').plain_write(i, "B", "×")
                a = random.randint(3, 8)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                try:
                    browser.quit()
                    print("出错了")
                except:
                    print("尝试关闭浏览器，但浏览器可能之前已关闭")
                a = random.randint(1, 8)
                time_sleep(a, f"++++++++++随机等待时间{a}")
