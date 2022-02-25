# 用户：夜卜小魔王
# 时间：2021/9/1 17:12

# Canny边缘检测
"""
1)使用高斯滤波器 平滑图像 滤除噪声
2)计算图像中每个像素点的梯度强度和方向
3)应用非极大值抑制(Non-Maximum Suppression) 以消除边缘检测带来的杂散响应
4)应用双阈值(Double-Threshold)检测来确定真实和潜在的边缘
5)通过抑制孤立弱边缘最终完成边缘检测
"""

import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def change_thresh(x):
    pass


img = cv2.imread("../image/13.jpg", 0)
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.createTrackbar("min_thresh", "edges", 0, 255, change_thresh)
cv2.createTrackbar("max_thresh", "edges", 0, 255, change_thresh)
"""
第一个参数是输入图像
第二个和第三个参数分别是minVal和maxVal
第三个参数是perture_size 它是用于查找图像渐变的Sobel内核的大小 默认情况下为3
最后一个参数是L2gradient，它指定用于查找梯度幅度的方程式 如果为True，则使用更精确的公式 默认情况下，它为False。
"""
while True:
    thresh1 = cv2.getTrackbarPos("min_thresh", "edges")
    thresh2 = cv2.getTrackbarPos("max_thresh", "edges")
    edges = cv2.Canny(img, thresh1, thresh2, L2gradient=True)
    cv_show("edges", edges)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
