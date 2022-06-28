from django.urls import path
from .views import *
urlpatterns = [
    path('', calendar_s),
    path('create', CreateEvent.as_view()),
    path('events', GetEvents.as_view()),
    path('event', GetDetailEvent.as_view()),
    path('update', UpdateEvent.as_view()),
    path('archives', GetArchivesEvents.as_view()),
]