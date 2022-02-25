# 用户：夜卜小魔王
# 时间：2021/9/4 14:28

# 直方图均衡
# 直方图均衡化的概念 利用它来提高图像的对比度
import cv2
import numpy as np
import matplotlib.pyplot as plt


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def hist_equalize():  # 直方图均衡化
    img = cv2.imread("../image/9.jpg", 0)
    equ = cv2.equalizeHist(img)
    res = np.vstack((img, equ))
    cv_show("res", res)


def clahe_equalize():  # 对比度受限的自适应直方图均衡
    img = cv2.imread('../image/9.jpg', 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)
    cv_show('clahe', cl1)


if __name__ == '__main__':
    hist_equalize()
    clahe_equalize()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
