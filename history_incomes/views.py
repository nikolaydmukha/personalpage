from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = {
        "active": "history_incomes",
        "title": "История платежей",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'history_incomes/history_incomes.html', context)
