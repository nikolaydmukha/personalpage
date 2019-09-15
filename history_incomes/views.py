# from datetime import datetime, time
# import time
# import datetime
import time
from pprint import pprint

import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import grpc
from personalpage.settings import GRPC_CHANNEL
from protos.pilling.rpc.protos import payments_pb2_grpc
from protos.pilling.rpc.protos.payments_pb2 import GetPaymentsRequest


@login_required()
def index(request):
    print(request.GET)
    # Если клиент сделал запрос трафика за нужную дату, то нужно эту дату выводить активной в списке выбора дат
    chosen_date_from = ''
    chosen_date_to = ''
    error_msg = ''
    incomes_history = dict()
    if 'from' in request.GET and 'to' in request.GET and request.GET['from'] != '' and request.GET['to'] != '':  #если пришли from, to и в них есть даты
        if int(time.mktime(datetime.datetime.strptime(request.GET['to'], "%d.%m.%y").timetuple())) < int(time.mktime(datetime.datetime.strptime(request.GET['from'], "%d.%m.%y").timetuple())):
            error_msg = "Дата начала не может быть меньше даты окончания выборки. Пожалуйста, укажите верный диапазон."
        else:
            # Установка соединения для получения информации и управления (ClientControl) услугами (об. платеж, блокировка),
            # подключенными у клиента
            channel = grpc.insecure_channel(GRPC_CHANNEL)
            incomes = payments_pb2_grpc.PaymentsStub(channel)
            # gRPC запрос для получения данных об услугах клиента
            raw_data_incomes = incomes.GetPayments(
                GetPaymentsRequest(client_id=request.session['user_info']['personal_data']['user_id'],
                                   login=request.session['user_info']['personal_data']['user_old_login'],
                                ts_from=int(time.mktime(datetime.datetime.strptime(request.GET['from'], "%d.%m.%y").timetuple())),
                                ts_to=int(time.mktime(datetime.datetime.strptime(request.GET['to'], "%d.%m.%y").timetuple()))))
            for item in raw_data_incomes.payments:
                incomes_history[item.id] = {
                    'target_descr': item.target_descr,
                    'curr_sum': item.curr_sum,
                    'vm_sum': item.vm_sum,
                    'currency_descr': item.currency.descr,
                    'created_ts': datetime.datetime.fromtimestamp(item.created_ts),
                    'organization': item.organization.descr
                }
            pprint(incomes_history)
            chosen_date_from = request.GET['from']
            chosen_date_to = request.GET['to']
    else:
        if 'from' not in request.GET and 'to' not in request.GET:  #если просто зашли на страницу incomes_history, но не кликнули кнопку Показать
            error_msg = ''
        elif len(request.GET['from']) == 0 and len(request.GET['to']) == 0:  #кликнули кнопку Показать, но не выбрали дату
            error_msg = "Необходимо указать диапазон дат для поиска."

    context = {
        "active": "history_incomes",
        "title": "История платежей",
        'error_msg': error_msg,
        'chosen_date_from': chosen_date_from,
        'chosen_date_to': chosen_date_to,
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data'],
        'incomes_history': incomes_history
    }
    return render(request, 'history_incomes/history_incomes.html', context)
