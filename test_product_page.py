import time

import pytest

from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_the_message_item_added_to_cart()
    page.check_the_message_total_price_in_basket()
#
# @pytest.mark.parametrize('promo_offer', [*range(0, 7), pytest.param(7, marks=pytest.mark.xfail(reason="bugged link")), *range(8, 10)])
# def test_promo_offer(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_button_add_to_basket()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.check_the_message_item_added_to_cart()
#     page.check_the_message_total_price_in_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_message_dissapeared_after_adding_product()