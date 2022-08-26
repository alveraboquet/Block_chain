import requests
import json
import re
import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

#从脆球官网获取
cuiqiu_token = '88434c9de6ef45b0b8f360a190f60abd'
cuiqiu_mail_id = '608142'

excel_row = 11   #待注册的邮箱
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
email_to_be_activate =  Do_Excel(excel_path,sheetname='Sheet1').read(excel_row, "C")
 

not_find_yet = True
while not_find_yet:
    activate_link = '' #空链接
    #获取邮件列表
    url = "https://domain-open-api.cuiqiu.com/v1/box/list"
    payload={'mail_id': cuiqiu_mail_id,
    'token': cuiqiu_token,
    'start_time': '2022-08-24',
    'end_time': '2022-08-26',
    'page': '1',
    'limit': '10'}
    files=[

    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    result = response.text 

    #==================================获取邮件id
    #字符串转json
    json1 = json.loads(result)
    # print(json1)
    # print(type(json1))
    print("===================")
    #转为列表
    email_list = json1['data']['list']
    # print(email_list)

    result_box_id = 'kong'
    for i in email_list:
        # print(i, type(i))
        if email_to_be_activate in str(i):
            if 'Verify your email' in str(i):
                # print(i)
                print("待激活的邮件id是:", i['id'])
                result_box_id = i['id']
                time_sleep(5, "已经找到了激活邮件, 需要提取下链接")


    #========================================获取邮件详情. 提取激活链接
    # # box_id 请通过 v1/box/list 获取邮箱列表接口获取
    url = "https://domain-open-api.cuiqiu.com/v1/box/detail"

    payload={'mail_id': cuiqiu_mail_id,
    'token': cuiqiu_token,
    'box_id': result_box_id}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    result = response.text
    # print("邮件详情是: ",result)


    urls = re.findall('[a-zA-z]+://[^\s]*', result)
    print(urls)
    print("===================")

    for url in urls:
        if url.startswith("http://url6420.alchemy.com/ls/click?"):
            print("激活链接是:", url[:-2])
            not_find_yet = False
            activate_link = url[:-2] #找到了激活链接
            # return activate_link

    time_sleep(5, "等一下")

