# 用户：夜卜小魔王
# 时间：2021/9/1 15:51

# 图像平滑
# 使用各种低通滤镜模糊图像 - 将定制的滤镜应用于图像（2D卷积）

import cv2
import numpy as np
import matplotlib.pyplot as plt


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def convolution_2D():  # 2D卷积
    image = cv2.imread("../image/10.jpg")
    kernel = np.ones((5, 5))/25
    dst = cv2.filter2D(image, -1, kernel)
    res = np.hstack((image, dst))
    cv_show("res", res)


def image_blurring():  # 图像模糊（图像平滑）
    image = cv2.imread("../image/10.jpg")

    # 均值滤波 平均卷积操作 (3,3)为卷积核的大小
    blur = cv2.blur(image, (3, 3))

    # 方框滤波 基本与均值滤波一致 可以选择归一化 不归一化容易越界 大于255取255
    box = cv2.boxFilter(image, -1, (3, 3), normalize=True)
    # box = cv2.boxFilter(image, -1, (3, 3), normalize=False)

    # 高斯滤波 高斯模糊的卷积核里的数值满足高斯分布 相当于更重视中间的
    gaussian = cv2.GaussianBlur(image, (3, 3), 1)

    # 中值滤波 中间值
    median = cv2.medianBlur(image, 3)

    # 双边滤波 去除噪声的同时保持边缘清晰锐利
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    res = np.hstack((image, blur, box, gaussian, median, bilateral))  # 横向拼接
    cv_show("res", res)


if __name__ == '__main__':
    # convolution_2D()
    image_blurring()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
