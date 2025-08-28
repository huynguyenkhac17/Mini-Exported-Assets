# SGX Downloader Config
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
