import matplotlib.pyplot as plt
import cv2 # нужно поставить себе cv2 через conda install opencv
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
    b, g, r = cv2.split(img) # по умолчанию cv2 почему-то отдает цвета в порядке BGR вместо RGB
    new_image = cv2.merge([r, g, b])
    return new_image

def save_img(name, image, exp = 'png'):
    name = '{}.{}'.format(name, exp)
    cv2.imwrite(name,image[:,:,::-1])
    print(name + " saved!")

def change_img(old, img):
    old = load_img(old)
    x = old.shape[0]
    y = old.shape[1]
    old = old.reshape(x*y, 3)
    img = img.reshape(img.shape[1], 3)
    print(old.shape, img.shape)
    for i in range(min(img.shape[0], old.shape[0]//10)):
        old[i] = img[i]
    return old.reshape(x,y,3)

def img_to_code(img):
    res = ''
    for i in img:
        if tuple(i) in d:
            res += d[tuple(i)]
        else:
            break
    return res

def convert(i):
    i = tuple(i)
    return d[i]


def code_to_img(code):
    res = []
    for i in code:
        for j in d.keys():
            if d[j] == i:
                res.append((j))
                break
    img = np.array([res])
    return img


def encode(image_name, bfcode):
    img = change_image(image_name, bfcode)
    save_img(image_name[:-4] + '_encoded', img)

def decode(img):
    return img_to_code(img = img.reshape(img.shape[0] * img.shape[1], 3))
