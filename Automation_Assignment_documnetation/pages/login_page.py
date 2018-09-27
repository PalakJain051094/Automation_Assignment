"""

@package pages

"""
from base.base_page import BasePage


class LoginPage(BasePage):
    """

    This class inhert BasePage and has methods to login on survey monkey

    """

    def __init__(self, driver):
        """

        init of LoginPage

        * :param self: current instance of class
        * :param driver: web driver

        """
        super().__init__(driver)
        self.driver = driver

    #locator
    _login_link = "//a[text()='LOG IN']"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[@type='submit']"
    _login_success = "userAcctTab_MainMenu"
    _login_fail = "//div[@id='sign-in']//li[contains(text(),'The username or password you entered is incorrect')]"
    _logout = "//li[@id='dd-my-account']//a[text()='Sign Out']"

    def click_login_link(self):
        """

        This method click on login link

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._login_link, locator_type="xpath")

    def enter_email(self, email):
        """

        This method send email/username to element

        * :param self: current instance of class
        * :param email: username
        * :type email: string
        * :return: none

        """
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        """

        This method send password to element

        * :param self: current instance of class
        * :param password: password
        * :type password: string
        * :return: none

        """
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        """

        This method click on login button

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._login_button, locator_type="xpath")

    def login(self, email="", password=""):
        """

        This method login to survey monkey

        * :param self: current instance of class
        * :param email: email/username
        * :type email: string
        * :param password: password
        * :type password :string
        * :return: none

        """
        LoginPage.click_login_link(self)
        self.clear_field(locator=self._email_field)
        LoginPage.enter_email(self, email)
        self.clear_field(locator=self._password_field)
        LoginPage.enter_password(self, password)
        LoginPage.click_login_button(self)

    def logout(self):
        """

        This method logout from survey monkey

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(locator=self._login_success)
        self.element_click(locator=self._logout, locator_type="xpath")

    def verify_login_successful(self):
        """

        This method verify login success

        * :param self: current instance of class
        * :return: result -- True or False
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean

        """
        self.wait_for_element(locator=self._login_success, timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._login_success)
        return result

    def verify_login_failed(self):
        """

        This method check failer of login

        * :param self: current instance of class
        * :return: result -- True or False
            - True -- if element is present
            - False -- if element is not prsent
        * :rtype: Boolean

        """
        result = self.is_element_present(locator=self._login_fail, locator_type="xpath")
        return result
