import smtplib


class EmailSender():

    def send_email(self):

        sender = 'palak.jain@infobeans.com'
        receivers = ['mangesh.khude@infobeans.com']

        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test
        
        This is a test e-mail message.
        """

        try:
           smtpObj = smtplib.SMTP('localhost')
           smtpObj.sendmail(sender, receivers, message)
           print ("Successfully sent email")
        except Exception as e:
           print (e )

email_send = EmailSender()
email_send.send_email()