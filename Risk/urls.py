from django.urls import path
from . import views

urlpatterns =[
    #Render the Risk html page
    path('',views.index,name='index')
]
