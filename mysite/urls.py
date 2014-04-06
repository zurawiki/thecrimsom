from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from filebrowser.sites import site

from mysite import views


urlpatterns = patterns("",
                       url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
                       url(r'^section/news/$', views.section_news),
                       url(r'^section/opinion/$', views.section_opinion),
                       url(r'^section/fm/$', views.section_magazine),
                       url(r'^section/sports/$', views.section_sports),
                       url(r'^section/arts/$', views.section_arts),
                       url(r'^section/media/$', views.section_media),
                       url(r'^section/flyby/$', views.section_flyby),
                       url(r'^admissions/$', views.section_admissions),
                       url(r'^article/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<page_slug>[\w-]+)/$',
                           views.article_detail),



                       (r'^admin/filebrowser/', include(site.urls)),
                       (r'^redactor/', include('redactor.urls')),
                       (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       (r'^admin/', include(admin.site.urls)),  # admin site
                       url(r"^accounts/", include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
