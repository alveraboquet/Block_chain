# filebase 挂代理时,用全局
import json
from random_word import RandomWords
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

from faker import Faker
fake = Faker()

excel_start_row = 20 #从excel第几行开始
write_jsonCID_to_excel_column = 'G' #结果记录到哪一列

json_path = "/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/metadata.json"
excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
browser_wait_times = 10

filebaseURL = 'https://console.filebase.com/buckets'
filebase_email = '1570561804@qq.com'
filebase_pw = '6PaozA!zJj^v'

#=============== 修改json文件
def edit_json_file(json_path, pic_CID):
    whole_pic_CID = f'https://ipfs.filebase.io/ipfs/{pic_CID}'
    with open(json_path, 'r+') as f:
        # 读取demp.json文件内容
        data = json.load(f)
        # print(data)
        # print('================')
        # print(data["image"])

        # 修改CID的值
        data["image"] = whole_pic_CID
        data["name"] = RandomWords().get_random_word()  # 随机一个名字
        print("=========修改 image 的链接为:", whole_pic_CID)
        # print('================')
        # print(data)
        with open(json_path, 'w') as f2:
            json.dump(data, f2)  # 写入f2文件到本地
            f2.close() #打开后需要关闭，否则文件无变化，导致CID一直一样
        f.close()


while 1:
    for i in range(excel_start_row,201):
        #=======================如果没有ipfs_json 的话, 开始任务吧
        success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(i, write_jsonCID_to_excel_column)
        print("excel数据是:", str(success_or_fail))

        if "ipfs://" not in str(success_or_fail):
            print(f" {i} 号没有ipfs, 需要做创建ipfs")
            
            ##=========== 准备浏览器
            wait, browser = my_linux_chrome(time_out=browser_wait_times)
            browser.get(filebaseURL)
            switch_tab_by_handle(browser, 0, 0)  # 切换到filebase

            #===========================登录=============
            try:
                send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user_email']")))
                time_sleep(2,"准备输入用户名")
                send_password.send_keys(filebase_email)
                time.sleep(2)

                send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user_password']")))
                time_sleep(2,"准备输入用户名")
                send_password.send_keys(filebase_pw)

                remember_me = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='user_remember_me']")))
                time_sleep(2,"准备点击记住我")
                browser.execute_script("arguments[0].click();", remember_me)


                confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
                time_sleep(2,"准备点击登录")
                browser.execute_script("arguments[0].click();", confirm_login)
            except:
                print("可能已经登录了") 

            #=============回到bucket首页
            try:
                back_to_bucket = wait.until(EC.element_to_be_clickable((By.XPATH,"//nav/a[text()[contains(.,' Buckets')]]")))
                time_sleep(2,"准备回到bucket")
                browser.execute_script("arguments[0].click();", back_to_bucket)
                print("已经点击回到bucket")
            except:
                print("程序一开始, 点击返回bucket失败")

            try:
                #==========================创建bucket
                create_bucket = wait.until(EC.element_to_be_clickable((By.XPATH,"//span//button[text()[contains(.,'Create Bucket')]]")))
                time_sleep(2,"准备创建bucket")
                browser.execute_script("arguments[0].click();", create_bucket)

                c = fake.md5()
                print("bucket 名字是:",c)

                send_bucket_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='bucket_name']")))
                time_sleep(2,"准备输入bucket name")
                send_bucket_name.send_keys(c)
                time.sleep(2)

                #创建bucket
                confirm_bucket_name = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='save_bucket']")))
                time_sleep(2,"准备创建bucket")
                browser.execute_script("arguments[0].click();", confirm_bucket_name)
                time_sleep(10)

                #======================进入bucket
                # c = 'cd1183'
                login_bucket = wait.until(EC.element_to_be_clickable((By.XPATH,f"//p[text()[contains(.,'{c}')]]")))
                time_sleep(2,"准备进入bucket")
                browser.execute_script("arguments[0].click();", login_bucket)
                time_sleep(10)

                #======================上传图片文件,并获得图片CID
                upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='menu-button']")))
                time_sleep(2,"准备点击upload")
                browser.execute_script("arguments[0].click();", upload_button)

                #==========选择file按钮
                file_button  = browser.find_element(By.XPATH, "//label[text()[contains(.,'File')]]//span/input")
                time_sleep(2,"准备选择file上传")
                pic_path = f"/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/photos/{i}.png"
                file_button.send_keys(pic_path)

                time_sleep(15,"等待上传图片......")

                #获取图片的CID
                pic_CID = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]//span[@id='ipfs_cid']")))
                pic_CID_text = pic_CID.text 
                print("=============获取到的图片CID是:", pic_CID_text)

                #修改json 文件
                edit_json_file(json_path, pic_CID_text)

                #=======================上传json文件,并获得CID
                upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='menu-button']")))
                time_sleep(2,"准备点击upload")
                browser.execute_script("arguments[0].click();", upload_button)

                file_button  = browser.find_element(By.XPATH, "//label[text()[contains(.,'File')]]//span/input")
                time_sleep(2,"准备选择file上传")
                file_button.send_keys(json_path)
                time_sleep(8,"等待上传json文件......")

                # 获取json 的CID
                json_CID = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[2]//span[@id='ipfs_cid']")))
                json_CID_text = json_CID.text 
                print("===============获取到json的CID是:", json_CID_text)

                # 写入到excel去
                full_json_CID = "ipfs://" + json_CID_text                
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_jsonCID_to_excel_column, full_json_CID)

                browser.quit()
                time_sleep(20,"纯倒计时")
            except:
                print("任务失败,开始下一个")
                Do_Excel(excel_path, sheetname='Sheet1').plain_write(i, write_jsonCID_to_excel_column, "×")
                try:
                    browser.quit()
                except:
                    print("可能是已经退出了浏览器")
                a = random.randint(10, 15)
                time_sleep(a, f"++++++++++随机等待时间{a}")
                continue 
                


