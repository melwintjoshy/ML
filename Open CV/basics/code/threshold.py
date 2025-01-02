import cv2


image_path = r"C:\Users\melwi\Desktop\ML\project1\Open CV\basics\handwritten.png"

img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#simple  threshold - only one threshold value
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY) #The first argument is the source image, which should be a grayscale image.
                                                                         #The second argument is the threshold value which is used to classify the pixel values. 
                                                                         #The third argument is the maximum value which is assigned to pixel values exceeding the threshold. 
                                                                         #OpenCV provides different types of thresholding which is given by the fourth parameter of the function.


#adaptive threshold - computes threshold for small regions by itself

#cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
adaptive_thresh_g = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)  

#cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
adaptive_thresh_m = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 30)  

#the last two parameters for above 2 are block size and constant respectively. 
#block size: The size of the neighborhood (a square window) considered for calculating the threshold for each pixel. It must be an odd number.
#the constant C adjusts the result to handle noise or intensity variations.


cv2.imshow('img', img)
cv2.imshow('adaptive_thresh_gaussian', adaptive_thresh_g)
cv2.imshow('adaptive_thresh_mean', adaptive_thresh_m)
cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)