print("this is zk task")

import sys
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')


from functions import *
# excel_path = "/home/parallels/Documents/block_chain/sync_swap_50.xlsx"
excel_path = '/home/parallels/ubuntu_zk/Block_chain/eth1000_操作后.xlsx'
excel_start = 1
excel_which_column = "A"
# Do_Excel(excel_path, sheetname="SheetJS").plain_write(excel_start, excel_which_column, "成功")
text = Do_Excel(excel_path, sheetname="SheetJS").read(excel_start, excel_which_column)
print(text)
