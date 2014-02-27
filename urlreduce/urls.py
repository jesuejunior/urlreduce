from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from reducer.views import HomeTemplateView, MyLinksTemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^$', MyLinksTemplateView.as_view(), name='my-links'),

    # url(r'^urlreduce/', include('urlreduce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^users/*', RedirectView.as_view(url='/my-links/')),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
