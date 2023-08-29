from django.urls import path
from Programs.views import *

urlpatterns = [
    path('listview', listView, name = 'listview'),
    path('recView', recView, name = 'recView'),
    path('ongoingView', ongoingView, name = 'ongoingView'),
    path('detailview', detailView, name = 'detailview'),
    path('take_program', take_program, name = 'take_program'),
    path('inptest', inptest, name = 'inptest'),
]

app_name = 'Programs'