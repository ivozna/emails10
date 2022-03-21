
def test_send_email(email_auth, selection):
    for (subject, body) in selection:
        email_auth.send_email('ira.vozzna@ukr.net', subject, body)
    #assert email_auth.check_inbox(selection)
    dict_object = email_auth.create_dictionary()
    print(dict_object)

    reports = [email_auth.make_text(i[0], i[1]) for i in dict_object.items()]
    collected_emails = "\n\n".join(reports)
    email_auth.send_email('ira.vozzna@ukr.net', 'Collected emails', collected_emails)