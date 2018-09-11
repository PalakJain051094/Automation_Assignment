import pytest
import unittest
from pages.survey_question import SurveyQuestionPage
from utilities.test_data import *
from utilities.custom_logger import *
import logging


@pytest.mark.usefixtures("get_survey")
class TestQuestion(unittest.TestCase):
    """

      Test class for add questions

    """
    log = customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_level_setup(self, get_survey):
        """

        This test case is class level setup to get driver

        * :param self: current instance of class
        * :param get_survey: driver
        * :return: none

        """
        self.survey_questions = SurveyQuestionPage(get_survey)

    @pytest.mark.run(order=1)
    def test_question_1(self):
        """

         This test case check question one added successfully or not
          and assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_question_1 started")
        self.survey_questions.add_question_one(question_no_1)
        result = self.survey_questions.verify_question_one()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=2)
    def test_question_2(self):
        """

         This test case check question two added successfully or not
          and assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_question_2 started")
        self.survey_questions.add_question_two(question_no_2)
        result = self.survey_questions.verify_question_two()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=3)
    def test_question_3(self):
        """

         This test case check question three added successfully or not
          and assert true if result is true.

       * :param self: current instance of class

        """
        self.log.info("test_question_3 started")
        self.survey_questions.add_question_three(question_no_3)
        result = self.survey_questions.verify_question_three()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=4)
    def test_question_4(self):
        """

         This test case check question four added successfully or not
          and assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_question_4 started")
        self.survey_questions.add_question_four(question_no_4)
        result = self.survey_questions.verify_question_four()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=5)
    def test_question_5(self):
        """

         This test case check question five added successfully or not
          and assert true if result is true.

        * :param self: current instance of class

        """
        self.log.info("test_question_5 started")
        self.survey_questions.add_question_five(question_no_5)
        result = self.survey_questions.verify_question_five()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=6)
    def test_question_6(self):
        """

         This test case check question six added successfully or not
          and assert true if result is true.

         * :param self: current instance of class
        """

        self.log.info("test_question_6 started")
        self.survey_questions.add_question_six(question_no_6)
        result = self.survey_questions.verify_question_six()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=7)
    def test_question_7(self):
        """

         This test case check question seven added successfully or not
          and assert true if result is true.

         * :param self: current instance of class

        """
        self.log.info("test_question_7 started")
        self.survey_questions.add_question_seventh(question_no_7)
        result = self.survey_questions.verify_question_seven()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(before='test_question_9')
    def test_question_8(self):
        """

         This test case check question eight added successfully or not
          and assert true if result is true.

          * :param self: current instance of class

        """
        self.log.info("test_question_8 started")
        self.survey_questions.add_question_eight(question_no_8)
        result = self.survey_questions.verify_question_eight()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(order=9)
    def test_question_9(self):
        """

         This test case check question nine added successfully or not
          and assert true if result is true.

         * :param self: current instance of class

        """
        self.log.info("test_question_9 started")
        self.survey_questions.add_question_nine(question_no_9)
        result = self.survey_questions.verify_question_nine()
        self.log.info("Result: " + str(result))
        assert result == True

    @pytest.mark.run(after='test_question_9')
    def test_question_ten(self):
        """

         This test case check question ten added successfully or not
          and assert true if result is true.

           * :param self: current instance of class

        """
        self.log.info("test_question_10 started")
        self.survey_questions.add_question_ten(question_no_10)
        result = self.survey_questions.verify_question_ten()
        self.log.info("Result: " + str(result))
        assert result == True
