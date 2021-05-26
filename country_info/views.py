from django.shortcuts import render
from . import scraper
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request,'country_info/home.html',context)

def info(request,country):
    if country not in scraper.countries:
        return HttpResponse('What are you up to??🤨')
    else:
        paras = scraper.info(country)
        para_1 = paras[0]
        para_2 = paras[1]
        trending = scraper.twitter_trends(country)
        context ={'country':country, 'para_1':para_1, 'para_2':para_2,'trending':trending}
        return render(request,'country_info/info.html',context)
