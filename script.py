import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
smtp_server = os.environ.get('EMAIL_HOST')
smtp_port = int(os.environ.get('EMAIL_PORT'))
smtp_user = 'ujjwal.varshney_cs21@gla.ac.in'
smtp_password = os.environ.get('SMTP_PASSWORD')

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()  # Use starttls() if using TLS
        server.login(smtp_user, smtp_password)
        print("SMTP connection successful")
except smtplib.SMTPConnectError:
    print("Failed to connect to the SMTP server")
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate with the SMTP server")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
