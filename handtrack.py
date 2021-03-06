import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy=int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)

                



            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.imshow("image",img)
    key = cv2.waitKey(25) &0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
    