from django.urls import path
from .views import *

urlpatterns = [
    path('api/', MainListView.as_view(), name='api'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('main/', main, name='main'),
    path('add/', add, name='add'),
    path('main_list/', Search.as_view(), name='main_list'),
    path('main_list/delete/<int:id>/', delete, name='delete'),
]