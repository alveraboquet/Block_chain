# 方法1：http://cuketest.com/zh-cn/web/howto/chrome_options
#方法2：直接浏览器多开：https://cloud.tencent.com/developer/article/1908546?from=article.detail.1704027

#-------------引入功能包---------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from my_ixigua import ixigua_func
import pathlib, time, os


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
time.sleep(2)
driver = webdriver.Chrome(driver_path, chrome_options = options)
print(driver.title)  #测试是否打开了浏览器
print("hellpo")
time.sleep(2222)


driver.quit()
