from django.http import HttpResponse

def removeProject(request):
	print request
	return HttpResponse('removed')