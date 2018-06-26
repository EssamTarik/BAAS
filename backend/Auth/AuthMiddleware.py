import json
from Config.JwtConfig import encode, decode 
from AuthFunctions import CheckUser, CheckToken

class AuthMiddleware(object):
	def __init__(self, app):
		self.app = app
		self.whitelist = ['login', 'signup']

	def killUnauthorized(self, response):
		write = self.start_response('401 Unauthorized', [('Content-Type', 'text/json')])
		return response
	def parseQueryString(self, string):
		if len(string) == 0:
			return {}
		queryParams = string.split('&')
		queryParamsDict = {}
		for param in queryParams:
			paramArray = param.split('=')
			queryParamsDict[paramArray[0]] = paramArray[1]
		return queryParamsDict
	def __call__(self, environ, start_response):
		self.dbname = self.parseQueryString(environ['QUERY_STRING']).get('dbname', False)
		if environ['PATH_INFO'][1:] in self.whitelist or environ['PATH_INFO'][1:].startswith('admin'):
			return self.app(environ, start_response)
			
		self.start_response = start_response

		token = environ.get('HTTP_AUTHTOKEN', False)
		if token == False or len(token) == 0:
			msg = json.dumps({"code": 2, "message": "No Authorization Token supplied"})
			return self.killUnauthorized(msg)

		if self.dbname and CheckToken(token, self.dbname):
			return self.app(environ, start_response)
		else:
			msg = json.dumps({"code": 2, "message": "Unauthorized"})
			return self.killUnauthorized(msg)