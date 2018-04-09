from pymongo import MongoClient
from bson.json_util import dumps
import json
from json import loads

client = MongoClient()

def update():
	requiredArgs=['dbname','collection','data','condition']
	receivedArgs=request.args
	for arg in requiredArgs :
		if not arg in receivedArgs.keys() or len(receivedArgs[arg])==0:
			return json.dumps({"code":2 ,"message":"missing argument "+arg})

	if receivedArgs['collection'][0]=='_':
		return json.dumps({"code":2 ,"message":"collection name can't start with underscore"})

	if not receivedArgs['dbname'] in client.database_names():
		return json.dumps({"code":2 ,"message":"Database doesn't exist"})

	try:
		condition=json.loads(receivedArgs['condition'])
		receivedJSON = json.loads(receivedArgs['data'])
	except:
		return json.dumps({"code":2 ,"message":"inserted data must be in JSON"})

	try:
		db=client[receivedArgs['dbname']]
		collection=db[receivedArgs['collection']]
		exist=collection.update(condition,receivedJSON)
		
	except:
		return json.dumps({"code":2 ,"message":"Unexpected error"})




	return json.dumps({"code":1 ,"message":"date successfully updated"})