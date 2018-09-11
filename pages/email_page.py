import smtplib
from configreader.email_reader import YamlEmailConverter


class Email():

    def __init__(self):

        self.yaml_parser = YamlEmailConverter(file_name = "email_config.yaml")

    def send_email(self):
        try:
            sender = self.yaml_parser.get_senderid()
            receiver = self.yaml_parser.get_receiverid()
            password = self.yaml_parser.get_password()
            smtpid = self.yaml_parser.get_smtpid()
            smtport = self.yaml_parser.get_smtport()
            smtpserver = smtplib.SMTP(smtpid , smtport)
            smtpserver.ehlo()
            smtpserver.ehlo
            smtpserver.login(sender, password)
            msg = 'Hello'
            smtpserver.sendmail(sender, receiver, msg)
            print('Sent')
        except Exception as e:
            print(e)
        finally:
            smtpserver.close()

email=Email()
email.send_email()