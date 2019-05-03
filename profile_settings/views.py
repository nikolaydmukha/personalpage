from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'profile_settings/profile_settings.html')
