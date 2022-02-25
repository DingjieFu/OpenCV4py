# 用户：夜卜小魔王
# 时间：2021/9/4 14:01

# 直方图：查找、绘制和分析
# 使用OpenCV和Numpy函数查找直方图、使用OpenCV和Matplotlib函数绘制直方图
# cv2.calcHist()，np.histogram()

import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
cv.calcHist（images，channels，mask，histSize，ranges [，hist [，accumulate]]）
images：uint8或float32类型的源图像 应放在方括号中 即[img]
channels：以方括号给出 计算直方图的通道的索引 如果输入为灰度图像则其值为[0] 对彩色图像可传递[0]，[1]或[2]各颜色通道的直方图
mask：图像掩码 完整图像的直方图指定为None 查找图像特定区域的直方图则必须为此创建一个掩码图像并将其作为掩码
histSize：表示BIN计数 需要放在方括号中 对于全尺寸通过[256]
ranges：通常为[0,256]
"""


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(name, image)


def histogram_calc():  # 计算直方图
    img = cv2.imread("../image/13.jpg", 0)
    hist_1 = cv2.calcHist([img], [0], None, [256], [0, 256])  # OpenCV绘制 速度比numpy快得多
    hist_2, bins = np.histogram(img.ravel(), 256, [0, 256])


def histogram_draw():  # 绘制直方图
    img = cv2.imread("../image/9.jpg", 0)
    plt.hist(img.ravel(), 256, [0, 256]), plt.show()
    # color = ['b', 'g', 'r']
    # for i, col in enumerate(color):
    #     hist = cv2.calcHist(img, [i], None, [256], [0, 256])
    #     plt.plot(hist, color=col)
    #     plt.xlim([0, 256])
    # plt.show()


def application_of_mask():  # 掩码
    img = cv2.imread("../image/13.jpg", 0)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:1000, 500:2000] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask), plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    histogram_draw()
    # application_of_mask()
    pass
