import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


request_body = {
    'snippet': {
        'title': 'Upload Testing',
        'description': 'Hello World Description',
        'tags': ['Travel', 'video test', 'Travel Tips']
    },
    'status': {
        'privacyStatus': 'private',
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': False
}

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=MediaFileUpload('0.mp4')
).execute()