from django.urls import path
from . import views

# TEMPLATE URLS

app_name= 'basic_app'

urlpatterns = [
    path('', views.index, name ='index'),
    path('home/',views.index, name= 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special')

]
