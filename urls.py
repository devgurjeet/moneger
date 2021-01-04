# -*- coding: utf-8 -*-
from django.conf.urls import url, include, path
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

urlpatterns = [
   path('admin/', admin.site.urls),
] + aldryn_addons.urls.patterns() 

