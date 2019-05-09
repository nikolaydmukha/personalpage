from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "settings_personal", "title": "Настройки личного кабинета"}
    return render(request, 'settings_personal/settings_personal.html', context)
