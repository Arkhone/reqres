import pytest

from selenium import webdriver

import settings


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(settings.URL)
    yield driver
    driver.close()
    driver.quit()


