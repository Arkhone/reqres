import pytest

from selenium import webdriver

import settings


@pytest.fixture
def driver():
    # Инициализация WebDriver и открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(settings.URL)
    yield driver
    driver.close()
    driver.quit()
