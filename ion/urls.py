from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from website.models import Page, PageCategory

class PageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        lp = [page for page in Page.objects.all()]
        lpc = [pagecat for pagecat in PageCategory.objects.all()]
        return lp+lpc

    def lastmod(self, obj):
        if(type(obj) == Page):
            return obj.update_date

sitemaps = {"website":PageSitemap}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #,url(r'^polls/', include('polls.urls', namespace="polls"))
    url(r'^admin/', include(admin.site.urls))
    ,url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    ,url(r'^', include('website.urls', namespace="website"))
)
