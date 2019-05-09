from django.shortcuts import render


# Create your views here.


def index(request):
    context = {"active": "home", "title": "Состояние счета и подключенные услуги"}
    return render(request, 'main/home.html', context)
