from django.shortcuts import render
from django.http import HttpResponse
from ..models.projects import getAllProjects

def index(request):
	projects = []
	for project in getAllProjects():
		projects.append({"name": project.name, "collections": project.collection_names()})

	return render(request, 'index.html', {"projects": projects})
