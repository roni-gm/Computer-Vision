import cv2
import numpy as np

def gray_at_pixel(img, x, y):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray[y, x]

def hue_at_pixel(img, x, y):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv[y, x, 0]

def saturation_at_pixel(img, x, y):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv[y, x, 1]

def brightness_at_pixel(img, x, y):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv[y, x, 2]

def lightness_at_pixel(img, x, y):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    return hls[y, x, 1]