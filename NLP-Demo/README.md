# Chatbot sử dụng mô hình DialoGPT

Đoạn mã này triển khai một chatbot sử dụng mô hình DialoGPT từ thư viện Transformers. Mô hình được sử dụng để tạo ra các phản hồi tự động dựa trên đoạn văn bản đầu vào từ người dùng.

## Thư viện cần cài đặt

- transformers
- torch

## Cài đặt

1. Cài đặt thư viện `transformers` và `torch` bằng cách chạy lệnh sau trong terminal:

```
pip install transformers==4.30.2
pip install torch==2.0.1
```

Hoặc

```
pip install -r requirements.txt
```

## Giải thích
Đoạn code này giới thiệu cách triển khai một chatbot trò chuyện bằng cách sử dụng mô hình ngôn ngữ DialoGPT từ thư viện Transformers. Nó thiết lập mô hình và bộ từ mã hóa, sau đó đi vào một vòng lặp trong đó chatbot tương tác với người dùng. Trong mỗi lần lặp, nó yêu cầu người dùng nhập đầu vào, mã hóa đầu vào bằng bộ từ mã hóa, ghép nối với lịch sử trò chuyện và tạo ra một câu trả lời bằng cách sử dụng mô hình. Câu trả lời được tạo ra từ mã thông báo thành văn bản và được in ra như đầu ra của chatbot. Quá trình này lặp lại năm lần, cho phép một cuộc trò chuyện đa lượt giữa người dùng và chatbot.
