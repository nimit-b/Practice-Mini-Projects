import cv2

img = cv2.imread("image.jfif")
pix_val = img[100,100]
print(f"Pixel value at 100th row and 100t column: {pix_val}")
print("Red = ",img[100,100,2],"Red = ",img[100,100,1],"Blue = ",img[100,100,0])
