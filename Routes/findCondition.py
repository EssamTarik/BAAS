from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json
from json import loads


client = MongoClient()
def findCondition():
	requiredArgs = ['dbname','collection','condition']
	receivedArgs = request.args
	for item in requiredArgs:
		if not item in receivedArgs.keys() or len(receivedArgs[item])==0:
			return json.dumps({ "code": 2, "message": "Missing Argument " +item})
	if receivedArgs['collection'][0]=='_':
		return json.dumps({"code": 2, "message": "Collection name can't start with an underscore" })
	#now we have checked if the request is sent in a right form let's check if the data in the request r also correct db wisely
	if not receivedArgs['dbname'] in client.database_names() :
		return json.dumps({"code": 2, "message": receivedArgs['dbname'] + "Is not an existing Database" })
	try:
		condition = json.loads(receivedArgs['condition'])
	except:
		return json.dumps({"code": 2, "message": "The condition must be in JSON format" })
	
	try: 
		db =client[receivedArgs['dbname']]
		collection =db[receivedArgs['collection']] 
		found= collection.find(condition)

		if found.count()==0 :
			return json.dumps({"code": 2, "message":"data not found" })
		
		return json.dumps({"code": 1, "message":"successfully found" })
	except:
		return json.dumps({"code": 2, "message":"Unknown Error" })	