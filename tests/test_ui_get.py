from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jsonschema import validate

import settings
import schemas.get as schemas


def test_get_list_users(driver):
    button = driver.find_element(By.XPATH, settings.LIST_USERS_BUT)
    button.click()
    validate(instance=driver.find_element(By.XPATH, settings.OUTPUT_RESPONSE).text, schema=schemas.list_users_schema)
    assert driver.find_element(By.CSS_SELECTOR, settings.PREFIX_URL).text == settings.GET_LIST_USERS
    assert driver.find_element(By.CLASS_NAME, settings.RESPONSE_CODE).text == '200'
