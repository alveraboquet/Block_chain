from randimage import get_random_image, show_array
from alive_progress import alive_bar

import matplotlib
img_size = (350,350)

with alive_bar(20, dual_line=True, title='进度条') as bar:
    for i in range(51, 71):
        img = get_random_image(img_size)  #returns numpy array
        # show_array(img) #shows the image
        savepath = '/home/parallels/ubuntu_zk/Block_chain/scripts_on_ubuntu/Alchemy/week 1/photos/'
        matplotlib.image.imsave( savepath +f"{i}.png", img)
        bar()