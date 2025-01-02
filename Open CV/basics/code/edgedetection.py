import cv2
import numpy as np

image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\rono.webp"

img = cv2.imread(image_path)
blurred = cv2.GaussianBlur(img, (3, 5), 5)

#canny edge detection algorithm
img_edge = cv2.Canny(blurred, 30, 200)

#dilation - makes edges thicker
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

#erosion - makes edges thinner
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)