from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from contracts.models import Advertiser


__author__ = 'roger'


class AdvertiserForm(ModelForm):
    class Meta:
        model = Advertiser


@login_required
def register_advertiser(request):
    if request.method == 'POST':
        form = AdvertiserForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            advertiser = form.save()
            profile = request.user.get_profile()
            profile.advertiser = advertiser
            profile.save()
            messages.success(request, 'Advertiser profile updated.')
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect('/')
    else:
        form = AdvertiserForm(instance=request.user.get_profile().advertiser)
        if request.user.get_profile().advertiser is None:
            messages.warning(request, 'Before ordering an ad contract, you must first fill in your contact profile.')
        return render(request, 'advertiser/form.html', {'form': form})

