from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "settings_inet", "title": "Настройки услуги 'Интернет'"}
    return render(request, 'settings_inet/settings_inet.html', context)
