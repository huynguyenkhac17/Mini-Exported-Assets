#!/usr/bin/env python3
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
