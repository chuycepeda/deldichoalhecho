from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deldichoalhecho_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('deldichoalhecho_web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# Your other patterns here
urlpatterns += [
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]