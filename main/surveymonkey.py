from base.browsersetup import Driver
from pages.login_page import LoginPage
from pages.createsurvey import CreateSurvey
from pages.survey_operations import EditElements
from pages.survey_question import SurveyQuestionPage
from utilities.test_data import *


class SurveyMonkeyWebsite():

    def __init__(self):
        web_driver = Driver()
        self.driver = web_driver.get_web_driver_instance()

    def get_survey(self):
        lp = LoginPage(self.driver)
        lp.login(username, pass_word)
        cs = CreateSurvey(self.driver)
        cs.create_survey(first_survey_title)
        edit_survey = EditElements(self.driver)
        edit_survey.survey_operations(new_survey_title, new_page_title)

    def get_questions(self):
        survey_questions = SurveyQuestionPage(self.driver)
        survey_questions.add_question_one(question_no_1)
        survey_questions.add_question_two(question_no_2)
        survey_questions.add_question_three(question_no_3)
        survey_questions.add_question_four(question_no_4)
        survey_questions.add_question_five(question_no_5)
        survey_questions.add_question_six(question_no_6)
        survey_questions.add_question_seventh(question_no_7)
        survey_questions.add_question_eight(question_no_8)
        survey_questions.add_question_nine(question_no_9)
        survey_questions.add_question_ten(question_no_10)
        self.driver.close()

survey_monkey = SurveyMonkeyWebsite()
survey_monkey.get_survey()
survey_monkey.get_questions()