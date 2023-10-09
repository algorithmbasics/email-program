import smtplib
import os

from dotenv import load_dotenv
load_dotenv()

# ---------------------------------------------------------------------------
# Email preferences

email_user = "algorithmbasics@gmail.com"
email_password = "password"

message = "HI! This is me. Me is good. Simple code."

# vector of all recipient email addresses
list = ["email1", "email2", "email3"]

for each_individual in list:

    # Import smtplib module to send emails
    # Create SMTP connection object, parameters are SMTP server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start TLS encryption on connection
    server.starttls()

    # Login to SMTP server with email and password
    server.login(email_user, email_password)

    # Send email - from, to, and message
    server.sendmail(email_user, each_individual, message)

    # Close the SMTP connection
    server.quit()
