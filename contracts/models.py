from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext as _


class Advertiser(models.Model):
    name = models.CharField(_("Name"), max_length=128)

    address_1 = models.CharField(_("Address"), max_length=128)
    address_2 = models.CharField(_("Address cont'd"), max_length=128, blank=True)

    city = models.CharField(_("City"), max_length=64)
    state = models.CharField(_("State"), max_length=2)
    zip_code = models.CharField(_("ZIP code"), max_length=5)

    contact = models.CharField(_("Contact"), max_length=128)
    position = models.CharField(_("Position"), max_length=128)
    telephone = models.CharField(_("Phone"), max_length=10)
    email = models.EmailField(_("Email"))

    def __str__(self):
        return self.name

    def address(self):
        if self.address_2:
            return "%s %s, %s, %s %s" % (self.address_1, self.address_2, self.city, self.state, self.zip_code)
        else:
            return "%s, %s, %s %s" % (self.address_1, self.city, self.state, self.zip_code)
    address.short_description = _("Mailing Address")


class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact', 'position', 'telephone', 'email')
    list_filter = ('city', 'state')


class Issue(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    volume = models.IntegerField(_("Volume"))
    issueNumber = models.IntegerField(_("Issue Number"))

    def __str__(self):
        return '%d, %d: %s' % (self.volume, self.issueNumber, self.title)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'issueNumber')
    list_filter = ('volume',)
    fieldsets = [('', {
        'fields': ('volume','issueNumber'),
    }),
    ('', {
        'fields': ('title',),
    })]


class Advert(models.Model):
    SIZES = (
        ('1/4', 'Quarter Page'),
        ('1/3', 'Third Page'),
        ('1/2', 'Half Page'),
        ('2/3', 'Two-Thirds Page'),
        ('FUL', 'Full Page'),
        ('CTR', 'Center Spread')
    )
    advertiser = models.ForeignKey(Advertiser)
    size = models.CharField(max_length=3, choices=SIZES, default='1/3')
    description = models.TextField(_("Description"))
    imageFile = models.ImageField(upload_to='adverts/%Y/%m')
    issues = models.ManyToManyField(Issue)
    listPrice = models.DecimalField(_("Listed Price"), max_digits=5, decimal_places=2)
    discounts = models.CharField(_("Discounts"), max_length=128, blank=True)
    finalPrice = models.DecimalField(_("Paid"), max_digits=6, decimal_places=2)

    active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '(%s) %s: %s' % (self.size, self.advertiser, self.description)

    def issues_count(self):
        return self.issues.count()

    issues_count.short_description = _("Issues ordered")


class AdvertAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('active', 'description', 'advertiser', 'issues_count', 'size', 'finalPrice', 'created_at')
    list_filter = ('advertiser', 'issues', 'active')