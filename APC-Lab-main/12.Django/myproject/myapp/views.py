from django.http.response import HttpResponse # type: ignore

def home(request):
    return HttpResponse("<h1>Hello World!</h1>")