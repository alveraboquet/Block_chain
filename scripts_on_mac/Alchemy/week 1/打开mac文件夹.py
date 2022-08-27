import time

from pykeyboard import PyKeyboard
from pymouse import PyMouse
#模擬鍵盤找到要上傳的文件，進行上傳

def upload_file(file):
    k = PyKeyboard()
    m = PyMouse()

    # 打开访达：Command + Option + Space
    k.press_keys(['Command', 'Alternate', 'Space'])
    time.sleep(3)

    #打开搜索栏，Command+Shift+G
    k.press_keys(['Command', 'Shift', 'G'])
    time.sleep(3) #一定要加延时

    #輸入文件路徑
    # x_dim, y_dim = m.screen_size()
    # m.click(x_dim // 2, y_dim // 2, 1)
    k.type_string(file)

    #前往文件
    k.press_keys(['Return'])
    # #點擊確定進行上傳
    # k.press_keys(['Return'])
file = '/Users/spencer/PycharmProjects/Block_chain/scripts_on_mac/Alchemy/week 1/photos/1.png'
upload_file(file)
