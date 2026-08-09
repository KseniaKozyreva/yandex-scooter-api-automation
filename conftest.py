import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Наш любимый Firefox, который работает без единой ошибки!
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    yield driver
    
    driver.quit()
