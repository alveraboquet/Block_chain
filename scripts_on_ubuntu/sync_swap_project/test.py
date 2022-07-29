
# import os,inspect
# current_dir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# print("目录是：",current_dir)
# os.chdir(current_dir)
import sys
# sys.path.append('../')
sys.path.append('/home/parallels/ubuntu_op/Block_chain')

from functions import *
# excel_path = "/home/parallels/Documents/block_chain/sync_swap_50.xlsx"
excel_path = '/home/parallels/ubuntu_op/Block_chain/eth1000_操作后.xlsx'
excel_start = 4
excel_which_column = "C"
# Do_Excel(excel_path, sheetname="SheetJS").plain_write(excel_start, excel_which_column, "成功")
text = Do_Excel(excel_path, sheetname="SheetJS").read(excel_start, excel_which_column)
print(text)
