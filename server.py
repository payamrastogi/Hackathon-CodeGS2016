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
		query_phrase = query_components["query"] 
		result = self._processQuery(query_phrase)
		print (unicode(json.dumps(result, ensure_ascii=False, indent=4, separators=(',', ': '))))
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

	def do_POST(self):
		self.doGET()

	def _processQuery(self, query):
		controller = Controller(query, logging.DEBUG)
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