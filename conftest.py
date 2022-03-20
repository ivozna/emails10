from undetected_chromedriver import Chrome
from pytest import fixture

from emails_page_object import EmailsProject
import string
import random


@fixture
def web_driver():
    driver = Chrome()
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
    for i in range(0, 10):
        subject = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        bunch.append((subject, body))
    return bunch
