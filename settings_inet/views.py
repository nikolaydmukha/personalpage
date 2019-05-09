from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "settings_inet", "title": "Настройки услуги 'Интернет'"}
    return render(request, 'settings_inet/settings_inet.html', context)
