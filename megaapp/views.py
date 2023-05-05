from django.shortcuts import render
from .models import (
    Glass,
    GlassCategory,
    GlassBrand,
    Watch,
    WatchCategory,
    WatchBrand,
    Coffe,
    CoffeCategory,
    CoffeBrand,
) 

# Create your views here.
def index(request):
    glasses = Glass.objects.all()
    coffes = Coffe.objects.all()
    watchs= Watch.objects.all()
    return render(request, "mega/index.html", {"glasses": glasses, "coffes": coffes, "watchs": watchs})

def deneme(request):
    glasses = Glass.objects.all()
    coffes = Coffe.objects.all()
    watchs= Watch.objects.all()
    return render(request, "mega/deneme.html", {"glasses": glasses, "coffes": coffes, "watchs": watchs})


def glasses(request):
    glasses = Glass.objects.all()
    
    get =request.GET
    if get.get('category') and get.get('category') != 'on':
        glasses = glasses.filter(category=get.get('category'))
    if get.get('brand') and get.get('brand') != 'on':
        glasses = glasses.filter(brand=get.get('brand'))
    if get.get('maxprice'):
        glasses = glasses.filter(price__lte=get.get('maxprice'))
    if get.get('minprice'):
        glasses = glasses.filter(price__gte=get.get('minprice'))
       
    categories = GlassCategory.objects.all()
    brands = GlassBrand.objects.all()
    data = list(Glass.objects.values('title', 'image', 'description', 'price', 'category', 'brand'))
   
    return render(
        request,
        "mega/glasses.html",
        {"active":'glasses',"glasses": glasses, "categories": categories, "brands": brands, "brands": brands,"filterCategory":get.get('category'),"filterBrand":get.get('brand'),"filterMaxPrice":get.get('maxprice'),"filterMinPrice":get.get('minprice')},
    )


def watchs(request):
    get =request.GET
    watchs = Watch.objects.all()
    if get.get('category') and get.get('category') != 'on':
        watchs = watchs.filter(category=get.get('category'))
    if get.get('brand') and get.get('brand') != 'on':
        watchs = watchs.filter(brand=get.get('brand'))
    if get.get('maxprice'):
        watchs = watchs.filter(price__lte=get.get('maxprice'))
    if get.get('minprice'):
        watchs = watchs.filter(price__gte=get.get('minprice'))
       
        
    # i_begin_int__lte=170, i_end_int__gte=170
    categories = WatchCategory.objects.all()
    brands = WatchBrand.objects.all()
    return render(
        request,
        "mega/watchs.html",
        {"active":'watch',"watchs": watchs, "categories": categories, "brands": brands,"filterCategory":get.get('category'),"filterBrand":get.get('brand'),"filterMaxPrice":get.get('maxprice'),"filterMinPrice":get.get('minprice')},
    )


def coffes(request):
    coffes = Coffe.objects.all()
    get =request.GET
    if get.get('category') and  get.get('category') != 'on' :
        coffes = coffes.filter(category=get.get('category'))
    if get.get('brand') and get.get('brand') != 'on':
        coffes = coffes.filter(brand=get.get('brand'))
    if get.get('maxprice'):
        coffes = coffes.filter(price__lte=get.get('maxprice'))
    if get.get('minprice'):
        coffes = coffes.filter(price__gte=get.get('minprice'))
       
    categories = CoffeCategory.objects.all()
    brands = CoffeBrand.objects.all()
    
    return render(
        request,
        "mega/coffes.html",
        {"active":'watch',"coffes": coffes, "categories": categories, "brands": brands, "brands": brands,"filterCategory":get.get('category'),"filterBrand":get.get('brand'),"filterMaxPrice":get.get('maxprice'),"filterMinPrice":get.get('minprice')},
    )
