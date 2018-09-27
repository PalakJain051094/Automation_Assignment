from pages.login_page import  LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
from utilities.test_data import *
import logging
import allure

@allure.title("test login class")
@allure.feature("tests")
@pytest.mark.usefixtures("get_driver")
class TestLogin(unittest.TestCase):
    """
     Test class for login survey
    """
    log = cl.customLogger(logging.DEBUG)

    @pytest.allure.step("objectsteup")
    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        """
        This test case is class level setup to get driver

        * :param self: current instance of class
        * :param get_driver: driver
        * :return: none

        """
        self.lp = LoginPage(get_driver)

    @allure.testcase("in valid login testcase")
    @pytest.allure.step("invalid login")
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        """

          This test case  is check invalid login
          assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_invalidLogin started")
        self.lp.logout()
        self.lp.login(username, invalid_password)
        result = self.lp.verify_login_failed()
        assert result == True

    @pytest.allure.step("valid login")
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        """

          This test case check login successfully or not
          assert true if result is true.

        * :param self: current instance of class


        """
        self.log.info("test_validLogin started")
        self.lp.login(username, pass_word)
        result = self.lp.verify_login_successful()
        assert result == True
