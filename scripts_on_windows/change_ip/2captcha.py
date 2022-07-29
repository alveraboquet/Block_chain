import time,os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains #用于操作鼠标
from selenium.webdriver import ChromeOptions #用于操作鼠标
import logging
import pyperclip #用于读取剪切板

url = "https://www.google.com/recaptcha/api2/demo"

#点击网页，得到code
def test(url, user_num):
    #获取驱动的路径
    driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
    # print(driver_path)

    TIME_OUT = 30  # 设置显示等待的超时时间
    option = ChromeOptions()
    # option.add_argument('--headless')#是否开启无头模式
    # option.add_argument('--disable-gpu')#屏蔽浏览器引擎

    option.add_experimental_option('excludeSwitches', ['enable-automation'])#防止被网站识别
    option.add_experimental_option('useAutomationExtension', False)

    user_data_path = f'--user-data-dir=D:\\auto_video_projects\\xigua_video\\adidas\\{user_num}'

    print("路径是：", user_data_path)
    option.add_argument(user_data_path)  # 用指定的浏览器进行测试

    browser = webdriver.Chrome(driver_path, options=option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                            )  # 反爬
    browser.get(url)
    wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类
    time.sleep(3)#过场动画

    # cap = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-demo"]/div/div[2]')))
    # browser.execute_script("arguments[0].click();", cap)
    print('cap点击结束')
    time.sleep(6000)
    print("等待出结果")


test(url, 1)
