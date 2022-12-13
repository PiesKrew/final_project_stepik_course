from .base_page import BasePage
from .locators import LoginPageLocators, FixturePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No 'login' in url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def should_be_user_login_message(self):
        try:
            self.browser.is_element_present(*LoginPageLocators.USER_LOGIN)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.USER_LOGIN), "User isn't login the system."

    def should_not_be_error_message(self):
        try:
            self.browser.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE)
        except():
            assert self.browser.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), "There is some error message."

    def register_new_user(self, email, password):
        self.browser.find_element(*FixturePageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*FixturePageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*FixturePageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*FixturePageLocators.BUTTON).click()
        time.sleep(5)
