from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class Inbox(BasePage):

    EMAILS_LIST = (By.CLASS_NAME, "msglist__row-subject")
    CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    DELETE_BUTTON = (By.XPATH, "//a[@class='controls-link remove']")

    def get_last_received(self, count):
        """Going to inbox, collecting data from all incoming mails and saving it as dictionary.
        Key is the theme of mail, value is the body."""
        self.go_to("desktop#msglist/f0/p0")

        elements = self.find_elements(self.EMAILS_LIST)
        text_items = [el.get_attribute('innerText').split() for el in elements][1:(count + 1)]
        return dict(text_items)

    def make_text(self, subject, body):
        """Creating a sentence describing each received email.
        The sentence needs to have subject, body, letters and numbers."""
        s = subject + body
        numbers = sum(c.isdigit() for c in s)
        letters = sum(c.isalpha() for c in s)
        return f"""Received mail on theme {subject} with message: {body}. 
        It contains {letters} letters and {numbers} numbers"""

    def delete_emails(self, count):
        """This method deletes all received emails except the last one."""
        self.go_to("desktop#msglist/f0/p0")
        checkboxes = self.find_elements(self.CHECKBOX)
        selected_checkboxes = checkboxes[2:(count+2)]
        for el in selected_checkboxes:
            el.click()
        delete = self.find_element(self.DELETE_BUTTON)
        delete.click()
