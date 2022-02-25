# 用户：夜卜小魔王
# 时间：2021/9/1 13:32

# 图像阈值
# 简单阈值，自适应阈值和Otsu阈值。
# 函数cv2.threshold和cv2.adaptiveThreshold

"""
ret,dst = cv2.threshold(src,threshold,maxvalue,type)
ret: 使用的阈值
src: 输入图 只能输入单通道 通常为灰度图
dst: 输出图
threshold: 阈值
maxvalue: 当像素值超过(或小于)阈值 根据type的类型来决定赋值
type: 二值化操作的类型 主要包含五种
cv2.THRESH_BINARY: 超过阈值部分取maxvalue 否则取0
cv2.THRESH_BINARY_INV: THRESH_BINARY的反转
cv2.THRESH_TRUNC: 大于阈值设置为阈值 否则不变
cv2.THRESH_TOZERO: 大于阈值的不变 否则设置为0
cv2.THRESH_TOZERO_INV: THRESH_TOZERO的反转
"""
import cv2
import matplotlib.pyplot as plt


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def thresh():  # 全局阈值
    image = cv2.imread("../image/2.jpg", 0)
    method = ["cv2.THRESH_BINARY", "cv2.THRESH_BINARY_INV", "cv2.THRESH_TRUNC",
              "cv2.THRESH_TOZERO", "cv2.THRESH_TOZERO_INV"]
    _, dst1 = cv2.threshold(image, 127, 255, eval(method[0]))
    _, dst2 = cv2.threshold(image, 127, 255, eval(method[1]))
    _, dst3 = cv2.threshold(image, 127, 255, eval(method[2]))
    _, dst4 = cv2.threshold(image, 127, 255, eval(method[3]))
    _, dst5 = cv2.threshold(image, 127, 255, eval(method[4]))
    images = [image, dst1, dst2, dst3, dst4, dst5]
    titles = ["origin"] + method
    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def adaptive_thresh():  # 自适应阈值
    # 如果图像在不同区域具有不同的光照条件 自适应阈值阈值化可以提供帮助
    # 方法cv2.adaptiveThreshold还包含三个输入参数：
    # adaptiveMethod决定阈值是如何计算的：
    # cv2.ADAPTIVE_THRESH_MEAN_C:阈值是邻近区域的平均值减去常数C。
    # cv2.ADAPTIVE_THRESH_GAUSSIAN_C:阈值是邻域值的高斯加权总和减去常数C。
    # BLOCKSIZE确定附近区域的大小
    # C是从邻域像素的平均或加权总和中减去的一个常数。
    image = cv2.imread("../image/13.jpg", 0)
    _, dst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv_show("dst", dst)
    dst_ = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
    cv_show("dst_", dst_)


def Otsu():  # 二值化
    image = cv2.imread("../image/contours.png", 0)
    _, dst1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    _, dst2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, dst3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_BINARY)
    # images = [image, 0, dst1, image, 0, dst2, blur, 0, dst3]
    # titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
    #           'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
    #           'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
    # for i in range(3):
    #     plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    #     plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    #     plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    #     plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    #     plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    #     plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    # plt.show()
    cv_show("dst1", dst1)
    cv_show("dst2", dst2)
    cv_show("dst3", dst3)
    pass


if __name__ == '__main__':
    # thresh()
    # adaptive_thresh()
    Otsu()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

