'''import cv2

def cropper(image_path: str, crop_per: int, save_img: bool, saved_img_name: str):
    img = cv2.imread(image_path)
    height = img.shape[0]
    width = img.shape[1]
    crop_percentage = crop_per / 100
    h1_per = crop_percentage * height
    h2_per = height * (1 - crop_percentage)
    w1_per = crop_percentage * width
    w2_per = width * (1 - crop_percentage)
    if crop_per <= 0 or crop_per >= 50:
       raise ValueError("crop_per must be between 1 and 49")
    if image_path is None or crop_per is None:
        raise ValueError("Image path and crop percentage must be provided.")
    if crop_per == 0 :
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Image", img)
    if crop_per >= 0 and crop_per <= 100 and save_img == False and saved_img_name == None:
        h1 = int(h1_per)
        h2 = int(h2_per)
        w1 = int(w1_per)
        w2 = int(w2_per)
        crop = img[h1:h2, w1:w2]
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Image", crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Previous Image Size: Height: {height} Width: {width}")
        print(f"Cropped Image Size: Height: {crop.shape[0]} Width: {crop.shape[1]}")
    if crop_per >= 0 and crop_per <= 100 and save_img == True:
        h1 = int(h1_per)
        h2 = int(h2_per)
        w1 = int(w1_per)
        w2 = int(w2_per)
        crop = img[h1:h2, w1:w2]
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Image", crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        success = cv2.imwrite(saved_img_name, crop)
        if success:
            print(f"Previous Image Size: Height: {height} Width: {width}")
            print(f"Cropped Image Size: Height: {crop.shape[0]} Width: {crop.shape[1]}")
            return f"Saved image as {saved_img_name} ."
        else:
            return"Not saved, check if name has the extensions '.png','.jpg' etc."
    return "Process Completed."
image = input("Enter Image Path: ")
crop_per = int(input("Enter Crop Percentage: "))
save_image = input("Want to save image(True or False): ")
save_image = True if save_image.lower() == 'true' else False

if save_image == True:
    saved_img_name = input("Enter Saved Image Name with Extension(ex: image.png): ")
    print(cropper(image, crop_per, save_image, saved_img_name))
else:
    print(cropper(image, crop_per, save_image, None))'''
import cv2
image = input("Enter Image Path: ")
image = cv2.imread(image)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", cv2.cvtColor(image, cv2.COLOR_LRGB2LUV))
cv2.waitKey(0)
cv2.destroyAllWindows()