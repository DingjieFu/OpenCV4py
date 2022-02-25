# 用户：夜卜小魔王
# 时间：2021/8/29 16:49

# 轨迹栏作为调色板
# cv2.getTrackbarPos，cv2.createTrackbar
import cv2
import numpy as np


def onchange(x):
    pass


img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow("image")
cv2.createTrackbar("R", "image", 0, 255, onchange)
cv2.createTrackbar("G", "image", 0, 255, onchange)
cv2.createTrackbar("B", "image", 0, 255, onchange)
while True:
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    img[:] = b, g, r
    hex_b = hex(b).split("x")[-1]
    hex_g = hex(g).split("x")[-1]
    hex_r = hex(r).split("x")[-1]
    color = f"#{hex_r}{hex_g}{hex_b}".upper()
    cv2.putText(img, f"COLOR:{color}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (125, 125, 125), 1, cv2.LINE_AA)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
