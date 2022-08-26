#修改json 文件
import json
from random_word import RandomWords
def edit_json_file(json_path, pic_CID):
    whole_pic_CID = f'https://ipfs.filebase.io/ipfs/{pic_CID}'
    with open(json_path, 'r+') as f:
        # 读取demp.json文件内容
        data = json.load(f)
        # print(data)
        # print('================')
        # print(data["image"])

        # 修改CID的值
        data["image"] = whole_pic_CID
        data["name"] = RandomWords().get_random_word()  # 随机一个名字
        # print('================')
        # print(data)
        with open(json_path, 'w') as f2:
            json.dump(data, f2)  # 写入f2文件到本地
            f2.close() #打开后需要关闭，否则文件无变化，导致CID一直一样
        f.close()
json_path = "/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/metadata.json"
edit_json_file(json_path, pic_CID_text)
