import requests


def get_forecasts(area, weather_settings):
    url = f'http://wttr.in/{area}'
    params = weather_settings
    response = requests.get(url, params)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    places = ['Лондон', 'svo', 'Череповец']
    settings = {'nTqm': '',
                'lang': 'ru'}
    for place in places:
        get_forecasts(place, settings)
