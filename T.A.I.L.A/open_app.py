from voice import *
from greet import *
import speech_recognition as sr
import os
import subprocess
import sys
import cv2
import webbrowser
import datetime
import time
import requests
import json
currentTime = time.strftime('%H:%M')

def open_applicatipons():
    while True:
        query = takeinstruction().lower()
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        hour = datetime.datetime.now().hour
        mints = datetime.datetime.now().minute
        sec = datetime.datetime.now().second

        if "open vs code" in query:
            apath = "//Applications//Visual Studio Code.app"
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, apath])
            speak('opening visual studio code for you')
        elif "open slack" in query:
            slack_path = "//Applications//Slack.app"
            subprocess.call([opener, slack_path])
            speak("Opening slack for you")
        elif "open chrome" in query:
            chrome_path = "//Applications//Google Chrome.app"
            subprocess.call([opener, chrome_path])
            speak("Opening Google Chrome for you")

        elif "open zoom" in query:
            zoom_path = "//Applications//zoom.us.app"
            subprocess.call([opener, zoom_path])
            speak("Opening Google Zoom meeting app for you")

        elif "open notes" in query:
            notes_path = "/System/Applications/Notes.app"
            subprocess.call([opener, notes_path])
            speak("Opening Notes")

        elif "open terminal" in query:
            # zoom_path="//Applications//zoom.us.app"
            # subprocess.call([opener, zoom_path])
            os.system('open -a Terminal .')
            speak("Opening terminal")

        elif "open camera" in query:
            frameWidth = 640
            frameHeight = 480
            cap = cv2.VideoCapture(0)
            cap.set(3, frameWidth)
            cap.set(4, frameHeight)
            cap.set(10, 150)

            while cap.isOpened():
                success, img = cap.read()
                if success:
                    cv2.imshow("Result", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        elif "open youtube" in query:
            speak('opening youtube')
            webbrowser.open("https://www.youtube.com/", new=0)
            speak("what do you want to watch?")
            search = takeinstruction().lower()
            speak("opening, " + search)
            webbrowser.open("https://www.youtube.com/results?search_query=" + search, new=0)
            import urllib.request
            import re
            search_keyword = search.replace(" ", "+")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            n = 0
            link_list = []
            for x in video_ids:
                link = "https://www.youtube.com/watch?v=" + x
                n += 1
                link_list.append(link)
            speak('here are the top search result, which one you want to watch ?')
            video_nos = takeinstruction().lower()

            if 'first video' in video_nos:
                webbrowser.open(link_list[0], new=0)
            elif 'second video' in video_nos:
                webbrowser.open(link_list[1], new=0)
            elif 'third video' in video_nos:
                webbrowser.open(link_list[2], new=0)
            elif 'fourth video' in video_nos:
                webbrowser.open(link_list[3], new=0)
            else:
                speak("Please say that again ")

        elif "open task management" in query:
            speak('opening task management system for you sir')
            webbrowser.open("https://frontend-task-management-sys.herokuapp.com/admins/edit/48", new=0)
            speak("do you want to add task? ")
            confirmation = takeinstruction().lower()
            if 'yes' in confirmation:
                webbrowser.open("https://frontend-task-management-sys.herokuapp.com/task", new=0)
            else:
                pass

        elif 'open student attendance' in query:
            webbrowser.open(
                'https://docs.google.com/spreadsheets/d/1QlKAUWWsMFKfxlNlZwnc5UyeC5Css_BmxgBReA-qHZw/edit?pli=1#gid=2055163731')
            speak('opening your cohort')



        elif 'open student progress' in query:
            webbrowser.open(
                'https://docs.google.com/spreadsheets/d/1U2h2eFiXqiaRJfC-cxbd81ZRbuX9HZHP2h9vLBRmQ20/edit?pli=1#gid=1719685566')
            webbrowser.open("https://trello.com/b/kUxhCJf1/ds-rajeswari")
            speak('Opening Data Science Student Progress report, along with trello')


        elif "open google" in query:
            speak('opening google')
            webbrowser.open("https://www.google.com/", new=0)

        elif hour == 15 and mints == 10:
            speak('All engineering Team, please fill the task management system, before 3 pm  ')
            pass

        elif hour == 14 and mints == 58:
            url = "https://hooks.slack.com/services/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"
            message = ("All engineering Team, please fill the task management system, before 3 pm.")
            title = (f"New Incoming Message :zap:")
            slack_data = {
                "username": "EngineeringTeamNotification",
                "icon_emoji": ":satellite:",
                # "channel" : "#team-developer",
                "attachments": [
                    {
                        "color": "#9733EE",
                        "fields": [
                            {
                                "title": title,
                                "value": message,
                                "short": "false",
                            }
                        ]
                    }
                ]
            }

            byte_length = str(sys.getsizeof(slack_data))
            headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
            response = requests.post(url, data=json.dumps(slack_data), headers=headers)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)

            pass


        elif hour == 15 and mints == 50 and sec in range(55,57):
            url = "https://hooks.slack.com/services/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"
            message = ("All engineering Team, please join for the evening meeting")
            title = (f"New Incoming Message :zap:")
            slack_data = {
                "username": "EngineeringTeamNotification",
                "icon_emoji": ":satellite:",
                # "channel" : "#team-developer",
                "attachments": [
                    {
                        "color": "#9733EE",
                        "fields": [
                            {
                                "title": title,
                                "value": message,
                                "short": "false",
                            }
                        ]
                    }
                ]
            }

            byte_length = str(sys.getsizeof(slack_data))
            headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
            response = requests.post(url, data=json.dumps(slack_data), headers=headers)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)

            pass
        elif 'fill my task management system' in query:
            username = "anshu@techis.io"
            password = "1234567890"
            # head to github login page
            driver = webdriver.Chrome('/Applications/chromedriver')
            driver.get("https://frontend-task-management-sys.herokuapp.com/login")
            time.sleep(5)
            # find username/email field and send the username itself to the input field
            driver.find_element_by_id("email").send_keys(username)
            # find password input field and insert password as well
            driver.find_element_by_id("password").send_keys(password)
            # click login button
            button=driver.find_elements_by_class_name("Sign In")


            #button = driver.find_elements_by_class_name("MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-yb0lig")
            button.click()
