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

url = "https://ozworld.adidas.com/view-code/"
url2 = "https://www.baidu.com"

# 保存剪切板数据
def save_data():
    time.sleep(4)  # 给点延时，剪切板正在写入
    code = pyperclip.paste()
    print(f"我是复制的内容：{code}")
    with open('./code.txt', 'a', encoding='utf-8') as file:
        file.write(f'{code}\n')
        file.close()

#点击网页，得到code
def get_code():
    #获取驱动的路径
    driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
    # print(driver_path)

    TIME_OUT = 30  # 设置显示等待的超时时间
    option = ChromeOptions()
    # option.add_argument('--headless')#是否开启无头模式
    # option.add_argument('--disable-gpu')#屏蔽浏览器引擎

    option.add_experimental_option('excludeSwitches', ['enable-automation'])#防止被网站识别
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(driver_path, options=option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                            )  # 反爬

    browser.get(url)
    wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类
    time.sleep(3)#过场动画

    # 第一步：等待cookie按钮出现，并点击
    try:
        COOKIES = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class ='NormalButton_NormalButton__qCZ_k CookieBanner_cookieButton__w9EeV NormalButton_secondary__dqyth']")))
        browser.execute_script("arguments[0].click();", COOKIES)
        print('cookie点击结束')
    except:
        #再试一次
        try:
            COOKIES = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "//button[@class ='NormalButton_NormalButton__qCZ_k CookieBanner_cookieButton__w9EeV NormalButton_secondary__dqyth']")))
            browser.execute_script("arguments[0].click();", COOKIES)
            print('cookie点击结束')
        except:
            print('cookie点击失败了')
            browser.quit()


    time.sleep(3)  # 过场动画
    # 第二步：等待ENTER按钮出现，并点击
    try:
        ENTER = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']/div[@class='NormalButton_textContainer__ytds4']")))
        ENTER = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']/div[@class='NormalButton_textContainer__ytds4']")))
        # time.sleep(2)#延时
        browser.execute_script("arguments[0].click();", ENTER)
        print('ENTER点击结束')
    except:
        #再试一次
        try:
            ENTER = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                 "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']/div[@class='NormalButton_textContainer__ytds4']")))
            ENTER = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']/div[@class='NormalButton_textContainer__ytds4']")))
            # time.sleep(2)#延时
            browser.execute_script("arguments[0].click();", ENTER)
            print('ENTER点击结束')
        except:
            print('ENTER点击失败了')
            browser.quit()
            

    time.sleep(3) #过场动画

    # 第三步：等待GO按钮出现，并点击
    try:
        GO = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
        GO = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
        # GO.click()
        browser.execute_script("arguments[0].click();", GO)
        print('GO点击结束')
    except:
        try:
            GO = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                              "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
            GO = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                        "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
            # GO.click()
            browser.execute_script("arguments[0].click();", GO)
            print('GO点击结束')
        except:
            print("GO点击失败")
            browser.quit()

    time.sleep(3)  # 过场动画
    #点击 6 个问题
    for i in range(1, 8):
        try:
            #用返回按钮做定位
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='Header_btn__5X1QK Header_btnStartOver__W5nL_']")))
            back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Header_btn__5X1QK Header_btnStartOver__W5nL_']")))
            print(f"处理问题{i}，相对按钮已找到".format(i))
            #问题1。等待出现TAP AND HOLD
            time.sleep(6) #注意这里时间设长点，过场动画
            # ActionChains(browser).move_to_element_with_offset(back_button, 480, 80).context_click().perform()
            # time.sleep(1)
            ActionChains(browser).move_to_element_with_offset(back_button, 480, 120).context_click().perform()
            time.sleep(1)
            ActionChains(browser).move_to_element_with_offset(back_button, 480, 150).click().perform()
            time.sleep(1)
            # ActionChains(browser).move_to_element_with_offset(back_button, 480, 180).context_click().perform()
            # time.sleep(1)
            # ActionChains(browser).move_to_element_with_offset(back_button, 480, 280).context_click().perform()
            # time.sleep(1)
            # ActionChains(browser).move_to_element_with_offset(back_button, 480, 380).context_click().perform()
            # time.sleep(1)
            ActionChains(browser).move_to_element_with_offset(back_button, 480, 480).double_click().perform()
            time.sleep(1)
            ActionChains(browser).move_to_element_with_offset(back_button, 480, 580).double_click().perform()
            time.sleep(1)
            # ActionChains(browser).move_to_element_with_offset(back_button, 400, 1).click().perform()
        except:
            print("点击问题失败")
            browser.quit()
            break
        #点击NEXT
        try:
            NEXT = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
            NEXT = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
            browser.execute_script("arguments[0].click();", NEXT)
            print(f'问题{i}结束，已经点击NEXT'.format(i))
        except:
            #再试点击一下NEXT
            try:
                NEXT = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
                NEXT = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_secondary__dqyth']")))
                browser.execute_script("arguments[0].click();", NEXT)
                print(f'问题{i}结束，已经点击NEXT'.format(i))
            except:
                print("NEXT点击失败")
                browser.quit()
            time.sleep(1)  # 过场动画

    time.sleep(8) #过场动画
    # 等待出现 LOOKS GOOD
    try:
        LOOKS_GOOD = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']")))
        LOOKS_GOOD = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']")))
        browser.execute_script("arguments[0].click();", LOOKS_GOOD)
    except:
        try:
            LOOKS_GOOD = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                      "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']")))
            LOOKS_GOOD = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                "//button[@class='NormalButton_NormalButton__qCZ_k BottomButtonBucket_button__DvVD1 NormalButton_primary__Th_Sh']")))
            browser.execute_script("arguments[0].click();", LOOKS_GOOD)
        except:
            print("LOOKS GOOD点击失败")
            browser.quit()

    # 等待出现 COPY CODE，保存到文件
    time.sleep(2)  # 过场动画
    try:
        COPY_CODE = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='CodeViewer_buttonContainer__6C6Y7']/button[2]")))
        COPY_CODE = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='CodeViewer_buttonContainer__6C6Y7']/button[2]")))
        browser.execute_script("arguments[0].click();", COPY_CODE)
        save_data()

    except:
        try:
            COPY_CODE = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='CodeViewer_buttonContainer__6C6Y7']/button[2]")))
            COPY_CODE = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='CodeViewer_buttonContainer__6C6Y7']/button[2]")))
            browser.execute_script("arguments[0].click();", COPY_CODE)
            save_data()
        except:
            print("COPY CODE点击失败")
            browser.quit()

    browser.quit()


while True:
    try:
        get_code()
    except:
        get_code()