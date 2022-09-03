import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
hand_mesh = mp.solutions.hands.Hands(max_num_hands=1)

screen_w , screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_mesh.process(rgb_frame)
    landmarks_points = output.multi_hand_landmarks
    frame_h , frame_w , _ = frame.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id, landmark in enumerate(landmarks[7:9]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x,screen_y)
        left = [landmarks[4],landmarks[8]]
        for landmark in left:
            screen_x = screen_w / frame_w * x
            screen_y = screen_h / frame_h * y
            pyautogui.moveTo(screen_x,screen_y)
        clickVal = left[0].y - left[1].y
        if clickVal <= 0.04:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Mouse Control',frame)
    cv2.waitKey(1)
    