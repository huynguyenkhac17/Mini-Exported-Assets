#!/usr/bin/env python3
"""
Demo script - Ví dụ cách sử dụng SGX Downloader
"""

from datetime import date
from sgx_downloader import SGXDownloader, setup_logging

def main():
    # Setup logging để xem quá trình
    setup_logging(verbose=True)

    # Tạo downloader
    downloader = SGXDownloader(output_dir="demo_downloads")

    print("🚀 Demo SGX Downloader")
    print("=" * 40)

    # Thử tải data hôm nay
    today = date.today()
    print(f"📅 Thử tải dữ liệu ngày: {today}")

    success = downloader.download_date(today)

    if success:
        print("✅ Demo thành công!")
        print("📁 Check thư mục demo_downloads để xem file")
    else:
        print("❌ Demo thất bại - có thể do:")
        print("   - Chưa có dữ liệu cho ngày hôm nay")
        print("   - URL ID không chính xác")
        print("   - Vấn đề mạng")
        print("💡 Thử với ngày khác: python demo.py")

if __name__ == '__main__':
    main()
