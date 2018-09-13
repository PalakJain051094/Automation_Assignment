import re
from datetime import datetime



class ValidationData():
    """

    This class has all methods for validation

    """

    def __init__(self):
        """

        INIT of class ValidationData having dictionary which contains type of all pattern

        """
        self.all_pattern = {'string': '^[a-zA-Z]+$',
                            'alphanumeric': '^[a-zA-Z0-9]{1,255}$',
                            'specialcharacters': '^[-a-zA-Z0-9!@#$&()`.+,/\"]{1,255}$',
                            'email': '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.com)$',
                            'normal_mb': '^[0-9]{10}',
                            'mobile_no': '^(0|91)-[1-9]{3}-[0-9]{3}-[0-9]{4}$',
                            'phone_no': '^[9,1]{2}-[1-9]{3},[0-9]{3},[0-9]{4}$',
                            'dd/mm/yyyy': '%d/%m/%Y',
                            'mm/dd/yyyy': '%m/%d/%Y',
                            'dd-mm-yyyy': '%d-%m-%Y',
                            'mm-dd-yyyy': '%m-%d-%Y',
                            'yyyy-mm-dd':'%Y-%m-%d',
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
        if pattern == 'string':
            return self.all_pattern['string']
        if pattern == 'alphanumeric':
            return self.all_pattern['alphanumeric']
        elif pattern == 'specialcharacters':
            return self.all_pattern['specialcharacters']
        elif pattern == 'email':
            return self.all_pattern['email']
        elif pattern == 'normal_mb':
            return self.all_pattern['normal_mb']
        elif pattern == 'mobile_no':
            return self.all_pattern['mobile_no']
        elif pattern == 'phone_no':
            return self.all_pattern['phone_no']
        elif pattern == 'dd/mm/yyyy':
            return self.all_pattern['dd/mm/yyyy']
        elif pattern == 'mm/dd/yyyy':
            return self.all_pattern['mm/dd/yyyy']
        elif pattern == 'dd-mm-yyyy':
            return self.all_pattern['dd-mm-yyyy']
        elif pattern == 'mm-dd-yyyy':
            return self.all_pattern['mm-dd-yyyy']
        elif pattern == 'yyyy-mm-dd':
            return self.all_pattern['yyyy-mm-dd']
        elif pattern == 'yyyy/mm/dd':
            return self.all_pattern['yyyy/mm/dd']
        elif pattern == 'integer':
            return self.all_pattern['integer']
        elif pattern == 'whole_numbers':
            return self.all_pattern['whole_numbers']
        elif pattern == 'float':
            return self.all_pattern['float']
        elif pattern == 'card_number':
            return self.all_pattern['card_number']
        else:
            print("Pattern with " + pattern + " not found")
            return False

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
            if value == "":
                print(pattern + "Value is required with minimum length of " + min_length + "and with maximum length of"
                      + max_length)
                return False
            else:
                pattern_type = self.get_pattern(pattern)
                valid_value = re.match(pattern_type, value)
                if valid_value and len(value) <= max_length:
                    print("validation of " + pattern + " with value " + value + " is done successfully")
                    return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False
        except Exception as e:
            print(e)

    def validate_email(self, pattern='email', value=""):
        """

        This method validate email value according to the pattern specify

        * :param self: current instance of class
        * :param pattern: email
        * :type email : pattern_type
        * :param value: input value from user
        * :type value :string
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean

        """
        try:
            if value == "":
                print(pattern + "Value is required")
                return False
            else:
                pattern_type = self.get_pattern(pattern)
                valid_value = re.match(pattern_type, value)
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
            if value == "":
                print(pattern + "Value is required")
                return False
            else:
                pattern_type = self.get_pattern(pattern)
                value = datetime.strptime(value, pattern_type)
                if value:
                    print("validation of " + pattern + " with value " + str(value) + " is done successfully")
                    return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False

        except Exception as e:
            print(e)

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
            if form_date == "" or to_date == "":
                print(pattern + "Value is required")
                return False
            else:
                pattern_type = self.get_pattern(pattern)
                start = datetime.strptime(form_date, pattern_type)
                end = datetime.strptime(to_date, pattern_type)
                if start and end:
                    if end < start:
                        print("end date" + str(to_date) + "can't be previous then start date" + str(form_date))
                        return False
                    else:
                        print("validation of " + pattern + " with to_date " + str(to_date) + "and form_date " + str(form_date) +
                              " is done successfully")
                        return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False

        except Exception as e:
            print(e)

    def validate_numbers(self, pattern='integer', value=""):
        """

        This method validate numbers  according to the pattern specify

        * :param self: current instance of class
        * :param pattern: integer
        * :type integer : number  pattern_type
        * :param value: input value from user
        * :type value :string
        * :return:
           -True -- if validation done
           -False -- if validation fails
        * :rtype : Boolean
        """
        try:
            if value == "":
                print(pattern + "Value is required")
                return False
            else:
                pattern_type = self.get_pattern(pattern)
                valid_value = re.match(pattern_type, value)
                if valid_value:
                    print("validation of " + pattern + " with value " + value + " is done successfully")
                    return True
                else:
                    print("Enter correct value of  " + pattern)
                    return False
        except Exception as e:
            print(e)
