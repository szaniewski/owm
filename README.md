# openweathermapy
Python package wrapping **OpenWeatherMap.org's** API 2.5.

# Status / Version
Development (Beta) / 0.1.0

# how to use
```Python
import owm.weather as owm
t = weather.Temp()

# 'curent' - user geoapi or city - stryng city name
print ( t.current( 'curent', api_key ) )
print ( t.current( 'city', api_key, 'Warszawa' ) )

# Return exemp "data"

data = {
    'weather_main': 'Clear',
    'weather_description': 'clear sky',
    'feel_c': 5.85,
    'temp_c': 10.85
}
```