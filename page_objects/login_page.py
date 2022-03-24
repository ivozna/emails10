from selenium.webdriver.common.by import By
import time
import pytest

from page_objects.base_page import BasePage

@pytest.mark.usefixtures('set_up')
class LoginPage(BasePage):
    LOGIN_INPUT = (By.NAME, "login")
    PASSWORD_INPUT = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    USER_PROFILE = (By.CLASS_NAME, 'login-button__user')


    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.go_to('login')

    def login(self, login, password):
        """Logging in to the email website.
        First we're checking is the user is logged in."""
        if self.is_logged_in():
            return

        self.find_element(self.LOGIN_INPUT).send_keys(login)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.SUBMIT_BUTTON).click()

    def is_logged_in(self):
        """This method helps to check if the user is already loggen in or not."""
        time.sleep(1)
        try:
            self.find_element(self.USER_PROFILE)
        except:
            return False
        return True

    def logout(self):
        self.go_to("q/logout")
