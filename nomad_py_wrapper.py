import requests
import base64

class nomad(object):
	
	def _init_(self):
		self.url = 'http://54.208.17.147/zappos/detect/'

	def detect(self, image_dir):
		with open(image_dir, "rb") as f:
		    data = f.read()
		    base64 = data.encode("base64")
		    data = "{ base64: " + base64 + "}"
		    response = requests.post(self.url, data = data)
		    return response

