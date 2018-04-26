from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json


client = MongoClient()
def delete():
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
		collection.remove(condition)
		return json.dumps({"code": 1, "message":"Successfully deleted" })	
	except Exception as e:
		print e
		return json.dumps({"code": 2, "message":"Unknown Error" })	