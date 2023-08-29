from django.urls import path
from Tests.views import *

urlpatterns = [
    path('listview', listView, name = 'listview'),
    path('detailview', detailView, name = 'detailview'),
    path('deleteview', deleteView, name = 'deleteview'),
    path('imgupload', imageupload, name='imageupload'),
]

app_name = 'Tests'