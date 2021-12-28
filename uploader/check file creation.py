import os, time

path="D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/uploader/"
list = os.listdir(path)
print (list[0])
print(time.ctime(os.path.getctime(path+list[0])))

