import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail():

    def __init__(self):
        self.email = 'yourEmail@here.com' # Email that will be sending email
        self.password = 'YourPassword'    # Password
        self.send_to_email = 'sendEmail@here.com'  # Where to send Email
        self.subject = 'Email Subject' # Email subject

    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.send_to_email
        msg['Subject'] = self.subject

        msg.attach(MIMEText(self.message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, self.send_to_email, text)
        server.quit()
        print("---Success---")
