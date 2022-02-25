# 用户：夜卜小魔王
# 时间：2021/9/5 15:10

# SIFT算法 Scale Invariant Feature Transform
# 尺度空间定义  高斯模糊
# 多分辨率金字塔  高斯差分金字塔(DOG)
# 关键点的精确定位
# 消除边界响应

import cv2
import numpy as np


img = cv2.imread("../image/9.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 得到特征点
sift = cv2.xfeatures2d.SIFT_create()
# sift.detect()函数在图像中找到关键点 如果只想搜索图像的一部分 则可以通过掩码
kp = sift.detect(gray, None)
# cv2.drawKeyPoints()函数在关键点的位置绘制小圆圈
# 标志cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS传递给它，它将绘制一个具有关键点大小的圆，甚至会显示其方向
img = cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.namedWindow("drawKeypoints", cv2.WINDOW_NORMAL)
cv2.imshow("drawKeypoints", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 计算特征
kp, des = sift.compute(gray, kp)  # 该函数根据我们找到的关键点来计算描述符
"""
在单步骤中直接找到关键点和描述符
sift = cv.xfeatures2d.SIFT_create() 
kp, des = sift.detectAndCompute(gray,None)
"""
print(np.array(kp).shape)  # 关键点个数
print(des.shape)  # 每个关键点是128维的向量
print(des[0])
