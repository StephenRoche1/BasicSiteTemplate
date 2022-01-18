from django.urls import path
from . import views

urlpatterns =[
    #render the Documents html
    path('',views.index,name='index')
]