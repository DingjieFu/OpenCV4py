# 用户：夜卜小魔王
# 时间：2021/9/5 14:52

# Shi-tomas拐角检测器和益于跟踪的特征
# Shi-Tomasi拐角检测器 cv2.goodFeaturesToTrack()

import cv2
import numpy as np

img = cv2.imread("../image/16.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
通过Shi-Tomasi方法（或哈里斯角检测，如果指定）找到图像中的N个最强角 
图像应该是灰度图像 
指定要查找的角数 
指定质量级别(0,1) 该值表示每个角落都被拒绝的最低拐角质量
提供检测到的角之间的最小欧式距离
它会根据质量以降序对剩余的角进行排序 首先获取最佳拐角 丢弃最小距离范围内的所有附近拐角 返回N个最佳拐角 
"""
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)
for pt in corners[:, 0, :]:
    x, y = pt
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


