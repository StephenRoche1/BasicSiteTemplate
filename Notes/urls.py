from django.urls import path
from . import views

urlpatterns =[
    #render the notes page
    path('',views.index,name='index')
]