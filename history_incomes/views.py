from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    print(request.GET)
    # Если клиент сделал запрос трафика за нужную дату, то нужно эту дату выводить активной в списке выбора дат
    choosen_date_from = ''
    choosen_date_to = ''
    error_msg = ''
    if 'from' in request.GET and 'to' in request.GET:
        choosen_date_from = request.GET['from']
        choosen_date_to = request.GET['to']
        if not request.GET['from'] or not request.GET['to']:
            error_msg = "Необходимо указать диапазон дат для поиска."
        elif request.GET['to'] < request.GET['from']:
            error_msg = "Дата начала не может быть меньше даты окончания выборки. Пожалуйста, укажите верный диапазон."
    context = {
        "active": "history_incomes",
        "title": "История платежей",
        'error_msg': error_msg,
        'choosen_date_from': choosen_date_from,
        'choosen_date_to': choosen_date_to,
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'history_incomes/history_incomes.html', context)
