import re
from datetime import datetime


class ValidationData:
    """

    This class has all methods for validation

    """

    def __init__(self):
        """

        INIT of class ValidationData having dictionary which contains type of all pattern

        """
        self.all_pattern = {'string': '^[a-zA-Z]{1,255}$',
                            'alphanumeric': '^[a-zA-Z0-9]{1,255}$',
                            'specialcharacters': '^[-a-zA-Z0-9!@#$&()`.+,/\"]{1,255}$',
                            'email': '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.com)$',
                            'normal_mb': '^[0-9]{10}',
                            'mobile_no': '^(0|91)-[1-9]{3}-[0-9]{3}-[0-9]{4}$',
                            'phone_no': '^(0|91)-[1-9]{3},[0-9]{3},[0-9]{4}$',
                            'dd/mm/yyyy': '%d/%m/%Y',
                            'mm/dd/yyyy': '%m/%d/%Y',
                            'dd-mm-yyyy': '%d-%m-%Y',
                            'mm-dd-yyyy': '%m-%d-%Y',
                            'yyyy-mm-dd': '%Y-%m-%d',
                            'yyyy/mm/dd': '%Y/%m/%d',
                            'integer': '^[1-9]\d*$',
                            'whole_numbers': '^([0-9]\d*)$',
                            'float': '^[0-9]+\.?[0-9]$',
                            'card_number': '(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}'
                            }

    def get_pattern(self, pattern):
        """

        This method get all patterns
        * :param self:current instance of class
        * :param pattern: pattern for value passed by user
        * :return:
            -pattern -- return pattern from dictionary
            - False -- when no pattern is specify

        """
        if pattern:
            return self.all_pattern[pattern]
        else:
            print("Pattern with " + pattern + " not found")
            return False

    def check_value(self, value, pattern):
        """

        This method check that input value should not be null.
        * :param self: current instance of class
        * :param value: input from user
        * :type value: string
        * :param pattern: pattern input from user
        * :type pattern: string
        * :return:
            -True -- if value is not null
            -False -- if value is null
        * :rtype: boolean
        """
        if value == "":
            print(pattern.upper() + " value is required ")
            return False
        else:
            return True

    def get_valid_value(self, pattern, value):
        """
        This method validate give valid value according to the pattern specify

        * :param self: current instance of class
        * :param pattern: specify by user
        * :type pattern : pattern_type
        * :param value: input value from user
        * :type value :string
        * :return: valid_value

        """
        pattern_type = self.get_pattern(pattern)
        valid_value = re.match(pattern_type, value)
        return valid_value

    def validate_string(self, pattern='alphanumeric', value="", min_length=1, max_length=255):
        """

        This method validate string values according to the pattern specify

        * :param self: current instance of class
        * :param pattern: alphanumeric
        * :type alphanumeric : pattern_type
        * :param value: input value from user
        * :type value :string
        * :param min_length: 1
        * :type min_length: int
        * :param max_length: 255
        * :type max_length: int
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean

        """
        try:
            check_value = self.check_value(value, pattern)
            if check_value is True:
                valid_value = self.get_valid_value(pattern, value)
                if valid_value:
                    print("validation of " + pattern + " with value " + value + " is done successfully")
                    return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False
        except Exception as e:
            print(e)

    def validate_numbers(self, pattern='card_number', value=""):
        """

        This method validate numbers values according to the pattern specify

        * :param self: current instance of class
        * :param pattern: alphanumeric
        * :type alphanumeric : pattern_type
        * :param value: input value from user
        * :type value :string
        * :param min_length: 1
        * :type min_length: int
        * :param max_length: 255
        * :type max_length: int
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean

        """
        try:
            check_value = self.check_value(value, pattern)
            if check_value is True:
                valid_value = self.get_valid_value(pattern, value)
                if valid_value:
                    print("validation of " + pattern + " with value " + value + " is done successfully")
                    return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False
        except Exception as e:
            print(e)

    def validate_date(self, pattern='dd/mm/yyyy', value=""):
        """

         This method validate date values according to the pattern specify

        * :param self: current instance of class
        * :param pattern: dd/mm/yyyy
        * :type dd/mm/yyyy : date pattern_type
        * :param value: input value from user
        * :type value :string
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean

        """
        try:
            check_value = self.check_value(value, pattern)
            if check_value is True:
                pattern_type = self.get_pattern(pattern)
                date_value = datetime.strptime(value, pattern_type)
                if date_value:
                    print("validation of " + pattern + " with value " + str(value) + " is done successfully")
                    return True
                else:
                    return False
        except Exception as e:
            print(str(e) + " , please enter Correct value of " + pattern)

    def date_compare(self, pattern='dd/mm/yyyy', form_date="", to_date=""):
        """

         This method compare dates values according to the pattern specify

        * :param self: current instance of class
        * :param pattern: dd/mm/yyyy
        * :type dd/mm/yyyy : date pattern_type
        * :param form_date: string input from user
        * :param to_date: string input from user
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean

        """

        try:
            check_start_date = self.check_value(form_date, pattern)
            check_end_date = self.check_value(to_date, pattern)
            if check_start_date and check_end_date is True:
                pattern_type = self.get_pattern(pattern)
                start = datetime.strptime(form_date, pattern_type)
                end = datetime.strptime(to_date, pattern_type)
                if end < start:
                    print("End date" + str(to_date) + " can't be previous then start date " + str(form_date))
                    return False
                else:
                    print("validation of " + pattern + " with form_date " + str(form_date) + "and to_date " +
                          str(to_date) + " is done successfully ")
                    return True
        except Exception as e:
            print(str(e) + " , please enter Correct value of " + pattern)
