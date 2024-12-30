import cv2

image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\imagein.png"


img = cv2.imread(image_path)

cropped_img = img[100:280, 0:250]


cv2.imshow('image', img)
cv2.imshow('cropped', cropped_img)
cv2.waitKey(0) 