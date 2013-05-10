from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from settings import root_directory

urlpatterns = patterns( '' ,
(r'^files/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': root_directory + '/static'}),
(r'^example_app/$','example_app.views.index'),
(r'^example_app/(?P<poll_id>\d+)/$','example_app.views.details'),
(r'^edit_field/',include('edit_field.urls')),        
(r'^edit_field/static/(?P<path>.*)$', 'django.views.static.serve',
  {'document_root':root_directory + '/edit_field/static'}))            

