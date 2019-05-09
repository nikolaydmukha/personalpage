from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"profile_settings": "home", "title": "Изменить контактные данные"}
    return render(request, 'profile_settings/profile_settings.html', context)
