
Getting Started:

    pip install virtualenv
    virtualenv venv
    source mysiteenv/bin/activate
    pip install -r requirements.txt
    pip install scrapy
    python manage.py syncdb

Scrape Crimson Site data
    scrapy crawl crimson -o crimson-scrape.json -t json
    python manage.py import_scrape crimson-scrape.json

Run Server
    python manage.py runserver
