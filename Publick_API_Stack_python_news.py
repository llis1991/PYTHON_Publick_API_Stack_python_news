import requests
import json
import pprint
import webbrowser
import datetime
#timedelta datatime
'''

API -Aplication Programing Interface

min 15 pkt
posortowane malejąco
z ostatniego tygodnia
kategoria python

'''

timeToday = datetime.datetime.today()
timeBefore = datetime.timedelta(days = 7)
timeToFiltr = timeToday - timeBefore

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(timeToFiltr.timestamp()),
    "tagged": "python",
    "min": 10,
}


r=requests.get("https://api.stackexchange.com/2.3/questions",params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    for question in questions["items"]:
        openNewWebsite = question["link"]
        webbrowser.open(str(openNewWebsite), new=1)
        print(openNewWebsite)


