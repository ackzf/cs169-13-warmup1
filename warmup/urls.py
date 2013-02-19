from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmup.views.home', name='home'),
    # url(r'^warmup/', include('warmup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$/', index, name='index'),
)

from django.http import HttpResponse

def index(request):
    return HttpResponse("<!DOCTYPE html><html><head><meta http-equiv='refresh' content='1; url=http://www.google.com/'/></head></body></html>")
