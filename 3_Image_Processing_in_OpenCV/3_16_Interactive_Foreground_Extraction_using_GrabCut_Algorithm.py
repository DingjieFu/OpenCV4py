# 用户：夜卜小魔王
# 时间：2021/9/4 22:12

# 交互式前景提取使用GrabCut算法

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../image/9.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 1000, 1000)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

