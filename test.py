import cv2

# 選擇攝影機
cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read(0)
  cv2.imshow('frame', frame)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(gray, 'Hello World', (150,150), font, 1, (255, 0, 0), 5, cv2.LINE_AA)
  cv2.imshow('gray', gray)
  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()