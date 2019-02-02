from bs4 import BeautifulSoup
import requests
import re
import json
from utilities import utils


#this should contain all scrapers
class scrapers(object):
	#initialise the validators so we initialis it one
	def __init__(self):
		self.u = utils()
		pass
	
	
		
	#mihaaru is a special case as it has weird ordering system
	def mihaaru(self,id):
		#arrticles are returned as a dictionoary 
		articles = []
		
		url = "https://mihaaru.com/news/"+str(id)
		page = requests.get(url)
		html = page.text
		#parse the received html
		parsed_html =  BeautifulSoup(html, 'html.parser')
		#definitely needsbetter error handling
		if len(parsed_html) != 61:
			#get required data
			headline = (parsed_html.h1).get_text()
			image = parsed_html.find("img", {"data-index":"1"})["src"]
			time = parsed_html.find("span",{"class":"date-time"}).get_text()
			author = parsed_html.find("address").get_text()  
			category_span = parsed_html.find_all("a",{"href":"/"})[2]
			category = category_span.find("span",{"class":"navbar-brand"}).get_text()
			   	

			#getting the article is diffrent
			article_div = parsed_html.find("article").find_all('p')
			article = ""
			for s in article_div: #this can be and must be improved
				article += "\n"+  s.get_text()


				
				#parses all the data
				parsed_data = self.u.ParseData(url,headline,image,author,category,article,time,"mihaaru",id)
			  

				
				return(parsed_data)



	#redoing sun with beatifulsoup parsing
	def SunSoup(self):
		try:
			xml = requests.get("https://sun.mv//feed/")
			parsed_xml = BeautifulSoup(xml.text, 'html.parser')
			entries = parsed_xml.find_all("item")
		except:
			return("error")
		#we loop over all entries
		valid_data = []
		i = 0
		for x in entries:
			#print(x)
			headline = x.find_all('title')[0].get_text()
			article = x.find_all("content:encoded")[0].get_text()
			url = x.find_all("url")[0].get_text()
			image = x.find_all("image")[0].get_text()
			date = x.find_all("pubdate")[0].get_text()
			author =""
			category = ""

			valid_data.append(self.u.ParseData(url,headline,image,author,category,article,date,"sun",1))
			i += 1

		return (valid_data)
		
	def sun(self,id):

		url = "https://sun.mv/"+str(id)
		html = requests.get(url)
		parsed_html = BeautifulSoup(html.text,'html.parser')

		if len(parsed_html) >= 4:
			headline = (parsed_html.h1).get_text()
			image = parsed_html.find("figure").find("img")["src"]
			time_tag = parsed_html.find("span",{"class":"time"}).get_text()
			category = ""
			author = ""

			#get the article content
			article_div = parsed_html.find("div",{"class","component-article-content clearfix"}).find_all("p")
			article = ""
			for x in article_div:
				article += "\n" + x.get_text()

			u = utils()
			valid_data = self.u.ParseData(url,headline,image,author,category,article,time_tag,"sun",id)

			return(valid_data)





	

	#scrape avas noos
	def avas(self,id):
   		#please pu try block here
		url = "https://avas.mv/"+str(id)
		html = requests.get(url)
		parsed_html = BeautifulSoup(html.text,'html.parser')





		


		if len(parsed_html) >= 3:
			headline = (parsed_html.h1).get_text()
			image = parsed_html.find("figure").find("img")["src"] # stupid lazy oneliner,but it works might have to redo it
			time_tag  = parsed_html.find("div",{"class","ltr text-sm text-grey-dark pl-2"}).find("timeago")["datetime"] #get the date/time
			#author = parsed_html.find("div",{"class":"font-waheed text-grey ml-3 pl-3 text-lg border-l border-grey border-dotted"}).find('a').get_text() #me back again with my lazy onliners
			author = "" #author empty as rrors sometimes occur during fetching this
			category = parsed_html.find("div",{"class":"rtl container mx-auto mb-7 mt-8 px-4 md:px-0"}).find("a").get_text()


			#paragraphs are seperate so loops and adds them up
			article_div = parsed_html.find("div",{"class","w-full md:w-5/6"}).find_all("p")
			article = ""
			for x in article_div:
				article += "\n" + x.get_text()

			u = utils()
			valid_data = self.u.ParseData(url,headline,image,author,category,article,time_tag,"avas",id)

			return(valid_data)

	#pretty similar to others but date is weird
	#vfp is cnm now
	def vfp(self,id):
		url = "https://cnm.mv/f/?id=" + str(id)
		html = requests.get(url)
		parsed_html = BeautifulSoup(html.text,'html.parser')
		if len(parsed_html) >= 5: 
		#get individual attributes
			headline = (parsed_html.h1).get_text()
			unparsed_image = parsed_html.find("img",{"class":"w-100"})["src"]
			image = "https://cnm.mv" + unparsed_image[2:]
			time_div = parsed_html.find("i",{"class":"fa fa-clock-o pr-2"}).get_text()
			time = time_div.split("|",1)[0]
			author = ""
			category = parsed_html.find("div",{"class":"col-12 py-3 t5"}).find("a").get_text()
			article = parsed_html.find("div",{"class":"artT"}).get_text()

			valid_data = self.u.ParseData(url,headline,image,author,category,article,time,"vfp",id)
			return valid_data
		else:
			print(parsed_html)
			return("error")


	def psm(self,id):
		try:
			url = "https://psmnews.mv/" + str(id)
			html = requests.get(url)
			parsed_html = BeautifulSoup(html.text,'html.parser')
		except:
			return("error")
		if len(parsed_html) >= 21: #weird lentghs
			#parse individual elements
			headline = (parsed_html.h1).get_text()
			image = parsed_html.find("img",{"class":"w-full"})["src"]
			time = parsed_html.find("time")["datetime"]
			author = ""
			category = parsed_html.find("div",{"class":"rtl bg-white container mx-auto p-6 md:p-6"}).find("a").get_text()
			article = parsed_html.find("div",{"class":"content block"}).find("p").get_text()

			valid_data = self.u.ParseData(url,headline,image,author,category,article,time,"psm",id)


			return (valid_data)
		





		








				
			










#TODO

