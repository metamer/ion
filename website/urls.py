from django.conf.urls import patterns, url
from django.views.generic import base
from django.views.generic.base import RedirectView
from website.feeds import LatestEntriesFeedRSS,LatestEntriesFeedAtom
from website.feeds import NewsFeedRSS,NewsFeedAtom
from website.feeds import CommentaryFeedRSS,CommentaryFeedAtom

from website import views

urlpatterns = patterns('',
        url(r'^latest/new_pages/rss.xml?$' , LatestEntriesFeedRSS(updates=False))
        ,url(r'^latest/new_pages/atom.xml?$' , LatestEntriesFeedAtom(updates=False))
        ,url(r'^latest/updates/rss.xml?$' , LatestEntriesFeedRSS(updates=True))
        ,url(r'^latest/updates/atom.xml?$' , LatestEntriesFeedAtom(updates=True))
        ,url(r'^latest/news/rss.xml?$' , NewsFeedRSS())
        ,url(r'^latest/news/atom.xml?$' , NewsFeedAtom())
        ,url(r'^latest/commentary/rss.xml?$' , CommentaryFeedRSS())
        ,url(r'^latest/commentary/atom.xml?$' , CommentaryFeedAtom())
        ,url(r'^all_pages/index.html$' , views.allPages, name='allPages')
        ,url(r'^all_pages/?(?P<cat_path>.*).html$' , views.allPages, name='allPages')
        ,url(r'^top/news.html?$' , views.news, name='news')
        ,url(r'^top/commentary.html?$' , views.commentary, name='commentary')
        ,url(r'^about/license.html?$' , views.licenseusage, name='licenseusage')
        ,url(r'^index.html$' , views.anyPC)
        #,url(r'^favicon\.ico$', RedirectView.as_view(url='static/img/favicon.ico'))
        ,url(r'^(?P<urlString>.+)/index.html$' , views.anyPC, name='anyPC')
        ,url(r'^(?P<urlString>.+).html$' , views.anyPC, name='anyPC')
        #url(r'^(?P<category_name>.+)/(?P<page_shortname>.+)$' , views.webpage, name='webpage')
        #,url(r'^(?P<category_name>.+)$' , views.category, name='category')
        #,url(r'^(?P<category_name>.+)$' , views.category, name='category')
        )
