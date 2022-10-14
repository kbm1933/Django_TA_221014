import imp
from django.urls import path
from . import views
from user import views

urlpatterns = [
    path('signup/',views.sign_up_view,name='singup'),
    path('login/',views.sign_in_view,name='login'),
]