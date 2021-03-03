#Jhony Ortiz
#INF 103
#4/22/18
#newShows.py

#import libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#URL for the website
my_url = 'http://www.tvguide.com/special/fall-preview/new-shows/'

# Opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#finds all the div with the class we want 
shows = page_soup.findAll('div',{'class':'seasonal-new-shows-item'})

#loops over all the information and prints it
for show in shows:
    show_title = show.findAll('h2',{'class':'seasonal-new-shows-item-content-title'})
    title = show_title[0].text

    show_channel = show.findAll('span',{'class':'seasonal-new-shows-item-content-channels'})
    channel = show_channel[0].text

    show_premiere = show.findAll('span',{'class':'seasonal-new-shows-item-content-premiere'})
    premiere = show_premiere[0].text

    show_descr = show.findAll('p',{'class':'seasonal-new-shows-item-content-description'})
    descr = show_descr[0].text

    print(title,'\n',channel,'\n', premiere,'\n', descr)

 
   
