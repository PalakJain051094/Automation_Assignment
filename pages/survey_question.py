"""

@package -page

"""
from base.base_page import BasePage
import time
from utilities.test_data import*


class SurveyQuestionPage(BasePage):
    """
    
    This class add survey questions 
    
    """

    def __init__(self, driver):
        """
        
        init of SurveyQuestionPage
         
        * :param self: current instance of class
        * :param driver: driver
        
        """
        super().__init__(driver)
        self.driver = driver
    
    #locator
    
    # Add questions in survey
    _design = "//li[@title='Builder']"
    _question_title_box = "editTitle"
    _editquestion_div = "editQuestion"
    _question_type = "changeQType"
    _save_question = "//div[@id='editQuestion']//section[@class='t1']//a[text()='SAVE']"
    _new_question = "//div[@id='livePreview']//a[text()='NEW QUESTION']"
    _destination = "//div[@class='add-question-btn zero-state-hide ui-droppable']"

    # question 1
    _question_1_type = "//div[@id='builderQuestionContainer']//span[text()='Single Textbox']"

    # question 2
    _question_2_type = "//div[@id='builderQuestionContainer']//span[text()='Multiple Choice']"
    _question_two_select_type = "//option[contains(text(),'Always - Never')]"
    _question_select_choice = "answerBankCategorySelect"

    # question 3
    _question_third_type = "//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
    _time_info_box = "//table[@id='rows']//label[text()='Time Info']"

    # question 4
    _question_four_type = "//ul[@class='add-q-menu-left']//a[text()='Star Rating']"

    # question 5
    _question_five_type = "//div[@id='builderQuestionContainer']//span[text()='Dropdown']"
    _question_select_choice = "answerBankCategorySelect"

    # question 6
    _question_six_type = "//ul[@class='add-q-menu-left']//a[text()='Checkboxes']"
    _checkbox_1 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/div[1]"
    _checkbox_2 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/div[1]"
    _checkbox_3 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[2]/div[1]/div[1]"
    _checkbox_4 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[7]/td[2]/div[1]/div[1]"
    _checkbox_5 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/div[1]"

    # question 7
    _question_seven_type = "//ul[@class='add-q-menu-right']//a[text()='Matrix / Rating Scale']"
    _row_label_1 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _row_label_2 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _row_label_3 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _column_label_1 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]"
    _column_label_2 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _column_label_3 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _column_label_4 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _remove_label = "//tr[6]//a[@title='Delete this choice.']"

    # question 8
    _question_eight_type = "//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"
    _multiple_textbox_level_1 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _multiple_textbox_level_2 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _multiple_textbox_level_3 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"

    # question 9
    _question_nine_select_type = "//option[contains(text(),'Yes - No')]"

    # question 10
    _question_ten_type = "//div[@id='builderQuestionContainer']//span[text()='Comment Box']"

    #verify questions
    _text_1 = "//h4[@class='question-title-container']//span[text()='"+ question_no_1+"']"
    _text_1_type="//a[@id='changeQType']//span[text()='" + type_singletextbox + "']"
    _text_2 = "//span[text()='"+ question_no_2+"']"
    _text_2_type = "//a[@id='changeQType']//span[text()='" + type_multiplechoice + "']"
    _text_3 = "//span[text()='"+ question_no_3+"']"
    _text_3_type = "//a[@id='changeQType']//span[text()='" + type_datetime + "']"
    _text_4 = "//span[text()='"+ question_no_4+"']"
    _text_4_type = "//a[@id='changeQType']//span[text()='" + type_starrating + "']"
    _text_5 = "//span[text()='"+ question_no_5+"']"
    _text_5_type = "//a[@id='changeQType']//span[text()='" + type_dropdown + "']"
    _text_6 = "//span[text()='"+ question_no_6+"']"
    _text_6_type = "//a[@id='changeQType']//span[text()='" + type_checkboxes + "']"
    _text_7 = "//span[text()='"+ question_no_7+"']"
    _text_7_type = "//a[@id='changeQType']//span[text()='" + type_matrix + "']"
    _text_8 = "//span[text()='"+ question_no_8+"']"
    _text_8_type = "//a[@id='changeQType']//span[text()='" + type_multipletextbox + "']"
    _text_9 = "//span[text()='"+ question_no_9+"']"
    _text_9_type = "//a[@id='changeQType']//span[text()='" + type_multiplechoice + "']"
    _text_10 = "//span[text()='"+ question_no_10+"']"
    _text_10_type = "//a[@id='changeQType']//span[text()='" + type_commentbox + "']"

    #checkboxes loctaor
    _check_box1="//div[text()='"+ checkbox_1_data+"']"
    _check_box2 = "//div[text()='" + checkbox_2_data + "']"
    _check_box3 = "//div[text()='" + checkbox_3_data + "']"
    _check_box4 = "//div[text()='" + checkbox_4_data + "']"
    _check_box5 = "//div[text()='" + checkbox_5_data + "']"

    #multiple textboxes locator
    _first_texbox = "//div[text()='1']"
    _second_texbox = "//div[text()='2']"
    _third_texbox = "//div[text()='3']"

    # matrix rating locator
    _row_1="//div[text()='"+ scale_1+"']"
    _row_2 = "//div[text()='" + scale_2 + "']"
    _row_3 = "//div[text()='" + scale_3 + "']"
    _column_1="//div[text()='" + one + "']"
    _column_2 = "//div[text()='" + two + "']"
    _column_3 = "//div[text()='" + three + "']"
    _column_4 = "//div[text()='" + four + "']"

    def save(self):
        """

        This method click on save button to save question

        * :param self: current instance of class
        * :return: none

        """
        time.sleep(5)
        self.wait_for_element(locator=self._save_question, locator_type="xpath", timeout=5,pollFrequency=1)
        time.sleep(5)
        self.element_click(self._save_question,locator_type="xpath")

    def next(self):
        """

        This method click on new question link

        * :param self: current instance of class
        * :return: none

        """
        self.wait_for_element(locator=self._new_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._new_question, locator_type="xpath")

    def get_question_type(self):
        """

        This method get question type.

        * :param self: current instance of class
        * :return: none
        """
        self.wait_for_element(self._question_type)
        self.element_click(self._question_type)

    def add_question_one(self,question_no_1=""):
        """

        This method  add question 1 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_1: question 1 title
        * :type question_no_1: string
        * :return none:

        """
        self.element_click(self._design, locator_type="xpath")
        self.web_scroll(direction="down")
        self.drag_drop(self._question_1_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_1, self._question_title_box)
        SurveyQuestionPage.save(self)

    def add_question_two(self, question_no_2=""):
        """

       This method  add question 2 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_2: question 2 title
        * :type question_no_2: string
        * :return none:

        """
        SurveyQuestionPage.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_2_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_2, self._question_title_box)
        self.wait_for_element(self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(self._question_two_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_select_type, locator_type="xpath")
        SurveyQuestionPage.save(self)
        
    def add_question_three(self, question_no_3=""):
        """

       This method  add question 3 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_3: question 3 title
        * :type question_no_3: string
        * :return none:

        """
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_3, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_third_type, locator_type="xpath")
        self.element_click(self._time_info_box, locator_type="xpath")
        SurveyQuestionPage.save(self)

    def add_question_four(self, question_no_4=""):
        """

       This method  add question 4 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_4: question 4 title
        * :type question_no_4: string
        * :return none:

        """
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_4, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_four_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_four_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    def add_question_five(self, question_no_5=""):
        """

        This method  add question 5 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_5: question 5 title
        * :type question_no_5: string
        * :return none:

        """
        SurveyQuestionPage.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_five_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_5, self._question_title_box)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_nine_select_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    def add_question_six(self, question_no_6=""):
        """

        This method  add question 6 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_6: question 6 title
        * :type question_no_6: string
       *  :return none:

        """
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_6, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_six_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_six_type, locator_type="xpath")
        SurveyQuestionPage.set_checkboxes(self)
        SurveyQuestionPage.save(self)

    def set_checkboxes(self):
        """

        This method add checkboxes abd send data on checkboxes

        * :param self: current instance of class
        * :return: none

        """
        self.send_keys(checkbox_1_data, self._checkbox_1,locator_type="xpath")
        self.send_keys(checkbox_2_data, self._checkbox_2, locator_type="xpath")
        self.send_keys(checkbox_3_data, self._checkbox_3, locator_type="xpath")
        self.send_keys(checkbox_4_data, self._checkbox_4, locator_type="xpath")
        self.send_keys(checkbox_5_data, self._checkbox_5, locator_type="xpath")

    def add_question_seventh(self, question_no_7=""):
        """

        This method  add question 7 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_7: question 7 title
        * :type question_no_7: string
        * :return none:

        """
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_7, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_seven_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_seven_type, locator_type="xpath")
        SurveyQuestionPage.set_labels_matix(self)
        SurveyQuestionPage.save(self)

    def set_labels_matix(self):
        """

        This method set matrix row and  columns

        * :param self: current instance of class
        * :return: none

        """
        self.send_keys(scale_1, self._row_label_1, locator_type="xpath")
        self.send_keys(scale_2, self._row_label_2, locator_type="xpath")
        self.send_keys(scale_3, self._row_label_3, locator_type="xpath")
        self.send_keys(one, self._column_label_1, locator_type="xpath")
        self.send_keys(two, self._column_label_2, locator_type="xpath")
        self.send_keys(three, self._column_label_3, locator_type="xpath")
        self.send_keys(four, self._column_label_4, locator_type="xpath")
        self.element_click(self._remove_label, locator_type="xpath")

    def add_question_eight(self,question_no_8=""):
        """
        This method  add question 8 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_8: question 8 title
        * :type question_no_8: string
        * :return: none

        """
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_8, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_eight_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_eight_type, locator_type="xpath")
        SurveyQuestionPage.set_multipletextbox_label(self)
        SurveyQuestionPage.save(self)

    def set_multipletextbox_label(self):
        """
        This method add multiple text box and send data to textbox.

        * :param self: current instance of class
        * :return none:

        """
        self.send_keys(multiple_textbox_label_1, self._multiple_textbox_level_1, locator_type="xpath")
        self.send_keys(multiple_textbox_label_2, self._multiple_textbox_level_2, locator_type="xpath")
        self.send_keys(multiple_textbox_label_3, self._multiple_textbox_level_3, locator_type="xpath")

    # method to add 9th question
    def add_question_nine(self, question_no_9=""):
        """

        This method  add question 9 ,call next method ,send title to element and call save method.

        * :param self: current instance of class
        * :param question_no_9: question 9 title
        * :type question_no_9: string
        * :return: none

        """
        SurveyQuestionPage.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_2_type, self._destination, locator_type="xpath")
        self.wait_for_element(self._question_title_box)
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_9, self._question_title_box)
        self.wait_for_element(locator=self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_nine_select_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    def add_question_ten(self, question_no_10=""):
        """

        This method  add question 10 ,send title to element,call save method.

        * :param self: current instance of class
        * :param question_no_10: question 10 title
        * :type question_no_10: string
        * :return: none

        """
        SurveyQuestionPage.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_ten_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_10, self._question_title_box)
        SurveyQuestionPage.save(self)

    def verify_question_one(self):
        """
          This method verify question 1 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean

        """
        result = None          # result is none initially
        self.element_click(self._text_1, locator_type="xpath")
        result = self.is_element_present(locator=self._text_1_type, locator_type="xpath")
        SurveyQuestionPage.save(self)
        return result

    def verify_question_two(self):
        """
          This method verify question 2 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean

        """
        result = None           # result is none initially
        self.element_click(self._text_2, locator_type="xpath")
        type = self.is_element_present(locator=self._text_2_type, locator_type="xpath")
        if type:
            result = self.is_element_present(locator=self._question_two_select_type,locator_type="xpath")
        else:
           result = False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_three(self):
        """
          This method verify question 3 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_3, locator_type="xpath")
        result = self.is_element_present(locator=self._text_3_type, locator_type="xpath")
        SurveyQuestionPage.save(self)
        return result

    def verify_question_four(self):
        """
          This method verify question 4 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_4, locator_type="xpath")
        result = self.is_element_present(locator=self._text_4_type, locator_type="xpath")
        SurveyQuestionPage.save(self)
        return result

    def verify_question_five(self):
        """
        This method verify question 5 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_5, locator_type="xpath")
        type = self.is_element_present(locator=self._text_5_type, locator_type="xpath")
        if type:
            result = self.is_element_present(locator=self._question_yes_no_select_type,locator_type="xpath")
            return result
        else:
            return False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_six(self):
        """
         This method verify question 6 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.wait_for_element(locator=self._text_6,locator_type="xpath")
        self.element_click(self._text_6, locator_type="xpath")
        type = self.is_element_present(locator=self._text_6_type, locator_type="xpath")
        if type:
            result1 = self.is_element_present(locator=self._check_box1, locator_type="xpath")
            result2 = self.is_element_present(locator=self._check_box2, locator_type="xpath")
            result3 = self.is_element_present(locator=self._check_box3, locator_type="xpath")
            result4 = self.is_element_present(locator=self._check_box4, locator_type="xpath")
            result5 = self.is_element_present(locator=self._check_box5, locator_type="xpath")
            if(result1 and result2 and result3 and result4 and result5):
                result = True
        else:
            result = False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_seven(self):
        """
          This method verify question 7 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_7, locator_type="xpath")
        type = self.is_element_present(locator=self._text_7_type, locator_type="xpath")
        if type:
            result1 = self.is_element_present(locator=self._row_1, locator_type="xpath")
            result2 = self.is_element_present(locator=self._row_2, locator_type="xpath")
            result3 = self.is_element_present(locator=self._row_3, locator_type="xpath")
            result4 = self.is_element_present(locator=self._column_1, locator_type="xpath")
            result5 = self.is_element_present(locator=self._column_2, locator_type="xpath")
            result6 = self.is_element_present(locator=self._column_3, locator_type="xpath")
            result7 = self.is_element_present(locator=self._column_4, locator_type="xpath")
            if(result1 and result2 and result3 and result4 and result5 and result6 and result7):
                result = True
        else:
            result = False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_eight(self):
        """
          This method verify question 8 is added or not.

        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None            # result is none initially
        self.element_click(self._text_2, locator_type="xpath")
        type = self.is_element_present(locator=self._text_8_type, locator_type="xpath")
        if type:
            result1 = self.is_element_present(locator=self._first_texbox, locator_type="xpath")
            result2 = self.is_element_present(locator=self._second_texbox, locator_type="xpath")
            result3 = self.is_element_present(locator=self._third_texbox, locator_type="xpath")
            if(result1 and result2 and result3):
                result = True
        else:
            result = False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_nine(self):
        """
        
          This method verify question 9 is added or not.
          
        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_9, locator_type="xpath")
        type = self.is_element_present(locator=self._text_9_type, locator_type="xpath")
        if type:
            result = self.is_element_present(locator=self._question_yes_no_select_type, locator_type="xpath")
            return result
        else:
            return False
        SurveyQuestionPage.save(self)
        return result

    def verify_question_ten(self):
        """
        
        This method verify question 10 is added or not.
        
        * :param self: current instance of class
        * :return: result
            - True -- if element is present
            - False -- if element is not present
        * :rtype: Boolean
        
        """
        result = None           # result is none initially
        self.element_click(self._text_10, locator_type="xpath")
        result = self.is_element_present(locator=self._text_10_type, locator_type="xpath")
        SurveyQuestionPage.save(self)
        return result
