import requests
import base64

class Nomad:
	def __init__(self):
		self.url = 'http://54.208.17.147/zappos/detect/'
		# self.url = 'http://localhost/zappos/detect/'

	def detect(self, image_dir):
		with open(image_dir, "rb") as f:
			data = f.read()
			base64 = data.encode("base64")
			data = { 'base64': base64 }
			response = requests.post(self.url, json=data)
			return response
# testing
api = Nomad()
print api.detect("hotdog.jpeg").text