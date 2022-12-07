import pytest
from pages.product_page import ProductPage


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_about_adding()
#     page.should_be_message_basket_total()


# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
class TestLookForBrokenLink:
    def test_guest_can_add_product_to_basket(self, browser, link):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        page = ProductPage(browser, link)
        page.open()
        page.go_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
