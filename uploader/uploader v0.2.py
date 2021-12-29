import os, time
from datetime import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

path="D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/video/"

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

while 1:
    list = os.listdir(path)

    for i in range(len(list)):
        print(list[i])

        osPathTime = os.path.getctime(path + list[i])
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')
        #print(currentTime)

        fileCreationTime = datetime.fromtimestamp(osPathTime).strftime('%Y-%m-%d %H:%M')
        #print(fileCreationTime)

        if currentTime[0:10] == fileCreationTime[0:10]:
            #print("File was created in same day")

            if int(currentTime[11:13]) <= int(fileCreationTime[11:13]):
                request_body = {
                    'snippet': {
                        'title': list[i],
                        'description': 'Making psychology and mental health content accessible for everyone.',
                        'tags': ['Psychology']
                    },
                    'status': {
                        'privacyStatus': 'public',
                        'selfDeclaredMadeForKids': False,
                    },
                    'notifySubscribers': False
                }

                try:
                    response_upload = service.videos().insert(
                        part='snippet,status',
                        body=request_body,
                        media_body=MediaFileUpload(path+list[i])
                    ).execute()

                except:
                    print("Write operation timed out")

                print("File was created in last hour")

    time.sleep(1800)