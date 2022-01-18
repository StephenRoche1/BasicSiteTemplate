from django.urls import path
from . import views

urlpatterns =[
    #calls the rendering function to display the html page
    path('',views.index,name='index')
]