from selenium.webdriver.common.by import By
import time

from page_objects.base_page import BasePage


class SendEmail(BasePage):
    COMPOSE_BUTTON = (By.CLASS_NAME, "compose")
    TO_FIELD = (By.NAME, "toFieldInput")
    SUBJECT_FIELD = (By.XPATH, "//input[@name='subject']")
    SEND_BUTTON = (By.XPATH, "//div[@class='sendmsg__bottom-controls']/button[contains(@class, 'send')]")

    def send(self, to, subject, body):
        """This method helps to send compose and send messages"""
        self.find_element(self.COMPOSE_BUTTON).click()
        self.find_element(self.TO_FIELD).send_keys(to)
        self.find_element(self.SUBJECT_FIELD).send_keys(subject)

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//div[@class='editor']//iframe"))
        self.driver.find_element(By.ID, "tinymce").clear()
        self.driver.find_element(By.ID, "tinymce").send_keys(body)
        self.driver.switch_to.default_content()

        time.sleep(1)
        self.find_element(self.SEND_BUTTON).click()
        time.sleep(1)