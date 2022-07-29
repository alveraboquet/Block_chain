from L2.functions import *
which_chrome = 1
wait, browser = my_chrome(which_chrome)
login_metamask(browser, wait, metamask_pw, metamask_home, "Arbitrum One")

new_tab(browser, yield_pool_url)  # 到 lifi去，这是第2个标签
time_sleep(5, "正在打开网页，在此之前请确保小狐狸切换到了对应网络")
switch_tab_by_handle(browser, 1, 0)  # 切换到被撸网站

#==========连接钱包
yield_whether_connect_wallet(browser, wait)

#========准备做：pool

# yield_prepare_pool(browser, wait)
# switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
# fox_confirm_yield_signature(browser, wait)
# switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

#========准备做：lend
yield_prepare_lend(browser, wait)
switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
fox_confirm_yield_signature(browser, wait)
switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸

#========准备做：borrow
yield_prepare_lend(browser, wait)
switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
fox_confirm_yield_signature(browser, wait)
switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸



time_sleep(600, "休息")
#=====尝试输入邀请
# text = gmx_whether_input_referal(browser, wait)
# if "yes" in text:
#     gmx_input_referal(browser, wait)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#     fox_confirm_gmx_referal(browser, wait)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到小狐狸


#========判断是否要允许杠杆
# gmx_prepare_input(browser, wait)
# text = gmx_whether_allow_leverage_or_formal_long(browser, wait)
# if "Leverage" in text:
#     #允许使用杠杆
#     print(text, "需要允许杠杆")
#     gmx_allow_leverage_long_trade(browser, wait)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#     success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
#     print(success_or_fail)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到 gmx

#=========开始正式交易
#选择做空或者做多
# a = random.randint(1,2)
# if a == 1:
#     gmx_formal_long_trade(browser, wait)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#     success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
#     print(success_or_fail)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到 gmx
#     time_sleep(30, "准备取消long")
#     #取消long
# elif a == 2:
#     gmx_formal_short_trade(browser, wait)
#     switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
#     success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
#     print(success_or_fail)
#     switch_tab_by_handle(browser, 1, 0)  # 切换到 gmx
#     time_sleep(30, "准备取消short")
#     # 取消short
# else:
#     print("没有这个任务")
#2)========换币


#3)============流动性
# gmx_buy_or_sell_GLP(browser, wait, "buy")
#
# switch_tab_by_handle(browser, 0, 1)  # 切换到小狐狸
# success_or_fail = fox_get_gas_fee_and_confirm_swap(browser, wait)
# print(success_or_fail)
# switch_tab_by_handle(browser, 1, 0)  # 切换到 gmx
#
#
#


# gmx_allow_leverage_short_trade(browser, wait)
# gmx_prepare_USDT_swap_ETH(browser, wait)


# hop_whether_connect_wallet(browser, wait)
# hop_prepare_transfer_coin(browser, wait, "Mainnet", "Arbitrum")

