from validation.validationdata import ValidationData


class CallValidation:
    """

    This class call all validation methods

    """

    def __init__(self):
        """

        Init of class CallValidation

        """
        self.validate_data = ValidationData()

    def start_call(self):
        """

        This method call all validation method

        :param self: current instance of class
        :return: none

        """
        self.validate_data.validate_string(pattern="alphanumeric", value="palakjain05")
        self.validate_data.validate_numbers(pattern='card_number', value="1234-5694-8961-4586")
        self.validate_data.validate_date(value="10/10/2018")
        self.validate_data.date_compare(pattern='dd-mm-yyyy', form_date="10-10-2017", to_date="28-02-2018")


start_validation = CallValidation()
start_validation.start_call()
