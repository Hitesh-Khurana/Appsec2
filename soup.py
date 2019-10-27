# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import re
from html.parser import HTMLParser
import mechanize
#import urllib2 
#import cookielib
#import feedparser
import urllib
#session = requests.Session()
#url = session.get("http://127.0.0.1:5000/register")
site = mechanize.Browser()
site.open("http://127.0.0.1:5000/register")
site.select_form(id="inputtext")
site.form['username'] = 'username12'
site.form['password'] = 'password1.'
site.form['twoFactor'] = '2fa12'
site.submit()

#print (site.response().read().prettify())
soup = BeautifulSoup(site.response().read(),"html.parser")
all_paragraphs = soup.find('p').getText()
print (all_paragraphs) #prints id success for registration



#page = urllib.request.urlopen(url)
#parse the html page.
#soup = BeautifulSoup(page, "html.parser")
#print(soup)

#alltext = soup.find('p')
#print(alltext)
#myinput = soup.find_all(input)
#elementidsuccess = soup.find_all(id="success")


#define url
#url = "http://127.0.0.1:5000/register"

