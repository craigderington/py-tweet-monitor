from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('This is the PyTweetMonitor index page')
    # return render(request, 'pyTweetMonitor/index.html', context)
