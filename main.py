import matplotlib.pyplot as plt
import cv2 #conda install opencv
import numpy as np


d = {
        (255, 0, 0): ">",  # red
        (128, 0, 0): "<",  # darkred
        (0, 255, 0): "+",  # green
        (0, 128, 0): "-",  # darkgreen
        (0, 0, 255): ".",  # blue
        (0, 0, 128): ",",  # darkblue
        (255, 255, 0): "[",  # yellow
        (128, 128, 0): "]",  # darkyellow
        (0, 255, 255): "R",  # cyan
        (0, 128, 128): "L"  # darkcyan
}


def draw_img(img, bgr=False):
    plt.figure(figsize=(10, 14))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

def load_img(path):
    img = cv2.imread(path)
    b, g, r = cv2.split(img) 
    new_image = cv2.merge([r, g, b])
    return new_image

def save_img(name, image, exp = 'png'):
    name = '{}.{}'.format(name, exp)
    cv2.imwrite(name,image[:,:,::-1])
    print(name + " saved!")

