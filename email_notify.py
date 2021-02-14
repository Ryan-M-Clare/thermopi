import smtplib
import info.mail_info

#Email Variables
SMTP_SERVER    = 'smtp.gmail.com'      #Email Server (don't change!)
SMTP_PORT      = 587                   #Server Port (don't change!)
GMAIL_USERNAME = mail_info.sender_gmail_username
GMAIL_PASSWORD = mail_info.sender_gmail_password
RCPNT_USERNAME = mail_info.recpnt_email_username

def sendmail(self, content):
     
    #Create Headers
    headers = ["From: " + GMAIL_USERNAME, "Subject: THERMOSTAT TERMINATED", "To: " + RCPNT_USERNAME,
               "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    #Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    #Login to Gmail
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    #Send Email & Exit
    session.sendmail(GMAIL_USERNAME, RCPNT_USERNAME, headers + "\r\n\r\n" + content)
    session.quit