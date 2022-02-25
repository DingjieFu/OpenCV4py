# 用户：夜卜小魔王
# 时间：2021/9/4 14:59

# 二维直方图
"""
cv2.calcHist() 对颜色直方图需要将图像从BGR转换为HSV
对于二维直方图，其参数将进行如下修改：
channel = [0,1]，因为我们需要同时处理H和S平面。
bins = [180,256] 对于H平面为180，对于S平面为256。
range = [0,180,0,256] 色相值介于0和180之间，饱和度介于0和256之间。
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("../image/13.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist, interpolation='nearest')
plt.show()