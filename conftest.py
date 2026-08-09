import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os

@pytest.fixture
def driver():
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
    
    yield driver
    driver.quit()
