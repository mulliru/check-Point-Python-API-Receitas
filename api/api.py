import requests

url = "https://food-recipes-with-images.p.rapidapi.com/"

querystring = {"q":"chicken soup"}

headers = {
	"X-RapidAPI-Key": "139d32fed9mshcd1dc3054219964p180a64jsn619b8b40b6cd",
	"X-RapidAPI-Host": "food-recipes-with-images.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())