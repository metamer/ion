from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey

class PageCategory(MPTTModel):
    category_name = models.CharField(max_length = 20, unique=True, validators = [RegexValidator("^[\w]+$", message="category name must be alphanumeric")])
    category_desc = models.CharField(max_length = 200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    def __str__(self):
        return self.category_name
    def ansc_path(self):
        """return path to self separated by slashes"""
        return "/".join(a.category_name for a in self.get_ancestors(include_self=True))
    def get_absolute_url(self):
        return "/"+self.ansc_path()+"/index.html"
    def get_pages(self):
        return self.page_set.all()

class Page(models.Model):
    page_title = models.CharField(max_length = 200, help_text="Title of the page")
    page_shortname = models.CharField(max_length = 20, validators = [RegexValidator("^[\w]+$", message="shortname must be alphanumeric")], help_text="Short name of page (no special chars or spaces). This will be used for the url location of the page. Use _ to separate words.")
    page_description = models.CharField(max_length = 500, blank=True, help_text = "Description of page")
    page_text = models.TextField(blank=True, help_text="HTML content of page")
    page_category = models.ForeignKey(PageCategory)
    pub_date = models.DateTimeField('date published', help_text = "Date page was first published")
    update_date = models.DateTimeField('date updated',help_text = "Date page was last updated")
    update_comment = models.CharField(max_length = 500, blank=True, help_text = "Changes made during last update")
    def __str__(self):
        return self.page_title

    def get_absolute_url(self):
        return "/"+self.page_category.ansc_path()+"/"+self.page_shortname+".html"

class NewsEntry(models.Model):
    title = models.CharField(max_length = 200, help_text="Title of the news entry")
    text = models.TextField(help_text="HTML content of page")
    pub_date = models.DateTimeField('date published', help_text = "Date page was first published")
    def __str__(self):
        return self.title

class MPTTMeta:
    order_insertion_by = ['name']
