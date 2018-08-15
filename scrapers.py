from bs4 import BeautifulSoup
import requests
import re
from utilities import utils

#this should contain all scrapers
class scrapers():
    #mihaaru is a special case as it has weird ordering system
    def mihaaru(id):
    	#arrticles are returned as a dictionoary 
        articles = []
        for id in range(id,id+1):
            url = "https://mihaaru.com/news/"+str(id)
            page = requests.get(url)
            html = page.text
            #parse the received html
            parsed_html =  BeautifulSoup(html, 'html.parser')
            print(len(parsed_html))
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
                u = utils()
                parsed_data = u.ParseData(url,headline,image,author,category,article)
              

                
                return(parsed_data)

                
            

check = scrapers.mihaaru(40342)    
print(check)        

#TODO
