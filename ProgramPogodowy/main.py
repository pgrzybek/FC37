from WeatherForecast import WeatherForecast
# from ReadFile import ReadFile
latLong = [50.09308038717427, 18.531524949051327]
latitude = 50.09308038717427
longitude = 18.531524949051327
#searched_date = datetime.date.today()
#searched_date="2025-10-30"
#print(searched_date)

searched_date = input("Podaj date w formacie ROK-MIESIAC-DZIEN \n")
forecast=WeatherForecast(latitude,longitude,searched_date)
print(forecast.items())



