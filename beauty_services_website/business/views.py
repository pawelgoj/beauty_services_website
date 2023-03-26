from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AboutMe
import base64

# Create your views here.
def index(request):
    return render(request, 'business/index.html')


def about_me(request):
    poll = get_object_or_404(AboutMe, aboutme_id=1)
    
    print(poll.image)
    data = {"results": {
        "text": poll.text
    }}
    return JsonResponse(data)