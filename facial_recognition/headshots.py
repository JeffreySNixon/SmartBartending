import cv2

name = 'Jeffrey' #replace with your name

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = 'facial_recognition/dataset/Jeffrey/image_{}.jpg'.format(img_counter)
        #image_path = 'D:/Coding/Projects/SmartBartendingV2/facial_recognition/dataset/Jeffrey/image_{}.jpg'
        if cv2.imwrite(img_name, frame): {
            print("I Worked")
        }
        else:{
            print("fuck")}
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
