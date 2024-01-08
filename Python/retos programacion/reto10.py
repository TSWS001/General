# RETO10 API

import requests

url = "https://google-search72.p.rapidapi.com/search"

querystring = {"q":"word cup","gl":"us","lr":"lang_en","num":"10","start":"0"}

headers = {
	"X-RapidAPI-Key": "7b6fc8c7f6mshb7ad58dc23d40d6p13df4djsn1baaa11211a6",
	"X-RapidAPI-Host": "google-search72.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())