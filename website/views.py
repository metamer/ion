from django.http import Http404
from django.shortcuts import render, get_object_or_404
from website.models import PageCategory, Page, NewsEntry, Comment

# Create your views here.
def commentary(request) :
    cat_path = "top"
    page_shortname = "commentary"
    pages = Page.objects.filter(page_shortname = page_shortname)
    if len(pages) == 0 :
        raise Http404("Page with name >{0}< does not exist".format(page_shortname))
    for page in pages:
        ansc_path = page.page_category.ansc_path()
        if(cat_path == ansc_path):
            return render(request, 'website/commentary.html',
                    {'page' : page 
                        , 'cat' : page.page_category
                        , 'comments' : Comment.objects.order_by("-pub_date")
                        , 'rootCats' : get_root_cats() 
                    })
    raise Http404("Page does with name {0} not exist in path {1}".format(page_shortname,cat_path))

def news(request) :
    cat_path = "top"
    page_shortname = "news"
    pages = Page.objects.filter(page_shortname = page_shortname)
    if len(pages) == 0 :
        raise Http404("Page with name >{0}< does not exist".format(page_shortname))
    for page in pages:
        ansc_path = page.page_category.ansc_path()
        if(cat_path == ansc_path):
            return render(request, 'website/news.html',
                    {'page' : page 
                        , 'cat' : page.page_category
                        , 'news_entries' : NewsEntry.objects.order_by("-pub_date")
                        , 'rootCats' : get_root_cats() 
                    })
    raise Http404("Page does with name {0} not exist in path {1}".format(page_shortname,cat_path))
def webpage(request, cat_path, page_shortname):
    pages = Page.objects.filter(page_shortname = page_shortname)
    if len(pages) == 0 :
        raise Http404("Page with name >{0}< does not exist".format(page_shortname))
    for page in pages:
        ansc_path = page.page_category.ansc_path()
        if(cat_path == ansc_path):
            return render(request, 'website/webpage.html',
                    {'page' : page 
                        , 'cat' : page.page_category
                        , 'rootCats' : get_root_cats() 
                    })
    raise Http404("Page does with name {0} not exist in path {1}".format(page_shortname,cat_path))

def category(request, cat_path):
    last_cat_name = (cat_path.split("/"))[-1]
    cats = PageCategory.objects.filter(category_name = last_cat_name)
    if len(cats) == 0:
        raise Http404("Category with name >{0}< does not exist".format(last_cat_name))
    
    cat = match_categories(cats, cat_path)
    if(cat):
        return render(request, 'website/category.html',
                {'cat' : cat 
                    , 'rootCats' : get_root_cats() 
                })
    else:
        raise Http404("Category >{0}< does not exist".format(cat_path))

def get_root_cats():
    return [i for i in PageCategory.objects.all() if i.is_root_node()]

def match_categories(cat_list, cat_path):
    for cat in cat_list:
        ansc_path = cat.ansc_path()
        if(cat_path == ansc_path):
            return cat
    return False

def allPages(request, cat_path=""):
    if(len(cat_path) == 0):
        return render(request, 'website/all_categories.html',
                {'cats' : get_root_cats()
                    , 'cat_path' : "/"
                    , 'rootCats' : get_root_cats() 
                })

    last_cat_name = (cat_path.split("/"))[-1]
    cats = PageCategory.objects.filter(category_name = last_cat_name)
    if len(cats) == 0:
        raise Http404("Category with name >{0}< does not exist".format(last_cat_name))
    
    cat = match_categories(cats, cat_path)
    if(cat):
        return render(request, 'website/all_categories.html',
                {'cats' : [cat]
                    , 'cat_path' : cat_path
                    , 'rootCats' : get_root_cats() 
                })
    else:
        raise Http404("Category >{0}< does not exist".format(cat_path))

def anyPC(request, urlString="top/home"):
    components = urlString.split("/")
    last_component = components[-1]
    if Page.objects.filter(page_shortname = last_component).count() != 0:
        sind = urlString.rfind("/")
        if sind == -1:
            return webpage(request, urlString ,urlString)
        else:
            return webpage(request, urlString[0:sind] ,components[-1])
    else:
        return category(request, urlString)
