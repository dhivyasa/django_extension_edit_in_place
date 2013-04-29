from django.conf.urls.defaults import patterns,include,url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('example_app.views',
url(r'^$','index'),
url(r'^(?P<poll_id>\d+)/$', 'details'),
)
