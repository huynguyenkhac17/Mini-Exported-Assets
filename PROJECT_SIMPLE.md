# 📁 SGX Downloader - Phiên bản Sinh viên

## File structure
```
sgx_project/
├── main.py                 # Entry point chính
├── sgx_downloader.py       # Logic download  
├── config.py               # Cấu hình
├── __init__.py             # Package init
├── requirements.txt        # Dependencies (chỉ requests)
├── README.md              # Hướng dẫn cơ bản
├── SETUP_GUIDE.md         # Hướng dẫn setup chi tiết
├── demo.py                # Script demo
├── test.py                # Test script
├── run.bat                # Batch script cho Windows
└── downloads/             # Thư mục chứa file tải về
    └── YYYYMMDD/          # Thư mục theo ngày
        ├── WEBPXTICK_DT-YYYYMMDD.zip
        ├── TickData_structure.dat
        ├── TC_YYYYMMDD.txt
        └── TC_structure.dat
```

## Đặc điểm phiên bản này

✅ **Đơn giản**: Chỉ 6 file chính + utilities  
✅ **Dễ hiểu**: Code straightforward, ít abstraction  
✅ **Minimal dependencies**: Chỉ cần requests  
✅ **Basic features**: Download cơ bản, command line  
✅ **Student-friendly**: Comments tiếng Việt, docs dễ hiểu  

## So sánh với version "chuyên nghiệp"

| Feature | Version này | Version chuyên nghiệp |
|---------|-------------|---------------------|
| File count | 6 files | 14+ files |
| Dependencies | requests only | 8+ packages |
| Architecture | Single class | Multi-module |
| Error handling | Basic try/catch | Comprehensive recovery |
| Logging | Simple print | Multi-level rotation |
| Config | Python constants | YAML + env vars |
| Scheduling | Manual run | Daemon mode |
| Recovery | None | Automatic retry |

## Phù hợp cho

👨‍🎓 **Sinh viên** học Python, web scraping  
👩‍💻 **Intern** làm data projects  
🔰 **Beginner** muốn hiểu cách download data  
📚 **Learning** Python requests, file handling  

## Có thể học được

- Command line argument parsing (argparse)
- HTTP requests và file download  
- File và directory handling
- Basic error handling
- Logging cơ bản
- Date/time manipulation
- Project structure

## Cách sử dụng nhanh

```bash
# Setup
pip install requests

# Run
python main.py --today --verbose
python main.py --date 2024-08-27

# Demo
python demo.py

# Test
python test.py
```

Thế này đủ để hiểu và làm được cơ bản rồi! 🎯
