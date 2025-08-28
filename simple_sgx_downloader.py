"""
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
