from django.shortcuts import render
from ..models.projects import getProject

def viewDB(request, dbname):
	project = getProject(dbname)
	projectName = project.name
	projectToken = list(project['_config'].find({'option': "token"}))[0]['value']
	collections = project.collection_names()

	return render(request, 'db.html' , {"project": {"name": projectName, "collections": collections, "token": projectToken}})