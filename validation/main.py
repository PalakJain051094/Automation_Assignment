from validation.validationdata import ValidationData


class CallValidation():
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
        self.validate_data.validate_string(pattern='alphanumeric', value="palakjain123")
        self.validate_data.validate_email(pattern='email', value="palak.jain5@gmail.com")
        self.validate_data.validate_date(pattern='mm-dd-yyyy', value="10-05-1994")
        self.validate_data.date_compare(form_date="12/09/2018", to_date="09/10/2018")
        self.validate_data.validate_numbers(pattern='card_number', value="1234-5678-1456-7895")


start_validation = CallValidation()
start_validation.start_call()
