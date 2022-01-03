import os, time
from datetime import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

path="D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/video1/"

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
bootTime = datetime.now().strftime('%Y-%m-%d %H:%M')
x=0

while 1:
    list = os.listdir(path)
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')

    print("bootTime " +bootTime)
    print("currentTime " +currentTime)

    bootdate = int(bootTime[14:16])
    currentdate = int(currentTime[14:16])

    if(currentdate - bootdate) >=10 or (currentdate - bootdate)<=-27:
        bootTime = datetime.now().strftime('%Y-%m-%d %H:%M')
        x=0
        print("10 min elapsed")

    for i in range(len(list)):
        x+=1
        # print(list[i])

        request_body = {
            'snippet': {
                'title': list[i],
                'description': 'If you liked this video, remember to like and subscribe!',
                'tags': ['Psychology']
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False,
            },
            'notifySubscribers': False
        }

        if x<=6:
            try:
                print("Uploading Video " + str(x))

                response_upload = service.videos().insert(
                    part='snippet,status',
                    body=request_body,
                    media_body=MediaFileUpload(path+list[i])
                ).execute()
                os.system("del " "\"D:\\Softwares\\Waleed Docs\\Projects\\Selenium\\Youtube Automation\\video1\\" + list[i] +"\"")
                time.sleep(60)

            except:
                print("Write operation timed out")

    time.sleep(3)

