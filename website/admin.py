from django.contrib import admin

# Register your models here.
from website.models import PageCategory

admin.site.register(PageCategory)

from website.models import Page
admin.site.register(Page)

from website.models import NewsEntry
admin.site.register(NewsEntry)

from website.models import Comment
admin.site.register(Comment)

from website.models import License, LicenseUsage
admin.site.register(License)
admin.site.register(LicenseUsage)
