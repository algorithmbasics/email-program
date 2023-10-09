import smtplib
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

msg = MIMEMultipart()

# ---------------------------------------------------------------------------
# Email credentials
email_user = os.environ.get("EMAIL_USER")
email_password = os.environ.get("EMAIL_PASSWORD")

# date
now = datetime.now()
date_str = now.strftime("%m/%d/%Y, %H:%M:%S")

# email subject
msg['Subject'] = f"Today's message {date_str}: using complex.py"

# message
message = "HI! This is me. Me is good. Complex code."

# vector of all recipient email addresses
list = ["email1", "email2", "email3"]

try:

    for each_individual in list:

        # Import smtplib module to send emails
        # Create SMTP connection object, parameters are SMTP server and port
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Start TLS encryption on connection
        server.starttls()

        # Login to SMTP server with email and password
        server.login(email_user, email_password)

        # message
        msg.attach(MIMEText(message, 'plain'))

        # Send email - from, to, and message
        server.sendmail(email_user, each_individual, msg.as_string())

        # Close the SMTP connection
        server.quit()

except Exception as e:
    print(e)
