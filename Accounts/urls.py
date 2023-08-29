from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('', index_page, name = 'index'),
    path('register', user_register, name = 'register'),
    path('login', user_login, name = 'login'),
    path('logout', user_logout, name = 'logout'),
    path('aboutus', aboutus, name = 'aboutus'),
    path('img', image, name = 'image'),
    path('home', home, name = 'home'),
    
    path('inptest', inptest, name = 'inptest'),
]

app_name = 'Accounts'