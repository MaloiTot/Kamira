import time
import pyautogui
import cv2
import numpy as np
import HandTrackingModule as htm
import mediapipe as mp



##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
#########################

def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt

start_init = False

prev = -1
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# noinspection PyUnresolvedReferences
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1, detectionCon=0.75)
wScr, hScr = pyautogui.size()
# print(wScr, hScr)

while True:
    end_time = time.time()
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        a1, b1 = lmList[16][1:]
        a2, b2 = lmList[20][1:]
        a3, b3 = lmList[4][1:]
        # print(x1, y1, x2, y2)
    # 3. Check which fingers are up
        fingers = detector.fingersUp()
    # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                    (255, 0, 255), 2)
    # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
        # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

        # 7. Move Mouse
        pyautogui.moveTo(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # 8. Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
        # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
        # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                            15, (0, 255, 0), cv2.FILLED)
                pyautogui.leftClick()

    # Media-player
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keyPoints)

        if not (prev == cnt):
            if not (start_init):
                start_time = time.time()
                start_init = True

            elif (end_time - start_time) > 0.2:
                if (cnt == 3):
                    pyautogui.press("up")

                elif (cnt == 4):
                    pyautogui.press("down")

                elif (cnt == 5):
                    pyautogui.press("space")

                prev = cnt
                start_init = False



        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        # 12. Display
        cv2.imshow("Image", img)
        cv2.waitKey(1)
