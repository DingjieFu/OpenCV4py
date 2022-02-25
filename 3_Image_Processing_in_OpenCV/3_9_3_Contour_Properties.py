# 用户：夜卜小魔王
# 时间：2021/9/1 20:46

# 轮廓属性
# 坚实度，等效直径，掩模图像，平均强度

import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def properties(contour):
    global img, gray
    # 1.长宽比 对象边界矩形的宽度与高度的比值
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    # 2.范围 轮廓区域与边界矩形区域的比值
    area = cv2.contourArea(contour)
    rec_area = w * h
    extent = float(area)/rec_area
    # 3.坚实度 等高线面积与其凸包面积之比
    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)
    solidity = float(area) / hull_area
    # 4.等效直径 面积与轮廓面积相同的圆的直径
    diameter = np.sqrt(4*area/np.pi)
    # 5.取向 物体指向的角度 以下方法还给出了主轴和副轴的长度
    (x, y), (MA, ma), angle = cv2.fitEllipse(contour)
    # 6.掩码和像素点
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    cv_show("mask", mask)
    pixelpoints = np.transpose(np.nonzero(mask))
    # pixelpoints = cv.findNonZero(mask)
    # 7. 最大值，最小值和它们的位置
    min_val, max_vak, min_loc, max_loc = cv2.minMaxLoc(gray, mask=mask)
    # 8.平均颜色或平均强度
    mean_val = cv2.mean(img, mask=mask)
    # print(mean_val)
    # 9.极端点 指对象的最顶部，最底部，最右侧和最左侧的点
    leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
    rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
    topmost = tuple(contour[contour[:, :, 1].argmin()][0])
    bottommost = tuple(contour[contour[:, :, 1].argmax()][0])
    for most in (leftmost, rightmost, topmost, bottommost):
        cv2.circle(img, most, 10, (0, 0, 255), -1)
    cv_show("img", img)


if __name__ == '__main__':
    img = cv2.imread("../image/contours_2.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    properties(cnt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
