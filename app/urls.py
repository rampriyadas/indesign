from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('jobs/addjob', addjob, name='addjob'),
    path('jobs/viewjobs', jobs, name='viewjobs')
]
