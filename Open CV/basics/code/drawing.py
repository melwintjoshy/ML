import cv2

image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\whiteboard.png"

img = cv2.imread(image_path)
print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (300, 350), (700, 200), (0, 0, 255), -1)

# circle
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 20, 200), 7)

cv2.imshow('img', img)
cv2.waitKey(0)