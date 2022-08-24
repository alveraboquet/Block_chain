from randimage import get_random_image, show_array
import matplotlib
img_size = (350,350)
for i in range(1, 141):
    img = get_random_image(img_size)  #returns numpy array
    # show_array(img) #shows the image
    savepath = './photos/'
    matplotlib.image.imsave( savepath +f"{i}.png", img)