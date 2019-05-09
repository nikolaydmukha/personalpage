from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "pay_sber", "title": "Оплатить в Сбербанке"}
    return render(request, 'pay_sber/pay_sber.html', context)
