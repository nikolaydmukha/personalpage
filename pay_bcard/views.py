from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "pay_bcard", "title": "Пополнить счёт"}
    return render(request, 'pay_bcard/pay_bcard.html', context)
