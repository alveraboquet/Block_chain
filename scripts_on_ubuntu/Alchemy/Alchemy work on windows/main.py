from functions import *

browser_wait_times = 15

##============= 一, 准备浏览器、切换IP、清理缓存
wait, browser = my_chrome(time_out=browser_wait_times)
browser.set_page_load_timeout(121)
open_clash_dashboard(browser, wait, url_dashboard)
random_select_clash_ip(browser, wait)
delete_cookie(browser)

##=====登录小狐狸
login_metamask(browser, wait, metamask_pw, metamask_home)

#=====开始新业务
url = "https://docs.openzeppelin.com/contracts/4.x/wizard"
new_tab(browser, url)
time_sleep(15, "等待网页加载")
switch_tab_by_handle(browser, 2, 0)  # 切换到标签页