from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class EmailsProject:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://gmail.com/")

    def login(self):
        self.driver.find_element(By.ID, "identifierId").send_keys('ihorrybak106@gmail.com')
        self.driver.find_element(By.ID, 'identifierNext').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, 'password').send_keys('Rozaroza123#')
        self.driver.find_element(By.ID, 'passwordNext').click()
        time.sleep(3)

        assert "Inbox" in self.driver.title

    def send_email(self):
        self.driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Compose')]").click()
        self.driver.find_element(By.XPATH, "//textarea[@name='to']").send_keys('ira.vozna@gmail.com')
        self.driver.find_element(By.ID, ':g9').send_keys('subject1')
        self.driver.find_element(By.ID, ':k7').send_keys('text1')
        self.driver.find_element(By.ID, ':gj').click()

    def get_sent(self):
        self.driver.find_element(By.ID, ':5r').click()
        assert 'text1' in self.driver.find_element(By.ID, ':1')

