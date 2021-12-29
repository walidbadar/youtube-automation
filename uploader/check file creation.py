import os, time
from datetime import datetime

path="D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/video/"

while 1:
    list = os.listdir(path)

    for i in range(len(list)):
        print(list[i])

        osPathTime = os.path.getctime(path + list[i])
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M')
        #print(currentTime)

        fileCreationTime = datetime.fromtimestamp(osPathTime).strftime('%Y-%m-%d %H:%M')
        print(fileCreationTime)

        if currentTime[0:10] == fileCreationTime[0:10]:
            print("File " + str(i) + " was created in same day")

            if int(currentTime[11:13]) <= int(fileCreationTime[11:13]):
                print("File " + str(i) + " was created in last hour")
            else:
                print("File " + str(i) + " was created hour ago")
    time.sleep(60)

