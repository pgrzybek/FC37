import json
import urllib
from re import search
from urllib import request
import datetime

from ReadFile import ReadFile
from WriteFile import WriteFile

# from ReadFile import ReadFile
latLong = [50.09308038717427, 18.531524949051327]
latitude = 50.09308038717427
longitude = 18.531524949051327
#searched_date = datetime.date.today()
#searched_date="2025-10-30"
#print(searched_date)

searched_date = input("Podaj date w formacie ROK-MIESIAC-DZIEN \n")
if searched_date == "":
    searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    try:
        searched_date = datetime.datetime.strptime(searched_date, "%Y-%m-%d")
        searched_date = searched_date.date()
    except ValueError:
        print("Podales zla date")
searched_date = str(searched_date)
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
# url = "https://api.github.com"

r = ReadFile("data.csv", searched_date)
toSave=r.lines
if not r.found:
    day=[]
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        rain = data['daily']['rain_sum'][0]
        toSave.append(searched_date)
        toSave.append(rain)
        w = WriteFile("data.csv", toSave)
        w.writeJson()
else:
    rain = r.foundLine[searched_date]
if rain > 0:
    #print(searched_date)
    print("Będzie padać")
elif rain == 0:
    #print(searched_date)
    print("Nie bedzie padać")
else:
    #print(searched_date)
    print("Nie wiem")


