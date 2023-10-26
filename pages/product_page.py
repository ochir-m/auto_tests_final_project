import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
            "Button 'add_to_basket' is not presented"

    def add_product_to_basket(self):
        link_add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link_add_product_to_basket.click()

    def check_the_message_item_added_to_cart(self):
        head_of_the_item = self.browser.find_element(*ProductPageLocators.HEAD_OF_THE_ITEM).text
        message_item_added_to_cart = (
            self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_ADDED_TO_CART).text)
        assert head_of_the_item == message_item_added_to_cart, \
            "head of the item in message is wrong"

    def check_the_message_total_price_in_basket(self):
        price_of_the_item = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_ITEM).text
        message_total_price_in_basket = (
            self.browser.find_element(*ProductPageLocators.MESSAGE_TOTAL_PRICE_IN_BASKET).text)
        assert price_of_the_item == message_total_price_in_basket, \
            "price of the item is not equal total price in basket"

