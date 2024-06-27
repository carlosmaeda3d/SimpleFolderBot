import os
import smtplib
import time
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to see if file exists
def checkForFile(folder_path, file_name):
    return os.path.isfile(os.path.join(folder_path, file_name))

# Function to send an email
def sendEmail(to_email, subject, body):
    from_email = from_email_config # Use email name to send
    from_password = from_password_config # Use password to from_email

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server
        print('Connecting to the SMTP server....')
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        print('Connected successfully with server.')

        # Log into the server
        print('Logging into the SMTP server.....')
        server.login(from_email, from_password)
        print('Login successful.')

        # Send email
        print('Sending email....')
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini.txt')

# Email configurations
from_email_config = config['EMAIL']['USER']
from_password_config = config['EMAIL']['PASSWORD']
smtp_server = 'smtp.mail.yahoo.com'
smtp_port = 587

# Folder path and file name to check, and to recipient email
folder_path = 'C:/Users/carlo/OneDrive/Desktop/PythonTestFolder'
file_name = 'test.txt'
to_email = 'carlosmaeda3d@yahoo.com'

# Main Code
#testEmailServer(smtp_server, smtp_port, from_email_config, from_password_config, to_email)

while True:
    if checkForFile(folder_path, file_name):
        sendEmail(to_email, 'File Found', f'The file {file_name} was found in the folder {folder_path}.')
        break
    else:
        print(f'{file_name} not found in {folder_path}')
    time.sleep(10)