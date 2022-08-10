import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

#============galaxy上的项目
Odyssey_url = "https://galaxy.eco/arbitrum/campaign/GCCNzUtQiW/"  # 2022,8,5,领取NFT


# 领取ORB NFT
def claim_orb_NFT(browser, wait):
    time_sleep(2, "准备打开 orb ")
    new_tab(browser, Odyssey_url)
    time_sleep(10, "正在打开 orb ")
    switch_tab_by_handle(browser, 2, 0)  # 切换到被撸网站
    time_sleep( 6, "waiting")
    browser.refresh()
    time_sleep( 6, "waiting")
    browser.refresh()
    time_sleep( 6, "waiting")
    browser.refresh()
    time_sleep( 6, "waiting")   #多刷新几次，防止说不能cliam

    #连接小狐狸
    # try:
    #     connect_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="topNavbar"]/div/div[2]/div[2]/div[1]/div[2]/button/span')))
    #     if "Connect Wallet" in connect_button.text:
    #         time_sleep(2)
    #         browser.execute_script("arguments[0].click();", connect_button)

    #         fox_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[2]/div[2]/div')))
    #         time_sleep(2)
    #         browser.execute_script("arguments[0].click();", fox_button)
    # except:
    #     print("可能已经连接了小狐狸")  
    try:
        claim_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div/button/span')))
        time_sleep(7,"button found")
        browser.execute_script("arguments[0].click();", claim_button)
        time_sleep(15)
        switch_tab_by_handle(browser, 1, 1)  # 切换到被撸网站
        fox_info = fox_confirm_galaxy(browser, wait)
        time_sleep(20)
        switch_tab_by_handle(browser, 2, 0)  # 切换到被撸网站
        
        if "成功" in fox_info:
            try:
                submitted_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[1]')))
                if "submitted" in submitted_button.text:
                    print("领取成功!")
                    return "领取成功"
            except: #小狐狸虽然确认成功了，但实际没有cliam成功
                return "失败,小狐狸虽然确认成功了，但实际没有cliam成功"
        else:
            print("这个号领不了NFT")
            return "失败"
    except:
        print("这个号领不了NFT")
        return "失败"
    


excel_path= '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/L2_project/ARB_NFT.xlsx'
#excel中, 标志列(用于记录任务成功或失败)
# B列 = goerli转到zk上,
# C列 = ETH转USDC, D列 = USDC转ETH
# E列 = 提供流动性, F列 = 解除流动性

write_success_to_excel_column = "B"  #把成功或失败记录到excel的列

read_from_excel_column = "B" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 72
browser_wait_times = 10

while 1:
    for i in range(excel_start_row, 201):
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, read_from_excel_column)
        print(f"现在的运行状态是：{success_or_fail}")
        if success_or_fail != "成功":
            print(f"第{i} 个号需要做 galaxy ")
            try:
                    ##=========== 准备浏览器
                wait, browser = my_linux_chrome()

                ##=========== 预备步骤：切换IP。先打开
                open_clash_dashboard(browser, wait, url_dashboard)
                # switch_tab_by_handle(browser, 0, 0)  # 再切回 clash
                # ip_switcher(browser, wait, url_google)  # 这里会新建一个标签页
                random_select_clash_ip(browser, wait)


                ##=========== 清理缓存（从上面新建的标签页里，打开下面的链接）
                delete_cookie(browser)

                ##=========== 登陆小狐狸，
                login_metamask(browser, wait, metamask_pw, metamask_home, "Arbitrum")
                switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸
                # 小狐狸换号
                print(f"==============开始换号{i} ==============")
                fox_change_account(browser, wait, i)  #换号，选列表里的
                
                ##=========== 开始做任务
                #记录保存信息到excel
                save_record = claim_orb_NFT(browser, wait)

                if "成功" in save_record:
                    Do_Excel(excel_path,sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "成功")
                else:
                    Do_Excel(excel_path,sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "×")
                
                # 
                ##=========== 这里要设置随机等待时间
                a = random.randint(100, 350)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                browser.quit()
                a = random.randint(100, 150)
                time_sleep(a, f"++++++++++随机等待时间{a}")
            #
            except:
                ##=========== 使用指定工作表，保存信息到excel
                print(f"----第{i}出错了，是excel没关闭吗？")
                Do_Excel(excel_path,sheetname='Sheet1').plain_write(i, write_success_to_excel_column, "×")
                time_sleep(10, "出错了")
                browser.quit()
                continue
