#Weather Application using Yahoo Weather API
#only works on Python 3 IDLE (not external python compiler unless has weather API module)
#have fun
### YAHOO NOW REQUIRES AN AUTH TOKEN AS OF 17th September 2019
from weather import Weather, Unit
import pandas as pd

class checkWeather():
    def menu(self):
        print('[1] Current Weather for city')
        print('[2] Forecast Weather Report for city')
        print('[3] Quit')

        try:
            ans = int(input('Choose an option: '))
            print(' ')
            if ans == 1:
                self.currentWeather()
            elif ans == 2:
                self.forecastWeather()
            elif ans == 3:
                exit()
        except:
            print('\nOops, there is an error!\n')
            self.menu()
    def currentWeather(self):
        weather = Weather(unit=Unit.CELSIUS)
        print(' ')
        try:
            city = input('Name a valid city: ')
            location = weather.lookup_by_location(city)
            condition = location.condition
            print(' ')
            print(condition.text)
            print(' ')
            self.menu()
        except:
            print('\nOops, there is an error!')
            self.currentWeather()
        print(' ')
        self.menu()

    def forecastWeather(self):
        weather = Weather(unit=Unit.FAHRENHEIT)
        print(' ')
        try:
            city = input('Name a valid city: ')
            location = weather.lookup_by_location(city)
            forecasts = location.forecast
            for forecast in forecasts:
     
                rawdata = {'Date':[forecast.date],
                           'Weather':[forecast.text],
                           'Daily High':[forecast.high],
                           'Daily Low':[forecast.low]}

                df = pd.DataFrame(rawdata)
                print(df)
                print(' ')

            print(' ')
            self.menu()
        except:
            print('\nOops. there is an error!')
            self.forecastWeather()
        
checkWeather = checkWeather()

checkWeather.menu()

