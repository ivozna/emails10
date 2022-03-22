
def test_send_email(email_auth, selection):
    for (subject, body) in selection:
        email_auth.send_email('ihorrybakk@ukr.net', subject, body)
    assert email_auth.check_sent(selection)
    dict_object = email_auth.create_dictionary()
    reports = [email_auth.make_text(i[0], i[1]) for i in dict_object.items()]
    collected_emails = "\n\n".join(reports)
    email_auth.send_email('ihorrybakk@ukr.net', 'Collected emails', collected_emails)
    email_auth.delete_emails()
