# netlix_email_update

This Python script will send you an email letting you know
what is being added to Netflix this current month, as well as what
is being removed.

In 'send_email.py' just enter your email information.
The email address that is sending the email must be "allow less secure apps".

To automate this script on unix systems:

I created a file called execute.sh that ran the python interpreter inside its virtual environment and called the script:
execute.sh
```
#!/bin/sh
/path/to/your/env/bin/python ~/path/to/repo/netlix_email_update/script.py
```
Then type this command in your terminal:
```
crontab -e
```
In the file type:
```
0 0 1 * * sh ~/path/to/your/sh/file/execute.sh
```
This will make the script execute at midnight on the 1st day of every month.
