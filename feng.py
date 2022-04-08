from Client import Client
from Mailer import Mailer
import time

# python-os-environ-object
mail_configuration = {
        # From @mail.com account
        'from': '',
        # Receiver @mail.com account
        'to': '',
        # From mail server
        'server': '',
        # From mail password
        'pwd': '',
        # From port
        'port': '',
        # Mail subject
        'subject': ''
        }

feng_configuration = {
        # Feng user
        'user': '',
        # Feng password
        'pwd': '',
        # Feng domain
        'domain': ''
       }


feng_client = Client(
    feng_configuration['user'],
    feng_configuration['pwd'],
    feng_configuration['domain']
)
mail_client = Mailer(
    mail_configuration['from'],
    mail_configuration['to'],
    mail_configuration['server'],
    mail_configuration['pwd'],
    mail_configuration['port'],
    mail_configuration['subject']
)

while True:
    tasks = feng_client.getTasks()
    if tasks:
        mail_client.send(tasks)
    time.sleep(600)
