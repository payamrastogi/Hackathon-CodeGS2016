import json
import requests
import urllib

class SentimentAnalysis:
	def __init__(self):
		pass

	def makeRequest(self, url):
		params = dict()
		#encode the URL
		urlEncoded = urllib.quote_plus(url)
		params['url'] = url
		params['apikey'] = '7e51f8247d558adc439f588695375e75f105a86c'
		params['outputMode'] = 'json'
		params['showSourceText'] = 0
		params['sourceText'] = 'cleaned'

		jsonParams = json.dumps(params)
		response = requests.post("http://gateway-a.watsonplatform.net/calls/url/URLGetTextSentiment", data=params)
		return response

	def parseResponse(self, response):
		if response.status_code != 200:
			return None
		else:
			result = json.loads(response.content.decode('utf-8'))
			if result.has_key("status") and result["status"] == "OK":
				return result["docSentiment"]
			else:
				return None

def main():
	sentimentAnalysis = SentimentAnalysis()
	checkUrl = "http://247wallst.com/energy-business/2016/03/04/us-oil-production-plunges-3-companies-that-should-be-profitable-this-year/"
	response = sentimentAnalysis.makeRequest(checkUrl)
	result = sentimentAnalysis.parseResponse(response)
	print result["type"]
	print result["score"]

if __name__ == "__main__":
	main()
