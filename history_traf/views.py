from django.shortcuts import render
from datetime import date


def index(request):
    # Сформируем даты для вывода в форме выбора дат, за который можно сделать отчёт.
    # Полагаем, что очтет доступен от текущей даты - 1 год.
    today = date.today()
    month_now = today.month
    year_now = today.year
    years = [year for year in range(today.year, today.year+1)]
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
             'Декабрь']
    form_date = list() # переменная для вставки в форма в шаблоне
    for year in years:
        if year != today.year:
            for month in months:
                formated_date = f"{month} {year}"
                form_date.append(formated_date)
        else:
            index = 0
            while index < months.index("Май"):
                formated_date = f"{months[index]} {year}"
                form_date.append(formated_date)
                index += 1
    context = {
        "active": "history_traf",
        "title": "Расходы и трафик",
        'form_date': form_date
    }
    return render(request, 'history_traf/history_traf.html', context)
