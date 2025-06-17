# Diễn giải Vision Transformer: Cải thiện biểu đồ kích hoạt lớp ở mỗi Head bằng điểm tin cậy dựa vào phương pháp biến đổi hình ảnh đầu vào

Đây là phần triển khai GitHub của phương pháp ScoreAGC.

## Mô tả

Vision Transformer (ViT) là một mô hình phổ biến trong thị giác máy tính nhờ vào kiến trúc đặc biệt, sử dụng cơ chế tự chú ý (self-attention) để trích xuất đặc trưng hiệu quả nhằm đưa ra dự đoán chính xác. Với hiệu năng cao như vậy, việc hiểu rõ các đặc trưng mà mô hình dựa vào để đưa ra quyết định là vô cùng quan trọng. Nghiên cứu này đề xuất một phương pháp trực quan hóa các đặc trưng được trích xuất bởi ViT bằng cách xác định các Bản đồ Kích hoạt theo Lớp (CAMs) tại từng head trong module self-attention. Chúng tôi đánh giá mức độ quan trọng của từng CAM và tổng hợp chúng lại để tạo ra biểu diễn CAM cuối cùng. Ngoài ra, chúng tôi sử dụng các chỉ số đánh giá như *Localization metrics* và *Faithfulness metrics* để kiểm tra xem phương pháp giải thích của chúng tôi có thực sự cung cấp những hiểu biết ý nghĩa về quá trình ra quyết định của mô hình hay không.

## Kaggle

Tất cả các thí nghiệm được thực hiện trên nền tảng Kaggle.

Để chạy trên Kaggle, bạn cần thực hiện các bước sau:

1. Tải về hai tập tin "ILSVRC2012\_img\_val.tar" và "ILSVRC2012\_devkit\_t12.tar.gz" từ trang [Imagenet](https://www.image-net.org).

2. Tải hai tập tin này lên Google Drive cá nhân của bạn.

3. Bật chế độ chia sẻ và sao chép ID của hai tập tin này.

4. Dán ID vào notebook của chúng tôi trên Kaggle là bạn có thể bắt đầu.

**Đánh giá khả năng định vị (Localization)**: [liên kết](https://www.kaggle.com/code/nientrandai/localization-evaluation)

**Đánh giá chèn/xóa (Insertion Deletion)**: [liên kết](https://www.kaggle.com/code/nientrandai/insertion-deletion-evaluation)

**Đánh giá độ tin cậy (Faithfulness)**: [liên kết](https://www.kaggle.com/code/nientrandai/faithfulness-evaluation)

**Hiển thị bản đồ chú ý (Saliency maps)**: [liên kết](https://www.kaggle.com/code/nientrandai/display-saliency-map)

📌 Bạn có thể lưu trữ các bản đồ saliency/heatmaps của các phương pháp XAI để sử dụng sau bằng cách lưu chúng lên Google Drive và sử dụng ID của chúng trong notebook Kaggle của chúng tôi.

## Tham khảo GitHub

* Xin gửi lời cảm ơn đặc biệt đến các kho GitHub sau đã hỗ trợ cho quá trình đánh giá và tham khảo của chúng tôi:

[Attention Guided CAM: Giải thích trực quan Vision Transformer được dẫn dắt bởi Self-Attention](https://github.com/LeemSaebom/Attention-Guided-CAM-Visual-Explanations-of-Vision-Transformer-Guided-by-Self-Attention)

[Giải thích và đánh giá Vision Transformer: Nghiên cứu thực nghiệm chuyên sâu](https://github.com/ValentinCord/TFE_XAI_ViT/tree/main)

[Giải thích luồng thông tin bên trong Vision Transformer bằng cách sử dụng chuỗi Markov](https://github.com/XianrenYty/Transition_Attention_Maps)

* Chi tiết cách sử dụng:

Chúng tôi đã clone các kho GitHub này và triển khai phương pháp của mình bên trong chúng. Ngoài ra, chúng tôi cũng sử dụng các đoạn mã có sẵn trong đó để hỗ trợ đánh giá các chỉ số.

* Tham khảo các GitHub sau để xem chi tiết phần triển khai của ScoreAGC (tham khảo phần README để biết hướng dẫn chi tiết):

Đánh giá Localization: [liên kết](https://github.com/trandainien1/better_agc_ubuntu)

Đánh giá Insertion/Deletion: [liên kết](https://github.com/trandainien1/tam)

Đánh giá Faithfulness: [liên kết](https://github.com/trandainien1/quantus)
