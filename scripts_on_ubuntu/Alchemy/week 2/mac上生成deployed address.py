import sys
sys.path.append('/home/parallels/ubuntu_syncswap/Block_chain')
from functions import *


api_info_excel_column = "H" #api 放在这里
excel_path = '/home/parallels/ubuntu_syncswap/Block_chain/scripts_on_ubuntu/Alchemy/week 2/week 2.xlsx'

your_api = Do_Excel(excel_path,sheetname='Sheet1').read(25, api_info_excel_column)
print("你的api是: ", your_api)

#需要读取excel表格
API = "Yt6aU9B8lnnGk_x7zTXhSRlRTCDKT7Rj"
private_key = "7106b6ae7ce69daf7a3282871f731e1ffcf35c561417968939cb2bcd8a26dbae"
#第26个号， 0x2bc1971582EbBFF3Ad69da41BDa4821720177211
#BuyMeACoffee deployed to: 0xa1E7a770509673cA99627BaD68C0E4a3288514D0

line1 = "GOERLI_URL=https://eth-goerli.alchemyapi.io/v2/" + API + "\n"
line2 = "GOERLI_API_KEY=" + API + "\n"
line3 = "PRIVATE_KEY=" + private_key

env_file_path = "/Users/spencer/BuyMeACoffee-contracts/.env"

with open(env_file_path,'a+',encoding='utf-8') as test:
    test.truncate(0)
with open(env_file_path,'a+',encoding='utf-8') as test:
    test.write(line1)
    test.write(line2)
    test.write(line3)

import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is not None:
        await window.async_create_tab()
    else:
        print("No current window")
    session = app.current_window.current_tab.current_session
    if session is not None:
        print(session)
        await session.async_send_text('cd /Users/spencer/BuyMeACoffee-contracts\n')
        await session.async_send_text('npx hardhat run scripts/deploy.js --network goerli\n')

iterm2.run_until_complete(main)
