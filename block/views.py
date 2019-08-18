from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import grpc
from personalpage.settings import GRPC_CHANNEL
from protos.pilling.rpc.protos import client_control_pb2_grpc
from protos.pilling.rpc.protos.client_control_pb2 import GetVoluntaryBlockTargetsRequest, GetVoluntaryBlocksRequest, SetVoluntaryBlockRequest


@login_required()
def index(request):
    # Установка соединения для получения информации и управления (ClientControl) услугами (об. платеж, блокировка),
    # подключенными у клиента
    channel = grpc.insecure_channel(GRPC_CHANNEL)
    client_control = client_control_pb2_grpc.ClientControlStub(channel)
    # gRPC запрос для получения данных об услугах клиента
    raw_data_block = client_control.GetVoluntaryBlockTargets(GetVoluntaryBlockTargetsRequest(client_id=request.session['user_info']['personal_data']['user_id']))
    raw_data_block_history = client_control.GetVoluntaryBlocks(GetVoluntaryBlocksRequest(client_id=request.session['user_info']['personal_data']['user_id'], login=request.session['user_info']['personal_data']['user_old_login']))
    # Обработка целевых услуг, которым можно поставить блокировку
    voluntary_block_targets = dict()
    for item in raw_data_block.targets:
        voluntary_block_targets[item.login] = {
            'login': item.login,
            'name': item.name,
            'commercial': item.commercial,
            'active': item.active,
            'available': item.available,
            'reason': item.reason
        }
    # Обработка истории установки блокировок - считаем количество блокировок в текущем месяце
    voluntary_block_history = dict()
    for item in raw_data_block_history.voluntary_blocks:
        if item.login not in voluntary_block_history:
            voluntary_block_history[item.login] = {'blocks_in_month': 0}
        if datetime.utcfromtimestamp(item.ts_from).strftime('%m-%Y') == datetime.now().strftime("%m-%Y"):
            voluntary_block_history[item.login]['blocks_in_month'] += 1
    context = {
        "active": "block",
        "title": "Добровольная блокировка доступа",
        'personal_data': request.session['user_info']['personal_data'],
        'contracts_data': request.session['user_info']['contracts_data'],
        'voluntary_block_targets': voluntary_block_targets,
        'voluntary_block_history': voluntary_block_history
    }
    return render(request, 'block/block.html', context)
