# importing libraries
from bs4 import BeautifulSoup
#import urllib.request
import re
from html.parser import HTMLParser
import mechanize
#import urllib
import unittest
#import flaskr
import tempfile
from app import *
import requests
import testutils
from flask_sessionstore import Session
from flask import session
import http.cookiejar
#from factory import create_app
#import cookiejar

#cj = cookielib.LWPCookieJar() 

#session = requests.Session()
url = 'http://127.0.0.1:5000'

app.config['SESSION_TYPE'] = 'filesystem'
sessionstore = Session(app)
#site.open("http://127.0.0.1:5000/login")
#site.select_form(id="inputtext")
#site.form['username'] = 'username2212'
#site.form['password'] = 'password1.'
#site.form['twoFactor'] = '2fa12'
#site.submit()
#site = mechanize.Browser()
#		site.set_handle_robots(False)
#		#site.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#		site.open("http://127.0.0.1:5000/login")
#		site.select_form(id="inputtext")
#		site.form['username'] = 'admin'
#		site.form['password'] = 'admin'
#		site.form['twoFactor'] = '1234567890'
#		site.submit()
#		site = mechanize.Browser()
#		soup = BeautifulSoup(site.response().read(),"html.parser")
#		all_paragraphs = soup.find('p').getText()
#		site.close()

#print (site.response().read().prettify())
#soup = BeautifulSoup(site.response().read(),"html.parser")
#all_paragraphs = soup.find('p').getText()
#print (app.all_paragraphs) #prints id success for registration

#print (session['a'])
class apptest(unittest.TestCase):

	def setUp(self):
		#self.app.config['TESTING'] = True
		#self =app.run(debug=True)
		#self.app.config['DEBUG'] = True
		pass
		#flaskr.app.testing = True
		app.test_client()
	def tearDown(self):
		#request.environ.get('werkzeug.server.shutdown')
		#site.close()
		pass#app.shutdown()
		#db.session.remove()
		#db.drop_all()
	#def login(self):
		
			#self.assertEqual(result.data,json.dumps(sent))
	#def login(self, username, password, twofactor ):
	#	return self.requests.get('/login', data=dict(
    #    username=username,
    #    password=password, twoFactor=twofactor
    #), follow_redirects=True)
	#
	#x = soup.find('p').getText()
	

		#sent = {'username2aa212','password1','2fa12'}
		#result = ('/login', request.method='POST', data=sent)
	#	with app.test_client() as client:
	#		sent = {'username2aa212','password1','2fa12'}
#			result = client.post('/login',data=sent)
	#def test_register(self):
 	#	headers = {'content_type=application/x-www-form-urlencoded'}
	#	resp = requests.post('http://127.0.0.1/login', data='username=admin&password=admin&twoFactor=1234567890') 
	#	resp = requests.check_content_type()
	#	soup = BeautifulSoup(resp.response().read(),"html.parser")
	#	assert all_paragraphs == 'Logged in successfully'
			#soup = BeautifulSoup(client.response().read(),"html.parser")
		#client.post.login()
		#print (all_paragraphs)
#		assert soup == b'Registered successfully, Please Login'
	def test_login_invalid_phone(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/login")
		site.select_form(id="inputtext")
		site.form['username'] = 'username12'
		site.form['password'] = 'password1.'
		site.form['twoFactor'] = '2fa12'
		#mech->cookie_jar(HTTP::Cookies->new());
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		all_paragraphs = soup.find('p').getText()
		print ("Running Test 1", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'Two-factor failure'

	def test_register_with_invalid_phone(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/register")
		site.select_form(id="inputtext")
		site.form['username'] = 'username122x'
		site.form['password'] = 'password1.'
		site.form['twoFactor'] = '2fa12'
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		all_paragraphs = soup.find('p').getText()
		print ("Running Test 2 this is all_paragraphs: ", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'Two-factor failure'		

	def test_duplicate_user(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/register")
		site.select_form(id="inputtext")
		site.form['username'] = 'asd'
		site.form['password'] = 'password1.'
		site.form['twoFactor'] = '0123456789'
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		all_paragraphs = soup.find('p').getText()
		print ("Running Test 3", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'User already exists please login'	

	def test_login_is_valid(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/login")
		site.select_form(id="inputtext")
		site.form['username'] = 'admin'
		site.form['password'] = 'admin'
		site.form['twoFactor'] = '1234567890'
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		all_paragraphs = soup.find('p').getText()
		print ("Running Test 4", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'Logged in successfully'
	
	def test_misspelled_words(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/login")
		site.select_form(id="inputtext")
		site.form['username'] = 'username12'
		site.form['password'] = 'password1.'
		site.form['twoFactor'] = '0123456789'
		print("the login was successful")
		site.submit()
		#app.my_var = True
		#print (app.my_var)
		#site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/spell_check")
		#br.set_cookiejar(cj) 
		site.select_form(id="inputform")
		site.form['word'] = 'Take a sad sogn and make it better. Remember to let her under your skyn, then you begin to make it betta.'
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		#print (soup)
		all_paragraphs = soup.find('p',id='misspelled').getText()
		print ("Running Test 5", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'sogn, skyn, betta'
		

	def test_display_input_words(self):
		site = mechanize.Browser()
		site.open("http://127.0.0.1:5000/login")
		site.select_form(id="inputtext")
		site.form['username'] = 'username12'
		site.form['password'] = 'password1.'
		site.form['twoFactor'] = '0123456789'
		print("the login was successful")
		site.submit()
		site.open("http://127.0.0.1:5000/spell_check")
		site.select_form(id="inputform")
		site.form['word'] = 'Take a sad sogn and make it better. Remember to let her under your skyn, then you begin to make it betta.'
		site.submit()
		soup = BeautifulSoup(site.response().read(),"html.parser")
		all_paragraphs = soup.find('p',id='textout').getText()
		print ("Running Test 6", all_paragraphs) #prints id success for registration
		assert all_paragraphs == 'Take a sad sogn and make it better. Remember to let her under your skyn, then you begin to make it betta.'	

	def test_pages_exist__reference_rahul_video(self):
		PAGES = ["/login", "/register"]
		for page in PAGES:
			req = requests.get(url + page)
			self.assertEqual(req.status_code, 200)
		print ("Running Test 7") #prints id success for registration

		#assert all_paragraphs == 'Take a sad sogn and make it better. Remember to let her under your skyn, then you begin to make it betta.'	



if __name__ == '__main__':
	unittest.main()

# login,
# invalid, valid, two factor letters and not numbers,
# register,
# spell check,
# program done
# auto grader 
# unit testing
# tox, with unit testing
# sample attacking.
# see if it says to mitigate, that is more accurate
# using jinja templates 
# report
# next sunday the 26th
# max of 10 pages

#def test_login(self):
#	 assert 'Logged in successfully'
#Logged in successfully

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

