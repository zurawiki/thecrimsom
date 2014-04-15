Roger Zurawicki

rzurawicki@gmail.com

Lowell B-23

The Crimsom
-----------

http://cloud.rozu.co:9082/

https://github.com/rzurawicki/thecrimsom

## Purpose

The Crimsom is a parody of The Harvard Crimson online newspaper. This project is a simple Django webapp that provides the basic models to edit articles and arrange the front-facing seciton pages.

The comprehensive admin interface is powered by Django, Grappelli, and Reditor. The admin site can filter and search article by many fields. Article can include any kind of HTML, CSS, JS, as well as media uploads. the admin interface gives you the ability to layout articles with a preview image of where the articles would appear on the site.

A screen scraper for the crimson web site is also included. Instructions are provided in the README.


## What's included
    mysite - thecrimsom Django web project. run it using manage.py
    scraper - the thecrimson.com screen scraper to import articles

## Functionality
  * Looks **exactly** like thecrimson.com
  * Scrapes articles and authors from thecrimson.com
  * Imports those scraped articles
  * django provides supports for versions of articles
  * Articles can be linked to one or more authors
  * Articles can be published or saved as drafts
  * Authors have their own page featuring their own articles
  * The top 5 articles can be customly set
  * Each section page can be customized
  * The admin interface shows the layout of the page
  * The site supports comments using the disqus api

## How to Setup Backend
  1. Install python, pip, and the packages specified by requirements.txt. (Follow the direcitons below)
        
  2. Run server: `python manage.py runserver`
     This script setups up a Django web server. You must fist syncdb and collectstatic as specified below.


## Known Bugs
  * Only the homepage, news, and opinion pages have customizable slots.
  * Blog articles do not get scraped.
  * The tags on articles are static. (This was to keep the appearance identical)

Getting Started:

1. Install the Python environment (uses python 2.7)
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install scrapy
```
2. Setup the database and static files, scrape data form thecirmsom.com.
```
python manage.py syncdb
python manage.py collectstatic
srapy crawl crimson -o crimson-scrape.json -t json
python manage.py import_scrape crimson-scrape.json
```
3. Run Server
```
python manage.py runserver
```
