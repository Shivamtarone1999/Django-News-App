from django.shortcuts import render

# Create your views here.

def index(request):
    import requests
    import json
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(news_api_request.content)
    context = {'api':api}
    return render(request,'home.html',context)


def businessNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'business.html',context)


def entertainmentNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'entertainment.html',context)


def scienceNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'scienceNews.html',context)

def healthNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'healthNews.html',context)


def technologyNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'technologyNews.html',context)


def sportsNews(request):
    import requests
    import json  
    business_news_api = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=64b9a4f94b114625ade72fc00c395e8a")
    api = json.loads(business_news_api.content)
    context = {'api':api}
    return render(request,'sportsNews.html',context)

