from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from catalog import views

urlpatterns = [
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]

