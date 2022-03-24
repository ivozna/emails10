from page_objects.send_email_page import SendEmail
from page_objects.check_sent_page import Sent
from page_objects.inbox_page import Inbox
from page_objects.login_page import LoginPage
from pytest import fixture
import random
import string


@fixture
def example_data():
    """This function generates a set number of pairs (subject, body) for sending in emails.
    Subject and body consist of random string with 10 symbols (letters and numbers only)"""
    bunch = []
    for i in range(0, 10):
        subject = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        bunch.append((subject, body))
    return bunch


def test_email_box(example_data, web_driver):
    login_page = LoginPage(web_driver)
    login_page.login('ihorrybakk@ukr.net', 'test123#')

    send_email = SendEmail(web_driver)
    for (subject, body) in example_data:
        send_email.send('ihorrybakk@ukr.net', subject, body)
    
    sent = Sent(web_driver)
    assert sent.check_sent(example_data)

    inbox = Inbox(web_driver)
    received = inbox.get_last_received(len(example_data))
    reports = [inbox.make_text(i[0], i[1]) for i in received.items()]

    collected_emails = "\n\n".join(reports)
    send_email.send('ihorrybakk@ukr.net', 'Collected emails', collected_emails)

    inbox.delete_emails(len(example_data))
