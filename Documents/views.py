from django.shortcuts import render

# Create your views here.
#index will load the html file
def index(request):
    return render(request,'index.html')