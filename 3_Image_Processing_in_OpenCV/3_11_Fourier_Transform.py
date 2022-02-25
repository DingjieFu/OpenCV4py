# 用户：夜卜小魔王
# 时间：2021/9/4 15:20

# 傅里叶变换
# 使用OpenCV查找图像的傅立叶变换 利用Numpy中可用的FFT函数
# cv2.dft()、cv2.idft()
import cv2
import numpy as np
import matplotlib.pyplot as plt


def DFT():
    img = cv2.imread("../image/8.jpg", 0)
    img_float32 = np.float32(img)  # 输入图像必须先转换成np.float32格式

    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)  # 将低频值转移到中间位置
    # 得到灰度图能表示的形式
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    plt.subplot(121), plt.imshow(img, cmap="gray")
    plt.title("Input Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
    plt.title("Magnitude Spectrum"), plt.xticks([]), plt.yticks([])
    plt.show()


def low_pass():  # 低通滤波 只保留低频 会使图像变模糊
    img = cv2.imread("../image/8.jpg", 0)
    img_float32 = np.float32(img)
    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = img.shape[:2]
    crow, ccol = int(rows/2), int(cols/2)  # 中心位置

    # 低通滤波
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-50:crow+50, ccol-50:ccol+50] = 1

    # IDFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    plt.subplot(121), plt.imshow(img, cmap="gray")
    plt.title("Input Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap="gray")
    plt.title("Output Image"), plt.xticks([]), plt.yticks([])
    plt.show()


def high_pass():  # 高通滤波 只保留高频 会使图像细节增强
    img = cv2.imread("../image/8.jpg", 0)
    img_float32 = np.float32(img)
    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)
    # 高通滤波
    mask = np.ones((rows, cols, 2), np.uint8)
    mask[crow-50:crow+50, ccol-50:ccol+50] = 0
    # IDFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    plt.subplot(121), plt.imshow(img, cmap="gray")
    plt.title("Input Image"), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap="gray")
    plt.title("Output Image"), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    # DFT()
    # low_pass()
    high_pass()
