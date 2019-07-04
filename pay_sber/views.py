from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "pay_sber", "title": "Оплатить в Сбербанке"}
    return render(request, 'pay_sber/pay_sber.html', context)
