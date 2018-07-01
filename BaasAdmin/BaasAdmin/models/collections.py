from django.db import models
from pymongo import MongoClient
import uuid

client = MongoClient()
configCollection = '_config'

def getAllCollections(dbname):
	collections = client[dbname].collection_names()
	try:
		collections.remove('system.indexes')
	except Exception:
		pass
	return collections

def getProjectCollections(dbname):
	collections = []
	for collectionName in getAllCollections():
		if collectionName[0] == '_':
			collections.append(client[dbname][collectionName])
	return collection

def getCollection(dbname, collectionName):
	if collectionName[0] != '_' and collectionName in getAllCollections(dbname):
		return client[dbname][collectionName]
	else:
		return False

def removeCollection(dbname, collectionName):
	client[dbname][collectionName].drop()

def renameCollection(dbname, collectionName, newCollectionName):
	client[dbname][collectionName].rename(newCollectionName)

def createCollection(dbname, collectionName):
	print dbname
	client[dbname].create_collection(collectionName)