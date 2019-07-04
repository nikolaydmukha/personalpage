from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()

def index(request):
    context = {"active": "pay_bcard", "title": "Пополнить счёт"}
    return render(request, 'pay_bcard/pay_bcard.html', context)
