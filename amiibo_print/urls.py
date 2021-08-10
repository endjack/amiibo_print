from django.contrib import admin
from django.urls import path
from print.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('print/', amiibo_print, name='print-page'),
]
