import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.api_client import KinopoiskAPIClient


@pytest.fixture
def api_client():
    return KinopoiskAPIClient()


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
