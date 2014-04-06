from django.http import Http404
from django.shortcuts import render_to_response

from mysite.models import Article


def article_detail(request, year, month, day, page_slug):
    try:
        a = Article.objects.get(slug=page_slug, )
        if a.pub_status == 1:
            return render_to_response('article/detail.html', {'article': a})
        else:
            raise Http404
    except Article.DoesNotExist:
        raise Http404


def section_news(request):
    return None


def section_opinion(request):
    return None


def section_magazine(request):
    return None


def section_sports(request):
    return None


def section_media(request):
    return None


def section_flyby(request):
    return None


def section_admissions(request):
    return None