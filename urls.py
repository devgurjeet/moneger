# -*- coding: utf-8 -*-
from django.conf.urls import url, include, patterns
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

urlpatterns = [
   
] + aldryn_addons.urls.patterns() + patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
