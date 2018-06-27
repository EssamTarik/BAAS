from django.http import HttpResponse

def viewCollection(request, dbname, collection):
	strs = dbname + ' / ' + collection
	return HttpResponse(strs)