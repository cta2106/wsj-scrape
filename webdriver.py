import os

from selenium import webdriver


class WebDriver(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        binary_location = os.getenv("GOOGLE_CHROME_BIN")
        if binary_location != "None":
            options.binary_location = binary_location
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.headless = True
        executable_path = os.getenv("GOOGLE_CHROME_PATH")
        super(WebDriver, self).__init__(
            options=options, executable_path=executable_path, keep_alive=True
        )
