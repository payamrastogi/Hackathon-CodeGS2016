#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import urlparse, parse_qs
from Controller import Controller
import logging
import json

PORT_NUMBER = 7777

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		query_components = parse_qs(urlparse(self.path).query)
		if query_components:
			query_phrase = query_components["query"] 
			if query_phrase:
				result = self._processQuery(query_phrase)
			else:
				result = dict()
				result["status"] = "error:no_query"
		else:
			result = dict()
			result["status"] = "error:malformed_query"
		result_json = (unicode(json.dumps(result, ensure_ascii=False, indent=4, separators=(',', ': '))))
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.send_header("Access-Control-Allow-Origin","*")
		self.send_header("Access-Control-Expose-Headers: Access-Control-Allow-Origin")
		self.send_header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept")
		self.end_headers()
		self.wfile.write(result_json)
		return

	def do_POST(self):
		self.doGET()

	def _processQuery(self, query):
		controller = Controller(4, query,logging.DEBUG)
		result = controller.getWebResultsForQuery()
		return result

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()