from Config.config import DBName
from pymongo import MongoClient

UsersCollection = '_users'

client = MongoClient()
db = client[DBName]

def CheckUser(user):
	collection = db[UsersCollection]
	email = user.get('email', '')
	password = user.get('password', '')

	res = list(collection.find({"email": email, "password": password}))
	if len(res) > 0:
		return res[0]
	else:
		return False