import urllib, json
import datetime

class Review:

	def __init__(self, reviewData):
		self.price = reviewData['price']
		self.region_style = reviewData['region_style']
		self.rating = reviewData['rating']
		self.timestamp = reviewData['timestamp']
		self.author = reviewData['reviewer']
		self.name = reviewData['name']

		self.url = reviewData['url']
		self.apiUrl = self.__getApiUrl(self.url)
		self.data = self.__getData(self.apiUrl)


	def __getApiUrl(self, url):
		return url.replace('www.', 'api.')

	def __getData(self, url):
		print url
		response = urllib.urlopen(url)
		return json.loads(response.read())

	def findReview(self):
		for comment in self.data:
			commentData = comment['data']['children'][0]['data']
			if commentData['author'] == self.author and 'body' in commentData:
				return commentData

	def getBody(self):
		comment = self.findReview()
		return comment['body']

	def getDatetime(self):
		f = '%m/%d/%Y %H:%M:%S'
		t = '%Y-%m-%d %H:%M:%S'
		time = datetime.datetime.strptime(self.timestamp, f)
		return time.strftime(t)