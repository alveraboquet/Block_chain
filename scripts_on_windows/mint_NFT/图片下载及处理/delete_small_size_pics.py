import os

DirList = [
    './pic_sorce',
    ]

for path in DirList:
    print(path)
    tall = 0
    small = 0
    for filename in os.listdir(path):
        fullName = os.path.join(path, filename)
        size = os.path.getsize(fullName)
        if size < 20 * 1024:
            small = small + 1
            os.remove(fullName)
        tall = tall + 1
    print(tall, small, small/tall * 100)
