import requests
user = 'hilt'
url = "https://annuaire.uha.fr/index.php"
response = requests.post(url, allow_redirects=False, data={
		'search': user,
		'action': 'Chercher'
	})
print (response.content)