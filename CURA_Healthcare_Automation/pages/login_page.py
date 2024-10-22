from base.base_driver import BaseDriver
from pages.make_appointment_page import MakeAppointmentPage
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods


class LoginPage(BaseDriver):

    # Page Locators
    READONLY_USERNAME_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='Username' and @readonly]")
    READONLY_PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='Password' and @readonly]")
    LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, "#btn-login")
    USERNAME_FIELD_LOCATOR = (By.XPATH, "//input[@id='txt-username']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//input[@id='txt-password']")
    LOGIN_WARNING_TEXT_LOCATOR = (By.XPATH, "//p[contains(@class,'text-danger')]")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_fail(self, username, password, login_status_message):
        CommonMethods.wait_for_element_to_appear(self.driver, self.USERNAME_FIELD_LOCATOR)
        CommonMethods.set_element_text(self.driver, self.USERNAME_FIELD_LOCATOR, username)
        CommonMethods.set_element_text(self.driver, self.PASSWORD_FIELD_LOCATOR, password)
        CommonMethods.click_element(self.driver, self.LOGIN_BTN_LOCATOR)
        login_warning_text = CommonMethods.get_element_text(self.driver, self.LOGIN_WARNING_TEXT_LOCATOR)
        CommonMethods.assert_element_text(self.driver, login_warning_text, login_status_message)

    def login_success(self):
        # Wait for page refresh, get username and password, then login
        CommonMethods.wait_for_element_to_appear(self.driver, self.READONLY_USERNAME_FIELD_LOCATOR)

        username = CommonMethods.get_element_attribute(self.driver, self.READONLY_USERNAME_FIELD_LOCATOR, "value")
        CommonMethods.set_element_text(self.driver, self.USERNAME_FIELD_LOCATOR, username)

        password = CommonMethods.get_element_attribute(self.driver, self.READONLY_PASSWORD_FIELD_LOCATOR, "value")
        CommonMethods.set_element_text(self.driver, self.PASSWORD_FIELD_LOCATOR, password)

        CommonMethods.click_element(self.driver, self.LOGIN_BTN_LOCATOR)

        # Make object for next page and return
        make_appointment = MakeAppointmentPage(self.driver)
        return make_appointment