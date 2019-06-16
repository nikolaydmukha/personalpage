from pprint import pprint

from django.shortcuts import render
from protos.pilling.rpc.protos import client_pb2_grpc, services_pb2_grpc
from protos.pilling.rpc.protos.client_pb2 import AuthRequest, SearchRequest
from protos.pilling.rpc.protos.services_pb2 import ClientServicesReply, ClientServicesRequest

import grpc, grpc_tools


def index(request):
    login = "len11-22"
    password = "len11-22"
    channel = grpc.insecure_channel('stage.pilling.rinet.ru:57001')
    # Установка соединения для Авторизация(AuthRequest) клиента и
    # получение информации(Search) о клиенте
    client = client_pb2_grpc.ClientStub(channel)
    client.Auth(AuthRequest(login=login, password=password))

    # gRPC запрос для получения данных клиента
    raw_data_client = client.Search(SearchRequest(login=login)).clients

    # Установка соединения для получение(GetClientServices) всех услуг,
    # подключенных у клиента
    service = services_pb2_grpc.ServicesStub(channel)

    # gRPC запрос для получения данных об услугах клиента
    raw_data_services = service.GetClientServices(ClientServicesRequest(id=raw_data_client[0].id, with_balance=2))

    # Обработка полученных данных(ИНФОРМАЦИЯ) о клиенте.
    # Сохранение данных в переменные с понятым именем
    user_data_client = {
        'user_id': raw_data_client[0].id,
        'user_name': raw_data_client[0].name,
        'user_address': raw_data_client[0].address,                 # address: street, house, building, block, fraction
        'user_num_pre': raw_data_client[0].address.street.num_pre,  # numeric prefix (1 for "1 hvostov per")
        'user_house': raw_data_client[0].address.house,             # house number
        'user_street': raw_data_client[0].address.street,           # street
        'user_city': raw_data_client[0].address.street.city.pre,    # prefix (object name, "s" for selo, "g" for gorod)
        'user_is_active': raw_data_client[0].active,                # is client active
        'user_is_corp': raw_data_client[0].corp,                    # is client corp
        'user_is_cashless': raw_data_client[0].cashless,            # is client cashless
        'user_contacts': raw_data_client[0].contacts,               # client contacts info: EMAIL, PHONE, PIN
        'user_ts_to': raw_data_client[0].ts_to,                     # client abandoned unix timestamp
        'user_ts_from': raw_data_client[0].ts_from,                 # client abandoned unix timestamp
    }
    print(user_data_client)
    print("####### ALLALLALLALL")
    # Обработка полученных данных(УСЛУГИ) клиента.
    # Сохранение данных в переменные с понятым именем
    user_data_contracts = dict()
    for item in raw_data_services.contracts:
        print(item)
        print("Next \n")
        user_data_contracts[item.id] = {
            'id': item.id,                                          # contract id
            'login': item.login,                                    # contract login
            'active': item.active,                                  # is contract active
            'commercial': item.commercial,                          # contract commercial name
            'own': item.own,                                        # whether contract is for own services
            'advance': item.advance,                                # is contract billed in advance
            'organization': item.organization,                      # organization: ID? NAME(short lat), DESCR(full cyr)
            'provider': item.provider,                              # contract provider
            'payment_type': item.payment_type,                      # contract payment type
            'service_packs': item.service_packs,                    # contract service packs
            'ts_from': item.ts_from,                                # activation unix timestamp
            'ts_to': item.ts_to,                                    # cancellation unix timestamp
            'balance': item.balance,                                # contract balance
            'required_payment': item.required_payment,              # contract required payment
        }
    pprint(user_data_contracts)
    context = {"active": "home",
               "title": "Состояние счёта и подключенные услуги",
               'user_data_client': user_data_client,
               'user_data_contracts': user_data_contracts
               }
    return render(request, 'main/home.html', context)


def dummy(request):
    """ Форма обратно связи при клике на кнопку 'Заказать звонок' """
    context = {}
    return render(request, 'main/dummy.html', context)

