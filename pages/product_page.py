from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def product_add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON_LINK)
        basket_link.click()

    def should_be_product_page(self):
        self.should_be_basket_and_product_same_name()
        self.should_be_basket_and_product_same_price()

    def should_be_basket_and_product_same_name(self):
        # Проверка того, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который добавили
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name_basket == product_name_page, \
            f"Product names in page and basket are not the same! {product_name_page} != {product_name_basket}"

    def should_be_basket_and_product_same_price(self):
        # Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices in page and basket are not the same! {product_price} != {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    # def go_add_to_basket(self):
    #     add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
    #     add_to_basket.click()
    #
    # def should_be_message_about_adding(self):
    #     # Сначала проверяем, что элементы присутствуют на странице
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
    #         "Product name is not presented")
    #     assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
    #         "Message about adding is not presented")
    #     # Затем получаем текст элементов для проверки
    #     product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    #     message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
    #     # Проверяем, что название товара присутствует в сообщении о добавлении
    #     assert product_name in message, "No product name in the message"
    #
    # def should_be_message_basket_total(self):
    #     # Сначала проверяем, что элементы присутствуют на странице
    #     assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
    #         "Message basket total is not presented")
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
    #         "Product price is not presented")
    #     # Затем получаем текст элементов для проверки
    #     message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
    #     product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    #     # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
    #     assert product_price in message_basket_total, "No product price in the message"
