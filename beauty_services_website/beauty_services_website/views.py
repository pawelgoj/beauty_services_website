from django.shortcuts import render

# Create your views here.
# Tworzymy strony 
def index(request):
    return render(request, 'index.html')