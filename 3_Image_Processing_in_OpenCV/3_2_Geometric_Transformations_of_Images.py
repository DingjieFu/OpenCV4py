# 用户：夜卜小魔王
# 时间：2021/8/30 0:45

# 图像的几何变换
# 将不同的几何变换应用到图像上，如平移、旋转、仿射变换等。
# cv2.getPerspectiveTransform
# OpenCV提供了两个转换函数cv2.warpAffine和cv2.warpPerspective
# cv2.warpAffine采用2x3转换矩阵，而cv2.warpPerspective采用3x3转换矩阵作为输入。
import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def scale(image):  # 缩放
    # 首选的插值方法是cv2.INTER_AREA用于缩小，cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR用于缩放
    res1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    # 或者
    h, w = image.shape[:2]
    res2 = cv2.resize(image, (2*w, 2*h), interpolation=cv2.INTER_LINEAR)
    # print(res1 == res2)
    # cv_show("image", res)


def translation(image):  # 平移
    h, w = image.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 100]])
    dst = cv2.warpAffine(image, M, (w, h))
    cv_show("dst", dst)


def rotate(image):  # 旋转
    h, w = image.shape[:2]
    # cols-1 和 rows-1 是坐标限制
    M = cv2.getRotationMatrix2D(((w-1)/2.0, (h-1)/2.0), 60, 0.5)
    dst = cv2.warpAffine(image, M, (w, h))
    cv_show("dst", dst)


def affine():  # 仿射变换
    # 要创建2X3矩阵，需要6个方程，即三对点才能求解
    image = cv2.imread("../image/10.jpg")
    h, w, c = image.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    # cv2.circle(image, (50, 50), 10, (255, 0, 0), -1)
    # cv2.circle(image, (200, 50), 10, (0, 255, 0), -1)
    # cv2.circle(image, (50, 200), 10, (0, 0, 255), -1)
    pts2 = np.float32([[50, 50], [100, 200], [200, 100]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(image, M, (w, h))
    # cv2.circle(dst, (50, 50), 10, (255, 0, 0), -1)
    # cv2.circle(dst, (100, 200), 10, (0, 255, 0), -1)
    # cv2.circle(dst, (200, 100), 10, (0, 0, 255), -1)
    dst = np.hstack((image, dst))
    cv_show("dst", dst)


def perspective():  # 透视变换
    # 要创建3X3矩阵，需要8个方程，即4对点才能求解
    image = cv2.imread("../image/10.jpg")
    pts1 = np.float32([[50, 50], [50, 350], [350, 50], [350, 350]])
    pts2 = np.float32([[0, 0], [0, 300], [300, 0], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image, M, (300, 300))
    cv_show("dst", dst)


if __name__ == '__main__':
    img = cv2.imread("../image/7.jpg")
    # scale(img)
    # translation(img)
    # rotate(img)
    # affine()
    perspective()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
