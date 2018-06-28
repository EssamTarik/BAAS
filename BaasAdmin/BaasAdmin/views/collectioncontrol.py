from ..models.collections import removeCollection
from django.http import HttpResponse

def dropCollection(request):
	dbname = request.GET.get('dbname')
	collection = request.GET.get('collection')
	removeCollection(dbname, collection)
	return HttpResponse('dropped')