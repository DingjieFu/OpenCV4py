# 用户：夜卜小魔王
# 时间：2021/8/9 21:41

# 学习图像的几种算术运算，例如加法，减法，按位运算等。
# cv2.add，cv2.addWeighted
import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def calc():  # 图像加法
    jpg_1 = cv2.imread("../image/1.jpg")
    jpg_2 = cv2.imread("../image/2.jpg")
    jpg_1_2 = jpg_1 + 10  # 相当于对每一个像素点都 +10
    new_jpg_1 = jpg_1 + jpg_1_2 + 150  # 相当于对256取余 模运算
    new_jpg_2 = cv2.add(jpg_1, jpg_1_2 + 150)  # 超过255即取最大值255 饱和运算
    print(jpg_1[:2, :, 0])
    print("---------------------")
    print(jpg_1_2[:2, :, 0])
    print("---------------------")
    print(new_jpg_1[:2, :, 0])
    print("---------------------")
    print(new_jpg_2[:2, :, 0])


def image_mix():  # 图像融合
    jpg_2 = cv2.imread("../image/2.jpg")
    jpg_3 = cv2.imread("../image/3.jpg")
    jpg_3 = cv2.resize(jpg_3, (600, 688))  # 改变图片的大小 参数为(w,h) 注意图片shape值是(h,w)
    # cv2.imshow("resize", cv2.resize(jpg_3, (0, 0), fx=1, fy=1))  # 后面的参数为放大倍数 fx为宽 fy为长
    print(jpg_2.shape, jpg_3.shape)
    result = cv2.addWeighted(jpg_2, 0.9, jpg_3, 0.1, 0)  # x1(图片1),α(图片1权重),x2(图片2),β(图片2权重),γ(数值参数,相当于对图片数组加操作)
    cv2.imshow("mixin", result)
    cv2.namedWindow("mixin", cv2.WINDOW_FREERATIO)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def bitwise():  # 按位运算
    img1 = cv2.imread("../image/3.jpg")
    img2 = cv2.imread("../image/5.jpg")
    img2 = cv2.resize(img2, (300, 300))
    rows, cols, channels = img2.shape
    roi = img1[:rows, :cols]
    cv_show("roi", roi)
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    cv_show("mask", mask)
    cv_show("mask_inv", mask_inv)
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    cv_show("img1_bg", img1_bg)
    cv_show("img2_fg", img2_fg)

    dst = cv2.add(img1_bg, img2_fg)
    cv_show("dst", dst)
    img1[0:rows, 0:cols] = dst
    cv_show("img1", img1)


if __name__ == '__main__':
    # calc()
    # image_mix()
    bitwise()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
