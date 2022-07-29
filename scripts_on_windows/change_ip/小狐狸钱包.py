# 方法1：http://cuketest.com/zh-cn/web/howto/chrome_options
#方法2：直接浏览器多开：https://cloud.tencent.com/developer/article/1908546?from=article.detail.1704027

#-------------引入功能包---------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pathlib, time, os
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains  # 用于操作鼠标
from selenium.webdriver import ChromeOptions  #

print("开始")
#-------------上传至ixigua-----------------
options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:5004")

# options.add_argument('--user-data-dir=D:\\auto_video_projects\\xigua_video\\py_selenium2')
#切换谷歌账号，法1
options.add_argument('--user-data-dir=D:\\auto_video_projects\\xigua_video\\adidas\\1')


#切换谷歌账号，法2
# options.add_argument("--user-data-dir=C:\\Users\\Terry\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")

driver_path = "D:\\auto_video_projects\\xigua_video\\chromedriver.exe"
# 打开浏览器
# os.startfile(r'D:\auto_video_projects\xigua_video\2_chrome.exe.lnk')  #注意要加.lnk，前面包含保持和文件名一致

driver = webdriver.Chrome(driver_path, chrome_options = options)
print(driver.title)  #测试是否打开了浏览器
print("hellpo")
TIME_OUT = 15
wait = WebDriverWait(driver, TIME_OUT)  # wait是一个类
# url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#"
# driver.get(url)

#点击小狐狸，快捷键Alt + Shift + M


# #下面代码可实现键盘ctrl+q快捷键
# keyboard = Controller()
# # keyboard.press(Key.ctrl.value) #按ctrl键
# keyboard.press(Key.shift.value) #按ctrl键
# keyboard.press(Key.alt.value) #按ctrl键
# keyboard.press('M') #按q键
#
# keyboard.release(Key.shift.value)
# keyboard.release(Key.alt.value)
# keyboard.release('M')


# time.sleep(2)
# print("按完了")
#输入密码登陆


url1 = "DevTools-chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html"
url2 = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/SPECIFICPAGE.html"

# usr-agent = "djflhoibgkdhkhhcedjiklpkjnoahfmg"

url3 = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
#先登录小狐狸
driver.get(url3)
time.sleep(3) #等待网页加载
send_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
send_password.send_keys("nkbihfbeogaea")
#谷歌上的密码：nkbihfbeogaea
#360浏览器：hlefnkodbefgpgknn
#确定是否登录成功

time.sleep(3)

#建立新标签页，进入目标网站
url4 = "https://app.debridge.finance/" #debridge
new_window = 'window.open("{}")'.format(url4)
driver.execute_script(new_window)
time.sleep(8)#等待网页加载
print("开始连接钱包")
#点击“连接钱包”

#注意要切换到该标签页，否则selenium 找不到元素
print(driver.window_handles)  # ['CDwindow-560A9B54BF935A8249566C795D6D857D', 'CDwindow-108E4B9171C6D7FA4CCAAAF4FEACCAFE']
driver.switch_to.window(driver.window_handles[1])

# link_wallet = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary btn-block btn-lg __submit ng-star-inserted']")))
link_wallet2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary btn-block btn-lg __submit ng-star-inserted']")))
driver.execute_script("arguments[0].click();", link_wallet2)

#点击“同意协议”
try:  #如果小狐狸不可按下，说明没有点击“同意协议”，
    WebDriverWait(driver, 3, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='wallet-connect-metamask']")))
except:  #则去同意协议
    link_wallet4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='mat-slide-toggle-label'][@for='mat-slide-toggle-2-input']/div")))
    driver.execute_script("arguments[0].click();", link_wallet4)
finally: #最终都要点小狐狸
    link_wallet6 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='wallet-connect-metamask']")))
    driver.execute_script("arguments[0].click();", link_wallet6)

# for i in range(1,10):
#     # link_wallet3.click()  #这里滑块必须用.click方法——不是的，主要还是要找对元素，
#     driver.execute_script("arguments[0].click();", link_wallet3)
#     time.sleep(2)
#     print(f"点击滑块{i}次")

handles = driver.window_handles          #获取当前浏览器的所有窗口句柄
print(handles)

#点击小狐狸钱包
print("结束")
time.sleep(555555)
link_wallet5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='wallet-connect-metamask']")))
# link_wallet6 = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='mat-slide-toggle-label'][@for='mat-slide-toggle-2-input']/div")))
driver.execute_script("arguments[0].click();", link_wallet5)
print("已经点击小狐狸")

time.sleep(22222)


#助记词：almost dolphin advice figure frown fury room heart motor comfort diamond caught
driver.quit()
