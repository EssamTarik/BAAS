from flask import request
from Auth.AuthFunctions import CreateUser
from pymongo import MongoClient
from bson.json_util import dumps
import json


def signup():
	requiredArgs = ['email', 'password']
	receivedArgs = request.args
	for arg in requiredArgs :
		if not arg in receivedArgs.keys() or len(receivedArgs[arg])==0:
			return json.dumps({"code":2 ,"message":"missing argument "+arg})
	
	user = CreateUser(dict(receivedArgs))
	if user:
		if "error" in user.keys():
			return json.dumps({"code": 2 ,"message": user['error']})

		return json.dumps({"code": 1 ,"message": dumps(user)})
	else:
		return json.dumps({"code": 2 ,"message": "Failed to create user"})		
