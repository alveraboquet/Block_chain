import requests
import time, os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions  #

url = "http://127.0.0.1:9090/ui/#/proxies"

def main():
    print("开始转换IP")
    driver_path = os.path.abspath('.') + "\chromedriver.exe"  # driver版本要和Chrome对应
    TIME_OUT = 35  # 设置显示等待的超时时间，尽量设置的长一点，考虑到网络可能缓慢
    option = ChromeOptions()
    # option.add_argument('--headless')#是否开启无头模式
    # option.add_argument('--disable-gpu')#屏蔽浏览器引擎

    option.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
    option.add_experimental_option('excludeSwitches', ['enable-outomation'])  # 防止被网站识别
    option.add_experimental_option('useAutomationExtension', False)
    #用户2
    # option.add_argument("--user-data-dir=" + r"C:/Users/Terry/AppData/Local/Google/Chrome/User Data/Default")
    option.add_argument("--user-data-dir=" + r"C:/Users/Terry/AppData/Local/Google/Chrome/User Data/")
    # 安装小狐狸
    meta_mask_path = os.path.abspath('.') + "\metamask_10_14_1_0.crx"  #
    # option.add_extension(meta_mask_path)

    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    # option.add_argument(f'user-agent={user_agent}')

    browser = webdriver.Chrome(driver_path, options=option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {"source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"}
                            )  # 反爬
    wait = WebDriverWait(browser, TIME_OUT)  # wait是一个类

    try:
        browser.get(url)
    except:
        print("打开url失败，再次尝试......")
        browser.quit()
        try:
            time.sleep(1)
            browser.get(url)
        except:
            print("无法访问url链接，可能是网络故障")
            browser.quit()

    time.sleep(1)  # 过
    print("全局代理，展开节点")
    global_expand = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='tags-expand']")))
    global_expand = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='tags-expand']")))
    browser.execute_script("arguments[0].click();", global_expand)

    IPs = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='tags expand']/li[@class='can-click']")))
    print("节点个数",len(list(IPs)))
    #切换IP
    for i in range(1,len(list(IPs))):
        browser.execute_script("arguments[0].click();", IPs[i])
        time.sleep(1)
        print(f"现在是第{i}个")
    # for ip in IPs:
    #     print(ip)
    # # browser.execute_script("arguments[0].click();", LOOKS_GOOD)
    time.sleep(600)


    # #新建标签页，进入小狐狸
    # url2 = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
    # url2 = 'http://www.baidu.com'
    # meta_mask_url = 'window.open("{}")'.format(url2)  # js函数，此方法适用于所有的浏览器 br.execute_script(new_window)
    # browser.execute_script(meta_mask_url)
    #
    # print("已经进入小狐狸")
    # time.sleep(6000)

if __name__ == '__main__':
    main()
