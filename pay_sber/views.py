from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {
        "active": "pay_sber",
        "title": "Оплатить в Сбербанке",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'pay_sber/pay_sber.html', context)
