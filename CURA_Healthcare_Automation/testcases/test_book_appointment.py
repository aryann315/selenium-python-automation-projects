import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestBookAppointment:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self)

    LOGIN_WARNING_FAIL_MESSAGE = "Login failed! Please ensure the username and password are valid."
    @pytest.mark.parametrize("username, password, login_status_message",
                             [("", "", LOGIN_WARNING_FAIL_MESSAGE),
                              ("wrong_username", "", LOGIN_WARNING_FAIL_MESSAGE),
                              ("", "wrong_password", LOGIN_WARNING_FAIL_MESSAGE),
                              ("wrong_username", "wrong_password", LOGIN_WARNING_FAIL_MESSAGE)])
    def test_login_fail(self, username, password, login_status_message):
        self.lp.login_fail(username, password, login_status_message)

    @pytest.mark.parametrize("select_options, radio_options", [
        (["Hongkong CURA Healthcare Center", "Seoul CURA Healthcare Center","Tokyo CURA Healthcare Center"],
        ["Medicaid", "None", "Medicare"])
    ])
    def test_book_appointment(self, select_options, radio_options):
        make_appointment = self.lp.login_success()
        confirm_appointment_page = make_appointment.enter_details_and_book_appointment(select_options, radio_options)
        confirm_appointment_page.confirm_appointment_details()
        make_appointment.verify_page_heading()

