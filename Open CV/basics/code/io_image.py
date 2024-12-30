import cv2

image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\imagein.png"

#read image
img = cv2.imread(image_path)

#write image (save image to device)
image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\imageout.jpg"
cv2.imwrite(image_path, img)

#visualize image  
cv2.imshow('image', img)
cv2.waitKey(0)          #this fn must be added when show function is called. Otherwise, image will be closed before we can see it properly