from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver

    def get_today_date(self):
        today_date  = datetime.today().strftime('%d/%m/%Y')
        return today_date

    def wait_for_element_to_appear(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def get_element_text(self, locator):
        element_text = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)).text.strip()
        return element_text

    def get_element_attribute(self, locator, attribute):
        element_attribute = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)).get_attribute(
            attribute)
        return element_attribute

    def set_element_text(self, locator, text):
        CommonMethods.clear_element_text(self, locator)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def clear_element_text(self, locator):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)

    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator)).click()

    def assert_element_text(self, element_text, validation_text):
        assert element_text == validation_text, "Assertion Failed: " + element_text + " != " + validation_text
        print("Assertion Passed: " + element_text + " == " + validation_text)

    def assert_attribute_value(self, attribute_text, validation_value):
        assert attribute_text == validation_value, "Assertion Failed: " + attribute_text + " != " + validation_value
        print("Assertion Passed: " + attribute_text + " == " + validation_value)

    def select_dropdown_by_index(self, locator, index):
        select = Select(WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)))
        select.select_by_index(index)

    def select_dropdown_by_value(self, locator, value):
        select = Select(WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)))
        select.select_by_value(value)

    def get_selected_dropdown_value(self, locator):
        select = Select(WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)))
        select_value = select.first_selected_option
        return select_value.text.strip()

    def is_checked_or_selected(self, locator):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        assert element.is_selected() == True, "Assertion Failed: Checkbox / Radio not selected."
        print("Assertion Passed: Checkbox / Radio is selected.")

    def is_not_checked_or_not_selected(self, locator):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        assert element.is_selected() == False, "Assertion Failed: Checkbox / Radio selected."
        print("Assertion Passed: Checkbox / Radio not selected.")