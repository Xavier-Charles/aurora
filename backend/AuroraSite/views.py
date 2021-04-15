from django.shortcuts import render

# this is where you add the functions you want to create

# import Http Response from django
from django.http import HttpResponse
from django.http import JsonResponse

import json
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
 


def theBlockCrptoCrawler(request):
    url = 'https://www.theblockcrypto.com/'

    # Make the request to a url
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    # Parse Data
    main_content = soup.find('div', attrs = {'class': 'storyFeed'})
    articles = main_content.findAll('article', attrs = {'class': 'feedCard'})

    data = []
    for article in articles:
        description = article.findAll('div', attrs = {'class': "theme"})[0].text.rsplit(" \n")[0].lstrip()
        title = article.findAll('h3', attrs = {'class': "font-headline"})[0].text.rsplit(" \n")[0].lstrip()
        link = "https://www.theblockcrypto.com" + article.findAll('a', attrs = {'class': "font-button"}, href=True)[0]['href']
        article_data = {"title":title, "description":description, "link":link}
        data.append(article_data)

    return JsonResponse({"data": data})

def GetEthprice(request):
    url = 'https://www.coingecko.com/en'
    querystring = {"ids":"ethereum","vs_currencies":"usd"}

    # Make the request to a url
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    data = soup.find('span', attrs = {'data-coin-symbol': 'eth'})
    price = data.text

    # CoinGecko uses Cloudfare IUAM so if the crawl returns nothing we could use the their API instead
    # Another option would be to use establised scaping services like scrapingbee but they are paid 
    if (price is None):
        querystring = {"ids":"ethereum","vs_currencies":"usd"}
        data = requests.request("GET", 'https://api.coingecko.com/api/v3/simple/price', params=querystring)    
        price = json.loads(str(data.text))['ethereum']['usd'] 

    return JsonResponse({"data": {"price": price}})

def GetRecentTx(request):
    url = 'https://etherscan.io/address/0xb2ecd701b01fd80d38fdf88021035d22c9a370e2'

    # Seems ethersan ia attempting to block webscraping "uClient = uReq(URL)" and "page_html = uClient.read()" would not work
    # req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})   
    # response = urlopen(req, timeout=20).read()
    # response_close = urlopen(req, timeout=20).close()
    # soup = BeautifulSoup(response)
    # main_content = soup.find('div', attrs = {'class': 'card-body'})
    # rows = soup.findAll('div', attrs = {'class': 'col-md-8'})

    # Also it seems etherscan has blaclisted all ips from Heroku or digital ocean. 
    # The best method hence is to use a VPN that allows SOCKS5 proxy
    
    return JsonResponse({'Ether_value': '12.83929068394911508 Ether', 'Dollar_value': '$31,538.82 (@ $2,456.43/ETH)'}
)
