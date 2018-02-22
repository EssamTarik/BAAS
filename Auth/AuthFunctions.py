from Config.config import DBName
from pymongo import MongoClient

UsersCollection = '_users'

client = MongoClient()
db = client[DBName]

def CheckUser(user):
	collection = db[UsersCollection]
	res = list(collection.find(user))
	if len(res) > 0:
		return res[0]
	else:
		return False