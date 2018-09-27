import unittest
from testcases.test_login import TestLogin
from testcases.test_createsurvey import TestCreateSurvey
from testcases.test_surveyoperation import TestSurveyOperation
from testcases.test_question import TestQuestion



class Test_Suite(unittest.TestCase):
    """
    Test suite to run all test classes
    """

    def test_main(self):
        """

        suite of All TestCases
        * :param self: current instance of class
        * :return: none

        """
        self.suite = unittest.TestSuite()
        tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCreateSurvey)
        tc3 = unittest.TestLoader().loadTestsFromTestCase(TestSurveyOperation)
        tc4 = unittest.TestLoader().loadTestsFromTestCase(TestQuestion)
        self.suite.addTests([tc1, tc2, tc3, tc4])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
