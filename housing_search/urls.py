from django.contrib import admin
from django.urls import path
from django.conf.urls import url

import housing.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', housing.views.index, name = 'index'),
]
