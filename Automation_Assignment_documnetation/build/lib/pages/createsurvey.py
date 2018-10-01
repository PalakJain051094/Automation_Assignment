"""

@package pages

"""
from base.base_page import BasePage


class CreateSurvey(BasePage):
    """

    This class inherit BasePage class and has methods to create survey.

    """

    def __init__(self, driver):
        """
        INIT of CreateSurvey

        * :param self: current instance of class
        * :param driver: web driver
        * :return none:

        """
        super().__init__(driver)
        self.driver = driver

    # loactors
    _create_survey_link = "//a[text()='CREATE SURVEY']"
    _survey_name_textbox = "surveyTitle"
    _survey_options = "//div[text()='Survey category']"
    _category_list=['react-select-2--option-']
    _select_community =_category_list[0]+str(0)
    _select_customer_feedback = _category_list[0]+str(1)
    _select_customer_satisfaction = _category_list[0]+str(2)
    _select_demographics = _category_list[0]+str(3)
    _select_education = _category_list[0]+str(4)
    _select_events = _category_list[0]+str(5)
    _select_healthcare = _category_list[0]+str(6)
    _select_human_resources = _category_list[0]+str(7)
    _select_industry_specific = _category_list[0]+str(8)
    _select_just_for_fun = _category_list[0]+str(9)
    _select_market_research = _category_list[0]+str(10)
    _select_non_profit = _category_list[0]+str(11)
    _select_political = _category_list[0]+str(12)
    _select_other = _category_list[0]+str(13)
    _create_survey_button = "//button[text()='CREATE SURVEY']"
    _popup_Remove = "//div[@class='dialog-btn-bar']//a[contains(text(),'REMOVE')]"
    _survey_body = "create"
    _from_scratch = "scratch"
    _design_survey="//a[text()='DESIGN SURVEY']"

    def click_survey_link(self):
        """

        This method  click on survey link when survey is creating for first time.

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._create_survey_link, locator_type="xpath")

    def click_from_scratch_link(self):
        """

        This method click on from_scratch_link to create survey

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._from_scratch)

    def send_title(self,first_survey_title):
        """

        This method send title of surevy

        * :param self: current instance of class
        * :param first_survey_title: surevy title
        * :type first_survey_title: string
        * :return: none

        """
        self.send_keys(first_survey_title, self._survey_name_textbox)

    def send_survey_category(self):
        """

         This method send survey category

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._survey_options, locator_type="xpath")

    def select_option(self):
        """

        This method select survey option

        * :param self:current instance of class
        * :return: none

        """
        self.element_click(self._select_political,locator_type="id")

    def save_survey(self):
        """

        This method save survey

        * :param self: current instance of class
        * :return: none

        """

        self.element_click(self._create_survey_button,locator_type="xpath")

    def handle_remove_popuup(self):
        """

        This method remove popup

        * :param self: current instance of class
        * :return: none

        """
        self.element_click(self._popup_Remove, locator_type="xpath")

    def create_survey(self, first_survey_title=""):
        """

        This method create survey

        * :param self: current instance of class
        * :param first_survey_title: survey title
        * :type first_survey_title: string
        * :return: none

        """
        CreateSurvey.click_survey_link(self)
        if(self.is_element_present(locator=self._from_scratch)):
            CreateSurvey.click_from_scratch_link(self)
        CreateSurvey.send_title(self, first_survey_title)
        CreateSurvey.send_survey_category(self)
        CreateSurvey.select_option(self)
        CreateSurvey.save_survey(self)
        if(self.is_element_present(locator=self._popup_Remove, locator_type="xpath")):
            CreateSurvey.handle_remove_popuup(self)

    def verify_createsurvey_successful(self):
        """

        This method verify creation of survey

        * :param self: current instance of class
        * :return: result-- True or False
            - True -- if element is present
            - False -- if element is not prsent
        * :rtype Boolean

        """
        self.wait_for_element(locator=self._design_survey,locator_type="xpath")
        result = self.is_element_present(locator=self._design_survey, locator_type="xpath")
        return result
