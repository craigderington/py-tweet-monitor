from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):

    # read our json file line by line
    tweets = {}
    with open('data/stream_python.json', 'r') as tweet_data:
        for line in tweet_data:
            try:
                tweet = json.loads(line)
                for key, value in tweet.items():
                    if key == 'text':
                        print(value)
            except:
                continue

    return render(request, 'pyTweetMonitor/index.html', tweets)
