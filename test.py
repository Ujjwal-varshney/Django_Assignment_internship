# test_smtp_connection.py
import os
from dotenv import load_dotenv
load_dotenv()

print("EMAIL_HOST:", os.environ.get('EMAIL_HOST'))
print("EMAIL_PORT:", os.environ.get('EMAIL_PORT'))
print("EMAIL_HOST_USER:", os.environ.get('EMAIL_HOST_USER'))
print("SMTP_PASSWORD:", os.environ.get('SMTP_PASSWORD'))
