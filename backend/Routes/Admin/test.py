from pymongo import MongoClient
import json

client = MongoClient()

def test():
	dbs = list(client.database_names())
	return json.dumps(dbs)