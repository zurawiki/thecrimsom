import os
import urllib
import json

from django.core.files import File
from django.core.management.base import BaseCommand

from mysite.models import Article, Author, Section


def create_sections():
    SECTIONS = [
        "News", "Opinion", "Magazine", "Sports",
        "Arts", "Media", "Flyby", "Admissions"
    ]
    for s in SECTIONS:
        Section.objects.get_or_create(name=s)[0].save()


class Command(BaseCommand):
    args = '<scrapy-output.json>'
    help = 'Imports a scrapy json file of Harvard Crimson articles'

    def handle(self, *args, **options):
        create_sections()

        for file in args:
            # load json
            json_data = open(file)
            articles = json.load(json_data)

            # import article
            for article in articles:
                # make sure all authors exists
                # get all authors
                authors = []
                for author in article['authors']:
                    s = author.split()
                    f, m, l = s[0], s[1:-1], s[-1]
                    author_model, created = Author.objects.get_or_create(
                        first_name=f,
                        middle_name=''.join(m),
                        last_name=l)
                    authors.append(author_model)

                article.pop("authors")
                images = article.pop("image")
                fields = dict(article)

                fields['section'] = Section.objects.get(name=article['section'])
                fields['pub_status'] = 1

                instance, created = Article.objects.get_or_create(slug=article['slug'], defaults=fields)
                if not created:
                    for attr, value in fields.iteritems():
                        setattr(instance, attr, value)
                    instance.save()

                for i in authors:
                    instance.authors.add(i)

                # Download and save image
                if len(images) > 0:
                    image_url = images[1]
                    result = urllib.urlretrieve(image_url)  # image_url is a URL to an image

                    # self.photo is the ImageField
                    instance.image.save(
                        os.path.basename(image_url),
                        File(open(result[0], 'rb'))
                    )
                    instance.save()
                    self.stdout.write('Successfully updated "%s"' % instance)

            self.stdout.write('Updated %d articles.' % len(articles))