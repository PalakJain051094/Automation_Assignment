import pytest
import unittest
from pages.survey_operations import EditElements
from utilities.test_data import *
from utilities.custom_logger import *
import logging


@pytest.mark.usefixtures("get_survey")
class TestSurveyOperation(unittest.TestCase):
    """

       Test class for survey operations like edit page and survey title

    """
    log = customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_level_setup(self,get_survey):
        """

         This test case is class level setup to get driver

        * :param self: current instance of class
        * :param get_survey: driver
        * :return: none

        """
        self.operation_survey=EditElements(get_survey)

    @pytest.mark.run(order=1)
    def test_surveytitle(self):
        """

         This test case check question survey title edited  successfully or not
          and assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_survey_title started")
        self.operation_survey.edit_survey_title(new_survey_title)
        result = self.operation_survey.verify_survey_title()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=2)
    def test_pagetitle(self):
        """

         This test case check page title added successfully or not
          and assert true if result is true.

         * :param self: current instance of class

        """
        self.log.info("test_page_title started")
        self.operation_survey.edit_page_title(new_page_title)
        result = self.operation_survey.verify_page_title()
        self.log.info("Result: " + str(result))
        assert result == True
