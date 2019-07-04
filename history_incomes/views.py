from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {"active": "history_incomes", "title": "История платежей"}
    return render(request, 'history_incomes/history_incomes.html', context)
