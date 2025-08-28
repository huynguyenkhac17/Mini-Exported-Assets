# 📖 Hướng dẫn Setup SGX Downloader

## Bước 1: Chuẩn bị môi trường

### Cài Python (nếu chưa có)
- Download Python 3.8+ từ python.org
- Nhớ check "Add to PATH" khi cài

### Check Python version
```bash
python --version
# hoặc
python3 --version
```

## Bước 2: Cài đặt project

```bash
# Clone hoặc copy code về máy
mkdir sgx_project
cd sgx_project

# Copy các file:
# - main.py
# - sgx_downloader.py  
# - config.py
# - requirements.txt

# Cài dependencies
pip install -r requirements.txt
```

## Bước 3: Test chạy

```bash
# Test cơ bản
python main.py --help

# Thử tải file hôm nay
python main.py --today --verbose

# Thử tải ngày cụ thể
python main.py --date 2024-08-27
```

## Bước 4: Hiểu code

### File chính
- **main.py**: Entry point, xử lý command line
- **sgx_downloader.py**: Logic download chính
- **config.py**: Cấu hình constants

### Flow chính
1. Parse command line arguments  
2. Tạo SGXDownloader object
3. Xác định ngày cần tải
4. Download 4 loại file
5. Lưu vào thư mục theo ngày

### URL Pattern SGX
```
https://links.sgx.com/1.0.0/derivatives-historical/{url_id}/{filename}
```
- URL ID bắt đầu từ 2755 (ngày 2013-04-05)
- Tăng dần theo ngày (có thể không chính xác 100%)

## Bước 5: Troubleshooting

### Lỗi thường gặp

**Import Error**
```bash
ModuleNotFoundError: No module named 'requests'
```
*Fix*: `pip install requests`

**File not found 404**  
```
HTTP 404: WEBPXTICK_DT-20240827.zip
```
*Fix*: URL ID không đúng hoặc chưa có data cho ngày đó

**Permission denied**
```
PermissionError: [Errno 13] Permission denied: 'downloads'
```  
*Fix*: Chạy với quyền admin hoặc đổi thư mục output

### Debug tips
- Dùng `--verbose` để xem chi tiết
- Check log messages để hiểu lỗi
- Thử với ngày khác nếu một ngày không work
- Check network connection

## Bước 6: Mở rộng (Optional)

Có thể cải tiến:
- Better URL ID calculation
- Retry mechanism
- Config file support  
- GUI interface
- Database storage
- Error recovery
- Multiple date download

## Resources

- SGX Website: https://www.sgx.com/research-education/derivatives
- Python requests: https://docs.python-requests.org/
- Argparse tutorial: https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
