# 用户：夜卜小魔王
# 时间：2021/8/29 16:16

# 鼠标作为画笔 创建鼠标回调函数
# cv.setMouseCallback()
""" EVENT类型
EVENT_FLAG_ALTKEY = 32		摁住Alt
EVENT_FLAG_CTRLKEY = 8		摁住Ctrl

EVENT_FLAG_LBUTTON = 1		摁住左键
EVENT_FLAG_MBUTTON = 4		摁住中键
EVENT_FLAG_RBUTTON = 2		摁住右键
EVENT_FLAG_SHIFTKEY = 16	摁住Shift

EVENT_LBUTTONDBLCLK = 7		左键双击
EVENT_LBUTTONDOWN = 1		左键击下
EVENT_LBUTTONUP = 4			左键弹起
EVENT_MBUTTONDBLCLK = 9		中键双击
EVENT_MBUTTONDOWN = 3		中键击下
EVENT_MBUTTONUP = 6			中键弹起
EVENT_MOUSEHWHEEL = 11		滚动条向左，flags>0。向右，flags<0
EVENT_MOUSEMOVE = 0			鼠标移动
EVENT_MOUSEWHEEL = 10		滚动条向上，flags>0。向下，flags<0
EVENT_RBUTTONDBLCLK = 8		中键双击
EVENT_RBUTTONDOWN = 2		中键击下
EVENT_RBUTTONUP = 5			中键弹起
"""

import cv2
import numpy as np


def check_events():  # 查看所有鼠标回调事件类型
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


def callback(event, x, y, flags, param):
    global is_draw, x0, y0
    if event is cv2.EVENT_FLAG_LBUTTON:  # 只有先单击左键才能绘图 并确定初始点
        is_draw = ~is_draw
        x0, y0 = x, y
    elif event is cv2.EVENT_MOUSEMOVE:
        if is_draw:
            x1, y1 = x, y
            cv2.rectangle(img, (x0, y0), (x1, y1), (125, 50, 125), -1)
    elif event is cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (0, 0), img.shape[:2], 0, -1)
    pass


is_draw = False
x0, y0 = -1, -1
img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", callback)
while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
