from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains  # 用于操作鼠标
from selenium.webdriver import ChromeOptions  #
import time, os
import logging


url = "https://ozworld.adidas.com/view-code/"
url2 = "https://www.baidu.com/"

driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
TIME_OUT = 20  # 设置显示等待的超时时间，尽量设置的长一点，考虑到网络可能缓慢
option = ChromeOptions()
# option.add_argument('--headless')#是否开启无头模式
# option.add_argument('--disable-gpu')#屏蔽浏览器引擎

option.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
option.add_experimental_option('excludeSwitches', ['enable-outomation'])  # 防止被网站识别
option.add_experimental_option('useAutomationExtension', False)
#option.add_argument('--user-data-dir=C:\\user_data_3') #用指定的浏览器进行测试

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# option.add_argument(f'user-agent={user_agent}')

browser = webdriver.Chrome(driver_path, options=option)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                        )  # 反爬

wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类
 
# 打开浏览器，并打开链接
def open_url(url):
    print(f"开始尝试打开链接：{url}")
    try:
        browser.get(url)
    except:
        print("打开url失败，自动退出并再次尝试......")
        browser.quit()
        try:
            time.sleep(2)
            browser.get(url)
        except:
            print("无法访问url链接，可能是网络故障")
            browser.quit()

open_url(url2)
time.sleep(5)