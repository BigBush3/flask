import os
from requests import request


def get_weather(query=''):
	if not query:
		query = 'fetch:ip'
	response = request(
		method='GET',
		url='http://api.weatherstack.com/current',
		params={
			'access_key': 'ae4e5abd8d42f8dedc72d0a757d89e57',
			'query': query
		}
	)
	if response.status_code == 200:
		return{
			'icon': response.json()['current']['weather_icons'][0],
			'temperature': response.json()['current']['temperature'],
			'wind_speed': response.json()['current']['temperature']
		}