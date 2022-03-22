import os
import string
import random

from undetected_chromedriver import Chrome, ChromeOptions
from pytest import fixture
from emails_page_object import EmailsProject


@fixture
def web_driver():
    """This function opens a browser and saves sessions"""
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


@fixture
def email_auth(emails):
    emails.login('ihorrybakk@ukr.net', 'test123#')
    yield emails
    emails.logout()


@fixture
def selection():
    """This function generates a set number of pairs (subject, body) for sending in emails.
    Subject and body consist of random string with 10 symbols (letters and numbers only)"""
    bunch = []
    for i in range(0, 10):
        subject = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        bunch.append((subject, body))
    return bunch
