import logging
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AboutMe, SocialMedia, Service
from os import path
import base64
from .serializers import ServiceSerializer
# Folder with media items eg. images
from beauty_services_website.settings import MEDIA_ROOT

# Create your views here.
def index(request):
    return render(request, 'business/index.html')


def about_me(request):
    poll = get_object_or_404(AboutMe, aboutme_id=1)

    path = str(MEDIA_ROOT / str(poll.image))

    with open(path, "rb") as img_file:
        image_string = base64.b64encode(img_file.read()).decode()

    data = {"results": {
        "text": poll.text,
        "image": image_string
    }}
    return JsonResponse(data)


def social_data(request):
    poll = SocialMedia.objects.all()
    about_me = AboutMe.objects.get(aboutme_id=1)

    list_of_items = []
    my_contact = {"email": about_me.email, "phone": about_me.phone}

    for item in poll:

        list_of_items.append({
            "name": item.name,
            "link": item.link,
            "logo": item.logo,
            "description": item.description
            })

    data = {"results": {"my_contact": my_contact, "social_media": list_of_items}}
    return JsonResponse(data)


def price_list(request):
    data = Service.objects.all()
    serializer = ServiceSerializer(data, many=True)
    response = {"results": serializer.data}
    return JsonResponse(response)