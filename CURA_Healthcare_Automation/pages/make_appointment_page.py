from base.base_driver import BaseDriver
from pages.confirm_appointment_page import ConfirmAppointmentPage
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods


class MakeAppointmentPage(BaseDriver):
    # Page Locators
    APPOINTMENT_SECTION_TITLE_LOCATOR = (By.XPATH, "//h2")
    FACILITY_SELECT_LOCATOR = (By.CSS_SELECTOR, "#combo_facility")
    CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "#chk_hospotal_readmission")

    def get_radio_button_locator(self, option):
        option = option.lower()
        radio_btn_locator = (By.CSS_SELECTOR, "#radio_program_" + option)
        return radio_btn_locator

    COMMENTS_TEXT_AREA_LOCATOR = (By.CSS_SELECTOR, "#txt_comment")
    BOOK_APPOINTMENT_BTN_LOCATOR = (By.CSS_SELECTOR, "#btn-book-appointment")
    VISIT_DATE_LOCATOR = (By.CSS_SELECTOR, "#txt_visit_date")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Page methods
    def enter_details_and_book_appointment(self):
        self.verify_page_heading()
        self.verify_select_dropdown_behaviour()
        self.verify_checkbox_behaviour()
        self.verify_radio_button_behaviour()
        self.verify_text_area_behaviour()
        self.click_book_appointment_button()
        self.verify_mandatory_date_field_behaviour()
        self.click_book_appointment_button()

        # Make object for next page
        confirm_appointment_page = ConfirmAppointmentPage(self.driver)
        return confirm_appointment_page

    def verify_page_heading(self):
        BaseDriver.wait_for_element_to_appear(self.driver, self.APPOINTMENT_SECTION_TITLE_LOCATOR)
        appointment_page_heading = BaseDriver.get_element_text(self.driver, self.APPOINTMENT_SECTION_TITLE_LOCATOR)
        CommonMethods.assert_element_text(self.driver, "Make Appointment", appointment_page_heading)

    def verify_select_dropdown_behaviour(self):
        select_options = ["Hongkong CURA Healthcare Center", "Seoul CURA Healthcare Center","Tokyo CURA Healthcare Center"]

        # Select all the values and assert they are selected
        for option in select_options:
            BaseDriver.select_dropdown_by_value(self.driver, self.FACILITY_SELECT_LOCATOR, option)
            selected_value = BaseDriver.get_selected_dropdown_value(self.driver, self.FACILITY_SELECT_LOCATOR)
            CommonMethods.assert_element_text(self.driver, option, selected_value)

    def verify_checkbox_behaviour(self):
        # Check the checkbox and assert
        BaseDriver.click_element(self.driver, self.CHECKBOX_LOCATOR)
        BaseDriver.is_checked_or_selected(self.driver, self.CHECKBOX_LOCATOR)

        # Uncheck the checkbox and assert
        BaseDriver.click_element(self.driver, self.CHECKBOX_LOCATOR)
        BaseDriver.is_not_checked_or_not_selected(self.driver, self.CHECKBOX_LOCATOR)

    def verify_radio_button_behaviour(self):
        radio_options = ["Medicaid", "None", "Medicare"]

        # Select all the radio buttons, assert they are selected and others are not
        for option in radio_options:
            radio_btn_locator = self.get_radio_button_locator(option)
            BaseDriver.click_element(self.driver, radio_btn_locator)
            BaseDriver.is_checked_or_selected(self.driver, radio_btn_locator)
            radio_button_value = BaseDriver.get_element_attribute(self.driver, radio_btn_locator, "value")
            CommonMethods.assert_attribute_value(self.driver, option, radio_button_value)

            for other_radio in radio_options:
                if other_radio != option:
                    other_radio_locator = self.get_radio_button_locator(other_radio)
                    BaseDriver.is_not_checked_or_not_selected(self.driver, other_radio_locator)

    def verify_text_area_behaviour(self):
        # Enter the text in comments text area and assert
        BaseDriver.set_element_text(self.driver, self.COMMENTS_TEXT_AREA_LOCATOR, "Demo text in comments text area.")
        comments_text_value = BaseDriver.get_element_attribute(self.driver, self.COMMENTS_TEXT_AREA_LOCATOR, "value")
        CommonMethods.assert_attribute_value(self.driver, "Demo text in comments text area.", comments_text_value)

        # Clear the text and assert
        BaseDriver.clear_element_text(self.driver, self.COMMENTS_TEXT_AREA_LOCATOR)
        comments_text_value = BaseDriver.get_element_attribute(self.driver, self.COMMENTS_TEXT_AREA_LOCATOR, "value")
        CommonMethods.assert_attribute_value(self.driver, "", comments_text_value)

        # Enter the text before submitting
        BaseDriver.set_element_text(self.driver, self.COMMENTS_TEXT_AREA_LOCATOR, "Demo text in comments text area.")

    def click_book_appointment_button(self):
        BaseDriver.click_element(self.driver, self.BOOK_APPOINTMENT_BTN_LOCATOR)

    def verify_mandatory_date_field_behaviour(self):
        missing_date_validation_message = BaseDriver.get_element_attribute(self.driver, self.VISIT_DATE_LOCATOR, "validationMessage")

        # Assert the missing date field
        CommonMethods.assert_attribute_value(self.driver, "Please fill", missing_date_validation_message)

        today_date = CommonMethods.get_today_date(self.driver)
        # Enter today's date and book appointment
        BaseDriver.set_element_text(self.driver, self.VISIT_DATE_LOCATOR, today_date)



