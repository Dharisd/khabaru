import dateparser
import re

#this file will contain the utilities like texting text parser and date parsers that the scraper needs

class utils(object):
	#define self
	def __init__(self):
		pass
		

	#parse the date into python datetime object
	def ParseDate(self,unparsed_date,source):

		months_dhivehi= ["ޖަނަވަރީ", "ފެބްރުއަރީ", "މާޗް", "އޭޕްރިލް", "މެއި", "ޖޫން", "ޖުލައި", "އޯގަސްޓް", "ސެޕްޓެމްބަރ", "އޮކްޓޯބަރ", "ނޮވެމްބަރ", "ޑިސެމްބަރ"]
		months_english = ["january","february","March","april","may","june","july","august","september","october","november"]


		if source == "vfp" and ("ގަޑިއިރު ކުރިން" in unparsed_date):
			time_english = unparsed_date.replace("ގަޑިއިރު ކުރިން","hours ago")
			date = dateparser.parse(time_english)
			return(date)
		elif (source == "vfp"):
			months_dhivehi[7] = "އޯގަސްޓު"


		#all this function has to is to change the dhivehi month into english month and then feed into dateparser
		for month in months_dhivehi:
			if month in unparsed_date:
				month_n = months_dhivehi.index(month)
				month_english = months_english[month_n]
				#generate new string
				date_english = unparsed_date.replace(month, month_english)
				datetime_object = dateparser.parse(date_english) 
				return(datetime_object)
		try:
			date = dateparser.parse(unparsed_date)
			return(date)
		except:
			return("error")



	#this functions must parse dhivehi news categories into english categories
	def ParseCategory(self,unparsed_category):
		categories_dhivehi = ["ހަބަރު","ފޭޑި","ވާހަކަ","ވީޑިއޯ","ދުނިޔެ","ކޮލަމް","ވިޔަފާރި","މުނިފޫހިފިލުވުން","ލައިފްސްޓައިލް","ކުޅިވަރު","ރިޕޯޓް","ޚަބަރު"]
		categories_english = ["news","lifestyle","story","video","world","collumn","business","entertainment","lifestyle","sports","report","news"]
		#loop through all categories
		for category in categories_dhivehi:
			if category in unparsed_category:
				category_n = categories_dhivehi.index(category)
				category_english = categories_english[category_n] # gets category by replacing dhivehi category with english category that has the same index in its array
				return(category_english)
		if unparsed_category in categories_english:
			return(unparsed_category)
		return("error")
	

	#returns author , just removes the unnnecessary spaces
	def ParseAuthor(self,unparsed_author):
		author = re.sub("\s\s+"," ",unparsed_author)
		return(author)

	#checks whether the headlines are empty
	def ParseHeadline(self,unparsed_headline):
		if len(unparsed_headline) > 0:
			return unparsed_headline
		else:
			return("error")

	#parse image
	def ParseImage(self,unparsed_image):
		if unparsed_image.endswith(('.jpg','.jpeg','.png')):
			return unparsed_image
		else:
			return "error"

	#parse the article
	def ParseArticle(self,unparsed_article):
		if len(unparsed_article) > 0:
			return(unparsed_article)
		else:
			return "error"



	#use all parsers and return a dictionary
	def ParseData(self,url,headline,image,author,category,article,date,source,ids):
		article_data = {}
		article_data["url"] = url
		article_data["headline"] = self.ParseHeadline(headline)
		article_data["image"] = self.ParseImage(image)
		article_data["author"] = self.ParseAuthor(author)
		article_data["category"] = self.ParseCategory(category)
		article_data["article"] = self.ParseArticle(article)
		article_data["datetime"] = self.ParseDate(date,source)
		article_data["source"] = source
		article_data["id"] = ids
		return (article_data)




	



