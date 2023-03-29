import logging
from django.shortcuts import render
from django.http import HttpRequest
from beauty_services_website.settings import MEDIA_URL
from .serializers import PostSerializer

from rest_framework.response import Response
from .models import Post, Image
from rest_framework.decorators import api_view


# Create your views here.
# Tworzymy strony 
def index(request: HttpRequest):
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/index.html', {'posts': posts})

#Tworzymy api restowe by dostać posty
@api_view(['GET'])
def api_get_post(request: HttpRequest):
    # Aby otrzymać ?quantity 
    quantity = request.query_params.get('quantity', None)
    
    # Serializacja za pomocą utworzonego serializera
    # Get "quantity" of latest posts
    path_root: str = request.build_absolute_uri('')
    path_root = path_root.replace('/api/posts/', '')
    
    if quantity is not None:
        quantity = int(quantity)
        posts: list = PostSerializer(Post.objects.order_by('-date').all()[:quantity], many=True)

        add_images_data_to_response(posts, path_root)

    else:
        posts = PostSerializer(Post.objects.order_by('-date').all()[:10], many=True)

        add_images_data_to_response(posts, path_root)

    # Aby dostać dokumętację z Django Rest Framework, musimy wykorzystać 
    # Metodę Response 
    return Response({"results": posts.data})


def add_images_data_to_response(posts: list, path_root: str) -> None:

    for item in posts.data:
        i = 0
        for image_id in item['images']:
            image = Image.objects.get(id=image_id)
            path = str(path_root + MEDIA_URL + str(image.image))
            item['images'][i] = {'name': image.name, 'url': path}
            i += 1
            
