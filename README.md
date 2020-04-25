# openweathermapy
Python package wrapping **OpenWeatherMap.org's** API 2.5.

# Status / Version
Development (Beta) / 0.1.0

# how to use
```Python
import owm.weather as owm
t = weather.Temp( api_key )

# 'curent' - user geoapi or city - 'city name'
print ( t.current( 'curent') )
print ( t.current( 'city', 'Warszawa' ) )

# Return exemp "data"

data = {
    'weather_main': 'Clear',
    'weather_description': 'clear sky',
    'feel_c': 5.85,
    'temp_c': 10.85
}

#get local history data

print( t.get_local_data() )

# Return exemp "data"

{"_default": {"1": {"weather_main": "Clouds", "weather_description": "overcast clouds", "feel_c": 12.85, "temp_c": 18.85, "timestamp": 1587722085.811539, "location": "Mokot\u00f3w", "typeplase": "curent"}}}

t.show_data_chart()
[Weather Graph](http://roch.lh.pl/graph.png)

```