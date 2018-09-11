"""

@package pages

"""
from base.base_page import BasePage
import time


class EditElements(BasePage):
    """

    This class Edit survey elements like survey page title and survey title

    """

    def __init__(self, driver):
        """

        init of EditElements class

        * :param self: current instance of class
        * :param driver: web driver

        """
        super().__init__(driver)
        self.driver = driver

    # locator

    _survey_title = "//table[@role='presentation']//span[@class='title-text']"
    _survey_title_box = "surveyTitle"
    _save_new_survey_title = "//form[@id='surveyTitleForm']//a[text()='SAVE']"
    _pagetitle_edit = "//span[text()='PAGE TITLE']"
    _page_title = "pageTitle"
    _save_pagetitle = " //form[@id='pageTitleForm']//a[text()='SAVE'] "
    _survey_title_verify = "//div[@id='livePreview']//div[@class='survey-title-table-wrapper']"
    _page_title_verify = "//div[@id='livePreview']//span[@class='page-title user-generated']"

    def survey_title_link(self):
        """

        This method click survey title link

        * :param self: current instance of class
        * :return: none

        """
        self.wait_for_element(locator=self._survey_title, locator_type="xpath")
        self.element_click(self._survey_title, locator_type="xpath")

    def send_survey_title(self, new_survey_title):
        """

        This method send survey title to element

        * :param self: current instance of class
        * :param new_survey_title: new survey title
        * :type new_survey_title: string
        * :return: none

        """
        self.wait_for_element(locator=self._survey_title_box, locator_type="xpath", pollFrequency=1)
        self.clear_field(locator=self._survey_title_box)
        self.send_keys(new_survey_title, self._survey_title_box)

    def save_survey(self):
        """

        This method  save survey title

        * :param self: current instance of class
        * :return: none

        """
        self.wait_for_element(locator=self._save_new_survey_title, locator_type="xpath", pollFrequency=1)
        self.element_click(self._save_new_survey_title, locator_type="xpath")

    def edit_survey_title(self, new_survey_title=""):
        """

        This method has all methods for edit survey title

        * :param self: current instance of class
        * :param new_survey_title: survey title
        * :return: none

        """
        EditElements.survey_title_link(self)
        EditElements.send_survey_title(self, new_survey_title)
        EditElements.save_survey(self)

    def page_title_link(self):
        """

        This method click on page title link

        * :param self: current instance of class
        * :return: none

        """
        time.sleep(5)
        self.element_click(self._pagetitle_edit, locator_type="xpath")

    def send_page_title(self, new_page_title):
        """

        This method send page title data to element

        * :param self: current instance of class
        * :param new_page_title: page title
        * :type new_page_title: string
        * :return: none

        """

        self.send_keys(new_page_title, self._page_title)

    def save_page_title(self):
        """

        This method save page title

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._save_pagetitle, locator_type="xpath")

    def edit_page_title(self, new_page_title=""):
        """

        This method call all method to edit page title

        * :param self: current instance of class
        * :param new_page_title: new page title
        * :type new_page_title: string
        * :return: none

        """
        EditElements.page_title_link(self)
        EditElements.send_page_title(self, new_page_title)
        EditElements.save_page_title(self)

    def survey_operations(self, new_survey_title="", new_page_title=""):
        """

        This method call survey operation like edit survey title and edit page title.

        * :param self: current instance of class
        * :param new_survey_title: new survey title
        * :type new_survey_title: string
        * :param new_page_title: new page title
        * :type new_page_title: string
        * :return: none

        """
        EditElements.edit_survey_title(self, new_survey_title)
        EditElements.edit_page_title(self, new_page_title)

    def verify_survey_title(self):
        """

        This method verify survey title is edited or not

        * :param self: current instance of class
        * :return: result  - True or False
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean

        """
        self.wait_for_element(locator=self._survey_title_verify, locator_type="xpath")
        result = self.is_element_present(locator=self._survey_title_verify, locator_type="xpath")
        return result

    def verify_page_title(self):
        """

        This method verify page_title is successfully edited or not

        * :param self: current instance of class
        * :return: result - True or False
            - True -- if element is present
            -  False -- if element is not present
        * :rtype: Boolean

        """
        self.wait_for_element(locator=self._page_title_verify, locator_type="xpath")
        result = self.is_element_present(locator=self._page_title_verify, locator_type="xpath")
        return result
