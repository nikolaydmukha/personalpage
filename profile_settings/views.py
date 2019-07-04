from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "profile_settings", "title": "Изменить контактные данные"}
    return render(request, 'profile_settings/profile_settings.html', context)
