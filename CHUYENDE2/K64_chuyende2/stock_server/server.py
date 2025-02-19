import socket
import json

def start_server():
    # Khởi tạo socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 99))
    server_socket.listen(5)
    print("Server đang chạy và lắng nghe tại cổng 99...")

    # Data mẫu
    stock_data = {
        "FPT": {"current_price": 100000},
        "VNM": {"current_price": 82000},
        "HAG": {"current_price": 7800},
    }

    while True:
        try:
            # Chấp nhận kết nối từ client
            client_socket, address = server_socket.accept()
            print(f"Đã kết nối với client: {address}")

            # Nhận dữ liệu từ client
            data = client_socket.recv(1024).decode('utf-8').strip()
            if data.startswith("STOCK "):
                stock_code = data.split(" ")[1]
                # Kiểm tra mã chứng khoán
                if stock_code in stock_data:
                    response = stock_data[stock_code]
                else:
                    response = {"error": "Mã chứng khoán không tồn tại"}
            else:
                response = {"error": "Yêu cầu không hợp lệ"}

            # Gửi phản hồi về client
            client_socket.sendall(json.dumps(response).encode('utf-8'))
            client_socket.close()

        except Exception as e:
            print(f"Lỗi: {str(e)}")
            continue

if __name__ == "__main__":
    start_server()