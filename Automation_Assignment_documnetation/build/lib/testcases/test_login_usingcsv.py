from pages.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from ddt import ddt,data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("get_driver")
@ddt
class TestLogin(unittest.TestCase):
    """

    Test class for login survey when data is coming from csv file

    """
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        """

        This test case is class level setup to get driver

        * :param self: current instance of class
        * :param get_driver: driver
        * :return: none

        """
        self.lp = LoginPage(get_driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/Python_workspace/Automation_Assignment\Automation_Assignment_documnetation/logindata.csv"))
    @unpack
    def test_validLogin(self,username, pass_word):
        """
        This test case check login successfully or not
          assert true if result is true.

        * :param self: current instance of class
        * :param username: username
        * :param pass_word: password

        """
        self.log.info("test_validLogin started")
        self.lp.logout()
        self.lp.login(username, pass_word)
        result = self.lp.verify_login_successful()
        assert result == True

