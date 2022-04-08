import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:

    def __init__(self: object,
                 sender: str,
                 receiver: str,
                 mail_server: str,
                 password: str,
                 port: str,
                 message_subject: str):
        self.mail_server = mail_server
        self.password = password
        self.port = port
        self.sender = sender
        self.receiver = receiver
        self.message_subject = message_subject

    def send(self: object, tasks: list):
        message = MIMEMultipart()
        message["From"] = self.sender
        message["To"] = self.receiver
        message["Subject"] = self.message_subject
        body = self.__generateBody(tasks)
        message.attach(MIMEText(body, "plain"))
        self.message = message
        self.text = self.message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.mail_server,
                              self.port,
                              context=context) as server:
            server.login(
                self.message['From'],
                self.password
            )
            server.sendmail(
                self.message['From'],
                self.message['To'],
                self.text
            )

    def __generateBody(self: object, tasks: list):
        body = ''
        for task in tasks:
            body += task.url()+' - '+task.name()+'\n'
        return body
