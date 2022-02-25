# 用户：夜卜小魔王
# 时间：2021/9/1 17:27

# 轮廓入门
# 查找轮廓，绘制轮廓
# cv2.findContours()，cv2.drawContours()
# 为了更高的准确率 使用二值图像
# 注意：绘制轮廓要在原图像上绘制，而代码里面是在二值化后的图像上进行处理的
# 所以如果对灰度图(或二值化图)绘制轮廓 轮廓颜色将改变 会被默认执行灰度(或二值化)操作
"""
cv2.findContours(img,mode,method)
mode:轮廓检索模式
    RETR_EXTERNAL:只检索最外面的轮廓
    RETR_LIST:检索所有轮廓 并将其保存到一条链表中
    RETR_CCOMP:检索所有轮廓并将他们分为两层 顶层是各部分的外部边界 第二层是空洞的边界
    RETR_TREE:检索所有轮廓 并重构嵌套轮廓的整个层次
method:轮廓逼近方法
    CHAIN_APPROX_NONE:以Freeman链码的方式输出轮廓 所有其他方法输出多边形(顶点的序列)
    CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分 函数只保留他们的终点部分
"""

import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def contour(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # src: 输入图像  contours:轮廓信息  hierarchy:层级
    src, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 绘制轮廓 传入绘制图像 轮廓 轮廓索引 颜色模式 线条厚度
    # 注意要copy 否则drawContours()会改变原图
    res = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 2)
    cv_show("res", res)
    # 绘制某些轮廓
    cnt = contours[0]
    res2 = cv2.drawContours(image.copy(), [cnt], -1, (0, 0, 255), 2)
    cv_show("res2", res2)


def approximation(image):  # 轮廓近似方法
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, contours1, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    _, contours2, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours1[0])), print(len(contours2[0]))
    # cv2.CHAIN_APPROX_NONE 将存储所有边界点
    # cv2.CHAIN_APPROX_SIMPLE 删除所有冗余点并压缩轮廓，从而节省内存


if __name__ == '__main__':
    img = cv2.imread("../image/contours.png")
    # contour(img)
    approximation(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

