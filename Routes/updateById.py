from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json
from json import loads
from bson.objectid import ObjectId

client = MongoClient()
app=Flask(__name__)
@app.route('/updateByID',methods=["PATCH"])
def updateByID():
	requiredArgs=['dbname','collection','data','id']
	receivedArgs=request.args
	for arg in requiredArgs :
		if not arg in receivedArgs.keys() or len(receivedArgs[arg])==0:
			return json.dumps({"code":2 ,"message":"missing argument "+arg})

	if receivedArgs['collection'][0]=='_':
		return json.dumps({"code":2 ,"message":"collection name can't start with underscore"})

	if not receivedArgs['dbname'] in client.database_names():
		return json.dumps({"code":2 ,"message":"Database doesn't exist"})

	try:
		receivedID=receivedArgs['id']
		receivedJSON = json.loads(receivedArgs['data'])
	except:
		return json.dumps({"code":2 ,"message":"inserted data must be in JSON"})

	try:
		db=client[receivedArgs['dbname']]
		collection=db[receivedArgs['collection']]
		collection.update({"_id" :ObjectId(receivedArgs['id']) },receivedJSON)
	except:
		return json.dumps({"code":2 ,"message":"Unexpected error"})



	return json.dumps({"code":1 ,"message":"date successfully updated"})
		

  



app.run(host='localhost',debug=True)
		