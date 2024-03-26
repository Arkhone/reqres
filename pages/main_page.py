
from utils.base_ops import BaseOps

class MainPage(BaseOps):
    def __init__(self, driver):
        super().__init__(driver)

    def get_text(self, locator, locator_type):
        text = self.find_an_element(locator, locator_type).text
        return text