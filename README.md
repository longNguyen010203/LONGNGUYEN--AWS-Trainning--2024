# 🌈☁️ AWS FCJ Bootcamp 2024 🔥💨

## 📦 Technologies
 - `AWS`
 - `Terraform`

## 🌈💨 Image
<img src="./Images/aws-cloud-img.jpg">

## VPC
1. Amazon Virtual Private Cloud (VPC)
 - Là dịch vụ cung cấp môi trường mạng ảo riêng tư, được cô lập về mặt logic khỏi các mạng khác trên `AWS cloud`.
 - `VPC` cho phép khởi tạo các tài nguyên của AWS như máy chủ ảo, csdl, các thiết bị cân bằng tải,.. trong một môi trường mạng ảo riêng mà ta đã xác định và có quyền kiểm soát hoàn toàn
  <img src="./Images/Screenshot from 2024-08-10 21-48-10.png">

 - **Region** càng gần thì độ trễ càng thấp, thường ta hay chọn Singapore vì gần VietNam nhất, 1 region có tối thiểu 3 `AZ` 
 - **Availability Zone (AZ)** là một cụm trung tâm dữ liệu
  <img src="./Images/Screenshot from 2024-08-11 16-13-35.png">

 - VPC nằm trong 1 Region, khi tạo VPC cần khai báo 1 lớp mạng CIDR IPv4 (bắt buộc) và IPv6 tùy chọn
 - Giới hạn của VPC hiện tại là 5 VPC trên 1 AWS Region trên 1 AWS Account
 - Mục đích chính sử dụng VPC thường dùng để phân tách các môi trường (Production/Dev/Test/Staging)
 - **Lưu ý**: Nếu muốn các tài nguyên tách biệt hẳn (User không thể nhìn thấy một tài nguyên cụ thể thì cần tách thành nhiều AWS account, nhiều VPC không giải quyết được vấn đề này)  
  <img src="./Images/Screenshot from 2024-08-11 16-34-40.png">

 - **Subnet** - Mạng con ảo
    + Amazon VPC cho phép tạo nhiều mạng ảo và chia các mạng ảo này thành các mạng con (Subnet)
    + VPC Subnet sẽ nằm trong 1 AZ cụ thể (1 subnet chỉ nằm trong 1 VPC)
    + Khi tạo Subnet, chúng ta chỉ định CIDR cho mạng con đó và đây là một tập hợp con của khối VPC CIDR
    + Trong mỗi Subnet, AWS sẽ giữ lại 5 địa chỉ IP
    + Ví dụ: Nếu Subnet có CIDR là 10.10.1.0/24
      + địa chỉ network (10.10.1.0)
      + địa chỉ broadcast (10.10.1.255)
      + địa chỉ cho bộ định tuyến (10.10.1.1)
      + địa chỉ cho DNS (10.10.1.2)
      + địa chỉ cho tính năng tương lai (10.10.1.3)
    + subnet có hai loại là public subnet và private subnet
 - **Route table** - Bảng định tuyến
    + tập hợp các Route, để xác định đường đi cho mạng.
    + Khi tạo VPC, AWS sẽ tạo một Default Route table, Default Route table không thể bị xóa và chỉ chứa 1 Route duy nhất là Route cho phép tất cả các Subnet trong VPC liên lạc với nhau 
    + Route table sẽ được gán vào các Subnet mà ta tạo
    + Chúng ta có thể tạo Custom Route table (bảng định tuyến tùy chỉnh) => để chúng ta có thể tạo public subnet tức là subnet mà bên trong nó maý chủ của ta có thể ra được ngoài Internet, tuy nhiên sẽ không thể xóa default route (VPC CIDR - Local)
 - **Elastic Network Interface (ENI)**
    + Là một card mạng ảo, chúng ta có thể chuyển sang các `EC2` Instance khác
    + Khi chuyển sang một máy chủ mới, một card mạng ảo sẽ vẫn duy trì:
      + địa chỉ IP Private
      + địa chỉ Elastic IP address
      + địa chỉ MAC
 - **Elastic IP address (EIP)**: 
    + Là một địa chỉ public IPv4 tĩnh, có thể liên kết với một Elastic Network Interface
    + khi không sử dụng, sẽ bị charge phí. (tránh lãng phí)
 - **VPC Endpoint**: 
    + Cho phép chúng ta kết nối các tài nguyên nằm trong VPC tới các dịch vụ AWS được hỗ trợ (AWS PrivateLink - đi qua mạng private của AWS) mà không cần thông qua kết nối internet
    + Có 2 kiểu VPC Endpoint:
      + **Interface Endpoint**: Sử dụng một Elastic Network Interface trong VPC cùng với một địa chỉ IP Private để kết nối tới 1 dịch vụ hỗ trợ 
      + **Gateway Endpoint**: Sử dụng một route table để định tuyến tới Endpoint của dich vụ hỗ trợ (S3 và DynamoDB)
 - **Internet Gateway**:
    + Là một thành phần của Amazon VPC có khả năng mở rộng quy mô theo chiều ngang (scale out) cho phép các EC2 Instance trong VPC có thể truyền thông tin ra ngoài  Internet
    + Internet Gateway được quản lý bởi AWS, chúng ta không cần cấu hình autoscale hoặc high availability.
 - **NAT Gateway**: Cho phép các EC2 Instance trong Subnet truy cập tới internet hoặc các dịch vụ AWS khác. chỉ chấp nhận kết nối chiều ra và không chấp nhận kết nối chiều vào
 - **Security Group**: là một tường lửa ảo có lưu giữ trạng thái (stateful) giúp kiểm soát lượng truy cập đến và đi trong tài nguyên của AWS.
    + Security Group rule được hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối, hoặc một Security Group khác.
    + Security Group rule chỉ cho phép rule allow.
    + Security Group được áp dụng lên các Elastic Network Interface.
 - **Network Access Control List (NACL)**: là một tường lửa ảo không lưu giữ trạng thái (stateless) giúp kiểm soát lượng truy cập đến và đi trong tài nguyên của AWS.
    + NACL được hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối.
    + NACL được áp dụng lên các Amazon VPC Subnets.
    + Mặc định NACL cho phép mọi truy cập đến và đi.
 - **VPC Flow Logs**: là một tính năng cho phép bạn nắm bắt thông tin về lưu lượng IP đến và đi từ các giao diện mạng trong VPC của bạn
    + các tập tin logs có thể được xuất bản lên Amazon CloudWatch Logs hoặc Amazon S3.
    + VPC Flow Logs không capture nội dung gói tin.

1. VPC Peering & Transit Gateway
 - **VPC Peering**: là tính năng giúp kêt nối hai hay nhiều VPC để các tài nguyên bên trong hai VPC đó có thể liên lạc trực tiếp với nhau không cần phải thông qua Internet, góp phần gia tăng bảo mật cho VPC.
    + Cho phép kết nối 2 VPC với nhau
    + là kết nối cần tạo 1:1 giữa hai VPC thành viên, không hỗ trợ transitive routing.
    + không hỗ trợ khi 2 VPC bị overlap IP address space.
    <img src="./Images/Screenshot from 2024-08-14 23-35-02.png">

 - **Transit Gateway**: Một giải phép cho phép kết nối số lượng lớn VPC một cách dễ dàng và hiệu quả với nhau
    + được dùng để kết nối các VPC và mạng on-premises thông qua một hub trung tâm. Điều này đơn giản hóa mạng và kết thúc các mối quan hệ định tuyến phức tạp.
    + **Transit Gateway Attachment** là một công cụ để gán các subnet của từng VPC cần kết nối với nhau vào một TGW đã được khởi tạo. Transit Gateway Attachment hoạt động ở quy mô Availability Zone (AZ-level).
    + Trong VPC, khi một subnet ở một AZ có Transit Gateway Attachment với một TGW, các subnet khác trong cùng AZ đều có thể kết nối tới TGW đó.
    <img src="./Images/Screenshot from 2024-08-14 23-32-48.png">
    <img src="./Images/Screenshot from 2024-08-14 23-38-55.png">
    

2. VPN & Direct Connect
 - Kết nối môi trường AWS với các trung tâm dữ liệu nằm ở local (on premise)
 - **VPN & Direct Connect**: là hai giải pháp kết nối an toàn và tin cậy
3. Elastic Load Balancing
 - Hay còn gọi là cân bằng tải
 - Phân phối lưu lượng truy cập đến nhiều máy chủ đích
 - Đảm bảo khả năng chịu lỗi, đảm bảo hiệu năng mở rộng cho ứng dụng