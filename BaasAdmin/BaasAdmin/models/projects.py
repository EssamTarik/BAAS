from django.db import models
from pymongo import MongoClient
import uuid

client = MongoClient()
configCollection = '_config'

def getAllDbs():
	return client.database_names()

def getAllProjects():
	projects = []
	for db in getAllDbs():
		if configCollection in client[db].collection_names() and len(list(client[db][configCollection].find({"option": "token"}))) > 0:
			projects.append(client[db])
	return projects

def getProject(name):
	return client[name]

def removeDB(dbname):
	client.drop_database(dbname)

def createDB(dbname):
	try:
		db = client[dbname]
		collection = db[configCollection]
		collection.insert({"option": "token", "value": str(uuid.uuid4())})
		return 'created'
	except:
		return 'Failed to create database'