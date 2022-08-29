#把excel里的私钥导入到小狐狸
import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
wait, browser = my_linux_chrome()
login_metamask(browser, wait, metamask_pw, metamask_home)

excel_path = "/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/basic_funcs/做alchemy用的后面200个号.xlsx"
#点击图标——》导入账户——》粘贴私钥——》导入
for i in range(115, 201):
    key = Do_Excel(excel_path, sheetname='Sheet1').read(i, "A")
    print(f"第{i}个Your key is :",key)
    # time_sleep(3600)
    try:
        fox_import_private_key(browser, wait, key)
        account_info = fox_get_account(browser, wait)
        print(f"====={i}将要写入的信息是", account_info)
        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, "B", account_info)
    except:
        Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, "B", "重复了")
        try:
            ##=========== 点击完成
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='account-modal__close']")))
            time_sleep(1, "点击关闭")
            browser.execute_script("arguments[0].click();", close_button)
        except:
            print("点击关闭失败")
    time_sleep(3, "等等...")
    #获取帐号
    