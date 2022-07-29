from functions import *

url_dashboard = "http://127.0.0.1:9090/ui/#/proxies"
# url_dashboard = "http://clash.razord.top/#/proxies"
url_google = "https://www.google.com"
url_being_lu = "https://www.storkapp.me/"

#============OP上的项目
op_pika_url = "https://app.pikaprotocol.com/trade/ETH-USD"
op_showme_url = "https://optimismair.showme.fan/"
op_zipswap_url = "https://zipswap.fi/#/swap"
op_clipper_url = "https://clipper.exchange/app/swap"
######################


OP_USDC_addr = '0x7F5c764cBc14f9669B88837ca1490cCa17c31607'
arb_url = "https://bridge.arbitrum.io/"

#####各种代币地址
ETH_USDC_address = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
OP_sUSD_address = "0x8c6f28f2F1A3C87F0f938b96d27520d9751ec8d9"
OP_USDC_address = "0x7f5c764cbc14f9669b88837ca1490cca17c31607"
ARB_USDC_address = "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8"

#######构建浏览器

wait, browser = my_chrome()

#准备工作：登陆小狐狸，获取小狐狸账户个数。这是第0个标签
login_metamask(browser, wait, metamask_pw, metamask_home)
######获取小狐狸账号数量
# get_fox_accounts(browser, wait)

######切换账号，每个账号上的链和代币不一定相同
fox_change_account(browser, wait, 1)

#### 获取该账户下的所有网络、代币及余额
all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait)
# print(all_networks,"\n", all_token_and_balance)
#
# ####此处设置for循环，对每个account 做处理：

# networks = get_fox_network(browser, wait)

wallet_updata_Flag = 0 #执行下面的if，如果有执行，则之后要更新查询余额
if 'Arbitrum One' not in all_networks:
    print("需要连接ARB网络")
    fox_add_network(browser, wait, "Arbitrum One")  #该函数内部有Arb的信息列表
    time.sleep(5)
    wallet_updata_Flag = 1

if 'Optimism' not in all_networks:
    print("需要连接Optimism网络")
    fox_add_network(browser, wait, "Optimism")
    time.sleep(5)
    wallet_updata_Flag = 1

#判断ARB上有没有USDC
# if not return_fox_net_token_balance("Arbitrum", "USDC", all_networks, all_token_and_balance): #如果没有的话去添加代币
#     print("需要添加ARB——USDC")
#     fox_change_network(browser, wait, "Arbitrum")
#     fox_add_token(browser, wait, ARB_USDC_address)
#     time.sleep(5)
#     wallet_updata_Flag = 1
#
# if not return_fox_net_token_balance("Optimism", "sUSD", all_networks, all_token_and_balance):
#     print("需要添加OP——sUSD")
#     fox_change_network(browser, wait, "Optimism")
#     fox_add_token(browser, wait, OP_sUSD_address)
#     time.sleep(5)
#     wallet_updata_Flag = 1
#
# if not return_fox_net_token_balance("Optimism", "USDC", all_networks, all_token_and_balance):
#     print("需要添加OP——sUSD")
#     fox_change_network(browser, wait, "Optimism")
#     fox_add_token(browser, wait, OP_USDC_address)
#     time.sleep(5)
#     wallet_updata_Flag = 1
#
# if  wallet_updata_Flag:
#     print("更新查询钱包余额")
#     all_networks, all_token_and_balance = get_fox_network_token_balance(browser, wait) #获取该账户下的所有网络、代币及余额
#     print(all_networks,"\n", all_token_and_balance)
#
# print("最新账户余额是：", all_networks,"\n", all_token_and_balance)
