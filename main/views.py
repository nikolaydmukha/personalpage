import grpc, grpc_tools
from pprint import pprint
from django.shortcuts import render
from protos.pilling.rpc.protos import client_pb2_grpc, services_pb2_grpc
from protos.pilling.rpc.protos.client_pb2 import AuthRequest, SearchRequest
from protos.pilling.rpc.protos.services_pb2 import ClientServicesReply, ClientServicesRequest
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    print(request.session['user_info']['personal_data']['user_name_firstname'])
    for key, value in request.session['user_info']['personal_data'].items():
        print(key,"===>", value, "\n")
    context = {"active": "home",
               "title": "Состояние счёта и подключенные услуги",
               'personal_data': request.session['user_info']['personal_data'],
               'contracts_data': request.session['user_info']['contracts_data']
               }
    return render(request, 'main/home.html', context)


def dummy(request):
    """ Форма обратно связи при клике на кнопку 'Заказать звонок' """
    context = {}
    return render(request, 'main/dummy.html', context)

