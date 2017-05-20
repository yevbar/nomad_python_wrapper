import requests
import base64
import sys
import json

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

def containsHotDog(results):
	for res in result["results"]:
		if res["name"] == "hot dog" and res["confidence"] > 50:
			return True
	return false

if len(sys.argv) < 2:
	print "missing image directory"
else:
	api = Nomad()
	result = json.loads(api.detect(sys.argv[1]).text)
	print result
	if containsHotDog(result):
		print "Hotdog"
	else: 
		print "Not hotdog"


