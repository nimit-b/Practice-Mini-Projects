import cv2

img = cv2.imread("cropped_cat.jpg")
height = img.shape[0]
width = img.shape[1]

print(type(height), type(width))

cv2.namedWindow("Resize",cv2.WINDOW_NORMAL)
cv2.imshow("Resize", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Showing Pixel Value For Every Co-ordinate

print(img.size)
print(img.shape) #(height, width, channel)
print("Height = ",height, type(height))
print("Width = ",width, type(width))

for r in range(height):
    for c in range(width):
        print(f"Pixel Value at Coordinate({c},{r}) = {img[r, c]}")
    
