from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageObject():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME1 = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p")
    PRICE1 = (By.CSS_SELECTOR, ".alert-info strong")