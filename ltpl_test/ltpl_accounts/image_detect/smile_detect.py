import cv2
cascade_face = cv2.CascadeClassifier('F:\\LTPL\\ltpl_test\\ltpl_accounts\\image_detect\\haarcascade_frontalface_default.xml') 
cascade_smile = cv2.CascadeClassifier('F:\\LTPL\\ltpl_test\\ltpl_accounts\\image_detect\\haarcascade_smile.xml')

def smile_detect(img):
    # img = cv2.imread("michael.jpg")
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_arr = cascade_face.detectMultiScale(img,1.1, 4)
    is_smiled = False
    for (x, y, w, h) in face_arr:
        roi_img = img[y:y + h, x:x + w]
        smile_arr = cascade_smile.detectMultiScale(roi_img, 1.8, 20)
        is_smiled = True if len(smile_arr)>=1 else False
    return is_smiled
