"""

@package main

"""
from base.browsersetup import Driver
from pages.login_page import LoginPage

class SurveyMonkeyWebsite():
    """

    SurveyMonkeyWebsite class is a main class to run the project

    """

    def __init__(self):
        """

        INIT SurveyMonkeyWebsite class,get instanc eof broswer by calling get_web_driver_instance
          method of Driver class.

        * :param self: current instance of class

        """
        self.web_driver = Driver()
        self.driver = self.web_driver.get_web_driver_instance()

    def get_survey(self):
        """

        This method call all the methods to run the project
        login,create survey, surveyoperations

        * :param self: current instance of class
        * :return: none

        """
        username = self.web_driver.get_username()
        pass_word = self.web_driver.get_password()
        lp = LoginPage(self.driver)
        lp.login(username, pass_word)
        self.driver.close()

survey_monkey = SurveyMonkeyWebsite()
survey_monkey.get_survey()


