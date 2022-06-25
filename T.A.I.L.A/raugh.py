import time
import datetime
import webbrowser
import time
currentTime = time.strftime('%H:%M')
from selenium import webdriver
import webbrowser
import requests
import json
import sys
import random
#
# currentTime = time.strftime('%H:%M')
# print(currentTime)
#
# hour = datetime.datetime.now().hour
# mints = datetime.datetime.now().minute
# sec = datetime.datetime.now().second
# print(mints)
# print(sec)
# print('All engineering Team, please fill the task management system, before 3 pm')
# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# username = "anshu@techis.io"
# password = "1234567890"
# # head to github login page
# driver = webdriver.Chrome('/Applications/chromedriver')
# driver.get("https://frontend-task-management-sys.herokuapp.com/login")
# time.sleep(3)
#             # find username/email field and send the username itself to the input field
# driver.find_element_by_id("email").send_keys(username)
#             # find password input field and insert password as well
# driver.find_element_by_id("password").send_keys(password)
#             # click login button
# driver.find_elements_by_class_name("MuiLoadingButton-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth MuiButtonBase-root css-q2lgex")
#
#             #button = driver.find_elements_by_class_name("MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-yb0lig")
# #button.click()
hour = datetime.datetime.now().hour
mints = datetime.datetime.now().minute
sec = datetime.datetime.now().second
l=[20,21,22,23,24,25]
while True:
    if hour == 8 and mints == 41:
        print('hi')
        time.sleep(60)
        pass
