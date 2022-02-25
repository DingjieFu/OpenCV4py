# 用户：夜卜小魔王
# 时间：2021/9/1 16:33

# 图像梯度
#  查找图像梯度,边缘
#  函数：cv2.Sobel()，cv2.Scharr()，cv2.Laplacian()

import cv2
import numpy as np
import matplotlib.pyplot as plt


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def sobel(image):  # Sobel算子
    image = cv2.imread("../image/15.jpg", 0)
    # dst = cv2.Sobel(src,ddepth,dx,dy,ksize)
    # ddepth: 图像的深度 dx,dy: 分别表示水平和垂直方向 ksize: Sobel算子的大小
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)  # 取绝对值
    cv_show("sobelx", sobelx)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    # sobely = cv2.convertScaleAbs(sobely)
    cv_show("sobely", sobely)
    # sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  # 图片融合
    # 不建议直接计算 效果不是很好
    # sobelxy = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=3)
    # cv_show("sobelxy", sobelxy)


def scharr(image):  # Scharr算子
    # dst = cv2.Scharr(src,ddepth,dx,dy) ddepth: 图像的深度 dx,dy: 分别表示水平和垂直方向
    scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
    scharrx = cv2.convertScaleAbs(scharrx)  # 取绝对值
    cv_show("scharrx", scharrx)
    scharry = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    scharry = cv2.convertScaleAbs(scharry)
    cv_show("scharry", scharry)
    # scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)  # 图片融合
    # 不建议直接计算 效果不是很好
    # scharrxy = cv2.Scharr(image, cv2.CV_64F, 1, 1)
    # cv_show("scharrxy", scharrxy)


def laplace(image):  # laplacian算子
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
    laplacian = cv2.convertScaleAbs(laplacian)
    cv_show("laplacian", laplacian)


def gradient():
    image = cv2.imread("../text_ocr/text_1.jpg", 0)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=-1)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=-1)
    plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()


def demo():
    """
    黑色到白色的过渡被视为正斜率（具有正值），而白色到黑色的过渡被视为负斜率（具有负值）
    当将数据转换为np.uint8时，所有负斜率均设为零
    如果要检测两个边缘，更好的选择是将输出数据类型保留为更高的形式，例如cv.CV_16S，cv.CV_64F
    取其绝对值，然后转换回cv.CV_8U
    """
    image = cv2.imread("../image/6.jpg", 0)
    dst_64F = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=-1)
    dst_64F_abs = np.absolute(dst_64F)
    dst_8U = np.uint8(dst_64F_abs)  # 变暗了
    cv_show("image", image)
    cv_show("dst_64F_abs", dst_64F_abs)
    cv_show("dst_8U", dst_8U)


if __name__ == '__main__':
    img = cv2.imread("../image/15.jpg", 0)
    # sobel(img)
    # scharr(img)
    # laplace(img)
    # gradient()
    demo()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

