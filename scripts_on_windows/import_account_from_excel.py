from functions import *

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
wait, browser = my_chrome()
login_metamask(browser, wait, metamask_pw, metamask_home)

#点击图标——》导入账户——》粘贴私钥——》导入
for i in range(2, 202):
    key = Do_Excel('eth1000_操作后.xlsx').read(i, "Y")
    fox_import_private_key(browser, wait, key)
    time.sleep(1)