"""
@ package base
It has all drivers  methods which are common to all the pages throughout the application

For example: driver.sendkeys()

"""
from selenium import webdriver
import os
from base.browserconfig import *
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.custom_logger import*
from selenium.webdriver.common.action_chains import ActionChains


class Driver():
    """

    This class has all driver methods

    """
    log = customLogger(logging.DEBUG)

    def __init__(self):
        """

        * :param self: current instance of class

        """
        browser_type = browser.upper()

    def get_web_driver_instance(self):
        """

        This method get the web driver instance

        * :param self: current instance of class
        * :return:
           - chrome driver -- if browser is chrome
           - Internet explorer driver -- if browser is IE
           - firefox driver -- if browser is FIREFOX

        """
        browser_type = browser.upper()
        if (browser_type == "CHROME"):
            return Driver.set_chrome_driver(self)
        elif (browser_type == "IE"):
            return Driver.set_fire_fox_driver(self)
        elif (browser_type == "FIREFOX"):
            return Driver.set_internet_explorer(self)
        else:
            print("Not a Valid browser Please enter 'chrome','ie' or 'firefox' only ")

    def set_chrome_driver(self):
        """

        This method set driver for chrome broswer

        * :param self: current instance of class
        * :return: driver

        """
        driverlocation = "D:\\Python_workspace\\seleniumlib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def set_fire_fox_driver(self):
        """
        This method set driver for firefox broswer

        * :param self: current instance of class
        * :return driver:

        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def set_internet_explorer(self):
        """

        This method set driver for IE broswer

        * :param self: current instance of class
        * :return: driver

        """
        driverlocation="D:\\Python_workspace\\seleniumlib\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"]=driverlocation
        self.driver=webdriver.Ie(driverlocation)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def get_by_type(self, locator_type):
        """

        This method get element locator type.

        * :param self: current instance of class
        * :param locator_type: element locator type
        * :type locator_type: id,name,xpath,class,link
        * :return:
           - By.ID  -- if loctor_type is id
           - By.NAME -- if loctor_type is name
           - By.XPATH -- if loctor_type is xpath
           - By.CSS --  if loctor_type is css
           - By.CLASS_NAME -- if loctor_type is class
           - By.LINK_TEXT -- if loctor_type is link
        * :return False: when loctaor_type is not correct
        * :rtype False:Boolean

        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")
            return False

    def get_element(self, locator, locator_type="id"):
        """

        This method find element with provided locator and locator
        and take type from get_by_type method

        * :param self: current instance of class
        * :param self: current instance of class
        * :param locator: element locator for example xpath of element
        * :param locator_type: id
        * :return: element

        """
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """

        This method perform click action on the found element by get_element method
        Provided element or combination of locator and locator_type

        * :param self: current instance of class
        * :param locator: element loctaor
        * :param locator_type: id
        * :param element: none
        * :return none:

        """

        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        """
        This method perform send_keys action on founded element by get_element method
        Provided element or combination of locator and locator_type

        * :param self: current instance of class
        * :param data: data to be send on element
        * :param locator: element locator
        * :param locator_type: id
        * :param element: none
        * :return: none

        """

        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def clear_field(self, locator="", locator_type="id"):
        """
        This method clear field of element and
        element is get by get_element method,

        * :param self: current instance of class
        * :param locator: element locator
        * :param locator_type: id
        * :return: none

        """

        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locator_type)

    def wait_for_element(self, locator, locator_type="id",
                         timeout=60, pollFrequency=1):
        """

        This method will wait for element till element not found

        * :param self: current instance of class
        * :param locator: element locator
        * :param locator_type: id
        * :param timeout: 60sec
        * :param pollFrequency: 1
        * :return: element

        """
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def is_element_present(self, locator="", locator_type="id", element=None):
        """

        This method check element is present or not.
        Provided element or combination of locator and locator_type

       * :param self: current instance of class
       * :param locator: element locator
       * :param locator_type: id
       * :param element: none
       * :returns:
       * :return True: if element is present
       * :return False: if element is not present

        """

        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            self.log.info("Element not found")
            return False

    def web_scroll(self, direction="up"):
        """

        This method scroll the element in direction up or down

        * :param self: current instance of class
        * :param direction: up
        * :return: none

        """

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

        # method to do drag and drop it requries source and destination element

    def drag_drop(self, source_locator, destination_locator, locator_type="id"):
        """

        This method perform drag and drop action on element and get element from get_element method.
          Provided element or combination of locator and locator_type

        * :param self: current instance of class
        * :param source_locator: source element loctaor
        * :param destination_locator: destination element loctaor
        * :param locator_type: id
        * :return: none

        """
        source_element = None    # source_element is none initally
        destination_element = None  # destination_element is none initally
        try:
            if source_locator:
                source_element = self.get_element(source_locator, locator_type)
                self.log.info("source_element is found " + source_locator +
                              "with locator type" + locator_type)
            if destination_locator:
                destination_element = self.get_element(destination_locator, locator_type)
                self.log.info("destination element is found " + destination_locator +
                              "with locator type" + locator_type)
            actionChains = ActionChains(self.driver)
            self.log.info(actionChains)
            actionChains.drag_and_drop(source_element, destination_element).perform()
            self.log.info("drag and drop done")
        except:
            self.log.info("Cannot perfrom drag nad drop " + source_locator +
                          " locatorType: " + locator_type)
            print_stack()
