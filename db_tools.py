from settings import dbpassword, dbusername
import  mysql.connector

class DbTools(object):
	"""docstring for DbTools"""
	def __init__(self):
		self.sources = ["mihaaru","sun","avas","vfp","psm"]

	#the official db connector
	'''this method of storing password in txt file needs to be avoided paswords need to be  stored in enviroment variable'''
	def ConnectDb(self,dbname):
		db = mysql.connector.connect(
			host="127.0.0.1",
			user= dbusername,
			password = dbpassword,
			database = dbname
			)
		return(db)


	#initilaise the db 
	def InitDb(self):                                                                                                                         
		db = self.ConnectDb("")
		c = db.cursor()
		try:
			c.execute("CREATE DATABASE articledb")
		except:
			print("db already exists")
		db = self.ConnectDb("articledb")
		c = db.cursor()

		c.execute("CREATE TABLE last_update (id INT AUTO_INCREMENT PRIMARY KEY,source VARCHAR(255), last_update VARCHAR(255))")
		source_sql = "INSERT INTO last_update (source,last_update) VALUES(%s,%s)"


		#loop over all sources to get the id from which we start to scrape from  (to obtain thos goto the sources home pageand click on an article and get its id)
		for x in self.sources:
			last =  input("enter highest for " + x)
			print(x+":",last)
			val  = (x,last)
			c.execute(source_sql,val)
		db.commit()
		#now we create table for thee content table
		c.execute("CREATE TABLE content_db (id INT AUTO_INCREMENT PRIMARY KEY,source VARCHAR(255), url VARCHAR(255),headline VARCHAR(255),image VARCHAR(255),author VARCHAR(255),datetime TIME(6),category VARCHAR(255),article VARCHAR(3000),article_id VARCHAR(255))")
		db.commit()


	#returns the highest article id the db contains for the source
	def last_update(self,conn):
		#get the last_update for every source
		sql = "SELECT last_update FROM last_update"
		c = conn.cursor()
		highest = c.execute(sql)
		highest_id = c.fetchall()
		highest_dict = {}
		
		for i in range(0,len(highest_id)): #loop through all results to convert to dict
			highest_dict[self.sources[i]] = highest_id[i][0]
		
		return(highest_dict)

		#sets the highest id
	def SetHighest(self,conn,source,ids):
		c = conn.cursor()
		edit_sql = "UPDATE last_update SET last_update = %s where source = %s" # weak security
		values = (ids,source)
		c.execute(edit_sql,values)
		conn.commit()



		#techinically the hardest but should be possible
	def add_db(self,conn,valid_data,ids):
		c = conn.cursor()
		
		#checks for the essential attributes
		if valid_data != None and valid_data["headline"] != "error" and valid_data["url"] != "error" and valid_data["article"] != "error":
			# if  the essential data is valid checks wether the url is already present  
			select_sql = "SELECT * FROM content_db WHERE url=%s"
			url_value = valid_data["url"],
			c.execute(select_sql,url_value)
			check = c.fetchall()
			c_highest = ids
			source = valid_data["source"]
			#print(source,c_highest[source]," ",valid_data["id"])

			#this checks whether the provided id is the highest for the source
			if int(c_highest[source]) < valid_data["id"]:
				self.SetHighest(conn,source,valid_data["id"]) # if so sets the highest 

			#check if the query to check duplicates reurn 0 results,if so adds the data to db
			if len(check) == 0:


				sql = "INSERT INTO content_db (source,url,headline,image,author,datetime,category,article) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
				val = valid_data["source"],valid_data["url"],valid_data["headline"],valid_data["image"],valid_data["author"],valid_data["datetime"],valid_data["category"],valid_data["article"],
				c.execute(sql,val)
				print(valid_data["url"])
				conn.commit()
				return(True)
			else:
				return(False)





