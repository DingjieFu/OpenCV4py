# 用户：夜卜小魔王
# 时间：2021/8/29 22:33

# 图像基本操作
# 访问像素值并修改它们 - 访问图像属性 - 设置感兴趣区域(ROI) - 分割和合并图像
import cv2
import numpy as np


def func1(image):  # 访问和修改像素值
    pixel = image[100, 100]
    print(pixel)
    blue = image[100, 100, 0]  # 仅访问蓝色通道
    print(blue)
    image[100, 100] = [255, 255, 255]  # 修改像素值
    print(pixel)
    """
    上面的方法通常用于选择数组的区域，例如前5行和后3列。
    对于单个像素访问，Numpy数组方法array.item()和array.itemset()被认为更好，但是它们始终返回标量。
    如果要访问所有B，G，R值，则需要分别调用所有的array.item()。
    """
    print(image.item(100, 100, 0))
    image.itemset((100, 100, 0), 247)
    print(image.item(100, 100, 0))


def func2(image):  # 访问图像属性
    print(image.shape)
    print(image.size)
    print(image.dtype)


def func3(image):  # 拆分与合并通道
    b, g, r = cv2.split(image)
    image = cv2.merge((b, g, r))
    b = img[:, :, 0]  # 将蓝色像素置为0


def func4():  # 边界填充
    top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
    image = cv2.imread("../image/8_2.jpg")
    # 复制法 复制最边缘的像素
    replicate = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, cv2.BORDER_REPLICATE)
    cv2.imshow("replicate", replicate)
    # 反射法 对图像中的像素在两边进行复制 如: fedcba|(abcdefgh)|hgfedcb
    reflect = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
    cv2.imshow("reflect", reflect)
    # 反射法 以最边缘像素为轴 对称 如: gfedcb|(abcdefgh)|gfedcba
    reflect_101 = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
    cv2.imshow("reflect_101", reflect_101)
    # 外包装法 如: cdefgh|(abcdefgh)|abcdefg
    wrap = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
    cv2.imshow("wrap", wrap)
    # 常量法 常数值填充
    constant = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    cv2.imshow("constant", constant)


if __name__ == '__main__':
    img = cv2.imread("../image/8.jpg")
    # func1(img)
    # func2(img)
    # func3(img)
    func4()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
