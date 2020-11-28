# create training set
import cv2

global name
name = 1

# click picture of each frame
def pic():
    global name
    cam = cv2.VideoCapture(0+cv2.CAP_DSHOW)
    retval, frame = cam.read()
    if retval != True:
        print("Can't read frame")
    cv2.imwrite('images/img' + str(name) + '.png', frame)
    name = name + 1

# run the training set generating function
def run_train():
    while True:
        pic()
        print("Caputred Image: " + str(name))


run_train()