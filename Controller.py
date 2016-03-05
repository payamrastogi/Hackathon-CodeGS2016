from Searcher import Searcher
import sentiment
import argparse
import logging

class Controller:
	def __init__(self, query, log_level):
		self.query = query
		self.numPages = numPages
		self.log_level = log_level

	def getWebResultsForQuery(self):
		searcher = Searcher(self.query, log_level=self.log_level)
		result = searcher.search()
		resultQueue = []
		for i in range(len(result)):
			resultQueue.append(result[i]['url'])
		
		sentimentOutput = sentiment.SentimentAnalysis()
		sentimentScores = []
		sentimentTypes = []
		resultsDict = dict()
		totalScore = 0
		for i in range(len(resultQueue)):
			query = resultQueue[i]
			response = sentimentOutput.makeRequest(query)
			sentimentResult = sentimentOutput.parseResponse(response)
			if sentimentResult == None:
				continue
			sentimentResultType = sentimentResult["type"]
			sentimentResultScore = sentimentResult["score"]
			totalScore += sentimentResultScore
			typeScoreList = []
			typeScoreList.append(sentimentResultType)
			typeScoreList.append(sentimentResultScore)
			resultsDict[query] =  typeScoreList
		resultsDict["averageScore"] = totalScore/numPages
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
	controller = Controller(query, log_level)
	result = controller.getWebResultsForQuery()
	print len(result)

if __name__ == "__main__":
    main()