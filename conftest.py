import os
import time

from undetected_chromedriver import Chrome, ChromeOptions
from pytest import fixture

from emails_page_object import EmailsProject
import string
import random


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


@fixture
def email_auth(emails):
    emails.login('ira.vozzna@ukr.net', 'test123#')
    yield emails
    emails.logout()

@fixture
def selection():
    bunch = []
    for i in range(0, 3):
        subject = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        bunch.append((subject, body))
    return bunch
