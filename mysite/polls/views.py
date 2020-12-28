from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index_page(request, id):
    return HttpResponse('This is INT urls test. id = ' + str(id))

def index_str(request, id):
    return HttpResponse('This is STR urls test. id = ' + str(id))