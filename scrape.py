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
	print(ids)



	for i in range(-5,5):
		try:
			print(i)
		
			print("now fetching mihaaru" )
			mihaaru = s.mihaaru(int(ids["mihaaru"]) + i)
			c.add_db(conn,mihaaru,ids)
			
			print("now fetching avas" ) 
			avas = s.avas(int(ids["avas"]) + i)
			c.add_db(conn,avas,ids)
			
			print("now fetching vfp" )
			vfp = s.vfp(int(ids["vfp"]) + i) 
			c.add_db(conn,vfp,ids)
			
			print("now fetching psm")
			psm = s.psm(int(ids["psm"]) + i)
			c.add_db(conn,psm,ids)
			 
			print("now fetching sun") 
			sun = s.sun(int(ids["sun"]) + i)
			c.add_db(conn,sun,ids)
			

		except Exception as ex:
			template = "An exception of type {0} occurred. Arguments:\n{1!r} \n"
			message = template.format(type(ex).__name__, ex.args)
			print(message)


			
		

		#time.sleep(60) # waits 5 seconds


		#hows the speed on this thi

	





