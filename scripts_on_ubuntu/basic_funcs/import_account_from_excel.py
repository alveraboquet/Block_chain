#把excel里的私钥导入到小狐狸
from functions import *

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
wait, browser = my_linux_chrome()
login_metamask(browser, wait, metamask_pw, metamask_home)

excel_path = "/home/parallels/Documents/block_chain/sync_swap_50.xlsx"
#点击图标——》导入账户——》粘贴私钥——》导入
for i in range(2, 202):
    key = Do_Excel(excel_path,sheetname='Sheet1').read(i, "A")
    print("Your key is :",key)
    fox_import_private_key(browser, wait, key)
    time.sleep(1)
    