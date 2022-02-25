# 用户：夜卜小魔王
# 时间：2021/9/1 17:21

# 图像金字塔
# cv.pyrUp()，cv.pyrDown()
# 图像金字塔、高斯金字塔、拉普拉斯金字塔
import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


def gaussian_pyramid():
    origin = cv2.imread("../image/8.jpg")
    print(origin.shape)
    cv_show("origin", origin)
    up = cv2.pyrUp(origin)  # 向上采样
    print(up.shape)
    cv_show("up", up)
    down = cv2.pyrDown(origin)  # 向下采样
    print(down.shape)
    cv_show("down", down)

    up_down = cv2.pyrDown(up)  # 先向上采样再向下采样 两次图像都有损失 比原图模糊
    cv_show("up_down", up_down)
    cv_show("origin-up_down", origin-up_down)


def laplacian_pyramid():
    origin = cv2.imread("../image/8.jpg")
    down = cv2.pyrDown(origin)
    down_up = cv2.pyrUp(down)
    l_1 = origin - down_up
    cv_show("l_1", l_1)
    pass


if __name__ == '__main__':
    # gaussian_pyramid()
    laplacian_pyramid()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
