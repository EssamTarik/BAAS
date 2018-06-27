from django.http import HttpResponse
from ..models.projects import getAllProjects, removeDB, createDB

def removeProject(request):
	dbname = request.GET.get('name', '')
	if dbname not in [x.name for x in getAllProjects()]:
		return HttpResponse('this project doesn\'t exist')
	try:
		removeDB(dbname)
		return HttpResponse('removed')
	except Exception as e:
		print str(e)
		return HttpResponse('failed to remove the database')

def createProject(request):
	dbname = request.GET.get('name', False)
	if dbname == False:
		return HttpResponse('invalid name')

	if dbname[0] == '_':
		return HttpResponse('Database name cannot start with an underscore')
	else:
		res = createDB(dbname)
		return HttpResponse(res)