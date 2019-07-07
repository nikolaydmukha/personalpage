from pprint import pprint

from protos.pilling.rpc.protos import client_pb2_grpc, services_pb2_grpc
from protos.pilling.rpc.protos.client_pb2 import AuthRequest, SearchRequest
from protos.pilling.rpc.protos.services_pb2 import ClientServicesReply, ClientServicesRequest
import grpc, grpc_tools


def get_userdata(login, password):
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
    ###print("====\n", raw_data_services)
    # Обработка полученных данных(ИНФОРМАЦИЯ) о клиенте.
    # Сохранение данных в переменные с понятым именем и далее сохраним в словарь для передачи в сессию
    session_dict = {}
    info = raw_data_client[0]
    user_data_client = {
        'user_id': info.id,
        'user_name': info.name,
        'user_city': info.address.house.street.city.name,
        'user_city_pre': info.address.house.street.city.pre,        # prefix (object name, "s" for selo, "g" for gorod)
        'user_street': info.address.house.street.name,              # street
        'user_street_num_pre': info.address.house.street.num_pre,   # street.num_pre
        'user_street_pre': info.address.house.street.pre,           # street.pre
        'user_street_post': info.address.house.street.post,         # street.post
        'user_house': info.address.house.house,                     # house number
        'user_house_building': info.address.house.building,         # house builidng
        'user_house_block': info.address.house.block,               # house block
        'user_house_fraction': info.address.house.fraction,         # house fraction
        'user_house_num_pre': info.address.house.street.num_pre,    # numeric prefix (1 for "1 hvostov per")
        'user_is_active': info.active,                              # is client active
        'user_is_corp': info.corp,                                  # is client corp
        'user_is_cashless': info.cashless,                          # is client cashless
        'user_email_main': info.contacts.main_email,                # client contacts info: EMAIL(main)
        'user_email_add': info.contacts.add_email,                  # client contacts info: EMAIL(add)
        'user_phone_main': info.contacts.main_phone,                # client contacts info: PHONE(main)
        'user_pin': info.contacts.pin,                              # client contacts info: PIN
        'user_ts_to': info.ts_to,                                   # client abandoned unix timestamp
        'user_ts_from': info.ts_from,                               # client abandoned unix timestamp
        'user_old_login': login                                     # old login(get from login form)
    }
    # Обработка полученных данных(УСЛУГИ) клиента.
    # Сохранение данных в переменные с понятым именем
    user_data_contracts = dict()

    for item in raw_data_services.contracts:
        ##print("contarcts ===>", item)
        user_data_contracts[item.organization.name] = {
            'id': item.id,                                          # contract id
            'login': item.login,                                    # contract login
            'active': item.active,                                  # is contract active
            'commercial': item.commercial,                          # contract commercial name
            'own': item.own,                                        # whether contract is for own services
            'advance': item.advance,                                # is contract billed in advance
            'organization_id': item.organization.id,
            'organization_name': item.organization.name,
            'organization_descr': item.organization.descr,
            'provider_id': item.provider.id,
            'provider_name': item.provider.name,
            'provider_descr': item.provider.descr,
            'payment_type_id': item.payment_type.id,
            'payment_type_name': item.payment_type.name,
            'payment_type_descr': item.payment_type.descr,
            'ts_from': item.ts_from,                                # activation unix timestamp
            'ts_to': item.ts_to,                                    # cancellation unix timestamp
            'balance': item.balance,                                # contract balance
            'required_payment': item.required_payment,              # contract required payment
        }
        # Распарсим service_packs(услуги клиента. ВНИМАНИЕ! В одном сервис-паке можт быть несколько услуг. Например,
        # в service_packs интернета есть внешний адрес, тариф, бандл-ТВ. А в service_packs Смотёршки только 1 услуга!
        service_packs = {}
        service_packs_total_cost = 0                                # общая стоимсоть всех услуг клиента
        for service in item.service_packs:
            ##print('####### ==== ######', service)
            service_packs[service.id] = {
                'id': service.id,
                'login': service.login,
                'commercial': service.commercial,
                'total_cost': service.total_cost,
                'conditional_cost': service.conditional_cost,
                'unconditional_cost': service.unconditional_cost,
                'charge_interval': service.charge_interval,
                'ts_from': service.ts_from,
                'balance': service.balance,
                'required_payment': service.required_payment
            }
            service_packs_total_cost += int(service.total_cost)
        user_data_contracts[item.organization.name]['service_packs'] = service_packs
        user_data_contracts[item.organization.name]['service_packs_total_cost'] = service_packs_total_cost

        session_dict = {
            'personal_data': user_data_client,
            'contracts_data': user_data_contracts,
        }
    return session_dict