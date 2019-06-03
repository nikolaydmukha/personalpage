from django.shortcuts import render


# Create your views here.


def index(request):
    context = {"active": "home", "title": "Состояние счёта и подключенные услуги"}
    return render(request, 'main/home.html', context)


def dummy(request):
    context = {}
    return render(request, 'main/dummy.html', context)