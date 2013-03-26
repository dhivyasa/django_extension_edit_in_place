from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ssrweb.local_extensions.views',
   url(r'^editinplace$','edit_in_place'),
)

