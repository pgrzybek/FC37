# plik nie do sprawdzania
import unittest
from datetime import date

from pyexpat.errors import messages

from ReadFile import ReadFile
# importujemy testowaną funkcję
from WeatherForecast import WeatherForecast


class UnitTest(unittest.TestCase):
    def test_Forecast(self):
        latLong = [50.09308038717427, 18.531524949051327]
        latitude = 50.09308038717427
        longitude = 18.531524949051327
        searched_date = str(date.today())
        try:
            w = WeatherForecast(latitude, longitude, searched_date)
            gen= w.items()
            while gen:
                try:
                    print(next(gen))
                except StopIteration:
                    break



        except Exception as e:
            self.fail(f"Funkcja rzuciła wyjątek: {e}")
        searched_date = "2025-10-31"
        try:
            w = WeatherForecast(latitude, longitude, searched_date)

        except Exception as e:
            self.fail(f"Funkcja rzuciła wyjątek: {e}")

    def testjson(self):
        try:
            searched = str(date.today())
            r = ReadFile("data.json", searched)
            self.messages(r)
        except Exception as e: #Exception as e:
            self.fail(f"Funkcja rzuciła wylatek {e}")
            #print("Nie działa")
    def testcsv(self):
        try:
            searched = str(date.today())
            r = ReadFile("data.json", searched)
            self.messages(r)
        except Exception as e: #Exception as e:
            self.fail(f"Funkcja rzuciła wylatek {e}")
            #print("Nie działa")
    @staticmethod
    def  messages(r):
            print(f"r.foundLine {r.foundLine}")
            print(f"r.found {r.found}")
            print(f"r.lines {r.lines}")

if __name__ == "__main__":
    unittest.main()
