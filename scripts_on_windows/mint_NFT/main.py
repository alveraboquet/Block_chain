#通过IPFS软件，获得图片的CID
import os
import pyautogui
import json
from random_words import RandomWords
test_url = "http://127.0.0.1:5001/ipfs/bafybeiednzu62vskme5wpoj4bjjikeg3xovfpp4t7vxk5ty2jxdi4mv4bu/#/files"

from L2.functions import *
which_chrome = 1
wait, browser = my_chrome(which_chrome)
browser.get(test_url)
time_sleep(2, "应该已经打开网页了")

def delet_all_file(browser, wait):
    print("进入delet_all_file，准备删除已经存在的文件")
    try:
        select_all_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/main/div/section/header/div[1]/label')))
        time_sleep(1)
        browser.execute_script("arguments[0].click();", select_all_button)

        delet_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/main/div/section/div[2]/div/div[2]/button[3]')))
        time_sleep(1)
        browser.execute_script("arguments[0].click();", delet_button)

        confirm_delete_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div[2]/button[2]')))
        time_sleep(1)
        browser.execute_script("arguments[0].click();", confirm_delete_button)
        time_sleep(3, "已经删除")
    except:
        print("可能是没有文件，不需要删除")
        return 0

def import_a_pic(browser, wait, pic_path):
    print("进入 import_a_pic，准备上传一张图片")
    input_path = '//*[@id="file-input"]'
    browser.find_element_by_xpath(input_path).send_keys(pic_path)
    time_sleep(3,"上传中")

    pic_CID = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/main/div/section/div/div[1]/div/div/div/div/div/button[1]/div[2]/div[2]/div[1]/div')))
    time_sleep(1)
    your_pic_CID = pic_CID.text
    print("图片的CID是：",your_pic_CID)
    return your_pic_CID

def copy_pic_CID(browser, wait):
    print("进入 copy_pic_CID，准备上传一张图片")
    menu_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/main/div/section/div/div[1]/div/div/div/div/div/button[2]')))
    time_sleep(1)
    browser.execute_script("arguments[0].click();", menu_button)
    #
    print("选择CID")
    CID_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/main/div/div[1]/div/div[2]/div[2]/div/button[2]')))
    time_sleep(1)
    browser.execute_script("arguments[0].click();", CID_button)

    pyautogui.click()  # 当前位置单击
    pyautogui.hotkey('Ctrl', 'c') # 相当于先按下ctrl,shift,esc,再逐个释放esc,shift,ctrl
    time_sleep(6)
    pyautogui.press('enter')  # 按下并释放enter
    time_sleep(2)
    # alert = browser.switch_to.alert
    # #
    # print(alert.text)  # 打印输出 alert 的内容

    # alert.send_keys(Keys.CONTROL, 'c')
    # time_sleep(5, "等待写入剪切板")
    save_data(3, "pic_CID") #文件命名为 pic_CID.txt
    time_sleep(1, "读取剪切板内容结束")

    # time_sleep(1)
    # browser.find_element_by_xpath(alert).send_keys(Keys.ENTER)



    # # 定位到弹窗，接受
    # alert = browser.switch_to.alert
    # print(alert.text)  # 打印输出 alert 的内容
    # alert.accept()  # 针对 alert 执行 accept（接受）方法或 dismiss()方法

def edit_json_file(pic_CID):
    whole_pic_CID = f'https://ipfs.io/ipfs/{pic_CID}'
    with open('./online-json-editor.json', 'r+') as f:
        # 读取demp.json文件内容
        data = json.load(f)
        # print(data)
        # print('================')
        # print(data["image"])

        # 修改CID的值
        data["image"] = whole_pic_CID
        data["name"] = RandomWords().random_word()  # 随机一个名字
        # print('================')
        # print(data)
        with open("./new_json_file.json", 'w') as f2:
            json.dump(data, f2)  # 写入f2文件到本地
            f2.close() #打开后需要关闭，否则文件无变化，导致CID一直一样
        f.close()

def import_a_json(browser, wait):

    print("进入 import_a_json，准备上传 json 文件")
    input_path = '//*[@id="file-input"]'
    pic_path = r'C:\Users\Terry\PycharmProjects\autopy\L2\mint_NFT\new_json_file.json'
    browser.find_element_by_xpath(input_path).send_keys(pic_path)
    time_sleep(3,"上传中")
    # browser.refresh()
    # time_sleep(5, "刷新下网页，不然CID全部一样")
    json_CID = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]/div/div[1]/div[1]/main/div/section/div/div[1]/div/div/div/div/div/button[1]/div[2]/div[2]/div[1]/div')))
    time_sleep(1)
    your_json_CID = json_CID.text
    print("json的CID是：", your_json_CID)
    return your_json_CID



# copy_pic_CID(browser, wait)

#获取文件夹所有的图片

pics = [] #用于装所有 pics 文件的绝对路径
pic_dir = r"C:\Users\Terry\PycharmProjects\autopy\L2\mint_NFT\pic_sorce"
# root 表示整个路径， dirs 表示该文件夹下的子文件夹，files 表示该文件夹下的文件
for root, dirs, files in os.walk(pic_dir):
    for file in files:
        pics.append(os.path.join(root, file)) #文件的绝对路径


for i in range(0, len(pics)+1):
    print(f"第{i}个图片，总共{len(pics)}个图片")
    pic_path = pics[i]
    print(pic_path)
    # 尝试删除所有文件
    delet_all_file(browser, wait)
    # 上传图片、获取图片的CID
    pic_CID = import_a_pic(browser, wait, pic_path)
    print("你的 pic_CID = ", pic_CID)
    # 再次删除图片
    delet_all_file(browser, wait)
    # 修改json文件
    edit_json_file(pic_CID)
    # 导入json文件、获取其CID
    json_CID = import_a_json(browser, wait)
    # 保存 json 文件的CID
    save_data_to_txt(json_CID, "json_CID")
    time_sleep(3,"下一轮")

