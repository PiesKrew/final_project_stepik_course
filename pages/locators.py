from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "login_submit.button")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_LOGIN = (By.XPATH, "//*[@id=\"messages\"]/div")
    ERROR_MESSAGE = (By.XPATH, "//*[@id=\"register_form\"]/div[1]")


class ProductPageLocators:
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1 strong")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div.content")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div:nth-child(n)")


class FixturePageLocators:
    EMAIL = (By.XPATH, "//*[@id=\"id_registration-email\"]")
    PASSWORD1 = (By.XPATH, "//*[@id=\"id_registration-password1\"]")
    PASSWORD2 = (By.XPATH, "//*[@id=\"id_registration-password2\"]")
    BUTTON = (By.XPATH, "//*[@id=\"register_form\"]/button")
