from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.00, (width, height))
# print(time_stamp)

webcam = cv2.VideoCapture(0)
# webcam = cv2.resize()

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    frame1 = cv2.resize(frame, (220, 160), interpolation=cv2.INTER_AREA)
    fr_height, fr_width, _ = frame1.shape
    img_final[0:fr_height, 0:fr_width, :] = frame1[0:fr_height, 0: fr_width, :]
    cv2.imshow('Capture', img_final)

    # cv2.imshow('webcam', frame)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
