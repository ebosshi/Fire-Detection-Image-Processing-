
import cv2 as cv 
import numpy as np
import smtplib

mail = False

def sendmail():
    recipient = "ebosshi@gmail.com"
    recipient = recipient.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("ebraryigitoglu96@gmail.com", 'infs mfnk plau bmma')
        server.sendmail('ebraryigitoglu96@gmail.com', recipient, "Warning! A Fire Has Been Detected!")
        print("sent to {}".format(recipient))
        server.close()
    except Exception as e: 
        print(e)


cam = cv.VideoCapture(0)

cv.namedWindow("test")

imgcounter = 0 

while True: 
    ret,frame = cam.read()
    blur = cv.GaussianBlur(frame, (15,15),0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    
    lower = [18,50,50]
    upper= [35,255,255]

    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv.inRange(hsv, lower, upper)

    output = cv.bitwise_and(frame, hsv,mask= mask)

    size = cv.countNonZero(mask)

    if int(size) > 15000: 
        print("Fire Detected.")

        if mail == False: 
            sendmail()
            mail == True


    if not ret: 
        print ("failed to grab frame")
        break 

    cv.imshow("test", output)

    k= cv.waitKey(1)
    if k%256 == 27:
        print("escape hit, closing...")
        break

