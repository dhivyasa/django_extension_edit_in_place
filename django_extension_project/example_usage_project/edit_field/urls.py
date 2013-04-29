from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('example_usage_project.edit_field.views',
   url(r'^editinplace$','edit_in_place'),
)

