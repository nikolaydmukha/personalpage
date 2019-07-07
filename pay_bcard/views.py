from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()

def index(request):
    context = {
        "active": "pay_bcard",
        "title": "Пополнить счёт",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'pay_bcard/pay_bcard.html', context)
