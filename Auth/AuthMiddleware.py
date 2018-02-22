import json
from Config.JwtConfig import encode, decode 
from AuthFunctions import CheckUser

class AuthMiddleware(object):
	def __init__(self, app):
		self.app = app

	def killUnauthorized(self, response):
		write = self.start_response('401 Unauthorized', [('Content-Type', 'text/json')])
		return response

	def __call__(self, environ, start_response):
		self.start_response = start_response

		token = environ.get('HTTP_AUTHTOKEN', False)
		if token == False or len(token) == 0:
			msg = json.dumps({"code": 2, "message": "No Authorization Token supplied"})
			return self.killUnauthorized(msg)

		try:
			user = decode(token)
		except:
			msg = json.dumps({"code": 2, "message": "Failed to decode token"})
			return self.killUnauthorized(msg)

		if CheckUser(user):
			return self.app(environ, start_response)
		else:
			write = start_response('401 Unauthorized', [('Content-Type', 'text/html')])
			msg = json.dumps({"code": 2, "message": "Unauthorized"})
			return self.killUnauthorized(msg)