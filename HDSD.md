
1. Nhấn Run All để chạy chương trình 
2. Chương trình sẽ in ra menu các chức năng có thể sử dụng và box để lựa chọn phía trên cùng màn hình ( yêu cầu máy đã ipynb )

----- QUẢN LÝ KHÁCH HÀNG -----
1. Thêm khách hàng
2. Sửa thông tin khách hàng
3. Xoá khách hàng
4. Tìm kiếm khách hàng
5. Hiển thị danh sách khách hàng
0. Thoát

3. Chức năng Thêm khách hàng:
Bước 1: Nhập số 1 vào thanh nhập và Enter
Bước 2: Nhập tên khách hàng, Enter
Bước 3: Nhập tuổi (phải là số nguyên), Enter
Bước 4: Nhập số điện thoại (chuỗi số hợp lệ), Enter
Bước 5: Nhập email theo định dạng chuẩn, Enter
Bước 6: Nhập tổng giá trị mua hàng (số thực), Enter
Bước 7: Chọn loại khách (loyalty hoặc casual), Enter

Nếu loyalty:
Nhập điểm tích lũy (số nguyên)
Nếu casual:
Nhập số lần mua hàng (số nguyên)

Bước 8: Hệ thống tự động sinh Customer ID (UUID)
Bước 9: Thông báo thêm thành công hoặc lỗi (nếu dữ liệu không hợp lệ)

4. Chức năng Sửa thông tin khách hàng:
Bước 1: Nhập số 2 và Enter
Bước 2: Nhập ID của khách hàng muốn sửa, Enter
Bước 3: Hệ thống kiểm tra:
Nếu không tìm thấy ID → hiển thị cảnh báo, quay lại menu chính
Nếu tìm thấy → hiển thị thông tin hiện tại
Bước 4: Lần lượt cho phép cập nhật các trường (nhấn Enter để giữ nguyên):
Tên
Tuổi (số nguyên)
Số điện thoại
Email
Tổng giá trị mua hàng
Điểm tích lũy (nếu khách hàng loyalty)
Số lần mua hàng (nếu khách hàng casual)
Bước 5: Nhập xong, hệ thống xử lý và hiển thị kết quả cập nhật

5. Chức năng xóa khách hàng
Bước 1: Nhập số 3 và Enter
Bước 2: Nhập số điện thoại của khách hàng cần xoá, Enter
Bước 3: Hệ thống tìm và:

Nếu tìm thấy → xoá và thông báo thành công
Nếu không tìm thấy → thông báo lỗi

6. Chức năng tìm kiếm khách hàng 
Bước 1: Nhập số 4 và Enter
Bước 2: Chọn phương thức tìm kiếm:

Nhập 1 để tìm theo số điện thoại
Nhập 2 để tìm theo ID

Bước 3: Nhập thông tin tương ứng, Enter
Bước 4: Hệ thống hiển thị:

Danh sách khách hàng khớp điều kiện
Hoặc thông báo không tìm thấy

7.Chức năng hiện thị danh sách khách hàng
Bước 1: Nhập số 5 và Enter
Bước 2: Chọn loại danh sách:

1: Tất cả khách hàng
2: Khách hàng loyalty
3: Khách hàng casual

Bước 3: Hệ thống liệt kê bảng thông tin:
ID, Tên, Tuổi, SĐT, Email, Tổng mua hàng, Điểm tích lũy / Số lần mua

8. Chức năng tính tổng doanh thu
Bước 1: Nhập số 6 và Enter
Bước 2: Chọn loại tổng doanh thu muốn xem

(Để trông nhấn Enter): Toàn bộ siêu thị
loyalty: Khách hàng thân thiết
casual: Khách hàng vãng lai

Bước 3 Hệ thống sẽ liệt kê loại bạn chọn và tổng tiền tương ứng

9. Chức năng tính trung bình giá trị mua hàng
Bước 1: Nhập số 7 và Enter
Bước 2 : Chọn loại muốn xem

1: Giá trị trung bình mỗi khách hàng
2: Khách hàng thân thiết
3: Khách hàng vãng lai

10. Chức năng hiện thị 3 khách hàng mua nhiều nhất
Bước 1: Nhập số 8 và Enter
Bước 2: Hệ thông sẽ liệt kê 3 khách hàng mua nhiều nhất trong danh sách các khách hàng

11. Chức năng hiển thị khách hàng nhận quà tết
Bước 1: Nhập số 9 và Enter
Bước 2: Hệ thống sẽ hiển thị những khách hàng đủ điều kiện nhận quà tết

12. Chức năng thoát chương trình
Nhập 0 và Enter → chương trình dừng, console đóng