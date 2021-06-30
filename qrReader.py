import cv2
from soco import SoCo
from time import sleep 

playlist = {'S3NK4SPLAY1':'http://rpi2020.btlan/music/pjonce.mp3',
            'S3NK4SPLAY2':'http://rpi2020.btlan/music/spToday.mp3',
            }

# initialise sonos
livingRoom = SoCo('192.168.1.206')

# initalize the cam
cap = cv2.VideoCapture(0)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

print ('scanning...')

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)

    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        # for i in range(len(bbox)):
            # draw all lines
            # cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

        if data:
            print("[+] QR Code detected, data:", data)
            if data[:10] == 'S3NK4SPLAY':
                print ('playing: ' + playlist[data])
                livingRoom.play_uri(playlist[data])

                print ('waiting 10 seconds before scanning again')
                sleep(10)
                #livingRoom.stop()
                print ('scanning...')
                
            if data[:10] == 'S3NK4SSTOP':
                print ('stopping...')
                livingRoom.stop()

            #break 

    # display the result
    cv2.imshow("img", img)
    
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
