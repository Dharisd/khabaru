import mysql.connector
import time

#define the functions

from db_tools import DbTools
from scrapers import scrapers


"""this script takes highest article ids from the database and scrapes the next ids.and if found adds to db.
it currently needs better error handlng routines.this also might be better with a cli with argumants"""

c = DbTools()
s = scrapers()
conn = c.ConnectDb("articledb")
t = 0
while t == 0:
	ids = c.last_update(conn) #fetch the highest artcle id for all sources
	sun = s.SunSoup()
	print("now fetching sun")
	#scraping loop
	for i in range(-20,20):
		try:
			mihaaru = s.mihaaru(int(ids["mihaaru"]) + i)
			print("now fetching mihaaru" )
			avas = s.avas(int(ids["avas"]) + i)
			print("now fetching avas" ) 
			vfp = s.vfp(int(ids["vfp"]) + i) 
			print("now fetching vfp" )
			psm = s.psm(int(ids["psm"]) + i)
			print("now fetching psm")

			
		

			add = c.add_db(conn,mihaaru,ids)
			add = c.add_db(conn,avas,ids)
			add = c.add_db(conn,mihaaru,ids)
			add = c.add_db(conn,vfp,ids)
			add = c.add_db(conn,psm,ids)
			for x in sun:
				c.add_db(conn,x,ids)

		except:
			print("error")


			
		

		time.sleep(5) # waits 5 seconds

	





