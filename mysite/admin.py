from django.contrib import admin
from django.core import exceptions
from redactor.widgets import RedactorEditor

from models import *


# Register your models here.
admin.site.register(Section)


class ArticleAdmin(admin.ModelAdmin):
    actions = ['make_published', 'make_draft']

    list_display = ('title', 'author', 'section', 'pub_status', 'created_on', 'modified_on')
    list_filter = ('author', 'section')

    formfield_overrides = {
        models.TextField: {'widget': RedactorEditor},
    }

    # actions
    def make_published(self, request, queryset):
        if not request.user.has_perm('content.content.can_publish'):
            raise exceptions.PermissionDenied
        rows_updated = queryset.update(pub_status=1)
        if rows_updated == 1:
            message_bit = "1 object was"
        else:
            message_bit = "%s objects were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_published.short_description = 'Publish content'

    def make_draft(self, request, queryset):
        if not request.user.has_perm('content.content.can_unpublish'):
            raise exceptions.PermissionDenied
        rows_updated = queryset.update(pub_status=0)
        if rows_updated == 1:
            message_bit = "1 object was"
        else:
            message_bit = "%s objects were" % rows_updated
        self.message_user(request, "%s successfully marked as draft." % message_bit)

    make_draft.short_description = 'Mark content as Draft'


admin.site.register(Article, ArticleAdmin)
