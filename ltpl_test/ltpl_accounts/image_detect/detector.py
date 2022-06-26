import cv2
image = cv2.imread("michael.jpg")
print(image)
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
faces = cascade_face.detectMultiScale(image, 1.3, 5)
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
smiles  = smile_cascade.detectMultiScale(image, scaleFactor = 1.8, minNeighbors = 20)

print(smiles,"smiles")
for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 255,0), 5)
            if len(smiles>1):
                print("yes")
            else:
                print("No")


cv2.imshow("Smile Detected", image)



cv2.waitKey(0)
cv2.destroyAllWindows()
