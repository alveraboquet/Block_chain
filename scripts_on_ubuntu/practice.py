from basic.functions import *
excel_path = "/home/parallels/Documents/block_chain/sync_swap_50.xlsx"

excel_start = 4
excel_which_column = "C"
Do_Excel(excel_path, sheetname="Sheet1").plain_write(excel_start, excel_which_column, "成功")
