import cv2
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cascade_eye = cv2.CascadeClassifier('haarcascade_eye.xml') 
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

def smile_detect(gray,frame):
    face_arr = cascade_face.detectMultiScale(gray, 1.3, 5)
    is_smiled = True if len(face_arr)>1 else False
    if is_smiled:
        for (x, y, w, h) in face_arr:
                roi_gray = gray[y:y + h, x:x + w]
                smiles = cascade_smile.detectMultiScale(roi_gray, 1.8, 20)
                is_smiled = True if len(smiles)>1 else False
    return is_smiled

src = cv2.imread("michael.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canvas = smile_detect(gray, src)
print(canvas)
