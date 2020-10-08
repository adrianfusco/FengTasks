# Feng Office tasks extraction and notice by mail 🚀

Extract pending tasks from Feng office and notice with title and URL task by mail.

## Starting

### Feng.py

1. Authentication against Feng office.
2. Query the URLs with pending tasks.
3. Send a notice by mail with all pending task: 

```url1 - title```

```url2 - title```

In this case, we have user value of '-1'. It means that the task is not assigned yet. If we wanna search for specific user we can change ```self.fval_no_user``` value with the user ID that we're looking for.

You need to change the following attributes with the domain base:

```
self.url_login
self.url_get_tasks
self.url_base_task
```
### Mail.py

1. Login against the mail server. It needs:
  - From mail server.
  - SMTP port.
  - From user mail account.
  - From user password.
2. Send the message with subject and body. It needs:
  - Subject.
  - Body.
  
### feng.py

1. Instance of Mail class:

  -You need to set all required data to authenticate against mail server and feng.
  
  ```
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
```

It sends a mail every 10 minutes if exists any pending task.

### Run 🔩

```
$ python3 feng.py &
```
