import datetime
import json
import urllib
from urllib import request
from ReadFile import ReadFile
from WriteFile import WriteFile


class WeatherForecast:
    def __init__(self, latitude, longitude, searched_date):
        self.latitude = latitude
        self.longitude = longitude
        self.searched_date = str(searched_date)
        self.rain=0
        self.data={}
        self.forecast()

    def forecast(self):
        # if self.searched_date == "":
        #     self.searched_date = datetime.date.today() + datetime.timedelta(days=1)
        # else:
        #     try:
        #         self.searched_date = datetime.datetime.strptime(self.searched_date, "%Y-%m-%d")
        #         self.searched_date = self.searched_date.date()
        #     except ValueError:
        #         print("Podales zla date")
        searched_date = str(self.searched_date)
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
        # url = "https://api.github.com"
        r = ReadFile("data.json", searched_date)
        toSave = r.lines
        if not r.found:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())
                self.rain = data['daily']['rain_sum'][0]
            day= {searched_date: self.rain}
            toSave.append(day)
            w = WriteFile("data.json", toSave)
            w.writeJson()
        else:
            self.rain = r.foundLine[searched_date]
        if self.rain > 0:
            # print(searched_date)
            print("Będzie padać")
        elif self.rain == 0:
            # print(searched_date)
            print("Nie bedzie padać")
        else:
            # print(searched_date)
            print("Nie wiem")
        self.data = toSave
    def __getitem__(self, item):
        r = ReadFile("data.csv", self.searched_date)
        self.data = dict(r.lines)
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for item in self.data:

            yield item, self.data[item]
