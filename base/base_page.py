"""
@package base_demo

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver_methods import SeleniumDriver

class BasePage(SeleniumDriver):

    def __init__(self,driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        self.driver = driver