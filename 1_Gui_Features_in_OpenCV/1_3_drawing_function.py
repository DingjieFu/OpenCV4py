# 用户：夜卜小魔王
# 时间：2021/8/29 16:04

# 1_3 绘图功能
# cv2.line()，cv2.circle()，cv2.rectangle()，cv2.ellipse()，cv2.putText()
import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)  # 定义一张全黑图像

cv2.line(img, (0, 0), img.shape[:2], (0, 0, 255), 1)
cv2.circle(img, (250, 250), 50, (0, 255, 0), 1)
cv2.rectangle(img, (0, 0), img.shape[:2], (255, 0, 0), 2)
cv2.ellipse(img, (250, 250), (100, 50), 0, 0, 360, (100, 100, 100), 1)
pts = np.array([[100, 50], [200, 300], [400, 200], [400, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
cv2.putText(img, "OpenCV", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
