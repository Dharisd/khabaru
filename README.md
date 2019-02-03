# News scraper
currently supports

1. Mihaaru
2. psm
3. avas
4. vfp(cnm)


## setup
it is best if you setup in new env
``` 
pip install --user -r requirements.txt

```

### To setup the database
This expects the db to have the following credentials
username=root
password = ""

### Adding credentials to .env file
```
cp .env.example .env
```
This will create a file called .env

DBUSER represents database username
DBPASS represents database password

Edit the following credentials according to your database setup.

this method needs to be revised
```
python db_setup.py

```
This will ask for artcleids for sources.obtain this by going into sources home page and getting article id of a recent  article 


# How it works

## For sites that dont provide api
scarpercontrol gets the last articleid from the db and then tries to scrape the next 5 article ids.If articles are found it saves the highest artcile id 

## For sites that Provide api 
its juts parses the data 



__scrapers.py__ : provides the scrapers object which provides methods to scrape from different sources
the output returned from these methods are a python dictionary with attributes
```
url
headline
image
author
category
article
datetime
source
id
```

__uitilities.py__ : provides the util class which contains methods to parse and validate the data from the scrapers to be stored in db.for example converts dhivehi dates to english dates

__db_tools.py__ : provides functions to initialise db and functions to add articles to db

__ScraperControl.py__: basically does the scraping process (gets the data rom scrapers and adds to db).



# To start Scraping
``` 
python ScraperControl.py

```

