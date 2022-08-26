import sys
sys.path.append('/home/parallels/ubuntu_op/Block_chain')
sys.path.append('/home/parallels/ubuntu_zk/Block_chain')
from functions import *
excel_start_row = 20 #从excel第几行开始
write_jsonCID_to_excel_column = 'G' #结果记录到哪一列

excel_path = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/alchemy可用邮箱手动整理版.xlsx'
success_or_fail = Do_Excel(excel_path,sheetname='Sheet1').read(22, "G")
if "ipfs://" not in str(success_or_fail):
    print("没有ipfs, 需要做创建ipfs")