from urllib.request import Request,urlopen,ProxyHandler
import bs4
from .models import *
from urllib.error import HTTPError

countries = []

if countries == []:
        initial= Request('https://www.worldometers.info/geography/alphabetical-list-of-countries/',headers={'User-Agent':'Chrome/9.0'})
        req = urlopen(initial).read()
        html = bs4.BeautifulSoup(req,'lxml')

        for i in html.find_all('tr')[1:]:
            country = i.find_all('td')[1].text
            countries.append(country)
    
def search_res(search):
    global countries
    
    result = []

    for count in countries:
        if count[:len(search)].lower() == search.lower():
            result.append(count)
        
    return result
			
def info(country):
        try :
            found = COUNTRY.objects.get(name=country)
            return found.para1, found.para2
        
        except:
            initial= Request('https://en.wikipedia.org/wiki/'+ country.lower().replace(' ','%20'), headers={'User-Agent':'Chrome/9.0'})
            req = urlopen(initial).read()
            html = bs4.BeautifulSoup(req,'lxml')
            paragraphs = html.find_all('p')[1:]
            PARA_1 = paragraphs[0].text
            PARA_2 = paragraphs[1].text
            COUNTRY.objects.create(name=country, para1= PARA_1 , para2= PARA_2)  

            return PARA_1,PARA_2
    

def twitter_trends(Country):
    try:
        proxies = {'http':'187.243.255.174:8080'}
        ProxyHandler(proxies=proxies)
        trending = {}
        initial = Request('https://twitter-trends.iamrohit.in/'+ Country.lower().replace(' ','-'), headers={'User-Agent':'Chrome/5.0'})
        req = urlopen(initial).read()
        html = bs4.BeautifulSoup(req,'lxml')
        for i in html.find_all('tr')[1:7]:
            trending[i.find_all('a')[0].text]=i.find_all('span')[0].text
            
        print('trending')
        return trending
    except HTTPError as e:
         print(e.read())

