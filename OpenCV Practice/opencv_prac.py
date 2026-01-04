import cv2

img = cv2.imread("image.jfif")
print(img.size) #image size
print(img.shape) # get image (height, width, channel) value, channel 3 = BGR format
print(img[120,78]) # Accessing BGR at image's 120 = y(row), 78 = x(column)

#Show image
cv2.namedWindow("Resized", cv2.WINDOW_NORMAL)
#Resized
cv2.imshow("Resized", img)
#cv2.imshow("Cat Image", img)#UnResized
cv2.waitKey(0) #Press Any button to exit
cv2.destroyAllWindows()#Closing image
"""
Resize Summary Table:
Summary Table
Method     Effect      Best For
WINDOW_AUTOSIZE  = Window matches image pixels exactly. = Small icons or low-res images.
WINDOW_NORMAL  =  Allows you to drag the window corner to shrink it.  =  Quick debugging of large images.
cv2.resize()  =  Changes the actual pixel data before display.  =  Presentations or consistent UI layouts.

2. Programmatically Resize the Image
If you want the image to always appear at a specific size (e.g., half size or a specific width), use cv2.resize().


# Scale down to 50% of original size
scale_percent = 50 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("Scaled Image", resized)
"""

#Grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray scale

print(gray.size)
print(gray.shape) #Grayscale has no channel, just (height, width)

cv2.namedWindow("Resized Window", cv2.WINDOW_NORMAL)
cv2.imshow("Resized Window", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
In maths:
(x, y)

But in NumPy / OpenCV:
(row, column)
(y, x)

Because images are stored as tables (matrices).

| Code           | Meaning            |
| -------------- | ------------------ |
| `img[0, 0]`    | Top-left pixel     |
| `img[0, 10]`   | 10 pixels right    |
| `img[10, 0]`   | 10 pixels down     |
| `img[100, 50]` | 100 down, 50 right |

"""

#Cropping

"""
Syntax: Cropping Syntax (MEMORIZE)
crop = img[y1:y2, x1:x2]

Step 1: Get shape
h, w, _ = img.shape

Step 2: Define center crop
crop = img[
    h//4 : 3*h//4,
    w//4 : 3*w//4
]


This crops:

Middle 50% height

Middle 50% width

Visual Explanation (Mental Model)

If:

height = 800
width  = 600


Then:

y from 200 → 600
x from 150 → 450


That’s the center rectangle.

Crop Using Percentages (Best Practice)
h, w, _ = img.shape

y1 = int(0.25 * h)
y2 = int(0.75 * h)
x1 = int(0.25 * w)
x2 = int(0.75 * w)

crop = img[y1:y2, x1:x2]
"""
h, w, _ = img.shape

crop = img[
    h//4:3*h//4,
    w//4:3*w//4
    ]
cv2.namedWindow("Resized Window", cv2.WINDOW_NORMAL) #Resizing Window
cv2.imshow("Resized Window", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("cropped_cat.jpg", crop) #saving

"""Better Saving Method:
success = cv2.imwrite("crop.jpg", crop)

if success:
    print("Image saved successfully")
else:
    print("Failed to save image")
"""
print(crop.size)
print(crop.shape)
print(crop[200,100,2]) #showing Pixel value for red channel at 200th row(y) and 100th column(x)

"""
OpenCV Channel Order = BGR

In OpenCV (cv2):

Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red


So:

img[y, x, 0]  # Blue
img[y, x, 1]  # Green
img[y, x, 2]  # Red
"""
