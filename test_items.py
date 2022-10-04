import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time



def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(20)
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except (NoSuchElementException):
        return False
    return True

