# 用户：夜卜小魔王
# 时间：2021/9/5 10:55

# 哈里斯角检测
# cv2.cornerHarris(),cv2.cornerSubPix()

import cv2
import numpy as np


def harris_opencv():  # 哈里斯角检测
    img = cv2.imread("../image/16.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_float32 = np.float32(gray)
    # cv2.cornerHarris() 其参数为：
    # img 输入图像，应为灰度和float32类型
    # blockSize 是拐角检测考虑的邻域大小(角点的大小尺寸)
    # ksize 使用的Sobel导数的光圈参数(Sobel算子中的卷积核大小)
    # k 等式中的哈里斯检测器自由参数 一般为[0.4,0.6]
    dst = cv2.cornerHarris(gray_float32, 5, 3, 0.04)
    # print(img.shape, dst.shape)
    img[dst > 0.01 * dst.max()] = (0, 0, 255)  # 筛选角点
    cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
    cv2.imshow("dst", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def harris_subpixel():
    img = cv2.imread("../image/10.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 寻找哈里斯角
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    _, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    # 寻找质心
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    # 定义停止和完善拐角的条件
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    # 绘制
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    img[res[:, 1], res[:, 0]] = [0, 0, 255]
    img[res[:, 3], res[:, 2]] = [0, 255, 0]
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    harris_opencv()
    # harris_subpixel()
    pass
