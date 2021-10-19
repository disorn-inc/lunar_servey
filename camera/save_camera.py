import cv2
import numpy as np
from datetime import datetime

path = "./save/"

def set_camera(cam_num,w=640,h=480,fps=30):
    cap = cv2.VideoCapture(cam_num)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
    cap.set(cv2.CAP_PROP_FPS, fps)
    return cap

def image_resize(img, w=640, h=480):
    res = cv2.resize(img, (w, h), interpolation = cv2.INTER_AREA)
    return res

def concat(frame1, frame2):
    # concat = np.hstack((frame1, frame2))
    concat = cv2.hconcat((frame1, frame2))
    return concat

def convert_2_rgb(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return img_rgb

def create_name(path, cam_num):
    name = path + str(cam_num) + "_" + str(datetime.now()) + ".mp4"
    return name

def video_writer(name, fourcc, cap, fps=10):
    out = cv2.VideoWriter(name, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
    return out

cam_list = [0,2,4,6,8]
state_cam1 = 1
state_cam2 = 1
state_cam3 = 1
state_cam4 = 1
cap1 = set_camera(cam_num = cam_list[1])
cap2 = set_camera(cam_num = cam_list[2])
cap3 = set_camera(cam_num = cam_list[3])
cap4 = set_camera(cam_num = cam_list[4])
fourcc = cv2.VideoWriter_fourcc(*'FMP4')
name1 = create_name(path, cam_list[1])
name2 = create_name(path, cam_list[2])
name3 = create_name(path, cam_list[3])
name4 = create_name(path, cam_list[4])
out1 = video_writer(name = name1, fourcc = fourcc, cap = cap1, fps=10)
out2 = video_writer(name = name2, fourcc = fourcc, cap = cap2, fps=10)
out3 = video_writer(name = name3, fourcc = fourcc, cap = cap3, fps=10)
out4 = video_writer(name = name4, fourcc = fourcc, cap = cap4, fps=10)
while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()
    # print(ret1,ret2)
    # print(ret1, ret2)
    if ret1 and ret2 and ret3:
        print("all camera connect")
    else:
        print("some device not connected")
    if ret1:
        img_rgb1 = convert_2_rgb(frame=frame1)
        out1.write(img_rgb1)
        cv2.imshow('camera1', img_rgb1)
        state_cam1 = 1
    else:
        # name1 = path + str(cam_list[1]) + str(datetime.now()) + ".mp4"
        cap1 = set_camera(cam_num = cam_list[1])
        if state_cam1 == 1:
            name1 = create_name(path, cam_list[1])
        out1 = video_writer(name = name1, fourcc = fourcc, cap = cap1, fps=10)
        state_cam1 = 0
    if ret2:
        img_rgb2 = convert_2_rgb(frame=frame2)
        out2 .write(img_rgb2)
        cv2.imshow('camera2', img_rgb2)
        state_cam2 = 1
    else:
        # name2 = path + str(cam_list[2]) + str(datetime.now()) + ".mp4"
        cap2 = set_camera(cam_num = cam_list[2])
        if state_cam2 == 1:
            name2 = create_name(path, cam_list[2])
        out2 = cv2.VideoWriter(name2, fourcc, 10.0, (int(cap2.get(3)), int(cap2.get(4))))
        state_cam2 = 0
    if ret3:
        img_rgb3 = convert_2_rgb(frame=frame3)
        out3 .write(img_rgb3)
        cv2.imshow('camera3', img_rgb3)
        state_cam3 = 1
    else:
        # name3 = path + str(cam_list[3]) + str(datetime.now()) + ".mp4"
        cap3 = set_camera(cam_num = cam_list[3])
        if state_cam3 == 1:
            # print("---------------------------------------------------------------------------------")
            name3 = create_name(path, cam_list[3])
        out3 = video_writer(name = name3, fourcc = fourcc, cap = cap3, fps=10)
        state_cam3 = 0
    if ret4:
        img_rgb4 = convert_2_rgb(frame=frame4)
        out4.write(img_rgb4)
        cv2.imshow('camera4', img_rgb4)
        state_cam4 = 1
    else:
        # name3 = path + str(cam_list[3]) + str(datetime.now()) + ".mp4"
        cap4 = set_camera(cam_num = cam_list[4])
        if state_cam4 == 1:
            # print("---------------------------------------------------------------------------------")
            name4 = create_name(path, cam_list[4])
        out4 = video_writer(name = name4, fourcc = fourcc, cap = cap4, fps=10)
        state_cam4 = 0
    print("capture mode")
    # print(frame.shape)
    # res = image_resize(frame)
    # con = concat(frame1, frame2)
    # cv2.imshow('frame1', con)out2
    # cv2.imshow('frame2', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap1.release()
cap2.release()
cap3.release()
cap4.release()
out1.release()
out2.release()
out3.release()
out4.release()

cv2.destroyAllWindows()