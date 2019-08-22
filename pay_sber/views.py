import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import pyqrcode
import grpc
from personalpage.settings import GRPC_CHANNEL
from protos.pilling.rpc.protos import payments_pb2_grpc
from protos.pilling.rpc.protos.payments_pb2 import QRPaymentRequest


@login_required()
def index(request):
    # Установка соединения для получения информации и управления (ClientControl) услугами (об. платеж, блокировка),
    # подключенными у клиента
    channel = grpc.insecure_channel(GRPC_CHANNEL)
    sber_payment = payments_pb2_grpc.PaymentsStub(channel)
    # gRPC запрос для получения данных об услугах клиента
    raw_data_sber = sber_payment.QRPayment(QRPaymentRequest(client_id=request.session['user_info']['personal_data']['user_id'],
                                           login=request.session['user_info']['personal_data']['user_old_login'],
                                           processing='sberbank'))
    print("11111", raw_data_sber.QRData)
    url = pyqrcode.create(raw_data_sber.QRData, encoding='utf-8')
    full_path = os.path.abspath("static/images/qrcodes")
    print(full_path)
    file_location = os.path.join(full_path, f'{request.session["user_info"]["personal_data"]["user_old_login"]}.svg')

    url.svg(file_location, scale=2)
    print(url.terminal(quiet_zone=1))
    context = {
        "active": "pay_sber",
        "title": "Оплатить в Сбербанке",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data']
    }
    return render(request, 'pay_sber/pay_sber.html', context)
