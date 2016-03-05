from Searcher import Searcher
import sentiment
import argparse
import logging

class Controller:
	def __init__(self, rsz, query, log_level):
		self.rsz = rsz
		self.query = query
		self.log_level = log_level

	def getWebResultsForQuery(self):
		searcher = Searcher(self.query, self.rsz, log_level=self.log_level)
		result = searcher.search()
		resultQueue = []
		resultsDict = dict()
		if result:
			for i in range(len(result)):
				resultQueue.append(result[i]['url'])
		
			sentimentOutput = sentiment.SentimentAnalysis()
			sentimentScores = []
			sentimentTypes = []
			totalScore = 0
			for i in range(len(resultQueue)):
				query = resultQueue[i]
				response = sentimentOutput.makeRequest(query)
				sentimentResult = sentimentOutput.parseResponse(response)
				if sentimentResult == None:
					continue
				sentimentResultType = sentimentResult["type"]
				sentimentResultScore = sentimentResult["score"]
				totalScore += float(sentimentResultScore)
				typeScoreList = []
				typeScoreList.append(sentimentResultType)
				typeScoreList.append(sentimentResultScore)
				resultsDict[query] =  typeScoreList
			resultsDict["averageScore"] = totalScore/self.rsz
		return resultsDict

def main():		
	parser = argparse.ArgumentParser(description="A simple Google search module for Python")
	parser.add_argument("query", nargs="*", default=None)
	args = parser.parse_args()
	query = " ".join(args.query)
	log_level = logging.DEBUG
	if not query: 
		parser.print_help()
 		exit()
	controller = Controller(4, query, log_level)
	result = controller.getWebResultsForQuery()

if __name__ == "__main__":
    main()