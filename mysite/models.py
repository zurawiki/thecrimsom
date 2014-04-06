from django.db import models


class Section(models.Model):
    name = models.CharField(blank=False, max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    PUB_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
        (-1, 'Deleted'),
    )

    title = models.CharField(max_length=200, blank=False, null=False, default='')
    subtitle = models.CharField(max_length=255, blank=True, null=False, default='')
    author = models.CharField(max_length=70, blank=False, null=False, default='')
    section = models.ForeignKey(Section, null=False, related_name='content')

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