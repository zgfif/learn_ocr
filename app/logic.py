import requests



# weather in Odessa, Ukraine
URL: str = 'https://api.open-meteo.com/v1/forecast?' \
            'latitude=46.4752&' \
            'longitude=30.7088&' \
            'current_weather=true'



def is_windy_day() -> bool:
    """
    Return True if the speed of wind > 10 km/h. Else - False.
    """
    response = requests.get(URL)
    # response.raise_for_status
    data = response.json()
    wind_speed = data['current_weather']['windspeed']
    return float(wind_speed) > 10.0
