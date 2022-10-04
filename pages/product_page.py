from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def get_book_name(self):
        self.browser.implicitly_wait(5)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name1 = self.browser.find_element(*ProductPageLocators.BOOK_NAME1).text
        assert book_name == book_name1
        print("book is correct")

    def get_price(self):
        self.browser.implicitly_wait(5)
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price1 =self.browser.find_element(*ProductPageLocators.PRICE1).text
        assert price == price1
        print("price is correct")
