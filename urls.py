# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.urls import path

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

api_urls = [
    url('todos/', include('todos.urls')),
    url('', include('users.urls')),
]

urlpatterns = [
    url('api/', include(api_urls)),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),

] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns(),  # MUST be the last entry!
 )


