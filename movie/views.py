# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    #return render( request,'home.html')
    return render(request,'home.html', {'name':'Juan Jose Villa Soria'})