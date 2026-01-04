import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jfif")
"""
cv2.namedWindow("Resize", cv2.WINDOW_NORMAL)
cv2.imshow("Resize",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

plt.imshow(img)
plt.axis()
plt.show()


print(img.size)
print(img.shape)
height = img.shape[0]
width = img.shape[1]
print("Height: ",type(height))
print("Width: ",type(width))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.size)
print(gray.shape)

print("Blue: ",img[200,100, 0])
print("Green: ",img[200,100, 1])
print("Red: ",img[200,100, 2])

"""#Cropping img[y1:y2 , x1:x2]
y1 = int(0.25 * height)
y2 = int(0.75 * height)
x1 = int(0.25 * width)
x2 = int(0.75 * width)
crop = img[y1: y2, x1: x2]
cv2.namedWindow("Resize", cv2.WINDOW_NORMAL)
cv2.imshow("Resize",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#Using Matplotlib
crop = cv2.cvtColor(img[500: 4000, 0: 3000], cv2.COLOR_BGR2RGB)
print("Blue: ",crop[200,100, 0])
print("Green: ",crop[200,100, 1])
print("Red: ",crop[200,100, 2])
plt.imshow(crop)
plt.axis("off")
plt.show()

crop2 = img[500: 4000, 0: 3000]
print("Blue: ",crop2[200,100, 0])
print("Green: ",crop2[200,100, 1])
print("Red: ",crop2[200,100, 2])
