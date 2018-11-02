# News scraper

## setup
it is best if you setup in new env
``` 
conda create --name news python=3.6
activate news
pip install mysql-connector
pip install beautifulsoup4
```

Now create a mysql db with 
```
user = "root"
password = ""
dbname ="articledb"

```

#To start Scraping
``` 
python ScraperControl.py

```

