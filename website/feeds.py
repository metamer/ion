from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse
from website.models import Page


class LatestEntriesFeedRSS(Feed):
    updates=True
    title = "Distant Constructs Updates"
    link = "/latest/updates/"
    description = "Updates on changes and additions to Distant Constructs."

    def __init__(self, updates=True):
        self.updates=updates
        if(self.updates):
            self.title = "Distant Constructs Updates"
            self.link = "/latest/updates/"
            self.description = "Updates on changes and additions to Distant Constructs."
        else:
            self.title = "Distant Constructs Additions"
            self.link = "/latest/new_pages/"
            self.description = "New Pages on Distant Constructs."

    def items(self):
        if(self.updates):
            return Page.objects.order_by('-update_date')[:5]
        else:
            return Page.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.page_title

    def item_description(self, item):
        if(self.updates):
            return item.update_comment
        else:
            return item.page_text

    def item_pubdate(self, item):
        if(self.updates):
            return item.update_date
        else:
            return item.pub_date

class LatestEntriesFeedAtom(LatestEntriesFeedRSS):
    feed_type = Atom1Feed
    subtitle = LatestEntriesFeedRSS.description



from website.models import NewsEntry

class NewsFeedRSS(Feed):
    title = "Distant Constructs News"
    link = "/latest/news/"
    description = "Distant Constructs site news"

    def items(self):
        return NewsEntry.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_pubdate(self, item):
        return item.pub_date

    def item_link(self, item):
        return "/top/news.html"

class NewsFeedAtom(NewsFeedRSS):
    feed_type = Atom1Feed
    subtitle = NewsFeedRSS.description

from website.models import Comment

class CommentaryFeedRSS(Feed):
    title = "Distant Constructs Commentary"
    link = "/latest/commentary/"
    description = "Distant Constructs Commentary"

    def items(self):
        return Comment.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.link_title

    def item_description(self, item):
        return item.text

    def item_pubdate(self, item):
        return item.pub_date

    def item_link(self, item):
        return item.link

class CommentaryFeedAtom(CommentaryFeedRSS):
    feed_type = Atom1Feed
    subtitle = CommentaryFeedRSS.description
