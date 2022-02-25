# 用户：夜卜小魔王
# 时间：2021/8/30 0:00

# 改变色彩空间
# 将图像从一个色彩空间转换到另一个，像BGR↔灰色，BGR↔HSV等
# 创建一个应用程序，以提取视频中的彩色对象
# cv2.cvtColor，cv2.inRange

# OpenCV中有超过150种颜色空间转换方法 研究最广泛使用的,BGR↔灰色和BGR↔HSV。
#  HSV的色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]
import cv2
import numpy as np


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def check_flags():  # 查看所有色彩空间转换
    flags = [i for i in dir(cv2) if i.startswith("COLOR")]
    print(flags)


def ob_tracking():  # 对象追踪
    capture = cv2.VideoCapture("../beat.mp4")
    while True:
        # 读取帧
        _, frame = capture.read()
        # 转换颜色空间 BGR 到 HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 定义HSV中颜色的范围
        lower_blue = np.array([80, 50, 50])
        upper_blue = np.array([110, 255, 255])
        # 设置HSV的阈值使得只取所设置的颜色
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # 将掩膜和图像逐像素相加
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv_show('frame', frame)
        # cv_show('mask', mask)
        cv_show('res', res)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    capture.release()
    cv2.destroyAllWindows()


def get_hsv():
    bgr_color = np.uint8([[[90, 50, 50]]])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    print(hsv_color)


if __name__ == '__main__':
    # check_flags()
    # get_hsv()
    ob_tracking()
    pass
