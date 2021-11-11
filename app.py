import requests
from lxml import html
url = "https://annuaire.uha.fr/index.php"
class anuaire:
	def __init__(self, url):
		self.name = str()
		self.tel = str()
		self.nom = str()
		self.prenom = str()
		self.uni = str()
		self.mail = str()
		self.name = str()
		self.tels = []
		self.noms = []
		self.prenoms = []
		self.unis = []
		self.mails = []
		self.tree = 0
	def search(self,name):
		user = name
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			})
		#print (response.content)
		self.tree = html.fromstring(response.content)
		self.nom = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenom = self.tree.xpath('//span[@class="gras"]/text()')
		del self.prenom[-1]
		self.uni = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12"]/p/text()')
		self.mail = test = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/a/text()')
		self.tel = self.tree.xpath('//div[@class="xl-col-6 l-col-6 m-col-6 ml-col-6 s-col-12 sl-col-12 droite"]/p/span/a/text()')

		#numero pas ascocier a l'utilisateur
	def searchglobal(self,term):
		user = term
		response = requests.post(url, allow_redirects=False, data={
				'search': user,
				'action': 'Chercher'
			})
		self.tree = html.fromstring(response.content)
		self.noms = self.tree.xpath('//span[@class="majuscules"]/text()')
		self.prenoms = self.tree.xpath('//span[@class="gras"]/text()')
		del self.prenoms[-1]
		for i in range(0,len(self.noms)):
			self.search(self.prenoms[i]+" "+self.noms[i])
			if not self.tel:
				self.tels.append("")
			else:
				self.tels.append(self.tel[0])
			if not self.uni :
				self.unis.append("")
			else:
				self.unis.append(self.uni[0])
			if not self.mail:
				self.mails.append("")
			else:
				self.mails.append(self.mail[0])


