import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "https://hooks.slack.com/services/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"
    message = ("A Sample Message")
    title = (f"New Incoming Message :zap:")
    slack_data = {
        "username": "EngineeringTeamNotification",
        "icon_emoji": ":satellite:",
        #"channel" : "#Team Developer",
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