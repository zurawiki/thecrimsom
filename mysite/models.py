from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from solo.models import SingletonModel

class Section(models.Model):
    name = models.CharField(blank=False, max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(blank=False, null=True, max_length=70)
    last_name = models.CharField(blank=False, null=True, max_length=100)
    middle_name = models.CharField(blank=True, null=True, max_length=70)
    created_on = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('mysite.views.writer_detail', args=[self.pk, self.first_name, self.middle_name, self.last_name])

    def __unicode__(self):
        if self.middle_name:
            return "%s %s. %s" % (self.first_name, self.middle_name[0], self.last_name)
        else:
            return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    PUB_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
        (-1, 'Deleted'),
    )

    title = models.CharField(max_length=200, blank=False, null=False, default='')
    subtitle = models.CharField(max_length=255, blank=True, null=False, default='')
    authors = models.ManyToManyField(Author, null=True, related_name='content')
    section = models.ForeignKey(Section, null=False, related_name='content')
    image = models.ImageField(null=True, blank=True, upload_to='images')

    content = models.TextField(blank=True, null=False, default='')

    slug = models.SlugField(max_length=70, unique=True, db_index=True, help_text="""
            The text that will be displayed in the URL of this article.
            Can only contain letters, numbers, and dashes (-).
            """
    )

    pub_status = models.IntegerField(null=False, choices=PUB_CHOICES,
                                     default=0, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_on = models.DateTimeField(auto_now=True)

    def list_preview(self):
        return render_to_string('article/list_preview.html', {'article': self})

    def __unicode__(self):
        return self.title


    def __str__(self):
        return "".join([x if ord(x) < 128 else '?' for x in unicode(self)])

    def get_absolute_url(self):
        year = self.created_on.year
        month = self.created_on.month
        day = self.created_on.day

        return reverse('mysite.views.article_detail', args=[year, month, day, self.slug])


    def teaser(self):
        if self.subtitle:
            return self.subtitle
        else:
            return strip_tags(self.content)


class BreakingNews(SingletonModel):
    description = models.TextField(blank=False, null=False, default='')
    link = models.CharField(max_length=255, blank=False, null=False, default='#')
    active = models.BooleanField()
    when = models.DateTimeField()


class HomePage(SingletonModel):
    primary1 = models.ForeignKey(Article, null=True, related_name='+')
    primary2 = models.ForeignKey(Article, null=True, related_name='+')
    primary3 = models.ForeignKey(Article, null=True, related_name='+')
    primary4 = models.ForeignKey(Article, null=True, related_name='+')
    primary5 = models.ForeignKey(Article, null=True, related_name='+')
    primary6 = models.ForeignKey(Article, null=True, related_name='+')


    def __unicode__(self):
        return u"The Home Page"  # something like this will make admin message strings more coherent

    class Meta:
        verbose_name = "Home Page"  # once again this will make sure your admin UI doesn't have illogical text
        verbose_name_plural = "Home Page"


class MostRead(SingletonModel):
    n1 = models.ForeignKey(Article, null=True, related_name='+')
    n2 = models.ForeignKey(Article, null=True, related_name='+')
    n3 = models.ForeignKey(Article, null=True, related_name='+')
    n4 = models.ForeignKey(Article, null=True, related_name='+')
    n5 = models.ForeignKey(Article, null=True, related_name='+')

    def __unicode__(self):
        return u"Most Read"  # something like this will make admin message strings more coherent

    class Meta:
        verbose_name = "Most Read"  # once again this will make sure your admin UI doesn't have illogical text
        verbose_name_plural = "Most Read"