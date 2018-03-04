from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pymongo import ObjectID

#from bson.json_util import utils
import json
client = MongoClient()


app = Flask(__name__)


#app.config['MONGO_DBNAME'] = 'maymandb'
#app.config['MONGO_URI'] = 'mongodb://mayman:12345@ds147118.mlab.com:47118/maymandb'
#mongo = PyMongo(app)
#print(app.config['MONGO_DBNAME'])







@app.route('/delete', methods=['DELETE'])
def delete():
	requiredArgs = ['dbname', 'collection']
	receviedArgs = request.args

	for arg in requiredArgs:
		if not arg in receviedArgs.keys() or len(receviedArgs[arg]) == 0:
			return json.dumps({"code": 2, "message": "missing args " + arg})

		if receviedArgs['collection'][0] == '_':
			return json.dumps({"code": 2, "message": "Can not start with _"})

		if not receviedArgs['dbname'] in client.database_names():
			return json.dumps({"code": 2, "message": "db does not exist"})

	
	if "id" in recievedArgs.keys():
		 id = receivedArgs['id']
 		collection.remove({'_id': ObjectID(id)})
	else if "condition" in recievedArgs.keys():
		condition = receviedArgs['condition']
 		collection.remove(receviedJson[data])
	else:
 		return json.dumps({"code": 2, message: "must supply id or condition"})

 	return json.dumps({"code": 1, message: "successfully deleted"})



		try:
			receviedJson = json.loads(receviedArgs['condition'])
		except:
			return json.dumps({"code": 2, "message": "data must be in JSON format"})

		db = client[receviedArgs]['dbname']
		collection = db[receviedArgs]['collection']
		condition = receviedArgs['condition']
		try:
			collection.remove(receviedJson[data])
		except:
			return json.dumps({"code": 2, "message": "invalid Collection"})

		id = receivedArgs['id']
		try:
 			collection.remove({'_id': ObjectID(id)})
 		except:
 			return json.dumps({"code": 2, "message": "Invalid ID"})



	







if __name__ == '__main__':
	app.run(debug=True)

