import os, time
from datetime import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "client_secret.json" # Get client_secret.json file from cloud.google.com using Oauth ID verification method
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

path="D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/Youtube Downloader/Videos/"

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
bootTime = datetime.now().strftime('%Y-%m-%d %H:%M')

with open(r'videoCount.txt', 'r') as pastvalue:
    videoCount = [line.strip() for line in pastvalue]
if len(videoCount) > 0:
    pastVideoCount = int(videoCount[0])

while 1:
    list = os.listdir(path)
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')

    # print("bootTime " +bootTime)
    # print("currentTime " +currentTime)

    bootdate = int(bootTime[8:10])
    currentdate = int(currentTime[8:10])

    if(currentdate - bootdate) >=1 or (currentdate - bootdate)<=-27:
        bootTime = datetime.now().strftime('%Y-%m-%d %H:%M')
        pastVideoCount=0
        print("1 day elapsed")

    for i in range(len(list)):
        pastVideoCount+=1
        # print(list[i])

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
        
        # 6 Videos will be uploaded to channel in a day and remaining video will continue from next day. 
        if pastVideoCount<=6:
            try:
                print("Uploading Video " + str(x))

                response_upload = service.videos().insert(
                    part='snippet,status',
                    body=request_body,
                    media_body=MediaFileUpload(path+list[i])
                ).execute()
                os.system("del " "\"D:\\Softwares\\Waleed Docs\\Projects\\Selenium\\Youtube Automation\\Youtube Downloader\\Videos\\" + list[i] +"\"")
                time.sleep(60)

            except:
                print("Write operation timed out")

    time.sleep(60)

