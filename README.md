# LTUDKT_QLKH
Bài tập nhóm 7 môn Lập trình ứng dụng kỹ thuật

Đề 5: Lập trình OOP với ngôn ngữ Python để xây dựng Hệ thống quản lý khách hàng tại siêu thị. Sau đó viết bộ testcase với code đã viết (Tối thiểu 30 trường hợp).
Lưu ý: Nhóm sinh viên tự lựa chọn phương thức xây dựng hệ thống quản lý phù hợp với năng lực của các thành viên trong nhóm (ví dụ: xây dựng web, lập trình console, ...)
Trong hệ thống quản lý khách hàng của siêu thị mỗi khách hàng được phân loại: khách hàng thân thiết hoặc khách hàng vãng lai. Cần quản lý các thông tin sau:
- Thông tin chung: Mã khách hàng. Tên khách hàng. Số điện thoại Email; 
- Đối với khách hàng thân thiết: Số điểm tích lũy, Tổng giá trị mua hàng 
- Đối với khách hàng vãng lai: Số lần mua hàng. Tổng giá trị mua hàng

Yêu cầu 1: Xây dựng các lớp để quản lý khách hàng:
Lớp Customer (lớp cha): Chứa các thông tin chung của khách hàng.
Lớp LoyalCustomer (kế thừa lớp Customer): Quản lý thông tin khách hàng thân thiết. Lớp CasualCustomer (kế thừa lớp Customer): Quản lý thông tin khách hàng vãng lai. 
# Đã xong

Yêu cầu 2: Xây dựng lớp ManageCustomer với các chức năng:-
- Thêm mới khách hàng: Phân loại và thêm khách hàng vào hệ thống (trong đó thông tin Mã khách hàng và Số điện thoại là bắt buộc)
- Sửa thông tin khách hàng. Cập nhật thông tin khách hàng dựa trên mã khách hàng.
- Cập nhật thông tin khách hàng. Đối với khách hàng vãng lai có tổng giá trị mua hàng lớn hơn 2.000.000 đồng sẽ được cập nhật là khách hàng thân thiết.
- Xóa khách hàng: Xóa khách hàng khỏi hệ thống.
- Tìm kiếm khách hàng: Tìm kiếm qua mã khách hàng hoặc tên khách hàng hoặc số điện thoại.
- Hiển thị danh sách khách hàng: Hiển thị danh sách theo phân loại (thân thiết/vãng lai). 
- Tính tổng doanh thu:
+ Tổng hợp doanh thu của toàn bộ siêu thị.
+ Tổng doanh thu của từng loại khách hàng.
- Tính trung bình giá trị mua hàng.
+ Tính trung bình số tiền mua hàng của từng khách hàng.
+ Tính trung bình số tiền mua hàng của từng loại khách hàng.
- Hiển thị 3 khách hàng mua hàng nhiều nhất (sắp xếp danh sách theo giá trị mua hàng giảm dan).
- Thống kê khách hàng thân thiết để tặng quà nhân dịp Tết Nguyên Đán biết các khách hàng đó cần có điểm tích lũy > 500 điểm và thuộc top 10 khách hàng có trung bình giá trị mua hàng lớn nhất

Yêu cầu 3: Xây dựng chương trình chính với nội dung sau (lưu ý chương trình chính hiến thị các tùy chọn cho phép người dùng lựa chọn):
- Thêm mới // Sửa thông tin // Xóa khách hàng.
- Tìm kiếm khách hàng theo mã hoặc tên.
- Hiển thị danh sách khách hàng theo phân loại khách hàng.
- Tính tổng doanh thu.
- Hiển thị danh sách 3 khách hàng mua hàng nhiều nhất
- Thống kê khách hàng thân thiết được nhận quà dịp Tết Nguyên Đán.
- Thoát chương trình.

Yêu cầu 4: Viết test cases cho các chức năng (tối thiểu 30)

CONVENTION:
- Tên class: PascalCase;
- Tên biến và phương thức: camelCase;
- Giữa các hàm cách 1 dòng
- NHỚ COMMENT CODE!!!

Cách dùng GIT branches
- Tạo thư mục ở máy
- git clone <link repo>
- Pull code về: git pull
- Chạy về đúng chức năng mình làm: git checkout <tên branch>
- Nhớ pull rồi mới add commit push
- push xong test xong hết rồi thì tạo PR (pull request) rồi merge
- Nếu conflict thì phải báo, gửi lên group để xem xét resolve