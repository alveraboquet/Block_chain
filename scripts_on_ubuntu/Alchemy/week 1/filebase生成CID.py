#pycharm通过git同步代码：窗口右上角粉色小箭头➡️
import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *

from faker import Faker
fake = Faker()

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
write_success_to_excel_column = "E"  #把成功或失败记录到excel的列
read_from_excel_column = "E" #从excel中的哪一列读取状态? 判断是不是要做任务?
excel_start_row = 4
browser_wait_times = 10

filebaseURL = 'https://console.filebase.com/buckets'
filebase_email = '1570561804@qq.com'
filebase_pw = '6PaozA!zJj^v'

##=========== 准备浏览器
wait, browser = my_linux_chrome(time_out=browser_wait_times)
browser.get(filebaseURL)
switch_tab_by_handle(browser, 0, 0)  # 切换到filebase


#===========================登录=============
# try:
#     send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user_email']")))
#     time_sleep(2,"准备输入用户名")
#     send_password.send_keys(filebase_email)
#     time.sleep(2)

#     send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user_password']")))
#     time_sleep(2,"准备输入用户名")
#     send_password.send_keys(filebase_pw)

#     remember_me = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='user_remember_me']")))
#     time_sleep(2,"准备点击记住我")
#     browser.execute_script("arguments[0].click();", remember_me)


#     confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
#     time_sleep(2,"准备点击登录")
#     browser.execute_script("arguments[0].click();", confirm_login)
# except:
#     print("可能已经登录了")


#==========================创建bucket
# create_bucket = wait.until(EC.element_to_be_clickable((By.XPATH,"//span//button[text()[contains(.,'Create Bucket')]]")))
# time_sleep(2,"准备创建bucket")
# browser.execute_script("arguments[0].click();", create_bucket)

# c = fake.md5()
# print("bucket 名字是:",c)

# send_bucket_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='bucket_name']")))
# time_sleep(2,"准备输入bucket name")
# send_bucket_name.send_keys(c)
# time.sleep(2)

# #创建bucket
# confirm_bucket_name = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='save_bucket']")))
# time_sleep(2,"准备创建bucket")
# browser.execute_script("arguments[0].click();", confirm_bucket_name)

#======================进入bucket
c = 'cd1183'
login_bucket = wait.until(EC.element_to_be_clickable((By.XPATH,f"//p[text()[contains(.,'{c}')]]")))
time_sleep(2,"准备进入bucket")
browser.execute_script("arguments[0].click();", login_bucket)

#===========上传
upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='menu-button']")))
time_sleep(2,"准备点击上传111")
browser.execute_script("arguments[0].click();", upload_button)

#选择上传file文件
# file_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()[contains(.,'File')]]")))
# time_sleep(2,"准备点击上传")
# file_button.send_keys("/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/pics/幻灯片5.png")
# # browser.execute_script("arguments[0].click();", file_button)

#选择file
# file_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='py-1']/form[1]/input[2]")))
file_button  = browser.find_element(By.XPATH, "//div[@class='py-1']/form[1]/input[1]")

# time_sleep(2,"准备点击上传")
# browser.execute_script("arguments[0].click();", file_button)

time_sleep(2,"准备注入java")
browser.execute_script("arguments[0].type='visible';", file_button)
time_sleep(2,"准备上传")
file_button.send_keys("/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/pics/幻灯片5.png")



time_sleep(200,"纯倒计时")

##=========== 开始做任务
# CID_text = DO_TXT(r"ZK/json_CID.txt", i).read_x_line()
# print("这次用的CID_text是",CID_text)
# save_record = zksync_mint_NFT(browser, wait, CID_text)

# print("记录是：",save_record)

a = random.randint(10, 15)
time_sleep(a, f"++++++++++随机等待时间{a}")
browser.quit()
a = random.randint(10, 15)
time_sleep(a, f"++++++++++随机等待时间{a}")



