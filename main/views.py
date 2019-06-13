from django.shortcuts import render
from protos.pilling.rpc.protos import client_pb2_grpc
from protos.pilling.rpc.protos.client_pb2 import AuthRequest, SearchRequest
import grpc, grpc_tools


def index(request):
    login = "len11-22"
    password = "len11-22"
    channel = grpc.insecure_channel('stage.pilling.rinet.ru:57001')
    client = client_pb2_grpc.ClientStub(channel)
    client.Auth(AuthRequest(login=login, password=password))

    print("222222@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(client.Search(SearchRequest(login=login)))
    raw_data = client.Search(SearchRequest(login=login)).clients
    user_data = {
        'user_id': raw_data[0].id,
        'user_name': raw_data[0].name,
        'user_address': raw_data[0].address,
        'user_num_pre': raw_data[0].address.street.num_pre,
        'user_house': raw_data[0].address.house,
        'user_city': raw_data[0].address.street.city.pre,
        'user_is_active': raw_data[0].active,
        'user_is_corp': raw_data[0].corp,
        'user_is_cashless': raw_data[0].cashless,
        'user_contacts': raw_data[0].contacts,
        'user_ts_from': raw_data[0].ts_from,
    }

    print(user_data)
    # print(user_address)
    # print(user_address.street.city.pre)
    # print(user_is_active)
    # print(user_is_cashless)
    # print(user_is_corp)
    # print(user_contacts)
    # print(user_ts_from)

    context = {"active": "home", "title": "Состояние счёта и подключенные услуги", 'user_data': user_data}
    return render(request, 'main/home.html', context)


def dummy(request):
    """ Форма обратно связи при клике на кнопку 'Заказать звонок' """
    context = {}
    return render(request, 'main/dummy.html', context)

