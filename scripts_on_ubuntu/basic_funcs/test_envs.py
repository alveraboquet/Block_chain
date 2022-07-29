from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
print("hello world")

req_url = "https://www.baidu.com"
option=ChromeOptions()
#设置chrome浏览器无界面模式
#chrome_options.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--disable-gpu')
option.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止被网站识别
option.add_experimental_option('useAutomationExtension', False)

#chrome://version/
#Executable Path	/usr/lib/chromium-browser/chromium-browser
#Profile Path	/home/parallels/.config/chromium/Default

user_data_path = '--user-data-dir=/home/parallels/.config/chromium/Default'
option.add_argument(user_data_path)  # 用指定的浏览器进行测试


option.binary_location = '/usr/lib/chromium-browser/chromium-browser'


browser = webdriver.Chrome(options=option)

# 开始请求
browser.get(req_url)
#打印页面源代码
#print(browser.page_source)
#time.sleep(10)
#关闭浏览器
#browser.close()
#关闭chreomedriver进程
#browser.quit()
