# filebase 挂代理时,用全局
from os import EX_CANTCREAT
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

from faker import Faker
fake = Faker()


browser_wait_times = 15
write_jsonCID_to_excel_column = 'A' # json CID 结果记录到哪一列

json_path = "/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/metadata.json"
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/备用json CID.xlsx'

filebaseURL = 'https://console.filebase.com/buckets'
filebase_email = '1570561804@qq.com'
filebase_pw = '6PaozA!zJj^v'

excel_start_row = 8 #从excel第几行开始
while 1:
    for i in range(excel_start_row, 72):
        #=======================如果没有ipfs_json 的话, 开始任务吧
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_jsonCID_to_excel_column)
        print("====json CID 数据是:", str(success_or_fail))

        if "ipfs://" not in str(success_or_fail):
            try:
                print(f" {i} 号没有ipfs, 需要做创建ipfs")
                ##=========== 准备浏览器
                wait, browser = my_linux_chrome(time_out=browser_wait_times)
                browser.refresh()  #不然显示不出网页
                # browser.set_page_load_timeout(121) #设置网页加载最多1分钟
                browser.get(filebaseURL)
                switch_tab_by_handle(browser, 0, 0)  # 切换到filebase

                #=============登录=============
                try:
                    login_filebase(browser, wait, filebase_email, filebase_pw)                                            
                except:
                    print("可能已经登录了") 

                #======随机创建bucket并进入
                filebase_random_create_bucket_and_enter(browser, wait)
                
                #=========在进入bucket后,上传图片文件,并获得图片CID
                pic_path = f"/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/photos/{i}.png"
                pic_CID_text = filebase_upload_pic_file_in_bucket(browser, wait, pic_path)
            
                #========修改json 文件
                edit_json_file(json_path, pic_CID_text)

                #============上传json文件,并获得CID
                json_CID_text = filebase_upload_json_file_in_bucket(browser, wait, json_path)
                    
                # ================= 写入到excel去
                full_json_CID = "ipfs://" + json_CID_text                
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_jsonCID_to_excel_column, full_json_CID)

                browser.quit()
                time_sleep(random.randint(10, 25),"===纯倒计时")
                
            except:
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_jsonCID_to_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能已经推出浏览器了")
                a = random.randint(10, 15)
                time_sleep(a, f"@ @ @ @ @ 超时出错了, 随机等待时间 {a} @ @ @ @")    


