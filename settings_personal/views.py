from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "settings_personal", "title": "Настройки личного кабинета"}
    return render(request, 'settings_personal/settings_personal.html', context)
