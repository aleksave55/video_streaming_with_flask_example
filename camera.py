import cv2
import numpy

from mss import mss
from PIL import Image

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        if success:
            print(type(image))
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

class ScreenShot(object):
    def __init__(self):
        self.sct = mss()

    def get_frame(self):
        sct_img = self.sct.grab(self.sct.monitors[0])
        pil_image = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        open_cv_image = numpy.array(pil_image)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1]#.copy()

        ret, jpeg = cv2.imencode('.jpg', open_cv_image)
        return jpeg.tobytes()