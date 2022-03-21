from selenium.webdriver.common.by import By
import time


class EmailsProject:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://mail.ukr.net/")

    def login(self, login, password):
        if self.is_logged_in():
            return

        self.driver.find_element(By.NAME, "login").send_keys(login)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def send_email(self, to, subject, body):
        time.sleep(4)
        self.driver.find_element(By.CLASS_NAME, "compose").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "toFieldInput").send_keys(to)
        self.driver.find_element(By.XPATH, "//input[@name='subject']").send_keys(subject)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//div[@class='editor']//iframe"))
        self.driver.find_element(By.ID, "tinymce").send_keys(body)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "//div[@class='sendmsg__bottom-controls']/button[contains(@class, 'send')]").click()
        time.sleep(1)

    def is_logged_in(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.CLASS_NAME, 'login-button__user')
        except:
            return False
        return True

    def logout(self):
        self.driver.get("https://mail.ukr.net/q/logout")

    def check_inbox(self, selection):
        self.driver.get("https://mail.ukr.net/desktop#msglist/f0/p0")
        data = self.driver.find_element(By.ID, 'msglist')
        text = data.get_attribute('innerText')

        for (subject, body) in selection:
            if subject not in text or body not in text:
                return False
        return True

    def create_dictionary(self):
        self.driver.get("https://mail.ukr.net/desktop#msglist/f0/p0")
        elements = self.driver.find_elements(By.CLASS_NAME, "msglist__row-subject")
        text_items = [el.get_attribute('innerText').split() for el in elements][1:11]
        dictionary = dict(text_items)
        return dictionary

    def make_text(self, subject, body):
        s = subject + body
        numbers = sum(c.isdigit() for c in s)
        letters = sum(c.isalpha() for c in s)
        return f"""Received mail on theme {subject} with message: {body}. 
        It contains {letters} letters and {numbers} numbers"""
