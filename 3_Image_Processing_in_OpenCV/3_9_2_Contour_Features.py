# 用户：夜卜小魔王
# 时间：2021/9/1 17:47

# 图像特征
# 找到轮廓的不同特征，例如面积，周长，质心，边界框

import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def features(contour):
    global img
    # 1.特征矩
    M = cv2.moments(contour)  # 所有计算出的矩值的字典
    # print(M)
    cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])  # 质心坐标
    # 2.轮廓面积
    area = cv2.contourArea(contour)  # 等于M['m00']
    # 3.轮廓周长
    perimeter = cv2.arcLength(contour, True)
    # 4.轮廓近似
    epsilon = 0.01*cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    # dst = cv2.drawContours(img.copy(), [approx], -1, (0, 0, 255), 3)
    # cv_show("dst", dst)
    # 5.轮廓凸包
    hull = cv2.convexHull(contour)
    # 6.检查凸度
    k = cv2.isContourConvex(contour)
    # 7.边界矩形
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)  # 直角矩形
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)  # 最小面积矩形
    # 最小闭合三角形
    _, triangle = cv2.minEnclosingTriangle(contour)
    pts = np.int32(triangle)  # 注意设成整数
    cv2.polylines(img, [pts], True, (255, 0, 255), 5)
    # 8.最小闭合圆
    (x, y), radius = cv2.minEnclosingCircle(contour)
    (x, y), radius = (int(x), int(y)), int(radius)
    cv2.circle(img, (x, y), radius, (0, 200, 200), 3)
    # 9.拟合椭圆
    (x, y), (axe1, axe2), angle = cv2.fitEllipse(contour)
    (x, y), (axe1, axe2), angle = (int(x), int(y)), (int(axe1), int(axe2)), int(angle)
    cv2.ellipse(img,  (x, y), (axe1, axe2), angle, 0, 360, (255, 255, 0), 2)
    # 10.拟合直线
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv2.line(img, (cols - 1, righty), (0, lefty), (150, 200, 150), 2)

    cv_show("img", img)


if __name__ == '__main__':
    img = cv2.imread("../image/contours_2.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    features(cnt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
