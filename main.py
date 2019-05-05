import matplotlib.pyplot as plt
import cv2

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