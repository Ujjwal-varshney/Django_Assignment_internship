from django.core.management.base import BaseCommand
import smtplib
import os

class Command(BaseCommand):
    help = 'Test SMTP connection'

    def handle(self, *args, **kwargs):
        smtp_server = os.environ.get('EMAIL_HOST')
        smtp_port = int(os.environ.get('EMAIL_PORT', 587))
        smtp_user = os.environ.get('EMAIL_HOST_USER')
        smtp_password = os.environ.get('SMTP_PASSWORD')

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Use server.starttls() if you're using TLS
                server.login(smtp_user, smtp_password)
                self.stdout.write(self.style.SUCCESS('SMTP connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'SMTP connection failed: {e}'))
