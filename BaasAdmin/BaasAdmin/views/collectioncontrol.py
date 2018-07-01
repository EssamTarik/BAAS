from ..models.collections import removeCollection, createCollection
from django.http import HttpResponse

def dropCollection(request):
	dbname = request.GET.get('dbname')
	collection = request.GET.get('collection')
	removeCollection(dbname, collection)
	return HttpResponse('dropped')

def newCollection(request):
	dbname = request.GET.get('dbname')
	collection = request.GET.get('collection', False)
	if not collection or collection[0] == '_' or len(collection) == 0:
		return HttpResponse('invalid collection name')
	createCollection(dbname, collection)
	return HttpResponse('created')