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

def CreateUser(user):
	collection = db[UsersCollection]
	try:
		res = list(collection.find({'email': user['email']}))
		if len(res) > 0:
			return {"error": "This user already exists"}

		res = collection.insert(user)
		return res
	except Exception as e:
		print e
		return False

