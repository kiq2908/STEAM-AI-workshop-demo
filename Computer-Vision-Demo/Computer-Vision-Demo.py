from cvzone.HandTrackingModule import HandDetector
#import thư viện HandTrackingModule của cvzone, một thư viện được xây dựng trên OpenCV cung cấp các công cụ để xử lý computer vision như nhận dạng bàn tay và khuôn mặt 
import cv2
#import thư viện OpenCV cho các công việc xử lý computer vision

cap = cv2.VideoCapture(0) #tính năng sử dụng nhận diện trên video thời gian thực của OpenCV
detector = HandDetector(detectionCon=0.8, maxHands=2)
#cài đặt độ chính xác (nếu độ chính xác vượt trên 80% thì chương trình sẽ nhận biết được đó là bàn tay) và số lượng bàn tay cần phát hiện (2 bàn tay)

while True: #tạo một vòng lặp vô hạn để chưởng trình chạy liên tục và xử lý liên tục các khung hình video
    success, img = cap.read() #đọc các khung hình video, biến success sẽ trả về True nếu đọc thành công và False nếu không thành công
    hands, img = detector.findHands(img)
    # Phát hiện và theo dõi bàn tay trong khung hình img sử dụng đối tượng HandDetector. Các bàn tay phát hiện được lưu vào biến hands, và khung hình với các đánh dấu các điểm đặc trưng trên bàn tay được lưu lại trong biến img
    if hands: # kiểm tra xem bàn tay đã được phát hiện hay chưa
        for hand in hands: # dùng vòng lặp duyệt qua từng bàn tay được phát hiện
            lmList = hand["lmList"] # Lấy danh sách các landmarks trên bàn tay
            bbox = hand["bbox"] # Lấy bounding box của bàn tay, bao gồm tọa độ của bb góc trên bên trái, chiểu rộng và chiều cao)
            centerPoint = hand['center'] # Lấy tọa độ điểm giữa của bàn tay
            handType = hand["type"] # Lấy kiểu bàn tay (left hoặc right)

            fingers = detector.fingersUp(hand) # Lấy danh sách các ngón tay được nhận diện khi duỗi ra
            finger_count = fingers.count(1)
            # Đếm số ngón tay được duỗi ra bằng cách đếm số lượng phần tử có giá trị 1 trong danh sách fingers do số ngón tay được duỗi ra sẽ có giá trị 1, còn số ngón tay không được duỗi ra sẽ có giá trị 0
            # finger_count sẽ bằng 3 nếu có 3 ngón tay được duỗi ra, tương ứng với 3 giá trị 1 trong danh sách fingers
            display_text = f"{handType}: {finger_count} fingers" # Tạo string hiển thị số ngón tay được duỗi ra và kiểu bàn tay
            cv2.putText(img, display_text, (bbox[0], bbox[1] - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            # cv2.putText là hàm để hiển thị text lên khung hình
            # img là khung hình ngay tại thời điểm xử lý và cần hiển thị text
            # string display_text lên khung hình img tại tọa độ (bbox[0], bbox[1] - 20) là điểm góc trên bên trái của bb với font chữ cv2.FONT_HERSHEY_SIMPLEX, kích thước font 1, màu trắng (255, 255, 255), độ đậm 2

    cv2.imshow("Image", img)
    # Hiển thị khung hình img lên cửa sổ có tên "Image", giống như hiện cửa sổ của một chương trình khác
    if cv2.waitKey(1) == ord('q'):
        break
    # để thoát chương trình, nhấn phím q

cap.release() # giải phóng tài nguyên camera để các chương trình khác có thể sử dụng
cv2.destroyAllWindows() #được sử dụng để đóng tất cả các cửa sổ đồ họa đã được tạo ra bởi OpenCV
