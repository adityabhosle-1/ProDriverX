from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httpsend import sendtoRenamer
from readfile import giveFile,readFile
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/script.projects','https://www.googleapis.com/auth/documents']
script_id="1WKJ5izeaB2IUJhiAaXrrd3ERvDS_BuDZW88BtiD5qhTwXD-Rbqdw2zyN"


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # service = build('drive', 'v3', credentials=creds)
        service = build('script', 'v1', credentials=creds)
        request = {"function": "doPost"}
        response = service.scripts().run(scriptId="AKfycbwBRTiVb82Dc-kPTYoY2QAw1p7kogk6UVhOpdT4lBv-8AukfP6JKd8H48bGSyYT439B",body=request).execute()
        print(response)
        # file_name=giveFile()
        # # Call the Drive v3 API
        # file_metadata = {
        #     'name': file_name,
        #     'mimeType': 'application/vnd.google-apps.document'
        # }
        # media = MediaFileUpload('files/'+file_name,
        #                         mimetype='application/pdf')
        # file = service.files().create(body=file_metadata,
        #                                     media_body=media,
        #                                     fields='id').execute()
        # print('File ID: {}'.format(file.get('id')))
        # sendtoRenamer(file.get('id'))
        # url="https://docs.google.com/document/d/"+file.get('id')
        # print(url)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()