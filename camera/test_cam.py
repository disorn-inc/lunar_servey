import cv2
import numpy as np

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

cam_list = [0,1,2,3,4]
cap1 = set_camera(cam_num = cam_list[2])
cap2 = set_camera(cam_num = cam_list[4])
while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    print(ret1,ret2)
    # print(ret1, ret2)
    if ret1 and ret2:
        print("all camera connect")
        
    print("capture mode")
    # print(frame.shape)
    # res = image_resize(frame)
    con = concat(frame1, frame2)
    cv2.imshow('frame1', con)
    # cv2.imshow('frame2', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if ret1 and ret2:
        print("all camera connect")
    else:
        print("stop capture")
        if not ret1:
            cap1 = set_camera(cam_num = cam_list[2])
        if not ret2:
            cap2 = set_camera(cam_num = cam_list[4])    
        # print("stop capture")
    
cap1.release()
cv2.destroyAllWindows()