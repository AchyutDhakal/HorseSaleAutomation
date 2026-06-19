import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-password-manager-reauthentication")
    options.add_argument("--start-maximized")

    # Unique profile per run — prevents profile lock conflicts
    tmpdir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={tmpdir}")

    options.add_experimental_option("prefs", {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=options)
    return driver