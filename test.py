#!/usr/bin/env python3
"""
Simple test script
"""

import os
import sys
from datetime import date
from pathlib import Path

def test_import():
    """Test import modules"""
    try:
        import requests
        print("✅ requests OK")
    except ImportError:
        print("❌ requests missing - run: pip install requests")
        return False

    try:
        from sgx_downloader import SGXDownloader, setup_logging
        print("✅ sgx_downloader OK")
    except ImportError as e:
        print(f"❌ sgx_downloader import error: {e}")
        return False

    return True

def test_basic_functionality():
    """Test cơ bản"""
    try:
        from sgx_downloader import SGXDownloader

        # Tạo downloader
        downloader = SGXDownloader("test_output")
        print("✅ SGXDownloader created")

        # Check output dir
        if Path("test_output").exists():
            print("✅ Output directory created")
        else:
            print("❌ Output directory not created")
            return False

        return True

    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    print("🧪 SGX Downloader Test")
    print("=" * 30)

    # Test imports
    if not test_import():
        print("❌ Import test failed")
        sys.exit(1)

    # Test basic functionality  
    if not test_basic_functionality():
        print("❌ Basic test failed")
        sys.exit(1)

    print("✅ All tests passed!")
    print("🚀 Ready to use SGX Downloader")

if __name__ == '__main__':
    main()
