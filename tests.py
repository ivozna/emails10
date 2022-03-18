
def test_python_org(emails):
    emails.login()
    emails.get_sent()
    assert True

def test_send_email(emails):
    emails.send_email()
