# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import Chrome, ChromeOptions
from pytest import fixture
import os

from emails_page_object import EmailsProject


@fixture
def web_driver():
    options = ChromeOptions()
    chrome_dir = os.getcwd()
    options.add_argument(f"--user-data-dir={chrome_dir}/sessions/Chrome")
    driver = Chrome(options=options)
    yield driver
    driver.close()


@fixture
def emails(web_driver):
    page = EmailsProject(web_driver)
    yield page
