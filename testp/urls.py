from django.conf.urls import patterns, include, url




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('books.views',

    url(r'^$', 'home', name='home'),
    url(r'^link/concrete/show/$','concrete'), # если поставить первым то конкрет выйдет на него
    url(r'^link/([^/]+)/show/$','every'),




    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),



)
