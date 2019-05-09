from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"active": "history_incomes", "title": "История платежей"}
    return render(request, 'history_incomes/history_incomes.html', context)
