import requests
from lxml import html
user = 'hilt'
url = "https://annuaire.uha.fr/index.php"
response = requests.post(url, allow_redirects=False, data={
		'search': user,
		'action': 'Chercher'
	})
#print (response.content)
tree = html.fromstring(response.content)
nom = tree.xpath('//span[@class="majuscules"]/text()')
prenom, uni = tree.xpath('//span[@class="gras"]/text()')