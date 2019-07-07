from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {
        "active": "settings_inet",
        "title": "Настройки услуги 'Интернет'",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'settings_inet/settings_inet.html', context)
