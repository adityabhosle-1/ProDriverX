from __future__ import print_function

from helper import downlaodcreds
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
import googleapiclient.discovery
from googleapiclient.errors import HttpError
# from httpsend import sendtoRenamer
# from readfile import giveFile,readFile
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/script.projects','https://www.googleapis.com/auth/documents',"https://www.googleapis.com/auth/script.external_request"]
script_id="1WKJ5izeaB2IUJhiAaXrrd3ERvDS_BuDZW88BtiD5qhTwXD-Rbqdw2zyN"
def doAuth():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	return creds
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
	    downlaodcreds()
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
	return creds
def doDrive(filename):
    creds=doAuth()
    try:
	service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
	
	return uploadImagetoDrive(service,filename)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print('An error occurred: {error}')

def doGAS(mode,stringtogas):
	    creds=doAuth()
            service1= googleapiclient.discovery.build('script', 'v1', credentials=creds)
	    if(mode==1):
            	request = {"function": "maketheDoc1","parameters":stringtogas,"devMode":True}
            	response = service1.scripts().run(scriptId='AKfycbyxOgt0OJ7uZcI_mwUAbNFyGeDFQ7WN4GTzhAVhZaxLS6uUb4AZ5XPipdGLL3oFRd80',body=request).execute()
            	return response
	    elif(mode==2):
            	request = {"function": "maketheDoc2","parameters":stringtogas,"devMode":True}
            	response = service1.scripts().run(scriptId='AKfycbyxOgt0OJ7uZcI_mwUAbNFyGeDFQ7WN4GTzhAVhZaxLS6uUb4AZ5XPipdGLL3oFRd80',body=request).execute()
            	return response




def uploadImagetoDrive(service,filename):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename,
                            mimetype='image/jpeg')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file.get('id')

