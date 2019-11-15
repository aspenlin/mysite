from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, FileResponse
from .models import BlogCategory, Blogs, PhotoGallery, Calligraphy, CalliCategory
import os
from glob import glob

def home(request):
	return render(request, 'main/index.html')

def cv(request):
    return FileResponse(open('static/main/pdf/JingjingLin_Resume_V3.pdf', 'rb'), content_type='application/pdf')

def blog(request):
    context = {'categories':BlogCategory.objects.all}
    return render(request, 'main/blog_categories.html', context)

def blog_category(request, category):
    blogs = Blogs.objects.filter(category__slug=category).order_by('-pub_date')
    context = {'blogs':blogs, 'category':category}
    return render(request, 'main/blog_category.html', context)

def blog_detail(request, category, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {'blog':blog}
    return render(request, 'main/blog_detail.html', context)


def photo(request):
      years = glob('media/upload/gallery/*/')
      folders = [int(y.split('/')[-2]) for y in years]
      context = {'folders':folders}
      return render(request, 'main/photo_folders.html', context)

def photo_folder(request, year):
    photos = PhotoGallery.objects.filter(pub_date__year=int(year))
    context = {'photos':photos}
    return render(request, 'main/photo_folder.html', context)

def photo_detail(request):
    # photo = get_object_or_404(PhotoGallery, pk=img_id)
    # url = photo.photo.url
    # context = {'photo':photo}
    return render(request, 'main/photo_detail.html')

def calligraphy(request):
    context = {'categories':CalliCategory.objects.all}
    return render(request, 'main/calligraphy_categories.html', context)

def calligraphy_category(request, category):
    photos = Calligraphy.objects.filter(category__slug=category).order_by('-pub_date')
    context = {'photos':photos}
    return render(request, 'main/calligraphy_category.html', context)
















