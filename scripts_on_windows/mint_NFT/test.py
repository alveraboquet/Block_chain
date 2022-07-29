import os
pics = [] #用于装所有 pics 文件的绝对路径

pic_dir = r"C:\Users\Terry\PycharmProjects\autopy\L2\mint_NFT\pic_sorce"
# root 表示整个路径， dirs 表示该文件夹下的子文件夹，files 表示该文件夹下的文件
for root, dirs, files in os.walk(pic_dir):
    for file in files:
        pics.append(os.path.join(root, file)) #文件的绝对路径
print(pics)
        # print(file)
      #其中os.path.splitext()函数将路径拆分为文件名+扩展名，例如os.path.splitext(“E:/lena.jpg”)将得到”E:/lena“+".jpg"。
        # if os.path.splitext(file)[1] == '.jpg':
        #     pics.append(os.path.join(root, file)) #文件的绝对路径