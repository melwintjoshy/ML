import cv2

#read video
video_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\videoin.mp4"
video = cv2.VideoCapture(video_path)

#visualize video
ret = True 

while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

#free memory 
video.release()
cv2.destroyAllWindows()