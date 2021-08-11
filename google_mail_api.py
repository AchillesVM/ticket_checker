from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import os.path
import base64
import json

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


class GoogleMailAPI:

    def __init__(self):
        creds = self.load_creds()
        self.service = build('gmail', 'v1', credentials=creds)

    @staticmethod
    def load_creds():

        if os.path.exists('token.json'):
            with open('token.json') as f:
                creds = json.load(f)

        else:
            keys = ('token', 'refresh_token', 'token_uri', 'client_id', 'client_secret', 'expiry')
            creds = {key: os.environ[key.upper()] for key in keys}

        creds['scopes'] = [SCOPES]

        return Credentials.from_authorized_user_info(creds, SCOPES)

    def send_email(self, recipient, subject, body):

        message = MIMEText(body)

        message['to'] = recipient
        message['subject'] = subject

        message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        self.service.users().messages().send(userId='me', body=message).execute()

