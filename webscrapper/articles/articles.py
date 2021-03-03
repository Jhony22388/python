#Jhony Ortiz
#4/22/18
#articles.py

#import the libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

# URL for the website
my_url = 'https://lifehacker.com/'

#opening file, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#get the top articles
articles = page_soup.findAll('div',{'class':'curation-module__zone grid__zone tall'})

#loops over all the articles and prints them
for n in articles:
    new = n.text
    print(new,'\n')
