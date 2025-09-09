import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def browser():
    options = Options()
    browser = webdriver.Firefox(options=options)
    browser.add_argument('--headless')
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()
