import json
from random_word import RandomWords
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