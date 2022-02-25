# 用户：夜卜小魔王
# 时间：2021/8/9 15:27

# 1_1 图像入门
"""
cv2.imread(filename, flags)
第二个参数是一个标志，它指定了读取图像的方式。
cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
cv.IMREAD_GRAYSCALE：以灰度模式加载图像
cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
除了这三个标志，可以分别简单地传递整数1、0或-1。
"""
import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_FREERATIO)
    cv2.imshow(name, image)
    cv2.waitKey(0)  # 毫秒
    cv2.destroyAllWindows()


def read_img():  # 图像读取与显示
    # image = cv2.imread(r"C:\Users\86183\Pictures\desktop\lofi\1.jpg")
    image = cv2.imread(r"C:\Users\86183\Pictures\desktop\lofi\1.jpg", cv2.COLOR_BGR2BGRA)  # 灰度图
    print(image)
    print(image.shape)  # 维度信息
    print(type(image))  # 格式信息
    print(image.size)  # 像素点个数
    print(image.dtype)
    cv_show("picture", image)
    cv2.imwrite("image/1.jpg", image)


if __name__ == '__main__':
    read_img()
