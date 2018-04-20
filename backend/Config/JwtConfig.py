from config import AppSecret
import jwt

algorithm = 'HS256'

def encode(params):
	encoded = jwt.encode(params, AppSecret, algorithm=algorithm)
	return encoded

def decode(JwtString):
	decoded = jwt.decode(JwtString, AppSecret, algorithm=algorithm)
	return decoded