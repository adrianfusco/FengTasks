from Client import Client
from Mailer import Mailer
import time

# python-os-environ-object
mail_configuration = {
        'from' : '',                                          # From mail account
        'to' : '',                                            # Receiver @dinahosting.com account
        'server' : '',                                        # From mail server
        'pwd' : '',                                           # From mail password
        'port' : '',                                          # From port
        'subject' : ''                                        # Mail subject
        }

feng_configuration = {
        'user' : '',                                          # Feng user
        'pwd' : '',                                           # Feng password
        'domain' : ''                                         # Feng domain
       }


feng_client = Client(feng_configuration['user'], feng_configuration['pwd'], feng_configuration['domain'])
mail_client = Mailer(mail_configuration['from'], mail_configuration['to'], mail_configuration['server'], mail_configuration['pwd'], mail_configuration['port'], mail_configuration['subject'])

while True:
    tasks = feng_client.getTasks()
    if tasks:
        mail_client.send(tasks) 
    time.sleep(600)
