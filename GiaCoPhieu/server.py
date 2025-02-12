import socket

# Khởi tạo server trên cổng 99
HOST = '0.0.0.0'  # Lắng nghe trên tất cả các IP
PORT = 99

# Dữ liệu stock giả lập
stock_data = {
    "AAPL": 175.6,
    "GOOGL": 2800.5,
    "TSLA": 850.3,
    "MSFT": 310.1,
    "AMZN": 3450.2
}

def handle_stock_request(code):
    """Xử lý yêu cầu STOCK <code>"""
    return stock_data.get(code, "Stock không tồn tại")

def start_server():
    """Khởi động server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"✅ Server đang chạy trên cổng {PORT}...")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"📡 Kết nối từ {addr}")
                data = conn.recv(1024).decode().strip()
                
                if data.startswith("STOCK "):
                    stock_code = data.split(" ")[1]
                    response = str(handle_stock_request(stock_code))
                else:
                    response = "❌ Lỗi: Yêu cầu không hợp lệ"

                conn.sendall(response.encode())

if __name__ == "__main__":
    start_server()
