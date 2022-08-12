from functions import *

for i in range(1,10):
    CID_text = DO_TXT(r"json_CID.txt", i).read_x_line()
    print("这次用的CID_text是", CID_text)
