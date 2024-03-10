import cv2

video_path = r'C:\Users\ADMIN\Downloads\Laugh.mp4'
img_path = r'C:\Users\ADMIN\Downloads\Bella.jpg'
cap = cv2.VideoCapture(video_path)
img = cv2.imread(img_path)
# # Ve Hinh Vuong
start_point =(25, 100)
end_point = (200, 330)
#color = (0, 0, 0)
#thicknesss = 10

while cap.isOpened():
    ret, frame = cap.read()
    #frame = cv2.rectangle(frame, start_point, end_point, color, thicknesss)
    cv2.rectangle(frame, (250, 150), (450, 350), (0, 0, 0), 2)
    image_resized = cv2.resize(img, (end_point[0] - start_point[0], end_point[1] - start_point[1]))
    frame[start_point[1]:end_point[1], start_point[0]:end_point[0]] = image_resized
    cv2.putText(frame, 'Dang Tran Thien Phuc', (150, 100), fontFace= cv2.FONT_ITALIC,  fontScale= 1, color= (0, 0, 0), thickness= 3, lineType= cv2.LINE_AA, bottomLeftOrigin=False)
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()