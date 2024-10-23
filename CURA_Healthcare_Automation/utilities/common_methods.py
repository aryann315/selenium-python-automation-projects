from datetime import datetime

class CommonMethods:
    def get_today_date(self):
        today_date  = datetime.today().strftime('%d/%m/%Y')
        return today_date

    def assert_element_text(self, element_text, validation_text):
        assert element_text == validation_text, "Assertion Failed: " + element_text + " != " + validation_text
        print("Assertion Passed: " + element_text + " == " + validation_text)

    def assert_attribute_value(self, attribute_text, validation_value):
        assert attribute_text == validation_value, "Assertion Failed: " + attribute_text + " != " + validation_value
        print("Assertion Passed: " + attribute_text + " == " + validation_value)

