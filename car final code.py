import cv2
import mediapipe as mp
import time
import serial

ser = serial.Serial('COM5', 9600)
temp = [0, 0]

def operations(finger):
    # if finger>0:
    #     for i in range(finger):
    #         time.sleep(0.2)
    #         ser.write(b'H')
    #         ser.write(b'L')
    #         time.sleep(0.2)

    if finger == 1:
        time.sleep(0.1)
        ser.write(b'F')
    elif finger == 2:
        time.sleep(0.1)
        ser.write(b'R')
        # time.sleep(0.1)
        # ser.write(b'Q')
    elif finger == 3:
        time.sleep(0.1)
        ser.write(b'S')
    elif finger == 4:
        time.sleep(0.1)
        ser.write(b'T')
    # elif finger == 5:
    #     time.sleep(0.1)
    #     ser.write(b'Q')
    else:
        time.sleep(0.1)
        ser.write(b'Q')

cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)

while True:
    success, image = cap.read()
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))

        for point in handList:
            cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)

        upCount = 0
        for coordinate in finger_Coord:
            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                upCount += 1
        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
            upCount += 1

        cv2.putText(image, str(upCount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (0, 255, 0), 12)
        print("Finger: ", upCount)
        temp[1] = upCount
        if temp[0]!=temp[1]:
            temp[0] = temp[1]
            operations(upCount)
    else:
        time.sleep(0.1)
        ser.write(b'Q')

    cv2.imshow("Counting number of fingers", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break