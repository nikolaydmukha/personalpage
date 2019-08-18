from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import grpc
from personalpage.settings import GRPC_CHANNEL
from protos.pilling.rpc.protos import client_control_pb2_grpc
from protos.pilling.rpc.protos.client_control_pb2 import GetDelayedPaymentTargetsRequest, GetDelayedPaymentsRequest, SetDelayedPaymentRequest

@login_required()
def index(request):
    # Установка соединения для получения информации и управления (ClientControl) услугами (об. платеж, блокировка),
    # подключенными у клиента
    channel = grpc.insecure_channel(GRPC_CHANNEL)
    client_control = client_control_pb2_grpc.ClientControlStub(channel)
    # gRPC запрос для получения данных об услугах клиента
    raw_data_dpay = client_control.GetDelayedPaymentTargets(GetDelayedPaymentTargetsRequest(client_id=request.session['user_info']['personal_data']['user_id']))
    raw_data_dpay_history = client_control.GetDelayedPayments(GetDelayedPaymentsRequest(client_id=request.session['user_info']['personal_data']['user_id']))
    # Обработка целевых услуг, которым можно поставить блокировку
    dpay_targets = dict()
    for item in raw_data_dpay.targets:
        dpay_targets[item.login] = {
            'login': item.login,
            'name': item.name,
            'commercial': item.commercial,
            'active': item.active,
            'available': item.available,
            'reason': item.reason
        }
    # Обработка истории установки блокировок - считаем количество блокировок в текущем месяце
    dpay_history = dict()
    for item in raw_data_dpay_history.delayed_payments:
        if item.login not in dpay_history:
            dpay_history[item.login] = list()
        dpay_history[item.login].append([datetime.utcfromtimestamp(item.ts_from).strftime('%d-%m-%Y %H:%M:%S'), datetime.utcfromtimestamp(item.ts_to).strftime('%d-%m-%Y %H:%M:%S')])
    context = {
        "active": "dpay",
        "title": "Обещанный платёж",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data'],
        'dpay_targets': dpay_targets,
        'dpay_history': dpay_history
    }
    return render(request, 'dpay/dpay.html', context)
