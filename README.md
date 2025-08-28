# SGX Data Downloader

🚀 **Tool đơn giản để tải dữ liệu từ Singapore Exchange**

## Cài đặt

```bash
pip install requests
```

## Cách dùng

```bash
# Tải file hôm nay
python main.py --today

# Tải file ngày cụ thể  
python main.py --date 2024-08-27

# Lưu vào thư mục khác
python main.py --today --output my_data

# Xem chi tiết
python main.py --today --verbose
```

## File được tải

1. `WEBPXTICK_DT-YYYYMMDD.zip` - Dữ liệu tick
2. `TickData_structure.dat` - Cấu trúc dữ liệu
3. `TC_YYYYMMDD.txt` - Trade cancellation  
4. `TC_structure.dat` - Cấu trúc TC

## Cấu trúc file

```
downloads/
├── 20240827/
│   ├── WEBPXTICK_DT-20240827.zip
│   ├── TickData_structure.dat
│   ├── TC_20240827.txt
│   └── TC_structure.dat
```

## Code structure

- `main.py` - Entry point chính
- `sgx_downloader.py` - Logic download  
- `config.py` - Cấu hình
- `requirements.txt` - Dependencies

## Lưu ý

- Tool này dùng ước tính URL ID nên có thể không chính xác 100%
- Chỉ test với dữ liệu gần đây
- Nếu lỗi thì thử ngày khác hoặc check lại URL

## Todo (có thể làm thêm)

- [ ] Better URL ID calculation
- [ ] Retry mechanism khi lỗi
- [ ] Download multiple dates  
- [ ] Config file support
- [ ] Better error messages
