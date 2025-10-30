import unittest
from datetime import date
# importujemy testowaną funkcję
from WeatherForecast import WeatherForecast
class UnitTest(unittest.TestCase):
    def test_Forecast(self):
        latLong = [50.09308038717427, 18.531524949051327]
        latitude = 50.09308038717427
        longitude = 18.531524949051327
        searched_date = str(date.today())
        try:
            w=WeatherForecast(latitude,longitude,searched_date)

        except Exception as e:
            self.fail(f"Funkcja rzuciła wyjątek: {e}")
        searched_date= "2025-10-31"
        try:
            w = WeatherForecast(latitude, longitude, searched_date)

        except Exception as e:
            self.fail(f"Funkcja rzuciła wyjątek: {e}")
if __name__ == "__main__":
    unittest.main()