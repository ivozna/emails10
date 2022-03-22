# Project about...
emails10 is a small project to test sending, receiving and deleting emails in https://mail.ukr.net/

# Install guide ...
1.Install pip and python:

apt install python-pip

apt install python

2.Install virtual environment:

pip install virtualenv

## Run guide ...

1. Clone the Python-Pytest-Selenium Repository:
https://github.com/ivozna/emails10.git
2. Create and Activate the virtual environment in the Python-Pytest-Selenium folder:

- For Linux/MacOS

virtualenv venv

source venv/bin/activate
- For Windows

python -m virtualenv venv

venv\Scripts\activate.bat
3. Install required packages.

pip install -r requirements.txt

4. Run tests:
``pytest tests.py``

## Project steps
1. Login to any email box. 
2. Send from 10 mails from current box to yourself with:
- Theme: Random string with 10 symbols (letters and numbers only)
- Body: Random string with 10 symbols (letters and numbers only)

3. Check that all 10 mails are delivered.
4. Collect data from all incoming mails and save it as Object (Dictionary), where:
- Key is theme of mail
- Value is body of mail

5. Send collected data to yourself as:

``Received mail on theme {Theme} with message: {Body}. It contains {Count of letters} letters and {Count of numbers} numbers``
(repeat for each mail).

7. Delete all received mails except the last one.


##Useful links

https://www.selenium.dev/
