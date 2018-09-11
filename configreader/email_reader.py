import yaml
import os
from os import path
from pprint import pprint as pp


class YamlEmailConverter:
    """

    This class take input from email_config yaml file

    """

    def __init__(self,file_name):
        """

        InIt of class YamlEmailConverter and in this we get full file name

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
                print("file not exist")
        except Exception as e:
            print(e)
        finally:
            data.close()

    def get_senderid(self):
        """

        This method get sender email address type
        * :param self: current instance of class
        * :return: sender

        """
        sender_id = YamlEmailConverter.yaml_read_file(self)
        sender = sender_id['production']['smtp_settings']['senderid']
        pp(sender)
        return sender

    def get_receiverid(self):
        """

        This method get receicer email address type
        * :param self: current instance of class
        * :return: reciver

        """
        reciver_id = YamlEmailConverter.yaml_read_file(self)
        reciver = reciver_id['production']['smtp_settings']['receiverid']
        pp(reciver)
        return reciver

    def get_password(self):
        """

        This method get password
        * :param self: current instance of class
        * :return: pass_word

        """
        password = YamlEmailConverter.yaml_read_file(self)
        pass_word = password['production']['smtp_settings']['password']
        pp(pass_word)
        return pass_word

    def get_smtpid(self):
        """

        This method get smtp id
        * :param self: current instance of class
        * :return: id

        """
        smtp_id = YamlEmailConverter.yaml_read_file(self)
        id = smtp_id['production']['smtp_settings']['smtpid']
        pp(id)
        return id

    def get_smtport(self):
        """

        This method get smt port number
        * :param self: current instance of class
        * :return: port

        """
        smtpport = YamlEmailConverter.yaml_read_file(self)
        port = smtpport['production']['smtp_settings']['smtport']
        pp(port)
        return port

email_raeder=YamlEmailConverter( file_name = "email_config.yaml")
email_raeder.get_senderid()
email_raeder.get_receiverid()
email_raeder.get_password()
email_raeder.get_smtpid()
email_raeder.get_smtport()

