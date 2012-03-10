from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mostly_static_pages.views.home', name='home'),
    # url(r'^mostly_static_pages/', include('mostly_static_pages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

   
   url(r'^admin/', include(admin.site.urls)),
   url(r'^home$', 'mostly_static_pages.home.views.home'),
   url(r'^contact$', 'mostly_static_pages.contact.views.contact'),
   url(r'^about$', 'mostly_static_pages.about.views.about'),
   

   )
