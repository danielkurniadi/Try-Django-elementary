from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    about_data = {
        'LinkedIn': 'LinkedIn Daniel Kurniadi',
        'github': '@iqDF',
        'colors': ['yellow', 'green', 'blue', 'red', 'violet'],
    }
    return render(request, 'about.html', about_data)

def social_view(request, *args, **kwargs):
    return render(request, 'social_media.html', {})