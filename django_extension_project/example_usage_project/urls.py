from django.conf.urls.defaults import patterns, include
from settings import root_directory

urlpatterns = patterns( '' ,
(r'^edit_field/',include('edit_field.urls')),        
(r'^edit_field/static/(?P<path>.*)$', 'django.views.static.serve',
  {'document_root':root_directory + '/edit_field/static'}))            

