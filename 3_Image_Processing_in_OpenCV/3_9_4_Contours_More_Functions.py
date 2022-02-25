# 用户：夜卜小魔王
# 时间：2021/9/1 21:42

import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


