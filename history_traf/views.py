import locale
locale.setlocale(locale.LC_ALL, "")
import datetime
from django.shortcuts import render
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    # Если клиент сделал запрос трафика за нужную дату, то нужно эту дату выводить активной в списке выбора дат
    choosen_date = ''
    if 'month' in request.GET:
        choosen_date = request.GET['month']
    # Сформируем даты для вывода в форме выбора дат, за который можно сделать отчёт.
    # Полагаем, что очтет доступен от текущей даты - 1 год.
    current_month = datetime.datetime.now().strftime("%B")  # Текущий месяц

    today = date.today()
    month_now = today.month
    year_now = today.year
    years = [year for year in range(today.year-1, today.year+1)]
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    months_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    form_date = list()  # переменная для вставки в форма в шаблоне
    for year in years[::-1]:
        if year != today.year:
            for month in months:
                formated_date = f"{month} {year}"
                form_date.append(formated_date)
        else:
            index = 0
            while index < months.index(current_month):
                formated_date = f"{months[index]} {year}"
                form_date.append(formated_date)
                index += 1
    context = {
        'active': 'history_traf',
        'title': 'Расходы и трафик',
        'form_date': form_date,
        'choosen_date': choosen_date,
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'history_traf/history_traf.html', context)
