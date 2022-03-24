import os
from undetected_chromedriver import Chrome, ChromeOptions
from pytest import fixture


@fixture
def web_driver():
    """This function opens a browser and saves sessions"""
    options = ChromeOptions()
    chrome_dir = os.getcwd()
    options.add_argument(f"--user-data-dir={chrome_dir}/sessions/Chrome")
    driver = Chrome(options=options)
    yield driver
    driver.close()
    driver.quit()
