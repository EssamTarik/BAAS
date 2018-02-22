from flask import request
from Auth.AuthFunctions import CheckUser
from pymongo import MongoClient
from Config.JwtConfig import encode
from bson.json_util import dumps
import json

client = MongoClient()

def login():
	requiredArgs = ['email', 'password']
	receivedArgs = request.args
	for arg in requiredArgs :
		if not arg in receivedArgs.keys() or len(receivedArgs[arg])==0:
			return json.dumps({"code":2 ,"message":"missing argument "+arg})
	userObj = {"email": receivedArgs['email'], "password": receivedArgs['password']}
	user = CheckUser(userObj)
	if user:
		token = encode(json.loads(dumps(user)))
		return json.dumps({"code":1 ,"message": token})
	else:
		return json.dumps({"code": 2 ,"message": "Invalid Credentials"})		
