# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<!DOCTYPE html><html><head><meta http-equiv='refresh' content='1; url=http://www.google.com/'/></head></body></html>")
