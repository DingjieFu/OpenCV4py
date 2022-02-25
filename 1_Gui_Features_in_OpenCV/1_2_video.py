# 用户：夜卜小魔王
# 时间：2021/8/9 17:19

# 1_2 视频入门
import cv2


def cv_video():
    video = cv2.VideoCapture("../beat.mp4")  # 读取视频
    if video.isOpened():  # 判断是否读取成功
        open_, frame = video.read()  # 对视频的每一帧进行读取 返回两个参数 第一个为bool变量 第二个为图片的矩阵
    else:
        open_ = False
        print("请检查文件是否存在！")
    while open_:
        ret, frame = video.read()
        if frame is None:
            break
        if ret is True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转为灰度图
            cv2.namedWindow("result", cv2.WINDOW_FREERATIO)  # 可以自由切换窗口大小
            cv2.imshow("result", gray)
            if cv2.waitKey(10) & 0xFF == 27:  # 每十毫秒切下一张 或按ESC直接退出(ascii码)
                break
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cv_video()

