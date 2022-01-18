from django.urls import path
from . import views

urlpatterns =[
    #render the admin page
    path('',views.index,name='index')
]