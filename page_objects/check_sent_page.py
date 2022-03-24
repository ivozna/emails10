from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time

class Sent(BasePage):
    DATA = (By.ID, 'msglist')

    def check_sent(self, selection):
        """This method goes to Inbox messages and checks if all the emails
         have the same subjects and messages as we've sent before"""
        self.go_to("desktop#msglist/f10001/p0")
        time.sleep(1)

        data = self.find_element(self.DATA)
        text = data.get_attribute('innerText')

        return any([item[0] not in text for item in selection])