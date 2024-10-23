from datetime import datetime

class CommonMethods:
    def get_today_date(self):
        today_date  = datetime.today().strftime('%d/%m/%Y')
        return today_date

    def assert_element_text(self, validation_text, element_text):
        assert validation_text in element_text, "Assertion Failed: " + element_text + " != " + validation_text
        print("Assertion Passed: " + element_text + " == " + validation_text)

    def assert_attribute_value(self, validation_text, attribute_text):
        assert validation_text in attribute_text, "Assertion Failed: " + attribute_text + " != " + validation_text
        print("Assertion Passed: " + attribute_text + " == " + validation_text)

