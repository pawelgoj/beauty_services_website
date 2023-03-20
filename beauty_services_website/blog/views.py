from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Post

# Create your views here.
# Tworzymy strony 
def index(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/index.html', {'posts': posts})

#Tworzymy api restowe by dostać posty
def api_get_post(rquest):
    posts = Post.objects.all().order_by('title')
    json = serializers.serialize("json", posts)
    return HttpResponse(json)
