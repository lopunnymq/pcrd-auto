import cv2
import numpy as np

def read_img(img_path):
    img = cv2.imdecode(np.fromfile(img_path, dtype = np.uint8), -1)
    return img

# def rotate_screen_to_landscape:


class UIDetecter:
    @staticmethod
    def find_img(screen_shot, img_paths):
