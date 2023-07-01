# Theo dõi Bàn tay

Chương trình này sử dụng thư viện `cvzone.HandTrackingModule` và `OpenCV` để nhận diện và theo dõi bàn tay trên video thời gian thực. Chương trình hiển thị số ngón tay được giơ lên và kiểu bàn tay (trái hoặc phải) trên màn hình.

## Thư viện cần cài đặt

- cvzone
- OpenCV

## Cài đặt

1. Cài đặt `cvzone` và `OpenCV` bằng cách chạy các lệnh sau trong terminal:

```
pip install opencv-python==4.7.0.72
pip install cvzone==1.5.6
```

Hoặc

```
pip install -r requirements.txt
```

## Giải thích:


Đoạn mã này sử dụng lớp HandDetector từ thư viện cvzone.HandTrackingModule để phát hiện và theo dõi bàn tay trong các khung hình video. Phương thức findHands trả về một danh sách các bàn tay được phát hiện cùng với hình ảnh đã được chú thích.

Đối với mỗi bàn tay được phát hiện, mã lấy thông tin như các đặc trưng (landmarks), tọa độ hình hộp giới hạn (bounding box), điểm trung tâm và loại bàn tay (trái hoặc phải). Sau đó, nó đếm số ngón tay được giơ lên bằng cách sử dụng phương thức fingersUp được cung cấp bởi đối tượng HandDetector.

Số ngón tay được giơ lên và loại bàn tay được hiển thị trên hình ảnh bằng cách sử dụng hàm cv2.putText. Hình ảnh đã được chú thích sẽ được hiển thị liên tục trong một cửa sổ có tên "Image" cho đến khi người dùng nhấn phím 'q' để thoát khỏi chương trình.
