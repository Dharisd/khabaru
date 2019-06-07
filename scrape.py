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




def printStats(source,idxs):
	print("{0}: current:{1} fetching:{2} \n".format(source,(idxs[source]),(int(idxs[source]) + i)))













while t == 0:
	ids = c.last_update(conn) #fetch the highest artcle id for all sources
	print(ids)



	for i in range(-5,20):
		try:

			ids = c.last_update(conn) #fetch the highest artcle id for all sources
			print(ids)
			print("trying {} --------------------------------------".format(i))
		
			printStats("mihaaru",ids)
			mihaaru = s.mihaaru(int(ids["mihaaru"]) + i)
			c.add_db(conn,mihaaru,ids)
			

			printStats("avas",ids)
			avas = s.avas(int(ids["avas"]) + i)
			c.add_db(conn,avas,ids)
			
			printStats("vfp",ids)
			vfp = s.vfp(int(ids["vfp"]) + i) 
			c.add_db(conn,vfp,ids)
			
			printStats("psm",ids)
			psm = s.psm(int(ids["psm"]) + i)
			c.add_db(conn,psm,ids)
			 
			printStats("sun",ids)
			sun = s.sun(int(ids["sun"]) + i)
			c.add_db(conn,sun,ids)

		except Exception as ex:
			template = "An exception of type {0} occurred. Arguments:\n{1!r} \n"
			message = template.format(type(ex).__name__, ex.args)
			print(message)


			
		

	#time.sleep(5) # waits 5 seconds


		#hows the speed on this thi

	





