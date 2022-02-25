# 用户：夜卜小魔王
# 时间：2021/9/1 16:08

# 形态学转换
# 学习不同的形态学操作，例如侵蚀，膨胀，开运算，闭运算等。
# 将看到不同的功能，例如：cv2.erode(),cv2.dilate(), cv2.morphologyEx()等。
import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def erode(image):  # 腐蚀操作
    kernel = np.ones((10, 10), np.uint8)  # 卷积核
    erosion = cv2.erode(image, kernel, iterations=1)  # 腐蚀操作 iterations为迭代次数
    cv_show("erosion", erosion)


def dilate(image):  # 膨胀操作
    kernel = np.ones((5, 5), np.uint8)  # 卷积核
    erosion = cv2.erode(image, kernel, iterations=3)  # 膨胀操作 iterations为迭代次数
    dilation = cv2.dilate(erosion, kernel, iterations=3)
    cv_show("dilation", dilation)


def morph_open(image):  # 开运算 先腐蚀再膨胀
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=3)
    cv_show("opening", opening)


def morph_close(image):  # 闭运算 先膨胀再腐蚀
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv_show("closing", closing)


def morph_gradient(image):  # 形态学梯度=膨胀-腐蚀 得到轮廓
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel, iterations=5)
    cv_show("gradient", gradient)


def top_hat(image):  # 顶帽：原始输入-开运算结果
    kernel = np.ones((5, 5), np.uint8)
    tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel, iterations=3)
    cv_show("tophat", tophat)


def black_hat(image):  # 黑帽：闭运算结果-原始输入
    kernel = np.ones((5, 5), np.uint8)
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel, iterations=3)
    cv_show("blackhat", blackhat)


def structure_ele():  # 结构元素 矩形/椭圆形/圆形的内核
    rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    print(rect), print(ellipse), print(cross)


if __name__ == '__main__':
    img = cv2.imread("../image/5.jpg")
    # cv_show("img", img)
    # erode(img)
    # dilate(img)
    # morph_open(img)
    # morph_close(img)
    # morph_gradient(img)
    # top_hat(img)
    # black_hat(img)
    structure_ele()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

