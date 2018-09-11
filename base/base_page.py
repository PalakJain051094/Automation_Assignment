"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.browsersetup import Driver

class BasePage(Driver):

    def __init__(self,driver):
        """
        Inits BasePage class

        :argument:

        :param self: current instance of class

        :param driver: web driver

        Returns:none
            None
        """
        self.driver = driver