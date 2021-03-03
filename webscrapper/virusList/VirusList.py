#Jhony Ortiz
#04/19/2018
#VirusList.py

#import the libraries
from urllib.request import urlopen as uReq # Web Cliet
from bs4 import BeautifulSoup as soup # HTML Data Structure

# URL for the website 
my_url = 'https://us.norton.com/online-threats/'

# Opening connection, grabbing the page, saving it to a variable
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, 'html.parser')

#grabs the html table we need
table = page_soup.findAll('table',{'class':'listings-table mixed'})
#grabs all the rows inside the table
row = page_soup.table.findAll('tr',{'class':'threat-row'})

#open a file to save the information
filename = 'viruslist.csv'  # File name
f = open(filename, 'w')     # Opening the file
headers = 'Threat Name, Threat Type, Date\n' # Adding headers to the file
f.write(headers) # Writing the headers to the file

#loops over each row and grabs the information 
for threat in row:
    #grabs the information from the class named threat-cell name
    threat_name = threat.findAll('td',{'class':'threat-cell name'})
    name = threat_name[0].text # pulls only the Text
    #grabs the information from the class named threat-cell type
    threat_kind = threat.findAll('td',{'class':'threat-cell type'})
    kind = threat_kind[0].text # pulls only the text
    #grabs the information from the call named threat-cell date
    threat_date = threat.findAll('td',{'class':'threat-cell date'})
    date = threat_date[0].text # pulls only the text

    #this will include the commas inside the kind variable
    kindCommas = "\"" + kind + "\""
    #writes the information on the file
    f.write(name + ',' + kindCommas + ',' + date + '\n')
#closes the file
f.close()
 
