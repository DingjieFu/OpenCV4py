# 用户：夜卜小魔王
# 时间：2021/9/4 15:34

# 模板匹配
# 使用模板匹配在图像中查找对象
# cv2.matchTemplate()，cv2.minMaxLoc()
import cv2


def cv_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)


origin = cv2.imread("../image/8.jpg")
img = cv2.imread("../image/8.jpg", 0)
template = cv2.imread("../image/8_2.jpg", 0)
h, w = template.shape[:2]
# print("img:", img.shape, "template:", template.shape)

# 常用的匹配方法
methods = ["cv2.TM_SQDIFF", "cv2.TM_CCORR", "cv2.TM_CCOEFF", "cv2.TM_SQDIFF_NORMED",
           "cv2.TM_CCORR_NORMED", "cv2.TM_CCOEFF_NORMED"]

for i, method in enumerate(methods):
    img2 = img.copy()
    origin2 = origin.copy()
    res = cv2.matchTemplate(img2, template, method=eval(method))
    # print("res:", res.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(min_val, max_val, min_loc, max_loc)

    # 如果是平方差匹配方法 取最小值
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0]+w, top_left[1]+h)
    show = cv2.rectangle(origin2, top_left, bottom_right, (0, 0, 255), 2)
    cv_show(method, show)

# 匹配多个结果: 不指定某一特定的location 用阈值来判断匹配程度 大于阈值的都绘制出来

cv2.waitKey(0)
cv2.destroyAllWindows()
