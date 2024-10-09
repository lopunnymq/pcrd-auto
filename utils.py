import cv2
import numpy as np

def read_img(img):
    return cv2.imread(img, cv2.IMREAD_COLOR)

# Rotate the screen if in portrait mode
def rotate_screen_to_landscape(device):
    orientation = device.orientation

    if orientation == "natural":
        device.set_orientation("l")

class UIDetecter:

    @staticmethod
    def detect_imgs(screen_shot, imgs):
        # Range the images
        for img in imgs:
            # Read the image to detect
            t = read_img(img)