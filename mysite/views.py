from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

from mysite.models import Article, BreakingNews, MostRead, Author, HomePage, NewsSection, Section


def article_detail(request, year, month, day, page_slug):
    try:
        a = Article.objects.get(slug=page_slug, )
        if a.pub_status == 1 or request.user.is_staff:
            return render_to_response('article/detail.html', {'article': a})
        else:
            raise Http404
    except Article.DoesNotExist:
        raise Http404


def section_news(request):
    data = {}
    data['most_read'] = MostRead.objects.get()
    data['layout'] = NewsSection.objects.get()
    news = Section.objects.filter(name="News")[0]
    data['col1'] = Article.objects.filter(section=news)[0:4]
    data['col2'] = Article.objects.filter(section=news)[4:8]
    # fill it
    return render_to_response('section/news.html', data)


def section_opinion(request):
    data = {}
    # fill it
    return render_to_response('section/opinion.html', data)


def section_magazine(request):
    data = {}
    # fill it
    return render_to_response('section/magazine.html', data)


def section_sports(request):
    data = {}
    # fill it
    return render_to_response('section/sports.html', data)


def section_media(request):
    data = {}
    # fill it
    return render_to_response('section/media.html', data)


def section_flyby(request):
    data = {}
    # fill it
    return render_to_response('section/flyby.html', data)


def section_admissions(request):
    data = {}
    # fill it
    return render_to_response('section/admissions.html', data)


def section_arts(request):
    data = {}
    # fill it
    return render_to_response('section/arts.html', data)


def home(request):
    data = {}
    data['most_read'] = MostRead.objects.get()
    data['layout'] = HomePage.objects.get()
    try:
        data['breaking_news'] = BreakingNews.objects.filter(active=True).latest('when')
    finally:
        return render_to_response('homepage.html', data)


def writer_detail(request, pk, first, middle, last):
    writer = get_object_or_404(Author, pk=pk)
    return render_to_response('writer/detail.html', {'writer': writer})