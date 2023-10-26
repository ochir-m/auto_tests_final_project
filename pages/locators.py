from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    HEAD_OF_THE_ITEM = (By.CSS_SELECTOR, ".product_main>h1")
    MESSAGE_ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner>strong")
    PRICE_OF_THE_ITEM = (By.CSS_SELECTOR, ".product_main>p")
    MESSAGE_TOTAL_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner>p>strong")