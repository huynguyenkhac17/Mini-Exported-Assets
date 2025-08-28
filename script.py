# Tạo lại version đơn giản hơn cho sinh viên/intern level

# 1. Main file đơn giản
simple_main = '''#!/usr/bin/env python3
"""
SGX Data Downloader - Phiên bản đơn giản
Tải dữ liệu từ Singapore Exchange
"""

import argparse
import logging
import os
import sys
from datetime import date, datetime
from sgx_downloader import SGXDownloader, setup_logging

def main():
    # Setup command line arguments
    parser = argparse.ArgumentParser(description='Tải dữ liệu SGX derivatives')
    parser.add_argument('--date', '-d', help='Ngày tải (YYYY-MM-DD)')
    parser.add_argument('--today', action='store_true', help='Tải file hôm nay')
    parser.add_argument('--output', '-o', default='downloads', help='Thư mục lưu file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Hiện chi tiết')
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(verbose=args.verbose)
    logger = logging.getLogger(__name__)
    
    try:
        # Tạo downloader
        downloader = SGXDownloader(output_dir=args.output)
        
        # Xác định ngày tải
        if args.today:
            target_date = date.today()
        elif args.date:
            target_date = datetime.strptime(args.date, '%Y-%m-%d').date()
        else:
            print("Cần chọn --today hoặc --date YYYY-MM-DD")
            return
            
        logger.info(f"🚀 Bắt đầu tải dữ liệu cho ngày {target_date}")
        
        # Download files
        success = downloader.download_date(target_date)
        
        if success:
            logger.info("✅ Tải thành công!")
        else:
            logger.error("❌ Có lỗi xảy ra")
            
    except Exception as e:
        logger.error(f"Lỗi: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
'''

# 2. Core downloader đơn giản  
simple_downloader = '''"""
SGX Downloader - Core module đơn giản
"""

import os
import requests
import logging
from pathlib import Path
from datetime import date

class SGXDownloader:
    """Class đơn giản để tải file từ SGX"""
    
    # Danh sách file cần tải
    FILES = [
        'WEBPXTICK_DT-{date}.zip',
        'TickData_structure.dat',
        'TC_{date}.txt', 
        'TC_structure.dat'
    ]
    
    def __init__(self, output_dir='downloads'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Setup session để tải file
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        self.logger = logging.getLogger(__name__)
        
    def download_date(self, target_date):
        """
        Tải tất cả file cho 1 ngày
        
        Args:
            target_date: Ngày cần tải (date object)
            
        Returns:
            bool: True nếu tải thành công
        """
        date_str = target_date.strftime('%Y%m%d')
        date_folder = self.output_dir / date_str
        date_folder.mkdir(exist_ok=True)
        
        self.logger.info(f"📁 Tạo thư mục: {date_folder}")
        
        success_count = 0
        total_files = len(self.FILES)
        
        for file_pattern in self.FILES:
            filename = file_pattern.format(date=date_str)
            
            if self._download_file(filename, date_folder, target_date):
                success_count += 1
                self.logger.info(f"✅ Tải thành công: {filename}")
            else:
                self.logger.error(f"❌ Tải thất bại: {filename}")
                
        self.logger.info(f"📊 Kết quả: {success_count}/{total_files} file thành công")
        return success_count == total_files
        
    def _download_file(self, filename, output_folder, target_date):
        """
        Tải 1 file cụ thể
        
        Args:
            filename: Tên file
            output_folder: Thư mục lưu
            target_date: Ngày tải
            
        Returns:
            bool: True nếu thành công
        """
        try:
            # Tính URL ID đơn giản (có thể không chính xác 100%)
            # SGX bắt đầu từ 2013-04-05 với URL ID 2755
            start_date = date(2013, 4, 5)
            days_diff = (target_date - start_date).days
            url_id = 2755 + days_diff  # Ước tính đơn giản
            
            # Tạo URL
            base_url = "https://links.sgx.com/1.0.0/derivatives-historical"
            url = f"{base_url}/{url_id}/{filename}"
            
            self.logger.debug(f"🔗 URL: {url}")
            
            # Download file
            response = self.session.get(url, timeout=30)
            
            if response.status_code == 200:
                output_path = output_folder / filename
                
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                    
                # Kiểm tra file có nội dung
                if output_path.stat().st_size > 0:
                    return True
                else:
                    self.logger.warning(f"File rỗng: {filename}")
                    return False
            else:
                self.logger.error(f"HTTP {response.status_code}: {filename}")
                return False
                
        except Exception as e:
            self.logger.error(f"Lỗi tải {filename}: {e}")
            return False

def setup_logging(verbose=False):
    """Setup logging đơn giản"""
    level = logging.DEBUG if verbose else logging.INFO
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    
    # Tắt log của requests
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
'''

# 3. Config đơn giản
simple_config = '''# SGX Downloader Config
# Cấu hình cơ bản

# SGX website settings
BASE_URL = "https://links.sgx.com/1.0.0/derivatives-historical"
TIMEOUT = 30  # seconds

# File settings
OUTPUT_DIR = "downloads"
FILES_TO_DOWNLOAD = [
    "WEBPXTICK_DT-{date}.zip",
    "TickData_structure.dat", 
    "TC_{date}.txt",
    "TC_structure.dat"
]

# SGX URL mapping (ước tính)
START_DATE = "2013-04-05"  # Ngày đầu tiên có dữ liệu
START_URL_ID = 2755        # URL ID tương ứng

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
'''

# 4. Requirements đơn giản
simple_requirements = '''requests>=2.25.0
'''

# 5. README đơn giản
simple_readme = '''# SGX Data Downloader

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
'''

# 6. Package structure
package_init = '''"""
SGX Downloader - Simple version
Tải dữ liệu từ Singapore Exchange
"""

from .sgx_downloader import SGXDownloader, setup_logging

__version__ = '1.0.0'
__author__ = 'Student Project'
'''

# Save files
simple_files = {
    'simple_main.py': simple_main,
    'simple_sgx_downloader.py': simple_downloader,
    'simple_config.py': simple_config,
    'simple_requirements.txt': simple_requirements,
    'simple_README.md': simple_readme,
    'simple___init__.py': package_init
}

for filename, content in simple_files.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Tạo file: {filename}")

print(f"\n📁 Đã tạo {len(simple_files)} file version đơn giản")
print("🎯 Phù hợp cho sinh viên/intern level!")