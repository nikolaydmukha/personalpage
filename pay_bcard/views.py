from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "bcard", "title": "Пополнить счёт"}
    return render(request, 'pay_bcard/pay_bcard.html', context)
