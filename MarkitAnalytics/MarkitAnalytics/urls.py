from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

import curves.views

urlpatterns = patterns(
    '',
    url(r'^$', curves.views.home, name='home'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
