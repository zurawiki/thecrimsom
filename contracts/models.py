from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext as _


class Advertiser(models.Model):
    name = models.CharField(_("name"), max_length=128)

    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)

    city = models.CharField(_("city"), max_length=64)
    state = models.CharField(_("state"), max_length=2)
    zip_code = models.CharField(_("zip code"), max_length=5)

    contact = models.CharField(_("contact"), max_length=128)
    position = models.CharField(_("position"), max_length=128)
    telephone = models.CharField(_("telephone"), max_length=10)
    email = models.EmailField(_("email"))

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    volume = models.IntegerField(_("Volume"))
    issueNumber = models.IntegerField(_("Issue Number"))

    def __str__(self):
        return '%d, %d: %s' % (self.volume, self.issueNumber, self.title)


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
    imageFile = models.ImageField(upload_to='uploads/adverts/%Y/%m')
    issues = models.ManyToManyField(Issue)
    listPrice = models.DecimalField(_("Cost of Ad"), max_digits=5, decimal_places=2)
    discounts = models.CharField(_("Discounts"), max_length=128, blank=True)
    finalPrice = models.DecimalField(_("Total Cost"), max_digits=6, decimal_places=2)

    disabled = models.BooleanField(_("Disabled"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '(%s) %s: %s' % (self.size, self.advertiser, self.description)