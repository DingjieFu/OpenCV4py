# 用户：夜卜小魔王
# 时间：2021/9/4 13:39

# 轮廓分层 hierarchy
# [Next, Previous, First_Child, Parent]
"""
1. RETR_LIST:检索所有的轮廓，但不创建任何亲子关系。在这个规则下，父轮廓和子轮廓是平等的，他们只是轮廓 第3和第4项总是-1
2. RETR_EXTERNAL:只返回极端外部标志 所有孩子的轮廓都被留下了
3. RETR_CCOMP:
4. RETR_TREE:
"""
import cv2


img = cv2.imread("../image/contours_2.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, _, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)


