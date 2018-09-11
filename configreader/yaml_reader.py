import yaml
import os
from os import path
from pprint import pprint as pp


class YamlConverter:
    """

    This class take input from yaml file

    """

    def __init__(self,file_name):
        """

        InIt of class ConvertYaml and in this we get full file name

        * :param file_name: name of file
        * :param self :current instance of class

        """
        main_folder_path = os.path.dirname(__file__)
        relative_folder_path = "../config_files/" + file_name
        full_file_name = os.path.join(main_folder_path, relative_folder_path)
        self.file = full_file_name          #  full file name

    def yaml_read_file(self):
        """

        This method read whole yaml file and store data in dictionary

        * :param self: current instance of class
        * :return: file_data in dictionary format

        """
        data = ""          # data is null at initial level
        try:
            if (path.exists(self.file)):
                data = open(self.file, "r")
                file_data = yaml.load(data)
                return file_data
            else:
                pp("file not exist")
        except Exception as e:
            pp(e)
        finally:
            data.close()

    def get_browser(self):
        """

        This method get browser type
        * :param self: current instance of class
        * :return: broswer

        """
        browser_type = YamlConverter.yaml_read_file(self)
        browser = browser_type['platfrom']['browser']
        pp(browser)
        return browser

    def get_url(self):
        """

         This method get url of site
        * :param self: current instance of class
        * :return: url

        """
        website_url = YamlConverter.yaml_read_file(self)
        url = website_url['siteconfiguration']['url']
        pp(url)
        return url

    def get_username(self):
        """

         This method get username
        * :param self: current instance of class
        * :return: username

        """
        user = YamlConverter.yaml_read_file(self)
        username = user['login']['user']
        pp(username)
        return username

    def get_password(self):
        """

         This method get password
        * :param self: current instance of class
        * :return: pass_word

        """
        password = YamlConverter.yaml_read_file(self)
        pass_word = password['login']['password']
        pp(pass_word)
        return pass_word

