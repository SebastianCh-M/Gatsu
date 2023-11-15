from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



app_name= 'manga'

urlpatterns = [

]

urlpatterns = format_suffix_patterns(urlpatterns)
