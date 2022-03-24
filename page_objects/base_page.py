from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pytest import fixture

class BasePage:

    def __init__(self, web_driver):
        self.driver = web_driver

    @fixture(autouse=True)
    def set_up(self):
        self.go_to()

    def go_to(self, link=''):
        self.driver.get("https://mail.ukr.net/" + link)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")
