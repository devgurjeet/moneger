# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

api_urls = [
    path('todos/', include('todos.urls')),
    path('', include('users.urls')),
]

urlpatterns = [
    path('api/', include(api_urls)),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns(),  # MUST be the last entry!
    
)
