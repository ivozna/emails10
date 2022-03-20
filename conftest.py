from undetected_chromedriver import Chrome
from pytest import fixture

from emails_page_object import EmailsProject


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
