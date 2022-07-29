# L2 做 ARB 的任务
from L2.functions import *

#============OP上的项目
arb_showme_url = "https://arbitrumone.showme.fan/"

#做 ARB上的 showme
def ARB_showme():
    # 将小狐狸的网络切换成 arb
    # switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
    # fox_change_network(browser, wait, "Arbitrum One")
    print("开始arb_showme任务")
    new_tab(browser, arb_showme_url)
    time_sleep(20,"等待showme加载")
    switch_tab_by_handle(browser, 2, 0)  # 切换到showme

    time_sleep(1, "第一次可能要showme签名")
    try:
        switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
        fox_confirm_sign(browser, wait)  # 第一次是确认连接小狐狸签名
        time_sleep(5, "小狐狸签名成功")
    except:
        print("可能不要小狐狸签名")

    # time_sleep(1, "第一次可能要连接小狐狸")
    # if showme_whether_connect_wallet(browser, wait) == "Connect Wallet":
    #     print("需要连接钱包")
    #     showme_connect_wallet(browser, wait)
    #     switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    #     time.sleep(5)
    #     fox_confirm_connect_network(browser, wait)  # 小狐狸【批准】、【切换网络】
    #     switch_tab_by_handle(browser, 2, 0)  # 切换到第1个标签页：被撸网站
    # else:
    #     print("不用连接钱包，准备下一步操作")

    #======领取NFT
    switch_tab_by_handle(browser, 2, 0)  # 切换到showme
    show_claim_NFT(browser, wait)

    #========小狐狸确认
    switch_tab_by_handle(browser, 1, 1)  # 切换到第0个标签页：小狐狸
    fox_info = fox_confirm_ARB(browser, wait)
    time.sleep(5)

    switch_tab_by_handle(browser, 2, 0)  # 切换到showme
    time.sleep(5)
    if "成功" in fox_info:
        return "ARB showme 任务完成；" + fox_info
    else:
        return fox_info

#user data 1：excel表格2~50，chrome2~50，Chrome1
#user data 2：excel表格51~100，相差49，chrome2~51，Chrome2
#user data 3：excel表格101~150，相差99，chrome2~51，Chrome3
#user data 4：excel表格151~200，相差149，chrome2~51，Chrome4
#user data 5：#excel表格2~200，相差0，chrome 2~201，Chrome5

# 得从第二个号开始才有钱
for i in range(3, 52):
    if str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i+149, "H")) == "·1" or str(Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').read(i+149, "H")) == "1":  # OP 所在列
        print(f"=====================第{i}, {i+149}个号需要做 ARB ==================")
        # try:
        ##=========== 准备浏览器

        wait, browser = my_chrome(4)
        ##=========== 预备步骤：切换IP。先打开
        open_clash_dashboard(browser, wait, url_dashboard)
        # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
        ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页

        ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
        delete_cookie(browser)

        ##=========== 登陆小狐狸，
        login_metamask(browser, wait, metamask_pw, metamask_home, "Arbitrum One")
        switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
        time_sleep(2)
        # 小狐狸换号
        print(f"=======开始换号{i}, {i+149} ==============")
        fox_change_account(browser, wait, i)  # 换号，选列表里的
        time_sleep(2)

        save_record = ARB_showme()  #测试通过
        # =====记录信息到 excel 中
        if "ARB showme" in save_record:
            Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i+149, "V", save_record)
            Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i+149, "O", "√")
            time_sleep(2, f"{save_record}，日志写入excel成功")
        else:
            Do_Excel(r'C:\Users\Terry\PycharmProjects\autopy\L2\eth1000_操作后.xlsx').write(i+149, "V", save_record)
            time_sleep(2, f"{save_record}，日志写入excel成功")
        ##=========== 这里要设置随机等待时间
        a = random.randint(60, 600)
        time_sleep(a, f"++++++++++随机等待时间{a}")
        browser.quit()
        a = random.randint(100, 1000)
        time_sleep(a, f"++++++++++随机等待时间{a}")
