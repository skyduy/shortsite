from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
document_root = settings.STATIC_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^$', 'short.views.index'),
    url(r'^Add/$', 'short.views.add'),

    url(r'^Js/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':document_root+'/js'}),
    url(r'^Images/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root':document_root+'/images'}),
    url(r'^Css/(?P<path>.*)$','django.views.static.serve',
                         {'document_root':document_root+'/css'}),
    url(r'^([a-z0-9]{4})$','short.views.jump'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)

# Serve static files for admin, use this for debug usage only
# `python manage.py collectstatic` is preferred.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()