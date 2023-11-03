# import thư viện opencv
import cv2
# Mở camera mặc định
cap = cv2.VideoCapture(0)
# Xét kích thươớt cố định cho khung hình
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# Lấy backgroud frame
# Giúp camera ổn định
for i in range(10):
  _, frame = cap.read()
# Resize bằng kích thướt màng hình
frame =cv2.resize(frame,(640, 480))
# Chuyển đổi màu sang gray
gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
#background = gray
#cv2.imshow("background", background)
last_name = gray
# Hiển thị các bức ảnh
while True:
    # Đọc bức ảnh
    _, frame =cap.read()
    # Xử lý frame tu camera len
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    # Trừ frame
    abs_img = cv2.absdiff(last_name,gray)
    # gán bức ảnh trước bằng bức ảnh hiện tại
    last_name=gray
    # lọc nhiễu truyền ảnh vào
    _,img_mask =cv2.threshold(abs_img,30,255,cv2.THRESH_BINARY)
    # phát hiện chuyển động
    contours, _ =cv2.findContours(img_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # Vẽ hình chữ nhật
    for contour in contours:
    #Lọc hàm nhỏ nhỏ qua
       if cv2.contourArea(contour)<900:
        continue

    x, y, w, h= cv2.boundingRect(contour)
    cv2.rectangle(frame,(x, y),(x+w, y+h),(0,255,0),3)


    # Hiển thi lên video
    cv2.imshow("windows", frame)
    cv2.imshow("windows", img_mask)
    # Thoát khỏi vòng lặp tắt camera
    if cv2.waitKey(1) == ord('q'):
        break



