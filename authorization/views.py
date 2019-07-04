from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from protos.pilling.rpc.protos import client_pb2_grpc, services_pb2_grpc
from protos.pilling.rpc.protos.client_pb2 import AuthRequest, SearchRequest
from django.contrib.auth import authenticate, logout, login
import grpc, grpc_tools


# ФУНКЦИЯ АВТОРИЗАЦИИ - LOGIN
def personalpage_login(request):
    template = 'authorization/login.html'
    if request.method == 'POST' and 'csrfmiddlewaretoken' in request.POST:
        # Аутентифицируем пользователя***:
        # 1. Если пользователь есть(проверяется таблица User средствами Django), то логиним его на главную страницу.
        # 2. Если пользователя нет в таблице User Django, то делаем запрос к серверу по grpc и в случае успеха создадим
        # пользователя в Django. Это необходимое условие, для тспользования во всех views декоратор login_required()
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:  # 1 условие ***
            # Логиним пользователя джанговским механизмом
            login(request, user)
            # Если пользователь сразу идёт на какую-либо страницу ЛК(без предварительного логина - ну, например, у него
            # какая-либо страница в закладках) и т.к. у нас работает декоратор login_required(),
            # то этот декоратор кидает пользователя на форму логина и передёт параметр ?next= - страница, куда хотел
            # зайти пользователь. Значит после авторизации пользователя туда и нужно его перекинуть
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect('/main')
        else:   # 2 условие ***
            print("ПОЛЬЗОВАТЕЛЯ НЕТ В ДЖАНГО. НАДО БЫ СОЗДАТЬ")
            print("=========")
            # Логин и пароль приходят из формы
            username = request.POST['username']
            password = request.POST['password']
            # Адрес сервера
            channel_address = 'stage.pilling.rinet.ru:57001'
            # Установка соединения для Авторизация(AuthRequest) клиента
            channel = grpc.insecure_channel(channel_address)
            client = client_pb2_grpc.ClientStub(channel)
            # Авторизация(возвращает True/False) - делаем запрос к серверу, чтобы понять, есть ли такой пользователь
            auth = client.Auth(AuthRequest(login=username, password=password))
            # Если есть, то создаём пользователя в User Django и редиректим на главную страницу
            # Создание пользователя в таблице Django, нужно чтобы во всех views использовать декоратор login_required()
            if auth.success:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('main/')
            else:
                context = create_context_username_csrf(request)
                context['errors'] = 'Неверный логин или пароль!'
                return render_to_response(template, context=context)
    else:
        context = create_context_username_csrf(request)
        return render_to_response(template, context=context)


# ФУНКЦИЯ ВЫХОДА - LOGOUT
def personalpage_logout(request):
    logout(request)
    # Переадресовать на страницу успешного выхода.
    return HttpResponseRedirect("/")


# Вспомогательный метод для формирования контекста с csrf_token
# и добавлением формы авторизации в этом контексте
def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['login_form'] = AuthenticationForm
    return context
