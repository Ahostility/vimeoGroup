from django.shortcuts import render

# Create your views here.

def home_page(request):
    data ={}
    return render(request,'home/home_page.html',context=data)


def player_vimeo(request):
    data = {}
    return render(request,'news/playerNews.html',context=data)


def category_page(request):
    data = {}
    # print(request)
    return render(request,'category/category_page.html',context=data)