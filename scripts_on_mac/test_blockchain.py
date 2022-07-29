import time

print("hello")
# 启动Chrome
from selenium import webdriver
from selenium.webdriver import ChromeOptions
opts = webdriver.ChromeOptions()

path = "/usr/local/bin/chromedriver" # chromedriver完整路径，path是重点。如果不行，试试chromedriver.exe

opts.binary_location='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' # Chrome path浏览器路径
opts.add_argument('--user-data-dir=/Users/spencer/Library/Application Support/Google/Chrome')
opts.add_argument('--start-maximized')
opts.add_argument('--disable-gpu')
opts.add_argument('--disable-desktop-notifications')
# opts.add_argument('no-startup-window') # 不激活窗口


# opts.binary_location='/Applications/New Chrome.app/Contents/MacOS/Google Chrome' # Chrome path浏览器路径
# opts.add_argument('--user-data-dir=/Users/Documents/NewChrome')


while True:
    driver = webdriver.Chrome(executable_path=path, options=opts)
    # driver.set_window_size(width=900, height=800)
    # driver.set_window_position(x=-10000, y=-200)

    driver.get('http://www.baidu.com/')  # 打开百度
    print("已经打开")
    driver.quit()
    time.sleep(2)
