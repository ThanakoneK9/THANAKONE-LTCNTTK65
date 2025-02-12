import socket

# Cấu hình server
SERVER_HOST = '127.0.0.1'  # IP của server (chạy local)
SERVER_PORT = 99           # Cổng 99

def request_stock(stock_code):
    """Gửi yêu cầu lấy giá cổ phiếu đến server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_HOST, SERVER_PORT))
        client.sendall(f"STOCK {stock_code}".encode())

        # Nhận phản hồi từ server
        response = client.recv(1024).decode()
        print(f"📊 Giá cổ phiếu {stock_code}: {response}")

if __name__ == "__main__":
    while True:
        stock_code = input("🔎 Nhập mã cổ phiếu (hoặc 'exit' để thoát): ").strip().upper()
        if stock_code == "EXIT":
            print("🚪 Đóng kết nối...")
            break
        request_stock(stock_code)
