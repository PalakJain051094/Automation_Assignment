.. Automation_Assignment documentation master file, created by
   sphinx-quickstart on Mon Sep 10 15:28:58 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Automation_Assignment's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


base.base_page
==================
.. automodule:: base.base_page
.. autoclass:: BasePage
  :members:
  :special-members:

base.browsersetup
==================
.. automodule:: base.browsersetup
.. autoclass:: Driver
  :members:
  :special-members:

pages.login_page
==================
.. automodule:: pages.login_page
.. autoclass:: LoginPage
  :members:
  :special-members:

pages.createsurvey
====================================
.. automodule:: pages.createsurvey
.. autoclass:: CreateSurvey
  :members:
  :special-members:

pages.survey_operations
====================================
.. automodule:: pages.survey_operations
.. autoclass:: EditElements
  :members:
  :special-members:

pages.survey_question
====================================
.. automodule:: pages.survey_question
.. autoclass:: SurveyQuestionPage
  :members:
  :special-members:


testcases.test_createsurvey
====================================
.. automodule:: testcases.test_createsurvey
.. autoclass:: TestCreateSurvey
  :members:


testcases.conftest
==================
.. automodule:: testcases.conftest
  :members: get_driver,get_survey


testcases.test_login
====================================
.. automodule:: testcases.test_login
.. autoclass:: TestLogin
  :members:
  :special-members:

testcases.test_login_usingcsv
====================================
.. automodule:: testcases.test_login_usingcsv
.. autoclass:: TestLogin
  :members:


testcases.test_question
====================================
.. automodule:: testcases.test_question
.. autoclass:: TestQuestion
  :members:

testcases.test_surveyoperation
====================================
.. automodule:: testcases.test_surveyoperation
.. autoclass:: TestSurveyOperation
  :members:


utilities.custom_logger
====================================
.. automodule:: utilities.custom_logger
.. autofunction:: customLogger



utilities.read_data
====================================
.. automodule:: utilities.read_data
.. autofunction:: getCSVData









