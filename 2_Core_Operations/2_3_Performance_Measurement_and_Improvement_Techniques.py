# 用户：夜卜小魔王
# 时间：2021/8/29 23:47

# 性能衡量和提升技术
# cv2.getTickCount，cv2.getTickFrequency
"""
cv2.getTickCount 函数返回从参考事件（如打开机器的那一刻）到调用此函数那一刻之间的时钟周期数
cv2.getTickFrequency 函数返回时钟周期的频率或每秒的时钟周期数
"""
import cv2
import time


# openCV衡量性能
def perf_measure():
    img1 = cv2.imread('../image/7.jpg')
    e1 = cv2.getTickCount()
    for i in range(5, 49, 2):
        img1 = cv2.medianBlur(img1, i)
    e2 = cv2.getTickCount()
    t = (e2 - e1) / cv2.getTickFrequency()
    print(t)


if __name__ == '__main__':
    # ??? 关闭优化比开启优化速度还快？
    print(cv2.useOptimized())  # 默认优化 返回True
    perf_measure()
    cv2.setUseOptimized(False)  # 关闭优化
    print(cv2.useOptimized())
    perf_measure()
