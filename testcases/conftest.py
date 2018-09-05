import pytest
from base.browsersetup import Driver
from pages.login_page import LoginPage
from pages.createsurvey import CreateSurvey
from utilities.test_data import*

@pytest.yield_fixture(scope="class")
def get_driver():
    web_driver = Driver()
    driver = web_driver.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login(username, pass_word)
    yield driver
    driver.quit()

@pytest.yield_fixture(scope="class")
def get_survey():
    web_driver = Driver()
    driver = web_driver.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login(username, pass_word)
    cs = CreateSurvey(driver)
    cs.create_survey(first_survey_title)
    yield driver
    driver.quit()




