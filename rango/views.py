from django.shortcuts import render
from django.http import HttpResponse

from django.template.defaultfilters import slugify

from rango.models import Category
from rango.models import Page

# Create your views here.
def index(request):
    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about'>About</a>") # chapter3 evidence
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', # chapter 3 output
        'categories' : category_list,
        'pages': page_list,
    }
    
    return render(request, 'rango/index.html', context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>") # chapter3 evidence
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context_dict)