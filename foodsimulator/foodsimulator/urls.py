from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'DTU Food Simulator App'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodsimulator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^learn/',include('learn.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)