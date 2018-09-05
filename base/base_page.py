"""
@package base_demo

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

"""
from base.browsersetup import Driver

class BasePage(Driver):

    def __init__(self,driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        self.driver = driver
