from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('projects/',views.project,name='projects'),
    path('error404/',views.error404,name='error404')
]


