from django.contrib import admin
from contracts.models import *

# Register your models here.

admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Advert, AdvertAdmin)