import time, os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions  #

TIME_OUT = 20

option = ChromeOptions()
# 安装小狐狸
meta_mask_path = os.path.abspath('.') + "\metamask_10_14_1_0.crx"  #
# option.add_extension(meta_mask_path)
option.add_argument('--user-data-dir=D:\\auto_video_projects\\xigua_video\\py_selenium2')

driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
browser = webdriver.Chrome(driver_path, options=option)

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                        )  # 反爬
wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类

url = "http://www.baidu.com"
browser.get(url)
time.sleep(33)
browser.quit()
