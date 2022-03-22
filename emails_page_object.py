from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time



class EmailsProject:

    def __init__(self, driver):
        self.driver = driver
        self.go_to()

    def go_to(self, link=''):
        self.driver.get("https://mail.ukr.net/" + link)

    def login(self, login, password):
        """Logging in to the email website.
        First we're checking is the user is logged in."""
        if self.is_logged_in():
            return

        self.driver.find_element(By.NAME, "login").send_keys(login)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def send_email(self, to, subject, body):
        """This method helps to send compose and send messages"""
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "compose"))).click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "toFieldInput").send_keys(to)
        self.driver.find_element(By.XPATH, "//input[@name='subject']").send_keys(subject)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//div[@class='editor']//iframe"))
        self.driver.find_element(By.ID, "tinymce").clear()
        self.driver.find_element(By.ID, "tinymce").send_keys(body)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "//div[@class='sendmsg__bottom-controls']/button[contains(@class, 'send')]").click()
        time.sleep(1)

    def is_logged_in(self):
        """This method helps to check if the user is already loggen in or not."""
        time.sleep(1)
        try:
            self.driver.find_element(By.CLASS_NAME, 'login-button__user')
        except:
            return False
        return True

    def logout(self):
        self.go_to("q/logout")

    def check_sent(self, selection):
        """This method goes to Inbox messages and checks if all the emails
         have the same subjects and messages as we've sent before"""
        self.go_to("desktop#msglist/f10001/p0")

        data = self.driver.find_element(By.ID, 'msglist')
        text = data.get_attribute('innerText')

        return any([item[0] not in text for item in selection])

    def create_dictionary(self):
        """Going to inbox, collecting data from all incoming mails and saving it as dictionary.
        Key is the theme of mail, value is the body."""
        self.go_to("desktop#msglist/f0/p0")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "msglist__row-subject")))

        elements = self.driver.find_elements(By.CLASS_NAME, "msglist__row-subject")
        text_items = [el.get_attribute('innerText').split() for el in elements][1:11]
        return dict(text_items)

    def make_text(self, subject, body):
        """Creating a sentence describing each received email.
        The sentence needs to have subject, body, letters and numbers."""
        s = subject + body
        numbers = sum(c.isdigit() for c in s)
        letters = sum(c.isalpha() for c in s)
        return f"""Received mail on theme {subject} with message: {body}. 
        It contains {letters} letters and {numbers} numbers"""

    def delete_emails(self):
        """This method deletes all received emails except the last one."""
        self.go_to("desktop#msglist/f0/p0")
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        selected_checkboxes = checkboxes[2:12]
        for el in selected_checkboxes:
            el.click()
        delete = self.driver.find_element(By.XPATH, "//a[@class='controls-link remove']")
        delete.click()
