from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods


class ConfirmAppointmentPage(BaseDriver):

    # Page Locators
    APPOINTMENT_SECTION_TITLE_LOCATOR = (By.XPATH, "//h2")
    APPOINTMENT_BOOKED_MESSAGE_LOCATOR = (By.XPATH, "//h2/../p")
    FACILITY_INFORMATION_LOCATOR = (By.CSS_SELECTOR, "#facility")
    HOSPITAL_READMISSION_VALUE_LOCATOR = (By.CSS_SELECTOR, "#hospital_readmission")
    HEALTHCARE_PROGRAM_LOCATOR = (By.CSS_SELECTOR, "#program")
    VISIT_DATE_LOCATOR = (By.CSS_SELECTOR, "#visit_date")
    COMMENT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#comment")
    GOTO_HOMEPAGE_BTN_LOCATOR = (By.XPATH, "//a[text()='Go to Homepage']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def confirm_appointment_details(self):
        self.verify_page_heading()
        self.verify_booking_status()
        self.verify_facility_information()
        self.verify_hospital_readmission()
        self.verify_healthcare_program()
        self.verify_appointment_date()
        self.verify_appointment_comments()
        self.go_to_homepage()

    def verify_page_heading(self):
        CommonMethods.wait_for_element_to_appear(self.driver, self.APPOINTMENT_SECTION_TITLE_LOCATOR)
        appointment_page_heading = CommonMethods.get_element_text(self.driver, self.APPOINTMENT_SECTION_TITLE_LOCATOR)
        CommonMethods.assert_element_text(self.driver, appointment_page_heading,  "Appointment Confirmation")

    def verify_booking_status(self):
        appointment_booking_status_message = CommonMethods.get_element_text(self.driver, self.APPOINTMENT_BOOKED_MESSAGE_LOCATOR)
        CommonMethods.assert_element_text(self.driver, appointment_booking_status_message,
                                          "Please be informed that your appointment has been booked as following:")

    def verify_facility_information(self):
        facility_information_value= CommonMethods.get_element_text(self.driver, self.FACILITY_INFORMATION_LOCATOR)
        CommonMethods.assert_element_text(self.driver, facility_information_value,  "Tokyo CURA Healthcare Center")

    def verify_hospital_readmission(self):
        hospital_readmission_value = CommonMethods.get_element_text(self.driver, self.HOSPITAL_READMISSION_VALUE_LOCATOR)
        CommonMethods.assert_element_text(self.driver, hospital_readmission_value,  "No")

    def verify_healthcare_program(self):
        healthcare_program_value = CommonMethods.get_element_text(self.driver, self.HEALTHCARE_PROGRAM_LOCATOR)
        CommonMethods.assert_element_text(self.driver, healthcare_program_value,  "Medicare")

    def verify_appointment_date(self):
        today_date = CommonMethods.get_today_date(self)
        CommonMethods.assert_element_text(self.driver, today_date, CommonMethods.get_today_date(self.driver))

    def verify_appointment_comments(self):
        comment_value = CommonMethods.get_element_text(self.driver, self.COMMENT_VALUE_LOCATOR)
        CommonMethods.assert_element_text(self.driver, comment_value,  "Demo text in comments text area.")

    def go_to_homepage(self):
        CommonMethods.click_element(self.driver, self.GOTO_HOMEPAGE_BTN_LOCATOR)
