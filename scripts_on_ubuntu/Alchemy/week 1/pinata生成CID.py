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

pinataURL = 'https://app.pinata.cloud/pinmanager'
pinata_email = '1570561804@qq.com'
pinata_pw = '6PaozA!zJj^v'

##=========== 准备浏览器
wait, browser = my_linux_chrome(time_out=browser_wait_times)
browser.get(pinataURL)
switch_tab_by_handle(browser, 0, 0)  # 切换到filebase
# time_sleep(200,"纯倒计时")

#===========================登录=============
# try:
#     send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
#     time_sleep(2,"准备输入用户名")
#     send_password.send_keys(pinata_email)
#     time.sleep(2)

#     send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
#     time_sleep(2,"准备输入用户名")
#     send_password.send_keys(pinata_pw)


#     confirm_login = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Sign In')]]")))
#     time_sleep(2,"准备点击登录")
#     browser.execute_script("arguments[0].click();", confirm_login)
# except:
#     print("可能已经登录了")

# time_sleep(200,"纯倒计时")


#=====================上传
upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='fade-button']")))
time_sleep(2,"准备点击上传")
browser.execute_script("arguments[0].click();", upload_button)

#选择上传file文件
file_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()[contains(.,'File')]]")))
time_sleep(2,"准备点击文件File")
browser.execute_script("arguments[0].click();", file_button)


#开始上传file
file_button  = browser.find_element(By.XPATH, "//div[@class='pinata-file-uploader']/input") #必须用这个
time_sleep(2,"准备上传")

filepath = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/photos/2.png'

file_button.send_keys(filepath)

#确定上传
# upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()[contains(.,'Upload')]]")))
upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-primary d-block w-100 mt-3']")))
time_sleep(2,"准备点击确认上传")
browser.execute_script("arguments[0].click();", upload_button)
time_sleep(20,"等待文件出现")



#获取最后一个文件的CID
PIC_CID_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody[@class='MuiTableBody-root css-1xnox0e']/tr[1]/td[2]/a")))
print("获取到的CID是:", PIC_CID_button.text)


time_sleep(3600,"纯倒计时")

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



