from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "login_submit.button")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "form#add_to_basket_form > button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")