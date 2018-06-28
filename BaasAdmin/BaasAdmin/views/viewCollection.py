from django.shortcuts import render
from django.http import HttpResponse
from ..models.collections import getCollection
from bson.json_util import dumps
import json

def extractID(obj):
	editedObj = {}
	editedObj['content'] = json.dumps(obj)
	editedObj['id'] = obj['_id']['$oid']
	return editedObj
def viewCollection(request, dbname, collectionName):
	collection = getCollection(dbname, collectionName)
	if not collection:
		return HttpResponse("Failed to find the collection in this database")
	else:
		data = map(extractID, json.loads(dumps(collection.find({}))))
		print data
		return render(request, 'collection.html', {"collection": {"db": dbname, "name": collectionName, "data": data}})