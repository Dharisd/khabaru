from bs4 import BeautifulSoup
import requests

#this should contain all scrapers
class scrapers():
    #mihaaru is a special case as it has weird ordering system
    def mihaaru(id):
        articles = []
        for id in range(id,id+1):
            url = "https://mihaaru.com/news/"+str(id)
            page = requests.get(url)
            html = page.text
            parsed_html =  BeautifulSoup(html, 'html.parser')
            print(len(parsed_html))
            if len(parsed_html) != 61:
                headline = (parsed_html.h1).get_text()
                image = parsed_html.find("img", {"data-index":"1"})["src"]
                time = parsed_html.find("span",{"class":"date-time"}).get_text()
                author = parsed_html.find("address").get_text() 
                content = parsed_html.find("article").get_text()
                category_span = parsed_html.find_all("a",{"href":"/"})[2]
                category = category_span.find("span",{"class":"navbar-brand"}).get_text()

                file = open("textfile.txt", "w",encoding="utf-8")
                file.write(content)

                file.close()
                return(headline,content)

                
            

scrapers.mihaaru(40093)            


  