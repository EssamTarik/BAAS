from django.db import models
from pymongo import MongoClient

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
