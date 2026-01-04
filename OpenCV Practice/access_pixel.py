import cv2

img = cv2.imread("image.jfif")
h, w = int(img.shape[0]), int(img.shape[1])
R = img[100,100,2]
G = img[100,100,1]
B = img[100,100,0]
print(f"R = {R}, G = {G}, B = {B}")
print(img.shape)
print("All Pixel RGB Value")
for y in range(0,h):
    for x in range(0,w):
        R = img[y,x,2]
        G = img[y,x,1]
        B = img[y,x,0]
        print(f"R = {R}, G = {G}, B = {B}")
