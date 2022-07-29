# 用的文献鸟Stork做的标记
import time

from functions import *
url_cuiqiu = "https://mail.cuiqiu.com/ucenter#/"
cuiqiu_account = "13284070073"
cuiqiu_password = "cht32489"



def login_cuiqiu(browser, wait, url_cuiqiu, cuiqiu_account, cuiqiu_password):
    print("我已经进入login_cuiqiu")
    try:
        browser.get(url_cuiqiu)
        phone = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='el-input el-input-group el-input-group--prepend']//input[@class='el-input__inner']")))
        phone.send_keys(cuiqiu_account)

        password = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type='password']")))
        password.send_keys(cuiqiu_password)

        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='el-button el-button--warning el-button--medium']")))
        browser.execute_script("arguments[0].click();", confirm_button)

        print("请输入验证码，以完成登录")
        time.sleep(5)

        manage_email = confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/table/tbody/tr/td[3]/div/button[1]')))
        browser.execute_script("arguments[0].click();", manage_email)

        in_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-mail-list"]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/div/a/button')))
        browser.execute_script("arguments[0].click();", in_email)

        return 1
    except:
        return 0

def cuiqiu_search(wait, Keys, keywords):
    search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rl-sub-left"]/div/div[2]/div[1]/div/div/div/input')))
    search.send_keys(keywords)
    search.send_keys(Keys.ENTER)

def main():
    wait, browser = my_chrome()
    # browser.minimize_window()
    #########################################
    # if login_cuiqiu(browser, wait, url_cuiqiu, cuiqiu_account, cuiqiu_password) == 0:  # 如果没有打开脆球，则退出重启
    #     return 0
    login_cuiqiu(browser, wait, url_cuiqiu, cuiqiu_account, cuiqiu_password)
    a = input("请输入验证码，以完成登录")

    switch_tab_by_handle(browser, 1, 0)
    cuiqiu_search(wait, Keys, "欢迎使用Stork")
    time_sleep(5, "等待搜索结果")

    all_emails = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="rl-sub-left"]/div/div[2]/div[4]/div[1]/div/div[9]/div/div/div[3]')))
    emails_num = list(all_emails)
    print("总数是：", len(emails_num))

    for i in range(1, len(emails_num)+1):
        try_emails = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#rl-sub-left > div > div.b-message-list-wrapper > div.b-content.nano.has-scrollbar.nano-scrolllimit-bottom.scroller-shadow-bottom > div.content.g-scrollbox > div > div.ui-draggable > div > div:nth-child({i}) > div.wrapper > div.checkedParent > i')))
        time.sleep(1)
        ActionChains(browser).click(try_emails).perform()  # 模拟鼠标点

        time.sleep(1)
        ActionChains(browser).click(try_emails).perform()  # 模拟鼠标点

        actual_email = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    '//*[@id="rl-sub-right"]/div/div[2]/div/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span/span[2]')))
        print(actual_email.text)
        time.sleep(3)
    #     time_sleep(2)
    # for i in range(0, len(emails_num)):
    #     click_email = emails_num[i]
    #     print("点击", click_email)
    #     browser.execute_script("arguments[0].click();", click_email)
    #     time_sleep(2)
    #     actual_email = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rl-sub-right"]/div/div[2]/div/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span/span[2]')))
    #     print(actual_email.text)


if __name__ == '__main__':
    main()

