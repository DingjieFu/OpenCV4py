# 用户：夜卜小魔王
# 时间：2021/9/4 15:06

# 直方图反投影
import cv2
import numpy as np


img = cv2.imread("../image/13.jpg")
roi = img[1400:, :200]
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 计算roi的直方图
roi_hist = cv2.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# 直方图归一化并利用反传算法
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([img_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
# 用圆盘进行卷积
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)
# 应用阈值作与操作
_, thresh = cv2.threshold(dst, 50, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(img, thresh)
res = np.vstack((img, thresh, res))
cv2.namedWindow("res", cv2.WINDOW_NORMAL)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
