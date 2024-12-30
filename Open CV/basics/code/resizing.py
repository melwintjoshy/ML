import cv2

image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\imagein.png"


img = cv2.imread(image_path)

resized_img = cv2.resize(img, (132, 214))       #(width, height)

print(f"(height, width, no. of channels) : {img.shape}")
print(f"(height, width, no. of channels) : {resized_img.shape}")

cv2.imshow('image', img)
cv2.imshow('resized', resized_img)
cv2.waitKey(0) 